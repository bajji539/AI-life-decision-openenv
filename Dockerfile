# Use Python 3.13 slim image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Set environment variables (can be overridden at runtime)
ENV API_BASE_URL=https://api.openai.com/v1
ENV MODEL_NAME=gpt-4o-mini
# HF_TOKEN and LOCAL_IMAGE_NAME should be set at runtime

# Expose any ports if needed (none for this app)

# Default command to run the interface
CMD ["python", "app.py"]