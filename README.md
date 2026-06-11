<div align="center">
    <img src="https://res.cloudinary.com/diwkfbsgv/image/upload/v1781154801/772067f0-7234-4537-abbd-06770a3b8fce_rn2ra4.png" alt="banner_img">
    <h1>Trackr</h1>
</div>

<br />

A CLI tool that manages a simulated multi-user project tracking system.

## Features

- Admins can manage users and projects
- Each user can have one or more projects
- Each project can have one or more tasks
- CLI commands to add, view and update users, projects and tasks:

```shell
add-user --name "Alex"
add-project --user "Alex" --title "CLI Tool"
add-task --project "CLI Tool" --title "Implement add task"
```

## System design

The project has three class objects that are in one way or the other interconnected. These classes being:

- Users: name, email
- Projects: title, description, due_date
- Tasks: title, status, assigned_to

with their corresponding attributes listed to the side of each.

Users can have multiple Projects, with the project belonging only to one user (A one to many relationship). Similarly, a Project can have multiple tasks but a task can only belong to a single project.

The project uses JSON for saving and loading users, projects and tasks to ensure data persistence.

## Project structure

```
.
├── data/                               # Local JSON or CSV files
├── models/                             # Class definitions
├── utils/                              # Helper functions and utilities
├── .gitignore                          # Git ignore rules
├── main.py                             # Main entry point for CLI
├── README.md                           # Project documentation
└── requirements.txt                    # Project dependencies
```
