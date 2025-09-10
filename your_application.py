"""
Fallback module for Render's default gunicorn configuration
This redirects to the actual FastAPI application in backend/main.py
"""
import sys
import os

# Add backend directory to Python path
backend_path = os.path.join(os.path.dirname(__file__), 'backend')
sys.path.insert(0, backend_path)

# Import the actual FastAPI app
from main import app

# WSGI application for gunicorn
wsgi = app
application = app