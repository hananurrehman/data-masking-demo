#Python image
FROM python:3.9-slim

#Working directory
WORKDIR /usr/src/app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Run the python app
CMD ["python", "./app.py"]
