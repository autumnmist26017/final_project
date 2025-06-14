# Use the official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libsndfile1 \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy all source code
COPY . .

# Expose the port (Cloud Run uses this env variable)
EXPOSE $PORT

# Streamlit default port is 8501, but override with $PORT
CMD ["streamlit", "run", "audio2.py", "--server.port=$PORT", "--server.address=0.0.0.0"]
