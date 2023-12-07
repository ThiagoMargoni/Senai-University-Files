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
  final TextEditingController _n1 = TextEditingController();
  final TextEditingController _n2 = TextEditingController();
  final TextEditingController _n3 = TextEditingController();
  double total = 0;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Number App'),
        ),
        body: Column(
          children: [
            Padding(
              padding: const EdgeInsets.all(32),
              child: TextField(
                keyboardType: TextInputType.number,
                decoration: const InputDecoration(labelText: 'Enter the first number'),
                style: const TextStyle(fontSize: 28),
                controller: _n1,
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(32),
              child: TextField(
                keyboardType: TextInputType.number,
                decoration: const InputDecoration(labelText: 'Enter the second number'),
                style: const TextStyle(fontSize: 28),
                controller: _n2,
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(32),
              child: TextField(
                keyboardType: TextInputType.number,
                decoration: const InputDecoration(labelText: 'Enter the third number'),
                style: const TextStyle(fontSize: 28),
                controller: _n3,
              ),
            ),
            ElevatedButton(
              onPressed: () {
                setState(() {
                  total = double.parse(_n1.text) + double.parse(_n2.text) + double.parse(_n3.text);
                });
              },
              child: const Text('Show the Total'),
            ),
            Container(
              color: Colors.blue,
              width: 200,
              height: 200,
              child: Text(
                'Total: $total',
                style: const TextStyle(fontSize: 22),
              ),
            ),
          ],
        ),
      ),
    );
  }
}