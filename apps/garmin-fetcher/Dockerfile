FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the Python script
COPY fetch_garmin_data.py /app/

# Install required dependencies
RUN pip install garminconnect flask

# Expose the Flask API port
EXPOSE 5000

# Run the script
CMD ["python", "/app/fetch_garmin_data.py"]
