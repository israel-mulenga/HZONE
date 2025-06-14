# HZone Project

## Description

HZone is a web application developed with Django, featuring user authentication, core functionalities potentially related to property listings or zones, and a real-time messaging system.

## Prerequisites

*   Python (version 3.10+ recommended)
*   Django (version 5.2, as specified in `requirements.txt`)
*   Other dependencies as listed in `requirements.txt` (including `channels` for real-time features and `pillow` for image handling)

## Setup and Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository_url>
    cd hzone
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r ../requirements.txt 
    ```
    *(Note: If `README.md` is in `hzone/`, `requirements.txt` is one level up)*
4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

## Running the Development Server

1.  Start the Django development server:
    ```bash
    python manage.py runserver
    ```
2.  Open your web browser and navigate to `http://127.0.0.1:8000/`.


## Project Structure Overview

*   **`authentification/`**: Django app for user authentication and management.
*   **`hzone_app/`**: Main Django app for HZone's core features (e.g., listings).
*   **`messagerie/`**: Django app for real-time messaging functionalities.
*   **`hzone/`**: Project-level Django configuration and settings.
*   **`static/`**: Default location for static files collected by `collectstatic` is `staticfiles/` at the root of the hzone Django project directory. Project-level static files (CSS, JavaScript, images) can be placed in `hzone/static/hzone/`.
    *   Each app also has its own `static/<app_name>/` directory for app-specific static files (e.g., `hzone_app/static/hzone_app/`).
*   **`media/`**: Directory for user-uploaded files, configured at the root of the hzone Django project directory.
*   **`templates/`**: Each app has a `templates/<app_name>/` directory for its HTML templates. The project also has `hzone/hzone/templates/hzone/` for base templates.
*   **`manage.py`**: Django's command-line utility for running management commands.
*   **`../requirements.txt`**: Lists Python package dependencies (located in the parent directory of this README).
*   **`db.sqlite3`**: SQLite database file (for development).
```
