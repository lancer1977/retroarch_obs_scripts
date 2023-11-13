FROM python:3.9

WORKDIR /app


# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy Flask app files
COPY . .

# Expose the port where the Flask app runs
EXPOSE 5000

# Set the entry point to start the Flask application
CMD ["python", "src/api.py"]