# CrewAI + Qualtrics Integration

This project is a simple integration of CrewAI with Qualtrics for AI-enabled survey functionalities.

## Files
- `app.py`: Main Flask application.
- `Dockerfile`: Docker configuration for containerization.
- `requirements.txt`: Python dependencies.
- `.dockerignore`: Files and folders to exclude in the Docker build.

## Deployment
1. Build Docker image: `docker build -t crewai_integration .`
2. Run Docker container: `docker run -p 5000:5000 crewai_integration`
