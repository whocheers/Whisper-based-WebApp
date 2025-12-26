# Task Manager Web Application with Whisper Voice-to-Text

A full-stack task management application built with React (Material-UI) and Flask (SQLite), featuring OpenAI Whisper integration for voice-to-text task creation.

## Features

- Add new tasks with title and description
- **Voice-to-text input** using OpenAI Whisper for task descriptions
- View all tasks in a clean, responsive interface
- Delete tasks
- Persistent storage using SQLite database
- **Fully Dockerized** for reproducible environments

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

### Option 1: Docker (Recommended)

**Prerequisites:**
- Docker Engine 20.10+
- Docker Compose 1.29+

**Quick Start:**

1. Clone the repository and navigate to the project directory

2. Build and run with docker-compose:
```bash
docker-compose up --build
```

3. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000

**Docker Features:**
- ✅ Multi-stage builds for optimized image sizes
- ✅ Automatic Whisper model download at build time
- ✅ FFmpeg pre-installed for audio processing
- ✅ Health checks for both services
- ✅ Persistent database with volume mounts
- ✅ Production-ready nginx configuration

**Docker Commands:**
```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild after code changes
docker-compose up --build

# Remove all containers and volumes
docker-compose down -v
```

### Option 2: Manual Setup

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
| POST | `/api/transcribe` | Transcribe audio to text | `multipart/form-data` with audio file |

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

## Technologies Used

### Backend
- **Flask** - Lightweight Python web framework
- **Flask-CORS** - Cross-Origin Resource Sharing support
- **SQLite** - Embedded database
- **OpenAI Whisper** - Speech-to-text model
- **FFmpeg** - Audio/video processing

### Frontend
- **React** - JavaScript library for building user interfaces
- **Material-UI** - React component library
- **Axios** - HTTP client for API calls
- **MediaRecorder API** - Browser audio recording

### DevOps
- **Docker** - Containerization platform
- **Docker Compose** - Multi-container orchestration
- **Nginx** - Web server for production frontend serving

## License

This project is for educational purposes.
