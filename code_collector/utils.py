import os
from typing import List

def get_default_extensions() -> List[str]:
    return ['.py', '.js', '.java', '.cpp', '.h', '.css', '.html']

def get_project_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))