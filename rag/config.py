"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VECTOR_DB_PATH = os.path.join(BASE_DIR, "..", "vectorstore")
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VECTOR_DB_PATH = os.path.join(BASE_DIR, "vectorstore")