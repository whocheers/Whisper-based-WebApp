# Multi-stage build for optimized image size
FROM python:3.9-slim as builder

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Production stage
FROM python:3.9-slim

# Install runtime dependencies (FFmpeg for Whisper)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy Python packages from builder
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY . .

# Ensure scripts in .local are in PATH
ENV PATH=/root/.local/bin:$PATH

# Create instance directory for SQLite database
RUN mkdir -p instance

# Download Whisper model at build time (base model ~140MB)
# This ensures the model is baked into the image for reproducibility
RUN python -c "import whisper; whisper.load_model('base')"

# Expose Flask port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
