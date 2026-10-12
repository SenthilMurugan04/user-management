
# User Management REST API

## Project Description
A beginner-friendly REST API developed using Python, FastAPI,
Pydantic, SQLAlchemy, and SQLite.

The API supports creating, viewing, updating, deleting, and
filtering users.

## Technologies
- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Swagger UI

## Installation
1. Create and activate a virtual environment.
2. Install dependencies:

   pip install -r requirements.txt

3. Start the application:

   uvicorn main:app --reload

4. Open Swagger UI:

   http://127.0.0.1:8000/docs

## Database
SQLite database: users.db
Table: users

Fields:
- id
- name
- email
- age
- city
- is_active

The database and table are created automatically
when the application starts.

## API Endpoints

| Method | Endpoint | Purpose |
| POST | /users | Create user |
| GET | /users | Get all users |
| GET | /users/{user_id} | Get user by ID |
| PUT | /users/{user_id} | Update user |
| DELETE | /users/{user_id} | Delete user |

## Bonus Filtering
- GET /users?city=Coimbatore
- GET /users?is_active=true

## Validation
- Name is required.
- Email must be valid and unique.
- Age must be between 18 and 60.
- City is required.
- Missing users return HTTP 404.
- Duplicate emails return HTTP 400.
- Invalid request data returns HTTP 422.

## Database Persistence
User records are stored in users.db and remain
available after restarting the application.
