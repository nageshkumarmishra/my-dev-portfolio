# 🧠 NLP2CRUD: Natural Language to CRUD API Generator (FastAPI)

Generate production-grade REST APIs from natural language prompts using FastAPI, SQLAlchemy, and optional LLMs.

---

## ✨ Features

- 💬 Natural language prompt → Config → FastAPI app
- 🧠 LLM support via plug-in parser (`--use-llm`)
- 🧱 Auto-generates SQLAlchemy models & Pydantic schemas
- 🔁 Full CRUD endpoints with validation
- 🔐 API Key authentication scaffolded
- 🧪 Modular & testable codebase
- 🧩 Database-agnostic (PostgreSQL, MySQL, SQLite, etc.)

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/nlp2crud
cd nlp2crud
python -m venv venv
source venv/bin/activate
pip install -e .
```

---

## 🚀 CLI Usage

### 👉 From Natural Prompt (LLM-powered)

```bash
python cli.py "Create API for Library with books, authors, issued_date" --use-llm --run
```

### 🛠 From Natural Prompt (Rule-based)

```bash
python cli.py "Manage inventory with items (name, count, price)" --run
```

---

## 📁 Folder Structure

```
nlp2crud/
├── cli.py                 # Entry point for CLI
├── main.py                # FastAPI app entry
├── app/
│   ├── core/              # Auth, config, prompt/LLM parser
│   ├── engine/            # Generators for models, routers, schemas
│   └── adapters/          # DB layer abstraction
├── tests/                 # Unit + integration tests
└── examples/              # Sample JSON configs
```

---

## 🔑 Authentication

Simple API key header required:

```
Authorization: Bearer <your-api-key>
```

---

## 🧠 Extending

- ✅ Add new entity types via config
- 🔁 Add custom relationship rules
- 🧠 Plug in any LLM (e.g., DeepSeek, GPT, Claude)
- 📄 Add validation logic in `schema_generator.py`

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📘 License

MIT — Use, modify, and share with credit.

---