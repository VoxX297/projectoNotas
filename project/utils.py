"""
Utility functions
"""
import os

def ensure_data_directory():
    """Ensure data directory exists"""
    os.makedirs("data", exist_ok=True)