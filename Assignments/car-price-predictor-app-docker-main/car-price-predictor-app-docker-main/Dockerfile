# Use an official, lightweight Python base image
FROM python:3.10-slim

# Set the working directory inside the container sandbox
WORKDIR /app

# Copy the requirements file first to optimize layer caching
COPY requirements.txt .

# Install dependencies inside the sandbox environment
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining project files
COPY . .

# Expose port 10000 (Render default port)
EXPOSE 10000

# Run Gunicorn production server bound to Render's default port
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]