# Base image
FROM python:3.9-slim-buster

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV FLASK_DEBUG=0

# Copy app files to container
WORKDIR /app
COPY . .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Start app
CMD ["flask", "run", "--host=0.0.0.0"]
