# Task Management API

## Overview

This is a REST API for managing tasks, built using Django REST Framework (DRF). It provides CRUD functionality for creating, retrieving, updating, and deleting tasks.

## Features

- Create a task
- Retrieve all tasks
- Retrieve a single task
- Update a task (including status updates)
- Delete a task

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite (default, can be changed to PostgreSQL/MySQL)

## Installation

### Prerequisites

Make sure you have Python installed (>=3.7).

### Setup

1. **Clone the repository**

```sh
 git clone <repository-url>
 cd <repository-folder>
```

2. **Create a virtual environment**

```sh
 python -m venv venv
 source venv/bin/activate  # On macOS/Linux
 venv\Scripts\activate  # On Windows
```

3. **Install dependencies**

```sh
 pip install -r requirements.txt
```

4. **Run migrations**

```sh
 python manage.py migrate
```

5. **Start the development server**

```sh
 python manage.py runserver
```

## API Endpoints

### 1. Create a Task

**POST** `/tasks/`

#### Request Body:

```json
{
  "title": "Complete project",
  "description": "Submit the project by EOD"
}
```

#### Response:

```json
{
  "id": 1,
  "title": "Complete project",
  "description": "Submit the project by EOD",
  "status": "pending"
}
```

### 2. Get All Tasks

**GET** `/tasks/`

#### Response:

```json
[
  {
    "id": 1,
    "title": "Complete project",
    "description": "Submit the project by EOD",
    "status": "pending"
  }
]
```

### 3. Get a Single Task

**GET** `/tasks/{id}/`

#### Response:

```json
{
  "id": 1,
  "title": "Complete project",
  "description": "Submit the project by EOD",
  "status": "pending"
}
```

### 4. Update a Task

**PUT** `/tasks/{id}/`

#### Request Body:

```json
{
  "status": "completed"
}
```

#### Response:

```json
{
  "id": 1,
  "title": "Complete project",
  "description": "Submit the project by EOD",
  "status": "completed"
}
```

### 5. Delete a Task

**DELETE** `/tasks/{id}/`

#### Response:

**204 No Content**

## Testing the API

- Use **Postman** or **cURL** for testing.
- Django’s **Browsable API** is enabled for easy testing via the browser.

## Error Handling

- `400 Bad Request`: Invalid input data.
- `404 Not Found`: Task does not exist.
- `500 Internal Server Error`: Unexpected server errors.

##

