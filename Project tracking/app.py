from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import mysql.connector
from mysql.connector import Error
import re
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# Configure secret key for session
app.secret_key = os.urandom(24)

# Configure MySQL
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'tiger',  # Set your database password here
    'database': 'project_manager'
}

conn = mysql.connector.connect(**DB_CONFIG)


# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        email = request.form['email']
        password = request.form['password']
        
        # Create cursor
        cur = conn.cursor()
        
        # Execute query
        cur.execute("SELECT * FROM users WHERE email = %s", [email])
        user = cur.fetchone()
        
        # Close connection
        
        # Check if user exists and password is correct
        if user and user[3] == password:  # In production, use proper password hashing
            # Create session data
            session['logged_in'] = True
            session['user_id'] = user[0]
            session['username'] = user[1]
            
            flash('Login successful', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid login credentials', 'danger')
            
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        # Validate input
        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return render_template('signup.html')
        
        # Check if email is valid
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address', 'danger')
            return render_template('signup.html')
        
        # Create cursor
        cur = conn.cursor()
        
        # Check if email already exists
        cur.execute("SELECT * FROM users WHERE email = %s", [email])
        user = cur.fetchone()
        
        if user:
            flash('Email already exists', 'danger')
            cur.close()
            return render_template('signup.html')
        
        # Insert user
        cur.execute("INSERT INTO users(name, email, password) VALUES(%s, %s, %s)", (name, email, password))
        
        # Commit to DB
        conn.commit()
        
        # Close connection
        cur.close()
        
        flash('Registration successful. You can now login', 'success')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    # Check if user is logged in
    if 'logged_in' in session:
        return render_template('dashboard.html', username=session.get('username', 'User'))
    
    flash('Please login to access dashboard', 'danger')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'success')
    return redirect(url_for('login'))

@app.route('/create-project', methods=['GET', 'POST'])
def create_project():
    if 'logged_in' not in session:
        flash('Please login to create a project', 'danger')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Get form data
        title = request.form['title']
        description = request.form['description']
        deadline = request.form['deadline']
        
        # Create cursor
        cur = conn.cursor()
        
        # Insert project
        cur.execute("INSERT INTO projects(title, description, deadline, user_id) VALUES(%s, %s, %s, %s)", 
                   (title, description, deadline, session['user_id']))
        
        # Commit to DB
        conn.commit()
        
        # Close connection
        cur.close()
        
        flash('Project created successfully', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('create_project.html')

# Helper function to initialize database
def init_db():
    # Create cursor
    cur =conn.cursor(dictionary=True)
    
    # Check if users table exists, if not create it
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            password VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Check if projects table exists, if not create it
    cur.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            description TEXT,
            deadline DATE,
            user_id INT,
            status VARCHAR(20) DEFAULT 'active',
            progress INT DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    
    # Check if tasks table exists, if not create it
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            description TEXT,
            deadline DATE,
            status VARCHAR(20) DEFAULT 'pending',
            project_id INT,
            user_id INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (project_id) REFERENCES projects(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
@app.route('/projects')
def projects():
    # Check if user is logged in
            if 'logged_in' not in session:
                flash('Please login to view projects', 'danger')
                return redirect(url_for('login'))
    # Create cursor
            cur = conn.cursor(dictionary=True)
    
    # Get all projects for the current user
            cur.execute("SELECT * FROM projects WHERE user_id = %s ORDER BY deadline", [session['user_id']])
            projects = cur.fetchall()
    # Close connection
            cur.close()
            return render_template('projects.html', projects=projects, username=session.get('username', 'User'))


if __name__ == '__main__':
    app.run(debug=True)
