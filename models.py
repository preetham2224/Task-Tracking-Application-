from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tasks_assigned = db.relationship('Task', backref='assignee', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default='todo')  # todo, in-progress, done
    due_date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    assignee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'assignee_id': self.assignee_id,
            'assignee_name': self.assignee.username if self.assignee else 'Unassigned'
        }
    def mark_complete(self):
        """Helper method to mark task as completed"""
        self.status = 'done'
        self.updated_at = datetime.utcnow()
        return self