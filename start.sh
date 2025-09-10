#!/bin/bash
echo "Starting MDF File Viewer Backend..."
cd backend
exec gunicorn main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
