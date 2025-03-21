# Use a lightweight Python image
FROM python:3.13-slim

# Prevent Python from writing .pyc files to disk and enable unbuffered output
ENV PYTHONUNBUFFERED=1

# Install system dependencies required for the app
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user to run the application
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set working directory
WORKDIR /app

# Copy dependencies separately to optimize caching
COPY requirements.txt .

# Create a virtual environment
RUN python -m venv /app/.venv

# Upgrade pip and install dependencies using a dedicated pip cache directory
RUN /app/.venv/bin/pip install --upgrade pip && \
    PIP_CACHE_DIR=/root/.cache/pip /app/.venv/bin/pip install -r requirements.txt

# Copy the rest of the application code
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

# Set PATH to use the virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Expose the application port
EXPOSE 5000

# Add a health check for monitoring
HEALTHCHECK --interval=500s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

# Run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "-c", "app/gunicorn.conf.py", "app.wsgi:app"]
