# 🔐 Flask Authentication System (Login + Profile + Security)

A complete **Flask-based user authentication system** with secure login, signup, profile management, and account deletion features. This project demonstrates real-world backend development concepts such as authentication, session handling, CRUD operations, and password security using hashing.

---

## 🚀 Features

- 👤 User Registration (Signup)
- 🔐 Secure Login System
- 🧠 Session Management (Login/Logout)
- ⏳ "Remember Me" Login Feature
- 📊 User Dashboard (Protected Route)
- 👤 Profile Page (User Info Display)
- ✏️ Edit Profile (Update Username)
- 🗑️ Secure Account Deletion (Type "DELETE" confirmation)
- 💬 Flash Messages (Success / Error notifications)
- 🔒 Password Hashing using Werkzeug
- 🎨 Modern UI with Glassmorphism Design
- 🗄️ SQLite Database Integration

---

## 🛠 Tech Stack

- Python 🐍
- Flask 🌐
- SQLite 🗄️
- HTML5 🧾
- CSS3 🎨
- Werkzeug Security 🔐

---

## 📁 Project Structure
FLASK-LOGIN-PROJECT/
│
├── app.py # Main Flask application
├── users.db # SQLite database (auto-generated)
├── requirements.txt # Project dependencies
├── README.md # Project documentation
│
├── templates/ # HTML pages
│ ├── login.html
│ ├── signup.html
│ ├── dashboard.html
│ ├── profile.html
│ ├── edit_profile.html
│ └── delete_account.html and more
│
├── static/ # Static files
│ ├── style.css
│ └──homepage.png
│ ├── login.png
│ ├── delete account.png
│ └── profile.png

📸 Screenshots
🔐 Login Page
📊 Dashboard
👤 Profile Page

🧠 How It Works
User registers via signup page
Password is securely hashed before saving in database
User logs in and session is created
Protected routes (dashboard/profile) require login
User can update profile details
User can delete account using safe confirmation system
Logout clears session


🗑️ Secure Delete Account Feature
To prevent accidental deletion:
User must type DELETE
System validates input
Only then account is permanently removed

🔒 Security Features
Password hashing using Werkzeug
Session-based authentication
Protected routes (login required)
Input validation for sensitive actions

🚀 Future Improvements
📧 Email verification system
🔑 Password reset via email
🧑‍💼 Admin dashboard panel
🗄️ PostgreSQL / MySQL integration
🌐 REST API version (Flask API)
📱 Responsive mobile UI improvements
📌 Learning Outcomes

This project helps understand:
Flask routing system
Authentication flow
Database operations (CRUD)
Session management
Secure password storage
Frontend-backend integration

👨‍💻 Author
Built by Techy-Ahmad as a learning + portfolio project in Flask backend development.

⭐ Support

If you like this project:
Give it a ⭐ on GitHub
Fork it and improve it
Use it in your portfolio

📜 License
This project is open-source and free to use for learning purposes.
