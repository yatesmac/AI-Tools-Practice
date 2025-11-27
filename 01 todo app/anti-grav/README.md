# Django ToDo App

A simple, robust ToDo application built with Django and Tailwind CSS.

## Features

- **Create Tasks**: Add new tasks with titles, descriptions, and due dates.
- **Manage Status**: Toggle tasks between "Pending" and "Completed".
- **Edit & Delete**: Update task details or remove them permanently.
- **Responsive Design**: Works on desktop and mobile devices.

## Getting Started

### Prerequisites

- Python 3.x installed
- Git (optional, for cloning)

### Installation

1.  **Clone or Download** the project to your local machine.
2.  **Navigate** to the project directory:
    ```powershell
    cd "path\to\01-ToDo App"
    ```
3.  **Create and Activate Virtual Environment**:
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```
4.  **Install Dependencies**:
    ```powershell
    pip install django
    ```
5.  **Apply Migrations**:
    ```powershell
    python manage.py migrate
    ```

### Running the App

1.  **Start the Development Server**:
    ```powershell
    python manage.py runserver
    ```
2.  **Open in Browser**:
    Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

- **Add a Task**: Click the "Add New Task" button in the navigation bar.
- **Mark as Complete**: Click the status badge ("Pending"/"Completed") on any task to toggle its status.
- **Edit/Delete**: Use the "Edit" and "Delete" links next to each task.
