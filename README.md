# Task Tracker Application

A full-stack web application designed to track tasks, manage assignments, and monitor project progress. This project features a **RESTful API** backend built with Flask and a dynamic, responsive frontend using vanilla JavaScript and the Fetch API.

##  Features

* **Task Management:** Full CRUD capabilities (Create, Read, Update, Delete) for tasks.
* **Dynamic Filtering:** Filter tasks by "All", "Assigned to Me", or "Completed" without page reloads.
* **User Assignment:** Assign tasks to specific users (comes with pre-seeded users: Preetham, Chandan, Sharath).
* **Status Tracking:** Visual indicators for task status (To Do, In Progress, Done).
* **Responsive Design:** Clean, card-based UI styled with CSS variables and Flexbox/Grid.
* **REST API:** Custom-built backend API handling JSON data.

##  Tech Stack

* **Backend:** Python 3, Flask, SQLAlchemy (ORM)
* **Database:** SQLite
* **Frontend:** HTML5, CSS3, JavaScript (ES6+)
* **API Communication:** JavaScript Fetch API

##  Project Structure

```text
├── static/
│   ├── style.css       # Custom styling and CSS variables
│   └── script.js       # Frontend logic and API calls
├── templates/
│   ├── base.html       # Master layout template
│   ├── tasks.html      # Main dashboard (Task List)
│   ├── add_task.html   # Task creation form
│   └── task_detail.html# Individual task view
├── app.py              # Flask application and API routes
├── models.py           # Database models (User, Task)
├── requirements.txt    # Python dependencies
└── tasks.db            # SQLite database (generated on first run)
