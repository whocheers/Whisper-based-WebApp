# Task Manager Web Application

A simple full-stack task management application built with React (Material-UI) and Flask (SQLite).

## Features

- Add new tasks with title and description
- View all tasks in a clean, responsive interface
- Delete tasks
- Persistent storage using SQLite database

## Project Structure

```
web_app_with_whisper/
├── backend/              # Flask REST API
│   ├── app.py           # Main Flask application
│   ├── database.py      # SQLite database layer
│   ├── models.py        # Task model
│   ├── requirements.txt # Python dependencies
│   └── instance/        # SQLite database location
├── frontend/            # React application
│   ├── public/          # Static files
│   ├── src/
│   │   ├── components/  # React components
│   │   ├── services/    # API service layer
│   │   └── App.js       # Main App component
│   └── package.json
└── README.md
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Flask server:
```bash
python app.py
```

The backend will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the React development server:
```bash
npm start
```

The frontend will run on `http://localhost:3000`

**Note:** If you're using Node.js version 12 or older, you may need to upgrade to Node.js 14 or higher to run the frontend.

## API Endpoints

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| GET | `/api/tasks` | Get all tasks | - |
| POST | `/api/tasks` | Create a new task | `{title, description}` |
| DELETE | `/api/tasks/:id` | Delete a task | - |
| PUT | `/api/tasks/:id` | Update a task | `{completed}` |

## Testing the Backend API

You can test the backend API using curl:

```bash
# Get all tasks
curl http://localhost:5000/api/tasks

# Create a new task
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "My Task", "description": "Task description"}'

# Delete a task
curl -X DELETE http://localhost:5000/api/tasks/1
```

## Future Enhancements

This application is designed to be extended with Whisper voice-to-text functionality for task creation. The modular architecture supports adding:
- Voice input component
- Speech-to-text endpoint using Whisper
- Audio recording functionality

## Technologies Used

### Backend
- **Flask** - Lightweight Python web framework
- **Flask-CORS** - Cross-Origin Resource Sharing support
- **SQLite** - Embedded database

### Frontend
- **React** - JavaScript library for building user interfaces
- **Material-UI** - React component library
- **Axios** - HTTP client for API calls

## License

This project is for educational purposes.
