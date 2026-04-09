# 🚀 Chatbot for SIM Plan Details

💬 An AI-powered chatbot that recommends the best telecom recharge plans based on **budget, validity, and SIM provider** (Airtel, Jio, VI).

---

## 🏷️ Badges

<p align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?logo=sqlite)
![Status](https://img.shields.io/badge/Status-Active-success)
![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

## ✨ Features

* 💬 Chat-based UI
* 📊 Smart recharge plan suggestions
* 🔍 Extracts:

  * Budget (₹)
  * Validity (days)
  * SIM provider
* ⚡ Fast SQLite-based filtering
* 🎨 Modern Glassmorphism UI
* 🧠 Regex-powered chatbot logic

---

## 🛠️ Tech Stack

| Layer    | Technology     |
| -------- | -------------- |
| Frontend | HTML, CSS      |
| Backend  | Flask (Python) |
| Database | SQLite         |
| Logic    | Regex + SQL    |

---

## 📂 Project Structure

```
📦 Chatbot-for-Sim-Plan-Details
 ┣ 📜 app.py
 ┣ 📜 chatbot_logic.py
 ┣ 📜 plans.db
 ┣ 📜 plans.sql
 ┣ 📂 templates
 ┃ ┗ 📜 index.html
 ┣ 📂 static
 ┃ ┗ 📜 style.css
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
```

---

## ▶️ Installation

```
git clone https://github.com/Aditiyakesavaraj/Chatbot-for-Sim-Plan-Details.git
cd Chatbot-for-Sim-Plan-Details
pip install -r requirements.txt
python3 app.py
```

👉 Open: http://127.0.0.1:5000/

---

## 📦 requirements.txt

```
Flask==3.0.3
```

---

## 🌐 Deployment

### 🚀 Render

* Build Command:

```
pip install -r requirements.txt
```

* Start Command:

```
python3 app.py
```

---

### 🚀 Railway

* Start Command:

```
python3 app.py
```

---

## ⚙️ How It Works

1️⃣ User enters:

```
Jio 300 28 days
```

2️⃣ Chatbot:

* Extracts values using regex
* Identifies SIM
* Queries database

3️⃣ Output:

```
Data: 2GB/day, Validity: 28 days, Price: ₹299
```

---

## 💡 Example Inputs

* Airtel 299 28 days
* Jio 500 56 days
* VI 200 14 days

---

## ⚠️ Limitations

* Needs structured input
* Static database
* Limited providers

---

## 🔮 Future Improvements

* 🤖 NLP-based chatbot
* 🌐 Live telecom APIs
* 📱 Mobile app
* 🎙️ Voice assistant

---

## 👨‍💻 Author

**Aditiya Kesavaraj**

---

## ⭐ Support

If you like this project:

* ⭐ Star this repo
* 🍴 Fork it
* 🚀 Share it
