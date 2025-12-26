from flask import Flask, request, jsonify
from flask_cors import CORS
from database import init_db, get_db
from models import Task
import whisper
import os
import tempfile

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Initialize database on first run
init_db()

# Load Whisper model (using 'base' model for balance of speed and accuracy)
# First run will download the model (~140MB)
print("Loading Whisper model...")
whisper_model = whisper.load_model("base")
print("Whisper model loaded successfully!")

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM tasks ORDER BY created_at DESC')
        rows = cursor.fetchall()
        db.close()

        tasks = []
        for row in rows:
            task = Task(
                id=row['id'],
                title=row['title'],
                description=row['description'],
                completed=row['completed'],
                created_at=row['created_at']
            )
            tasks.append(task.to_dict())

        return jsonify(tasks), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    try:
        data = request.get_json()

        if not data or 'title' not in data:
            return jsonify({'error': 'Title is required'}), 400

        title = data.get('title')
        description = data.get('description', '')

        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'INSERT INTO tasks (title, description) VALUES (?, ?)',
            (title, description)
        )
        db.commit()

        task_id = cursor.lastrowid

        # Fetch the created task
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        row = cursor.fetchone()
        db.close()

        task = Task(
            id=row['id'],
            title=row['title'],
            description=row['description'],
            completed=row['completed'],
            created_at=row['created_at']
        )

        return jsonify(task.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task by ID"""
    try:
        db = get_db()
        cursor = db.cursor()

        # Check if task exists
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        task = cursor.fetchone()

        if not task:
            db.close()
            return jsonify({'error': 'Task not found'}), 404

        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        db.commit()
        db.close()

        return jsonify({'message': 'Task deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a task (toggle completion)"""
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No data provided'}), 400

        db = get_db()
        cursor = db.cursor()

        # Check if task exists
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        task = cursor.fetchone()

        if not task:
            db.close()
            return jsonify({'error': 'Task not found'}), 404

        # Update completed status
        completed = data.get('completed', task['completed'])
        cursor.execute(
            'UPDATE tasks SET completed = ? WHERE id = ?',
            (completed, task_id)
        )
        db.commit()

        # Fetch updated task
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        row = cursor.fetchone()
        db.close()

        updated_task = Task(
            id=row['id'],
            title=row['title'],
            description=row['description'],
            completed=row['completed'],
            created_at=row['created_at']
        )

        return jsonify(updated_task.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/transcribe', methods=['POST'])
def transcribe_audio():
    """Transcribe audio to text using Whisper"""
    try:
        # Check if audio file is present
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400

        audio_file = request.files['audio']

        if audio_file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        # Create a temporary file to save the audio
        with tempfile.NamedTemporaryFile(delete=False, suffix='.webm') as temp_audio:
            audio_file.save(temp_audio.name)
            temp_path = temp_audio.name

        try:
            # Transcribe using Whisper
            result = whisper_model.transcribe(temp_path)
            transcribed_text = result['text'].strip()

            return jsonify({
                'text': transcribed_text,
                'language': result.get('language', 'unknown')
            }), 200
        finally:
            # Clean up temporary file
            if os.path.exists(temp_path):
                os.remove(temp_path)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
