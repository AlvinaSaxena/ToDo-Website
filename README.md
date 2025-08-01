## ✅ ToDo‑Website
A full‑stack 🧠 Flask-based To‑Do List Web App to manage daily tasks 📝
Create, mark complete ✅, and delete ❌ tasks in a simple, responsive interface.

## 🚀 Features
➕ Add new tasks

✅ Mark tasks as completed

🗑️ Delete tasks

📂 View active & completed tasks separately

🧱 Uses SQLite for lightweight database storage

🎨 Clean UI with HTML, CSS, and JavaScript

## 🛠️ Tech Stack
Layer	Technology Used
💻 Frontend	HTML5, CSS3, JavaScript
🐍 Backend	Python with Flask
🗄️ Database	SQLite (todo.db)
🧩 Templating	Jinja2 (via Flask templates)

## 🧱 System Architecture
pgsql
Copy
Edit
User ↔️ Browser ↔️ Flask Server ↔️ SQLite DB
       HTML/CSS/JS   |    app.py   |   todo.db
## 📦 Installation
Clone the repo:

bash
Copy
Edit
git clone https://github.com/AlvinaSaxena/ToDo-Website.git
cd ToDo-Website
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install flask
## 📁 Project Structure
bash
Copy
Edit
ToDo-Website/
├── app.py             # 🎯 Main Flask application
├── todo.db            # 🧾 SQLite DB file
├── templates/         # 🖼️ HTML templates
│   ├── index.html     # ➕ Task input page
│   └── completed.html # ✅ Completed tasks
└── README.md          # 📘 Project documentation
## ▶️ Running the App
Start the Flask server:

bash
Copy
Edit
python app.py
Then visit: 🌐 http://localhost:5000

You can now:

Add tasks ✍️

Mark them as done ✅

View completed ones ✔️

Remove tasks 🗑️

## 🧪 Usage Example
In app.py, the following routes are defined:

/ → Home page, task input

/complete/<int:task_id> → Mark a task complete

/delete/<int:task_id> → Delete a task

/completed → View completed tasks

All interactions dynamically update the todo.db file.

## 🤝 Contributing
🍴 Fork this repo

🛠️ Create your feature branch (git checkout -b feature/YourFeature)

✅ Commit your changes (git commit -m 'Add new feature')

🚀 Push to the branch (git push origin feature/YourFeature)

📝 Open a Pull Request

## 👩‍💻 Author
Alvina Saxena
🔗 GitHub Profile

## 🙌 Acknowledgements
🌐 Flask — Micro web framework for Python

🛢️ SQLite — Lightweight local DB

🎨 Frontend design with HTML, CSS, and JS

💡 Inspiration from minimal productivity tools

