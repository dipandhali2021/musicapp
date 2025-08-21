# Music App

A full-stack music application with a Flutter client and FastAPI server.

## Project Structure

- `client/` - Flutter mobile application
- `server/` - FastAPI backend server

## Features

- User authentication
- Music streaming
- Cross-platform support (iOS, Android, Web, Desktop)

## Getting Started

### Prerequisites

- Flutter SDK (latest stable version)
- Python 3.9+
- Git

### Client Setup

```bash
cd client
flutter pub get
flutter run
```

### Server Setup

```bash
cd server
pip install -r requirements.txt
python main.py
```

## Development

### Client (Flutter)

The Flutter client is located in the `client/` directory and includes:
- Authentication features
- Home screen with music player
- Theming support

### Server (FastAPI)

The backend server provides REST APIs for:
- User authentication
- Music streaming
- Playlist management

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
