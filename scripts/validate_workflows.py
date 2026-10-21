"""Validate the n8n workflow exports and (optionally) rebuild the README index.

    python scripts/validate_workflows.py            # validate, exit 1 on problems
    python scripts/validate_workflows.py --index    # also rewrite the README table

Checks: every .json parses as exactly one workflow with nodes and connections,
node names are unique, and no node parameter holds a literal secret (password,
apiKey, token...) instead of an n8n credential or {{ expression }}.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
START, END = "<!-- workflow-index:start -->", "<!-- workflow-index:end -->"
SECRET_KEYS = re.compile(r"^(password|passwd|api[_-]?key|apikey|secret|token|access[_-]?token|bearer)$", re.I)


def iter_secret_values(value, path=""):
    if isinstance(value, dict):
        for key, item in value.items():
            here = f"{path}.{key}" if path else key
            if SECRET_KEYS.match(key) and isinstance(item, str) and item and not item.startswith("="):
                yield here
            yield from iter_secret_values(item, here)
    elif isinstance(value, list):
        for i, item in enumerate(value):
            yield from iter_secret_values(item, f"{path}[{i}]")


def check(path: Path) -> tuple[dict | None, list[str]]:
    problems = []
    try:
        workflow = json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as exc:
        return None, [f"invalid JSON: {exc}"]
    if not isinstance(workflow, dict) or not isinstance(workflow.get("nodes"), list) or not workflow["nodes"]:
        return None, ["not an n8n workflow (no nodes)"]
    if not isinstance(workflow.get("connections"), dict):
        problems.append("missing connections")
    names = [node.get("name") for node in workflow["nodes"]]
    duplicates = sorted({n for n in names if names.count(n) > 1})
    if duplicates:
        problems.append(f"duplicate node names: {duplicates}")
    for node in workflow["nodes"]:
        for where in iter_secret_values(node.get("parameters", {})):
            problems.append(f"literal secret in node '{node.get('name')}' at {where}; use an n8n credential")
    return workflow, problems


def describe(path: Path, workflow: dict) -> tuple[str, int, str, str]:
    nodes = workflow["nodes"]
    types = [n.get("type", "").split(".")[-1] for n in nodes]
    trigger_like = {"webhook", "cron", "interval", "emailReadImap"}
    triggers = sorted({t.replace("Trigger", "") for t in types if t.lower().endswith("trigger") or t in trigger_like})
    skip = {"set", "if", "switch", "merge", "code", "noOp", "stickyNote", "splitInBatches", "splitOut", "aggregate",
            "filter", "wait", "executeWorkflow", "respondToWebhook", "function", "itemLists", "html", "dateTime"}
    services = sorted({t for t in types if t not in skip and not t.lower().endswith("trigger") and t not in trigger_like})
    name = workflow.get("name") or path.stem
    return name, len(nodes), ", ".join(triggers) or "manual", ", ".join(services[:6]) + (" …" if len(services) > 6 else "")


def build_table(rows: list[tuple[Path, dict]]) -> str:
    lines = ["| Workflow | File | Nodes | Trigger | Main nodes |", "| --- | --- | ---: | --- | --- |"]
    for path, workflow in rows:
        name, count, trigger, services = describe(path, workflow)
        rel = path.relative_to(ROOT).as_posix()
        cells = [c.replace("|", "\\|") for c in (name, rel, trigger, services)]
        lines.append(f"| {cells[0]} | [{cells[1]}]({quote(rel)}) | {count} | {cells[2]} | {cells[3]} |")
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--index", action="store_true", help="rewrite the workflow table in README.md")
    args = parser.parse_args(argv)

    files = sorted(p for p in ROOT.rglob("*.json") if ".git" not in p.parts)
    rows, failed = [], 0
    for path in files:
        workflow, problems = check(path)
        for problem in problems:
            print(f"FAIL {path.relative_to(ROOT)}: {problem}")
        failed += bool(problems)
        if workflow is not None:
            rows.append((path, workflow))
    print(f"{len(files) - failed}/{len(files)} workflow files OK")

    if args.index:
        text = README.read_text(encoding="utf-8")
        if START not in text:
            text = text.rstrip() + f"\n\n## Workflows\n\n{START}\n{END}\n"
        before, rest = text.split(START, 1)
        after = rest.split(END, 1)[1]
        README.write_text(f"{before}{START}\n{build_table(rows)}\n{END}{after}", encoding="utf-8")
        print(f"Wrote index of {len(rows)} workflows to README.md")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
