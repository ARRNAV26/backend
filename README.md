# Pair Programming App - Backend

## Overview
This backend application is built using FastAPI and provides a real-time collaborative coding environment for users. Users can create or join rooms to edit code simultaneously, with changes reflected instantly across all connected clients. The application also includes a mocked AI-style autocomplete feature to enhance the coding experience.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- PostgreSQL
- Docker (optional, for containerized deployment)

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd pair-programming-app/backend
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Create a PostgreSQL database and update the connection details in `app/core/config.py`.

5. Run database migrations (if applicable):
   ```
   alembic upgrade head
   ```

### Running the Application
To start the FastAPI application, run:
```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
The application will be accessible at `http://localhost:8000`.

## Architecture and Design Choices
- **FastAPI**: Chosen for its performance and ease of use in building APIs.
- **WebSockets**: Used for real-time communication between clients, allowing for instant code updates.
- **PostgreSQL**: Selected as the database for its robustness and support for complex queries.
- **Pydantic**: Utilized for data validation and serialization, ensuring that data structures are well-defined and validated.

## Improvements with More Time
- Implement user authentication and authorization.
- Enhance the AI autocomplete feature with real AI suggestions.
- Add more robust error handling and logging.
- Create a more comprehensive frontend with additional features.

## Limitations
- The current implementation supports only two users per room.
- The autocomplete feature is mocked and does not provide intelligent suggestions.
- In-memory storage for code state may lead to data loss if the server restarts.

## License
This project is licensed under the MIT License. See the LICENSE file for details.