"""
Task data management and storage
"""
import json
import os
from utils import ensure_data_directory

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.data_file = "data/tasks.json"
        ensure_data_directory()
        
    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.tasks = json.load(f)
                
    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.tasks, f)
            
    def add_task(self, text):
        """Add a new task"""
        task = {
            'id': len(self.tasks),
            'text': text,
            'completed': False
        }
        self.tasks.append(task)
        self.save_tasks()
        
    def delete_task(self, task_id):
        """Delete a task by ID"""
        self.tasks = [t for t in self.tasks if t['id'] != task_id]
        self.save_tasks()
        
    def toggle_task(self, task_id):
        """Toggle task completion status"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = not task['completed']
                break
        self.save_tasks()
        
    def get_tasks(self):
        """Return all tasks"""
        return self.tasks