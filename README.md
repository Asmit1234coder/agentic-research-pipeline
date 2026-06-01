# 🔬 ResearchMind – Multi-Agent AI Research Assistant

ResearchMind is an AI-powered Multi-Agent Research System that automates the complete research workflow using specialized AI agents. Instead of relying on a single LLM response, multiple agents collaborate to search, analyze, write, and critique research content.

The system demonstrates how Agentic AI can be used to perform complex tasks by dividing responsibilities among specialized agents.

---

## 🚀 Features

* Multi-Agent Architecture
* Automated Web Research
* Content Scraping and Extraction
* AI-Powered Report Generation
* Research Critique and Feedback
* Interactive Streamlit Dashboard
* Modular Agent Design
* LangChain Agent Framework

---

## 🏗️ System Architecture

The project consists of four specialized agents:

### 1. Search Agent

Responsibilities:

* Searches the web for relevant information
* Identifies recent and reliable sources
* Collects research material

Output:

* Search results and references

---

### 2. Reader Agent

Responsibilities:

* Analyzes search results
* Selects the most relevant source
* Scrapes and extracts detailed content

Output:

* Structured research information

---

### 3. Writer Agent

Responsibilities:

* Combines search findings and scraped content
* Generates a comprehensive research report
* Organizes information into readable sections

Output:

* Final research report

---

### 4. Critic Agent

Responsibilities:

* Reviews generated reports
* Evaluates quality and completeness
* Provides feedback and improvement suggestions

Output:

* Critique report

---

## 🔄 Workflow

User Topic
↓
Search Agent
↓
Reader Agent
↓
Writer Agent
↓
Critic Agent
↓
Final Research Package

The pipeline ensures that every report is researched, written, and reviewed before being presented to the user.

---

## 🛠️ Tech Stack

### AI & LLM

* LangChain
* Mistral AI

### Backend

* Python

### Frontend

* Streamlit

### Research Tools

* Web Search APIs
* Web Scraping Utilities

### Environment Management

* UV
* Python Virtual Environment

---

## 📂 Project Structure

```text
Multi-Agent/
│
├── Agents.py
├── pipeline.py
├── tools.py
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd Multi-Agent
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
uv pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
```

---

## ▶️ Running the Application

### Terminal Version

```bash
python pipeline.py
```

### Streamlit UI

```bash
streamlit run app.py
```

---

## 📸 Example Use Cases

Research topics such as:

* Artificial Intelligence Trends
* Quantum Computing
* Climate Change Technologies
* Cybersecurity Threat Analysis
* Renewable Energy Innovations
* Healthcare AI Applications

---

## 🎯 Learning Outcomes

This project demonstrates:

* Multi-Agent System Design
* Agent Orchestration
* Tool Calling
* Prompt Engineering
* Retrieval-Augmented Research
* AI Workflow Automation
* Streamlit Application Development
* LLM Integration using LangChain

---

## 🔮 Future Improvements

* Citation Generation
* Multi-Source Scraping
* Memory-Enabled Agents
* Research Report Scoring
* Research Report Comparison
* Agent Monitoring Dashboard
* Multi-LLM Support

---

## 👨‍💻 Author

Asmit Pandey

---

## ⭐ Project Goal

The goal of ResearchMind is to showcase how specialized AI agents can collaborate to perform research tasks more effectively than a single AI model, demonstrating the power of Agentic AI systems.
