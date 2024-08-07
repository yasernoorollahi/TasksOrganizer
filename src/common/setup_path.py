# utils/path_utils.py
import sys
import os

def app_path():
    """Add the project root to the PYTHONPATH."""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    print(project_root)
    if project_root not in sys.path:
        sys.path.append(project_root)
