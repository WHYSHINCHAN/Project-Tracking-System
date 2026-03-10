# Project Manager Web Application

A **Flask-based Project Management Web Application** that allows users to create accounts, log in securely, manage projects, and track tasks with deadlines. The application uses **Python (Flask)** for the backend and **MySQL** for database storage.

This project demonstrates concepts of **web development, authentication systems, session management, and database integration**.

---

## Features

### User Authentication
- User registration (Signup)
- User login
- Session-based authentication
- Logout functionality

### Project Management
- Create new projects
- Add project descriptions and deadlines
- View all projects created by the logged-in user

### Task Management
- Database schema supports task creation
- Tasks linked to projects and users

### Database Integration
- MySQL database
- Automatic table initialization
- Structured relational schema

---

## Tech Stack

**Backend**
- Python
- Flask

**Database**
- MySQL
- mysql-connector-python

**Frontend**
- HTML
- Jinja Templates

**Other Libraries**
- Regex (input validation)
- Flask sessions
- Flash messaging

---

## Project Structure

```
project-manager/
│
├── app.py
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── create_project.html
│   └── projects.html
│
└── README.md
```

---

## Database Schema

### Users Table

| Column | Type | Description |
|------|------|-------------|
| id | INT | Primary key |
| name | VARCHAR | User name |
| email | VARCHAR | Unique email |
| password | VARCHAR | User password |
| created_at | TIMESTAMP | Account creation time |

---

### Projects Table

| Column | Type | Description |
|------|------|-------------|
| id | INT | Primary key |
| title | VARCHAR | Project title |
| description | TEXT | Project details |
| deadline | DATE | Project deadline |
| user_id | INT | Owner of project |
| status | VARCHAR | Project status |
| progress | INT | Completion percentage |

---

### Tasks Table

| Column | Type | Description |
|------|------|-------------|
| id | INT | Primary key |
| title | VARCHAR | Task title |
| description | TEXT | Task details |
| deadline | DATE | Task deadline |
| status | VARCHAR | Task status |
| project_id | INT | Linked project |
| user_id | INT | Assigned user |

---

## Installation & Setup

### 1. Install Dependencies

```bash
pip install flask mysql-connector-python
```

---

### 2. Setup MySQL Database

Create a database in MySQL:

```sql
CREATE DATABASE project_manager;
```

Update credentials in `app.py`:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',
    'database': 'project_manager'
}
```

---

### 3. Run the Application

```bash
python app.py
```

The Flask server will start at:

```
http://127.0.0.1:5000
```

---

## Security Note

Passwords are currently stored as **plain text** for simplicity.

For production applications, implement:
- Password hashing (bcrypt)
- CSRF protection
- Input sanitization
- Secure session management

---

## Future Improvements

- Task creation and assignment
- Project progress tracking
- Dashboard analytics
- Password hashing
- Role-based access control
- REST API integration
- Responsive frontend UI

---

## Learning Outcomes

This project demonstrates:

- Flask routing
- Session management
- MySQL database integration
- CRUD operations
- Authentication systems
- Basic project management workflow
