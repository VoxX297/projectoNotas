"""
Main application window and UI setup
"""
import tkinter as tk
from tkinter import ttk, messagebox
from task_manager import TaskManager
from widgets import TaskFrame, InputFrame
from styles import *

class TaskListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task List")
        self.root.geometry("400x600")
        self.root.minsize(300, 400)
        
        self.task_manager = TaskManager()
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the main UI components"""
        # Main container
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Configure grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        title = ttk.Label(
            self.main_frame,
            text="Task List",
            font=TITLE_FONT
        )
        title.grid(row=0, column=0, pady=10)
        
        # Input frame
        self.input_frame = InputFrame(
            self.main_frame,
            self.add_task
        )
        self.input_frame.grid(row=1, column=0, sticky="ew", pady=5)
        
        # Task list frame
        self.task_frame = TaskFrame(
            self.main_frame,
            self.task_manager,
            self.delete_task,
            self.toggle_task
        )
        self.task_frame.grid(row=2, column=0, sticky="nsew", pady=5)
        self.main_frame.grid_rowconfigure(2, weight=1)
        
        # Load existing tasks
        self.load_tasks()
        
    def load_tasks(self):
        """Load existing tasks from storage"""
        try:
            self.task_manager.load_tasks()
            self.task_frame.refresh_tasks()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load tasks: {str(e)}")
            
    def add_task(self, task_text):
        """Add a new task"""
        try:
            if task_text.strip():
                self.task_manager.add_task(task_text)
                self.task_frame.refresh_tasks()
                self.input_frame.clear_input()
            else:
                messagebox.showwarning("Warning", "Task cannot be empty!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add task: {str(e)}")
            
    def delete_task(self, task_id):
        """Delete a task"""
        try:
            self.task_manager.delete_task(task_id)
            self.task_frame.refresh_tasks()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete task: {str(e)}")
            
    def toggle_task(self, task_id):
        """Toggle task completion status"""
        try:
            self.task_manager.toggle_task(task_id)
            self.task_frame.refresh_tasks()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update task: {str(e)}")