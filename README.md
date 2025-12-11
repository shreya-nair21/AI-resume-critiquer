📝 TestSpace – Online Exam Portal

A fully functional, web-based online examination system built using Django. TestSpace allows students to attempt exams smoothly and enables administrators to create, manage, and evaluate tests with ease.

---

🚀 Features
👤 User Management

Student login & registration

Secure authentication

Role-based access (Admin / Student)

📝 Exam System

Create and manage exams

Supports MCQs & descriptive questions

Timer-based exams with auto-submission

Random question ordering (optional)

📊 Results & Evaluation

Automatic scoring for MCQs

Submission records for each exam

Student-wise and exam-wise result views

🎨 UI / UX

Clean, responsive design

Dashboard for Students & Admin

---

🛠 Tech Stack

Backend: Django, Python

Frontend: HTML, CSS, Bootstrap

Database: SQLite (local) / PostgreSQL (Render)

Deployment: Render

Version Control: Git + GitHub

---

🖥️ Live Demo

Check out the deployed app here:
👉 https://testspace-yjyp.onrender.com

---

💻 Run Locally
1. Clone the repository
git clone https://github.com/<your-username>/TestSpace
cd TestSpace

2. Install dependencies
pip install -r requirements.txt

3. Set environment variables

Create a .env file:

SECRET_KEY=your_secret_key_here
DEBUG=True

4. Apply migrations
python manage.py migrate

5. Start the development server
python manage.py runserver


Visit: http://127.0.0.1:8000/

---

🚢 Deployment (Render)

Add environment variables:

SECRET_KEY=your_secret_key_without_quotes
DEBUG=False


Add your Render domain to ALLOWED_HOSTS

Use:

gunicorn testspace.wsgi


as the start command

Configure static files with STATIC_ROOT and collectstatic

---

👩‍💻 Author
Shreya Nair

---
