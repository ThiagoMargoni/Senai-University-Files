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
  final TextEditingController _textEditingController = TextEditingController();
  String? _a;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Testing Text Field'),
        ),
        body: Column(
          children: [
            Padding(
              padding: const EdgeInsets.all(32),
              child: TextField(
                keyboardType: TextInputType.emailAddress,
                decoration: const InputDecoration(labelText: 'Enter Your Name'),
                style: const TextStyle(fontSize: 28),
                controller: _textEditingController,
              ),
            ),
            ElevatedButton(
              onPressed: () {
                setState(() {
                  _a = _textEditingController.text;
                });
              },
              child: const Text('Save Your Name'),
            ),
            Container(
              color: Colors.blue,
              width: 200,
              height: 200,
              child: Text(
                "Name: $_a",
                style: const TextStyle(fontSize: 22),
              ),
            ),
          ],
        ),
      ),
    );
  }
}