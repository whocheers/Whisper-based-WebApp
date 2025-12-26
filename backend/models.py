class Task:
    """Task model for JSON serialization"""

    def __init__(self, id, title, description, completed, created_at):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at

    def to_dict(self):
        """Convert task to dictionary for JSON response"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': bool(self.completed),
            'created_at': self.created_at
        }
