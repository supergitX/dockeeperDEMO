# 📘 Doc-Keeper

**Doc-Keeper** is an AI-powered documentation generator for your codebase, powered by **Gemini 2.0**. It scans your entire repository, intelligently summarizes key modules, and creates clean and detailed Markdown documentation — automatically.

> 🔥 Perfect for DevOps, ML projects, open source, internal tools, and more!

---

## 🚀 Features

- 📂 Scans entire repo and subdirectories
- 🔍 Ignores irrelevant files (e.g. `.env`, `__pycache__`, `.git`, etc.)
- 🧠 Uses Google's Gemini 2.0 LLM to generate:
  - Project overview
  - Setup instructions
  - Module/function summaries
  - Folder structure explanation
  - CLI usage (if available)
- 📝 Outputs `DOCUMENTATION.md` with rich Markdown formatting
- 🔁 GitHub Actions support for auto-generation on every push

---

## 🛠️ Setup

### 1. 🔑 Get a Gemini API Key
Go to [Google AI Studio](https://makersuite.google.com/app/apikey) and get your API key.

### 2. 🔄 Clone This Repo

```bash
git clone https://github.com/your-username/doc-keeper.git
cd doc-keeper
```

### 3. 🧪 Create `.env` (optional but recommended)

```bash
echo "GEMINI_API_KEY=your-gemini-key-here" > .env
```

Or export it directly in terminal:

```bash
export GEMINI_API_KEY=your-gemini-key-here
```

### 4. 📦 Install Dependencies

```bash
pip install google-generativeai
```

---

## ⚙️ Usage

Simply run the `doc-keeper.py` script from the root of your repository.

```bash
python doc-keeper.py
```

It will generate a `DOCUMENTATION.md` file based on your codebase.

---

## 🧪 GitHub Actions Integration (Optional)

A workflow file is included at `.github/workflows/generate-docs.yml`. It will:

- Trigger on every push to any branch
- Run the doc-keeper agent
- Commit & push updated `DOCUMENTATION.md`

### 🔐 To enable:

1. Go to **Settings → Secrets → Actions**
2. Add a new secret:
   - Name: `GEMINI_API_KEY`
   - Value: _your Gemini API key_

You're all set!

---

## 📁 File Structure

```
doc-keeper/
├── doc-keeper.py           # 🔍 Main AI agent that reads repo and generates docs
├── DOCUMENTATION.md        # 📝 Output file
├── .github/
│   └── workflows/
│       └── generate-docs.yml  # 🤖 GitHub Actions automation
└── README.md               # 📘 You're reading it
```

---

## 📌 Requirements

- Python 3.8+
- `google-generativeai` Python SDK
- Gemini API Key from Google

---

## 🤝 Contributing

We welcome contributions! Feel free to open issues, create PRs, or fork and build on top of this agent.

---

## 📜 License

[MIT License](LICENSE)

---

## 🌟 Star This Repo

If this project helped you, consider leaving a ⭐️ to support it!

