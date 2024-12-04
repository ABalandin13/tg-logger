# Use an official Python runtime as the base image
FROM python:3.12-slim

RUN apt-get update \
    && apt-get install -y gcc python3-dev libpq-dev

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY docker/requirements.txt ./

# Install dependencies
RUN pip install --upgrade https://github.com/LonamiWebs/Telethon/archive/v2.zip#subdirectory=client
RUN pip install --no-cache-dir psycopg2 --global-option=build_ext --global-option="-I/usr/include/postgresql"
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the app's source code to the container
COPY . .

# Run the script when the container launches
CMD ["python", "main.py"]