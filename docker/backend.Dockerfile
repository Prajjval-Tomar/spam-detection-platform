FROM python:3.11

WORKDIR /app

# ✅ Copy entire project (IMPORTANT FIX)
COPY .. /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set PYTHONPATH so ml_engine is accessible
ENV PYTHONPATH=/app

CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000"]