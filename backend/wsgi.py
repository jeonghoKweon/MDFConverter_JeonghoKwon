"""
WSGI configuration for Render deployment compatibility
"""
from main import app

# For gunicorn compatibility
application = app