# Flutter Client

The Flutter mobile application for the Music App.

## Features

- Cross-platform support (iOS, Android, Web, Desktop)
- User authentication
- Music player interface
- Custom theming
- Responsive design

## Getting Started

### Prerequisites

- Flutter SDK (3.9.0 or higher)
- Dart SDK
- Android Studio / Xcode (for mobile development)

### Installation

1. Get Flutter dependencies:
```bash
flutter pub get
```

2. Run the app:
```bash
flutter run
```

### Available Commands

- `flutter run` - Run the app in debug mode
- `flutter build apk` - Build Android APK
- `flutter build ios` - Build iOS app
- `flutter build web` - Build web version
- `flutter test` - Run tests
- `flutter analyze` - Analyze code for issues

## Project Structure

```
lib/
├── main.dart              # App entry point
├── core/                  # Core functionality
│   └── theme/            # App theming
└── features/             # Feature modules
    ├── auth/             # Authentication
    └── home/             # Home screen
```

## Development

### Code Style

This project follows Flutter's official style guide and uses:
- `flutter_lints` for code analysis
- Consistent naming conventions
- Proper file organization

### Testing

Run tests with:
```bash
flutter test
```

### Building

For release builds:
```bash
# Android
flutter build apk --release

# iOS
flutter build ios --release

# Web
flutter build web --release
```

## Dependencies

See `pubspec.yaml` for the complete list of dependencies.

## Contributing

1. Follow Flutter style guidelines
2. Write tests for new features
3. Update documentation as needed

## Development Setup

For wireless debugging:
```bash
adb tcpip 5555
adb connect 192.168.137.82:5555
flutter devices
```
flutter run