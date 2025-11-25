from flask import Flask, render_template, request, jsonify, redirect, url_for
from models import db, User, Task
from datetime import datetime
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

db.init_app(app)
def init_db():
    with app.app_context():
        db.create_all()

        if User.query.count() == 0:
            users = [
                User(username='preetham', email='preetham@example.com'),
                User(username='chandan', email='chandan@example.com'),
                User(username='sharath', email='sharath@example.com'),
                User(username='preetham', email='preetham@example.com'),
                User(username='chandan', email='chandan@example.com'),
                User(username='sharath', email='sharath@example.com'),      
              
            ]
            db.session.bulk_save_objects(users)
            db.session.commit()

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    filter_type = request.args.get('filter', 'all')
    user_id = request.args.get('user_id', type=int)
    query = Task.query   
    if filter_type == 'completed':
        query = query.filter(Task.status == 'done')
    elif filter_type == 'assigned_to_me' and user_id:
        query = query.filter(Task.assignee_id == user_id)   
    tasks = query.order_by(Task.created_at.desc()).all()
    return jsonify([task.to_dict() for task in tasks])

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify(task.to_dict())

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    
    due_date = None
    if data.get('due_date'):
        due_date = datetime.strptime(data['due_date'], '%Y-%m-%d').date()
    
    task = Task(
        title=data['title'],
        description=data.get('description', ''),
        assignee_id=data.get('assignee_id'),
        due_date=due_date
    )
    
    db.session.add(task)
    db.session.commit()
    
    return jsonify(task.to_dict()), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    
    due_date = None
    if data.get('due_date'):
        due_date = datetime.strptime(data['due_date'], '%Y-%m-%d').date()
    
    task.title = data['title']
    task.description = data.get('description', '')
    task.assignee_id = data.get('assignee_id')
    task.due_date = due_date
    task.updated_at = datetime.utcnow()
    
    db.session.commit()
    return jsonify(task.to_dict())

@app.route('/api/tasks/<int:task_id>', methods=['PATCH'])
def patch_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    
    if 'status' in data:
        task.status = data['status']
    
    task.updated_at = datetime.utcnow()
    db.session.commit()
    
    return jsonify(task.to_dict())
@app.route('/api/tasks/<int:task_id>/complete', methods=['POST'])
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.mark_complete()
    db.session.commit()
    
    return jsonify(task.to_dict())

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    
    return jsonify({'message': 'Task deleted successfully'})
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])
@app.route('/')
def task_list():
    users = User.query.all()
    return render_template('tasks.html', users=users)

@app.route('/tasks/add')
def add_task_form():
    users = User.query.all()
    return render_template('add_task.html', users=users)

@app.route('/tasks/<int:task_id>')
def task_detail(task_id):
    task = Task.query.get_or_404(task_id)
    users = User.query.all()
    return render_template('task_detail.html', task=task, users=users)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)