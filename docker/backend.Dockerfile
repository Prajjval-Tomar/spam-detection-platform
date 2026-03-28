# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy project files
COPY ../backend /app

# Install dependencies
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]