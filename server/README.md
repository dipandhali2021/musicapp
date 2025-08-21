# Music App Server

FastAPI backend server for the Music App.

## Features

- RESTful API endpoints
- User authentication
- Music streaming capabilities
- Database integration

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
uvicorn main:app --reload
```

The server will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API docs: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

## Environment Variables

Create a `.env` file in the server directory with the following variables:
```
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@localhost/musicapp
DEBUG=True
```

## Development

The server uses FastAPI with:
- Automatic API documentation
- Type hints for better development experience
- Built-in validation

## Getting Started

### Requirements

- Python 3.11 or higher
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd server
   ```
2. Install dependencies:
   ```bash
   pip install "fastapi[standard]"
   ```

### Running the Server

```bash
uvicorn main:app --reload
```

## Project Structure

- `main.py`: Main FastAPI application file.

## License

MIT
