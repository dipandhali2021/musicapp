import 'dart:convert';

import 'package:http/http.dart' as http;

class AuthRemoteRepository {
  Future<void> signup({
    required String name,
    required String email,
    required String password,
  }) async {
    final response = await http.post(
      Uri.parse('http://192.168.137.1:8000/auth/signup'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'name': name, 'email': email, 'password': password}),
    );
    if (response.statusCode == 201) {
      // Handle successful signup
      print('Signup successful: ${response.body}');
    } else {
      // Handle signup error
      print(
        'Signup failed with status: ${response.statusCode}, body: ${response.body}',
      );
    }
  }

  Future<void> login({required String email, required String password}) async {
    final response = await http.post(
      Uri.parse('http://192.168.137.1:8000/auth/login'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'email': email, 'password': password}),
    );
    print('Login successful: ${response.body}');
    if (response.statusCode == 201) {
      // Handle successful login
      print('Login successful: ${response.body}');
    } else {
      // Handle login error
      print(
        'Login failed with status: ${response.statusCode}, body: ${response.body}',
      );
    }
  }
}
