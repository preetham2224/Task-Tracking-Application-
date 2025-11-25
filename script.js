
const TaskManager = {

    async loadTasks(filter = 'all', userId = null) {
        let url = `/api/tasks?filter=${filter}`;
        if (filter === 'assigned_to_me' && userId) {
            url += `&user_id=${userId}`;
        }
        
        try {
            const response = await fetch(url);
            return await response.json();
        } catch (error) {
            console.error('Error loading tasks:', error);
            return [];
        }
    },

    async createTask(taskData) {
        try {
            const response = await fetch('/api/tasks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(taskData)
            });
            return await response.json();
        } catch (error) {
            console.error('Error creating task:', error);
            throw error;
        }
    },

    async updateTaskStatus(taskId, status) {
        try {
            const response = await fetch(`/api/tasks/${taskId}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ status })
            });
            return await response.json();
        } catch (error) {
            console.error('Error updating task:', error);
            throw error;
        }
    },

    async deleteTask(taskId) {
        try {
            const response = await fetch(`/api/tasks/${taskId}`, {
                method: 'DELETE'
            });
            return await response.json();
        } catch (error) {
            console.error('Error deleting task:', error);
            throw error;
        }
    },

    async getUsers() {
        try {
            const response = await fetch('/api/users');
            return await response.json();
        } catch (error) {
            console.error('Error loading users:', error);
            return [];
        }
    }
};

function formatDate(dateString) {
    if (!dateString) return 'No due date';
    const date = new Date(dateString);
    return date.toLocaleDateString();
}

function showNotification(message, type = 'success') {
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.textContent = message;
    
    document.querySelector('.container').prepend(alert);
    
    setTimeout(() => {
        alert.remove();
    }, 3000);
}

const TaskManager = {

    async loadTasks(filter = 'all', userId = null) {
        let url = `/api/tasks?filter=${filter}`;
        if (filter === 'assigned_to_me' && userId) {
            url += `&user_id=${userId}`;
        }
        
        try {
            const response = await fetch(url);
            return await response.json();
        } catch (error) {
            console.error('Error loading tasks:', error);
            return [];
        }
    },

    async createTask(taskData) {
        try {
            const response = await fetch('/api/tasks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(taskData)
            });
            return await response.json();
        } catch (error) {
            console.error('Error creating task:', error);
            throw error;
        }
    },

    async updateTaskStatus(taskId, status) {
        try {
            const response = await fetch(`/api/tasks/${taskId}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ status })
            });
            return await response.json();
        } catch (error) {
            console.error('Error updating task:', error);
            throw error;
        }
    },

    async completeTask(taskId) {
        try {
            const response = await fetch(`/api/tasks/${taskId}/complete`, {
                method: 'POST'
            });
            return await response.json();
        } catch (error) {
            console.error('Error completing task:', error);
            throw error;
        }
    },

    async deleteTask(taskId) {
        try {
            const response = await fetch(`/api/tasks/${taskId}`, {
                method: 'DELETE'
            });
            return await response.json();
        } catch (error) {
            console.error('Error deleting task:', error);
            throw error;
        }
    },

    async getUsers() {
        try {
            const response = await fetch('/api/users');
            return await response.json();
        } catch (error) {
            console.error('Error loading users:', error);
            return [];
        }
    }
};

function formatDate(dateString) {
    if (!dateString) return 'No due date';
    const date = new Date(dateString);
    return date.toLocaleDateString();
}

function showNotification(message, type = 'success') {
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.textContent = message;
    
    document.querySelector('.container').prepend(alert);
    
    setTimeout(() => {
        alert.remove();
    }, 3000);
}


function quickCompleteTask(taskId, button) {
    if (confirm('Mark this task as completed?')) {
        button.disabled = true;
        button.textContent = 'Completing...';
        
        TaskManager.completeTask(taskId)
            .then(task => {
                showNotification('Task completed successfully!');
    
                const taskCard = document.getElementById(`task-${taskId}`);
                if (taskCard) {
                    taskCard.classList.add('done');
                    taskCard.querySelector('.status-badge').textContent = 'done';
                    taskCard.querySelector('.status-badge').className = 'status-badge done';
                    button.remove();
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showNotification('Error completing task', 'error');
                button.disabled = false;
                button.textContent = 'Complete Task';
            });
    }
}