# 💻 Error Explainer

> AI-powered tool that explains any programming error in plain English — no jargon, no confusion.

🔗 **Live Demo:** https://error-explainer-13au.onrender.com

---

## What It Does

Paste any error or stack trace and get:
- **What happened** — plain English explanation
- **Root Cause** — why the error occurred  
- **Exact Fix** — step-by-step solution with code examples
- **Pro Tip** — how to avoid it in future

---

## Tech Stack
- **Backend:** Django 5.2
- **AI:** Google Gemini 2.5 Flash
- **Frontend:** Bootstrap 5
- **Deployment:** Render

---

## Run Locally

```bash
git clone https://github.com/0115-navya/error-explainer.git
cd error-explainer
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
```
Add `.env` with `GEMINI_API_KEY`, `SECRET_KEY`, `DEBUG=True` then:
```bash
python manage.py migrate && python manage.py runserver
```
---

## Features
- 🤖 AI-powered error explanations
- 🌐 Auto-detects Python, JavaScript, Java & more
- 🚨 Severity detection (Warning / Error / Critical)
- 📜 Error history per user
- 🔐 User authentication

---

## Author
**Navya Jain** · [GitHub](https://github.com/0115-navya)
