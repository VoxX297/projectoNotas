"""
Task List Application - Main Entry Point
"""
import tkinter as tk
from app import TaskListApp

def main():
    """Initialize and run the main application"""
    root = tk.Tk()
    app = TaskListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()