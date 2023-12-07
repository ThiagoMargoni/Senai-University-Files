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
  String? name;

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
                decoration: const InputDecoration(labelText: 'Enter Your Name'),
                style: const TextStyle(fontSize: 28),
                controller: _textEditingController,
              ),
            ),
            ElevatedButton(
              onPressed: () {
                setState(() {
                  name = _textEditingController.text;
                });
              },
              child: const Text('Show Your Name'),
            ),
            Container(
              color: Colors.blue,
              width: 200,
              height: 200,
              child: Text(
                "Name: $name",
                style: const TextStyle(fontSize: 22),
              ),
            ),
          ],
        ),
      ),
    );
  }
}