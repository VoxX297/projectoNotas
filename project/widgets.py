"""
Custom widget components
"""
import tkinter as tk
from tkinter import ttk
from styles import *

class TaskFrame(ttk.Frame):
    def __init__(self, parent, task_manager, delete_callback, toggle_callback):
        super().__init__(parent)
        self.task_manager = task_manager
        self.delete_callback = delete_callback
        self.toggle_callback = toggle_callback
        
        # Create canvas and scrollbar
        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.canvas.yview
        )
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Layout
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        
    def refresh_tasks(self):
        """Refresh the task list display"""
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
            
        for task in self.task_manager.get_tasks():
            self.create_task_item(task)
            
    def create_task_item(self, task):
        """Create a single task item widget"""
        frame = ttk.Frame(self.scrollable_frame)
        frame.pack(fill="x", pady=2)
        
        check_var = tk.BooleanVar(value=task['completed'])
        checkbox = ttk.Checkbutton(
            frame,
            variable=check_var,
            command=lambda: self.toggle_callback(task['id'])
        )
        checkbox.pack(side="left")
        
        label = ttk.Label(
            frame,
            text=task['text'],
            font=TASK_FONT if not task['completed'] else COMPLETED_TASK_FONT
        )
        label.pack(side="left", padx=5, fill="x", expand=True)
        
        delete_btn = ttk.Button(
            frame,
            text="×",
            width=3,
            command=lambda: self.delete_callback(task['id'])
        )
        delete_btn.pack(side="right")

class InputFrame(ttk.Frame):
    def __init__(self, parent, add_callback):
        super().__init__(parent)
        self.add_callback = add_callback
        
        # Entry field
        self.entry = ttk.Entry(self)
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        # Add button
        self.add_btn = ttk.Button(
            self,
            text="Add Task",
            command=self.add_task
        )
        self.add_btn.pack(side="right")
        
        # Bind Enter key
        self.entry.bind("<Return>", lambda e: self.add_task())
        
    def add_task(self):
        """Add task from entry field"""
        task_text = self.entry.get()
        self.add_callback(task_text)
        
    def clear_input(self):
        """Clear the input field"""
        self.entry.delete(0, tk.END)