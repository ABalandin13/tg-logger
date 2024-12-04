README: Telegram Communication App

Project Description

The Telegram Communication App is a scalable tool for interacting with Telegram using the Telethon library. It enables user authentication, message management, and event handling, such as monitoring new, edited, and deleted messages. Built with Python and PostgreSQL, the app is containerized using Docker to streamline development and deployment.

Features

	•	Authenticate Telegram users.
	•	Monitor and log Telegram events (new, edited, and deleted messages).
	•	Fully asynchronous architecture using asyncio.
	•	Flexible configuration via .env file.

Getting Started

Prerequisites

	1.	Install Docker.
	2.	Install Docker Compose.
	3.	Clone this repository:

		git clone <repository_url>
		cd <project_directory>

Setup Instructions

1.	Configure Environment Variables:
	Create a .env file in the project root directory with the following structure:
	
	API_ID=<your_api_id>
	API_HASH=<your_api_hash>
	
	Replace <your_api_id> and <your_api_hash> with your Telegram API credentials.

2.	Build and Start the Project:
		Use the Makefile commands to initialize and run the project:
	
	# Build Docker containers
	make build
	
	# Start Docker containers
	make up


3.	Access the Application:

	The app will start and listen for new users and Telegram events. Logs will be displayed in the terminal.
	
4.	Stop the Project:
	
    make down

Database Management

The app uses PostgreSQL for storing message data. The database is automatically set up when the Docker container is initialized. To interact with the database:

	docker exec -it postgres_db psql -U postgres -d communication

Project Structure

	project/
	├── docker/               # Docker configurations
	│   ├── Dockerfile
	│   ├── docker-compose.yml
	├── utils/                # Utility functions and tools
	│   ├── logger.py
	├── models/               # Data models (e.g., message model)
	├── database/             # Database interaction and migrations
	├── telegram_auth/        # Telegram authentication logic
	├── main.py               # Main application entry point
	├── requirements.txt      # Python dependencies
	├── Makefile              # Makefile for common commands
	└── .env.example          # Example environment file
