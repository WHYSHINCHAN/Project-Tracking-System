-- Create the project_manager database if it doesn't exist
CREATE DATABASE IF NOT EXISTS project_manager;
USE project_manager;

-- Drop tables if they exist (for clean setup)
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS users;

-- Create users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create projects table
CREATE TABLE projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    deadline DATE NOT NULL,
    user_id INT NOT NULL,
    status VARCHAR(20) DEFAULT 'active',
    progress INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create tasks table
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    deadline DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    project_id INT NOT NULL,
    user_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Insert sample data

-- Sample users
INSERT INTO users (name, email, password) VALUES
('John Doe', 'john@example.com', 'password123'),
('Jane Smith', 'jane@example.com', 'password456'),
('Bob Johnson', 'bob@example.com', 'password789');

-- Sample projects
INSERT INTO projects (title, description, deadline, user_id, status, progress) VALUES
('Website Redesign', 'Redesign the company website with modern UI/UX principles', '2025-06-30', 1, 'active', 25),
('Mobile App Development', 'Create a cross-platform mobile app for project management', '2025-08-15', 1, 'active', 10),
('Database Migration', 'Migrate legacy database to new cloud infrastructure', '2025-05-20', 2, 'active', 50),
('Marketing Campaign', 'Launch Q2 marketing campaign for new product', '2025-04-30', 3, 'active', 75);

-- Sample tasks
INSERT INTO tasks (title, description, deadline, status, project_id, user_id) VALUES
('Design wireframes', 'Create wireframes for all main pages', '2025-05-15', 'completed', 1, 1),
('Implement homepage', 'Code the new homepage based on designs', '2025-06-01', 'pending', 1, 1),
('Implement user authentication', 'Set up secure login system', '2025-05-25', 'in-progress', 2, 1),
('Design database schema', 'Plan new database structure', '2025-04-25', 'completed', 3, 2),
('Data migration script', 'Write script to transfer data to new structure', '2025-05-10', 'in-progress', 3, 2),
('Create social media posts', 'Design and schedule promotional content', '2025-04-20', 'pending', 4, 3);

-- Create an index on commonly searched fields
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_project_user ON projects(user_id);
CREATE INDEX idx_task_project ON tasks(project_id);
CREATE INDEX idx_task_user ON tasks(user_id);
CREATE INDEX idx_project_status ON projects(status);
CREATE INDEX idx_task_status ON tasks(status);