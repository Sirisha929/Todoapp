**TODOAPP**
A simple and user-friendly Task Manager web application built with Python (Flask), SQLite, and HTML/CSS. This app allows users to add, edit, delete, and view tasks with due dates and priority levels. The app features a sleek dark mode design and uses Flask’s server-side rendering with Jinja templates.
Steps I have followed for Creating this Project:
I created the project structure
I organized the project into folders and files using the following structure:
todo-app/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── edit.html
└── static/
    └── style.css
I built the Flask backend logic
In app.py, I implemented route handlers to:

Display all tasks (/)

Add new tasks (/add)

Delete tasks by ID (/delete/<id>)

Edit tasks (/edit/<id>)
I also initialized a SQLite database and used SQL queries to manage task data.

I designed the user interface with HTML and Jinja
I used index.html to show the task list and add-task form, and edit.html for updating existing tasks. I utilized Jinja templating to loop through and render dynamic content.

I styled the app with CSS and added dark mode
I wrote custom styles in style.css to give the app a dark theme. I styled the input fields, buttons, and tables for better usability and modern look.

I installed dependencies and ran the app locally
I created a virtual environment, installed Flask using requirements.txt, and started the app with python app.py. I tested it on http://127.0.0.1:5000 and confirmed all features work: add, edit, delete, and view tasks. 

output:

