# Python-SQLAlchemy-CRUD-API (Task Manager)

This is a foundational backend web application built with Python's Flask framework to demonstrate mastery of essential **REST API** principles and **CRUD (Create, Read, Update, Delete)** operations. The application functions as a simple Task Manager, allowing users to track and manage items in a persistent database.

## Key Technologies & Concepts

| Category | Technology/Concept | 
 | ----- | ----- | 
| **Backend Framework** | **Flask** (Python) | 
| **Database/ORM** | **SQLAlchemy** (using SQLite) | 
| **Frontend Rendering** | **Jinja2** Templating Engine (HTML forms, no heavy JavaScript) | 
| **Data Handling** | Full CRUD implementation using standard HTTP GET/POST methods and form data (`request.form`). | 
| **Deployment** | Deployed to the cloud using **Heroku** and a **Gunicorn** production server. | 
| **Error Handling** | Implements custom error handling for **404 Not Found** exceptions when accessing non-existent record IDs. | 

## Application Functionality

The application provides a web interface where a user can:

1. **Create (C):** Add new tasks with a title and description via an HTML form.

2. **Read (R):** View a complete list of all tasks retrieved from the database.

3. **Update (U):** Navigate to a dedicated edit page (`/edit/<id>`) to modify existing data and save changes.

4. **Delete (D):** Permanently remove a task from the database.

## Installation and Local Setup

**To run this project locally, follow these steps:**

1. **Clone the Repository:** *https://github.com/aakankshabadgujar/Python-SQLAlchemy-CRUD-API.git*
