# n8n-workflows

A collection of my n8n automation workflows — backed up, version-controlled, and reusable.

## Importing a Workflow

1. Download the `.json` file.
2. Open n8n editor → `Import from File`.
3. Select the downloaded file and click **Import**.
4. Open each node that shows a credential warning and connect your own credentials (OpenAI, Gmail, Telegram, …). No credentials are stored in these files; n8n exports only credential names.

## Workflows

<!-- workflow-index:start -->
| Workflow | File | Nodes | Trigger | Main nodes |
| --- | --- | ---: | --- | --- |
| Very simple Human in the loop system email with AI e IMAP | [A Very Simple _Human in the Loop_ Email Response System Using AI and IMAP.json](A%20Very%20Simple%20_Human%20in%20the%20Loop_%20Email%20Response%20System%20Using%20AI%20and%20IMAP.json) | 16 | emailReadImap | agent, chainSummarization, emailSend, lmChatOpenAi, markdown |
| AI Agent with Ollama for current weather and wiki | [AI Agent with Ollama for current weather and wiki.json](AI%20Agent%20with%20Ollama%20for%20current%20weather%20and%20wiki.json) | 10 | manualChat | agent, lmChatOllama, memoryBufferWindow, toolHttpRequest, toolWikipedia |
| Stock Q&A Workflow | [AI Crew to Automate Fundamental Stock Analysis - Q&A Workflow.json](AI%20Crew%20to%20Automate%20Fundamental%20Stock%20Analysis%20-%20Q%26A%20Workflow.json) | 17 | manual, manualChat, webhook | chainRetrievalQa, documentBinaryInputLoader, embeddingsOpenAi, googleDrive, lmChatOpenAi, retrieverVectorStore … |
| Email AI Auto-responder. Summerize and send email | [AI-Powered Email Automation for Business_ Summarize & Respond with RAG.json](AI-Powered%20Email%20Automation%20for%20Business_%20Summarize%20%26%20Respond%20with%20RAG.json) | 26 | emailReadImap, manual | agent, chainLlm, chainSummarization, documentDefaultDataLoader, emailSend, embeddingsOpenAi … |
| Auto Categorise Outlook Emails with AI | [Auto Categorise Outlook Emails with AI.json](Auto%20Categorise%20Outlook%20Emails%20with%20AI.json) | 36 | manual | agent, lmChatOllama, markdown, microsoftOutlook |
| Auto-label incoming Gmail messages with AI nodes | [Auto-label incoming Gmail messages with AI nodes.json](Auto-label%20incoming%20Gmail%20messages%20with%20AI%20nodes.json) | 19 | gmail | chainLlm, gmail, lmChatOpenAi, outputParserStructured |
| [3/3] Anomaly detection tool (crops dataset) | [Automated Hugging Face Paper Summary Fetching & Categorization Workflow.json](Automated%20Hugging%20Face%20Paper%20Summary%20Fetching%20%26%20Categorization%20Workflow.json) | 17 | executeWorkflow | httpRequest |
| Build a Tax Code Assistant with Qdrant, Mistral.ai and OpenAI | [Build a Tax Code Assistant with Qdrant, Mistral.ai and OpenAI.json](Build%20a%20Tax%20Code%20Assistant%20with%20Qdrant%2C%20Mistral.ai%20and%20OpenAI.json) | 38 | chat, executeWorkflow, manual | agent, compression, documentDefaultDataLoader, embeddingsMistralCloud, extractFromFile, httpRequest … |
| Chat with PDF docs using AI | [Chat with PDF docs using AI.json](Chat%20with%20PDF%20docs%20using%20AI.json) | 22 | chat, manual | chainLlm, documentDefaultDataLoader, embeddingsOpenAi, googleDrive, lmChatOpenAi, outputParserStructured … |
| ETL pipeline | [ETL pipeline for text processing.json](ETL%20pipeline%20for%20text%20processing.json) | 9 | cron | googleCloudNaturalLanguage, mongoDb, postgres, slack, twitter |
| Host Your Own AI Deep Research Agent with n8n, Apify and OpenAI o3 | [Host Your Own AI Deep Research Agent with n8n, Apify and OpenAI o3.json](Host%20Your%20Own%20AI%20Deep%20Research%20Agent%20with%20n8n%2C%20Apify%20and%20OpenAI%20o3.json) | 87 | executeWorkflow, form | chainLlm, executionData, form, httpRequest, lmChatGoogleGemini, lmChatOpenAi … |
| Open Deep Research - AI-Powered Autonomous Research Workflow | [Open Deep Research - AI-Powered Autonomous Research Workflow.json](Open%20Deep%20Research%20-%20AI-Powered%20Autonomous%20Research%20Workflow.json) | 17 | chat | agent, chainLlm, httpRequest, lmChatOpenRouter, memoryBufferWindow, toolWikipedia |
| RAG:Context-Aware Chunking \| Google Drive to Pinecone via OpenRouter & Gemini | [RAG_Context-Aware Chunking _ Google Drive to Pinecone via OpenRouter & Gemini.json](RAG_Context-Aware%20Chunking%20_%20Google%20Drive%20to%20Pinecone%20via%20OpenRouter%20%26%20Gemini.json) | 17 | manual | agent, documentDefaultDataLoader, embeddingsGoogleGemini, extractFromFile, googleDrive, lmChatOpenRouter … |
| Siri AI Agent_ Apple Shortcuts powered voice template | [Siri AI Agent_ Apple Shortcuts powered voice template.json](Siri%20AI%20Agent_%20Apple%20Shortcuts%20powered%20voice%20template.json) | 7 | webhook | agent, lmChatOpenAi |
| Telegram AI Langchain bot | [Telegram AI bot with LangChain nodes.json](Telegram%20AI%20bot%20with%20LangChain%20nodes.json) | 12 | executeWorkflow, telegram | agent, httpRequest, lmChatOpenAi, memoryBufferWindow, telegram, toolWorkflow |
| [2/2] KNN classifier (lands dataset) | [Vector Database as a Big Data Analysis Tool for AI Agents [2_2 KNN].json](Vector%20Database%20as%20a%20Big%20Data%20Analysis%20Tool%20for%20AI%20Agents%20%5B2_2%20KNN%5D.json) | 18 | executeWorkflow | httpRequest |
| Website Monitor & Alert System | [email_automation/workflow_1.json](email_automation/workflow_1.json) | 5 | cron | emailSend, httpRequest |
| Database Backup Reminder System | [email_automation/workflow_2.json](email_automation/workflow_2.json) | 5 | schedule | emailSend, ftp |
| Form Submission Auto-Responder | [email_automation/workflow_3.json](email_automation/workflow_3.json) | 7 | webhook | emailSend |
| Social Media Mention Alert System | [email_automation/workflow_4.json](email_automation/workflow_4.json) | 5 | schedule | emailSend, twitter |
| Invoice Due Date Reminder System | [email_automation/workflow_5.json](email_automation/workflow_5.json) | 7 | schedule | emailSend, googleSheets |
| Http req tele bot | [http_req_tele_bot.json](http_req_tele_bot.json) | 5 | manual | httpRequest, telegram |
<!-- workflow-index:end -->

The table is generated from the files. After adding or changing a workflow, run:

```bash
python scripts/validate_workflows.py --index
```

## Validation

`scripts/validate_workflows.py` checks that every file is a single valid n8n workflow, node names are unique, and no node parameter contains a literal password, API key or token. GitHub Actions runs it on every push and pull request.
