import 'package:flutter/material.dart';

void main() {
  runApp(const TextFieldApp());
}

class TextFieldApp extends StatefulWidget {
  const TextFieldApp({super.key});

  @override
  State<TextFieldApp> createState() => _TextFieldApp();
}

class _TextFieldApp extends State<TextFieldApp> {
  final TextEditingController _user = TextEditingController();
  final TextEditingController _password = TextEditingController();
  String message = 'Try the Login';
  Color color = Colors.indigo;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Name App'),
        ),
        body: Column(
          children: [
            Padding(
              padding: const EdgeInsets.all(32),
              child: TextField(
                keyboardType: TextInputType.text,
                decoration:
                    const InputDecoration(labelText: 'Enter Your Username'),
                style: const TextStyle(fontSize: 28),
                controller: _user,
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(32),
              child: TextField(
                keyboardType: TextInputType.text,
                decoration:
                    const InputDecoration(labelText: 'Enter the Password'),
                style: const TextStyle(fontSize: 28),
                controller: _password,
              ),
            ),
            ElevatedButton(
              onPressed: () {
                if (_user.text == 'Senai' && _password.text == 'mobile23') {
                  setState(() {
                    message = 'Logged!!';
                    color = Colors.green;
                  });
                } else {
                  setState(() {
                    message = 'Incorrect Username/Password';
                    color = Colors.red;
                  });
                }
              },
              child: const Text('Login'),
            ),
            Container(
              color: color,
              width: 200,
              height: 200,
              child: Text(
                "Name: $message",
                style: const TextStyle(fontSize: 22, color: Colors.black),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
