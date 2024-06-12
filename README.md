# Todo-FFTC

Todo-FFTC is a simple and intuitive todo list application developed using Python and Django. This mini-project was created for learning purposes by following a tutorial from a YouTuber. The goal was to gain hands-on experience with Django and understand the fundamentals of web development.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features
- **Add Tasks**: Easily add new tasks to your todo list.
- **Edit Tasks**: Update task details as needed.
- **Delete Tasks**: Remove tasks that are no longer needed.
- **Mark Complete**: Mark tasks as completed.

## Requirements
- Python 3.x
- Django

## Installation
To install and run the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/manoj-323/todo-FFTC.git
   cd todo-FFTC
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage
- **Add Task**: Use the input field to add a new task to your todo list.
- **Edit Task**: Click on a task to edit its details.
- **Delete Task**: Click the delete button next to a task to remove it.
- **Mark Complete**: Click the checkbox next to a task to mark it as completed.

## Project Structure
- `app/`: Contains the Django application code.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django's command-line utility for administrative tasks.
- `requirements.txt`: List of dependencies.

## Contributing
We welcome contributions! If you have suggestions, bug reports, or improvements, feel free to submit a pull request or open an issue.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
This project was created by following a tutorial from a YouTuber. It was developed purely for learning purposes and to gain a better understanding of Django and web development.
