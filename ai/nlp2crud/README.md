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


```bash
python cli.py "Create an API for BooksDelivery that stores information about book deliveries. Each delivery should include: a unique delivery_id as the primary key, the delivery_date as a datetime field, a recipient_name (string), a recipient_email (string, must be unique), the status of delivery (e.g., 'pending', 'shipped', 'delivered'), stored as a string, the book_id (int), which should be a foreign key referencing a Book model. The Book model should include: book_id as primary key, title (string), author (string), published_year (integer), price (float)." --run
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

## 🖼️ Screenshots

<img width="2056" alt="Screenshot 2025-06-02 at 00 12 07" src="https://github.com/user-attachments/assets/e496e0ad-e8b8-4938-8d18-e0b5a7c3cb4c" />
<img width="2056" alt="Screenshot 2025-06-02 at 00 12 19" src="https://github.com/user-attachments/assets/32035e66-9dbd-4cde-b83c-724fefaa98a6" />
<img width="1924" alt="Screenshot 2025-06-01 at 22 05 58" src="https://github.com/user-attachments/assets/e85f6ffc-0ae1-4a24-bc9a-b9d4a3334993" />




