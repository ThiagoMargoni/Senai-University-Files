import 'package:flutter/material.dart';
import 'package:multiple_window/window_two.dart';

void main() {
  runApp(const MaterialApp(
    debugShowCheckedModeBanner: false,
    home: MainWindow(),
  ));
}

class MainWindow extends StatelessWidget {
  const MainWindow({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Multiple Window'),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
         children: [
          Container(
            color: Colors.blue,
            width: 400,
            height: 180,
            child: const Text(
              'Tela 1',
              style: TextStyle(fontSize: 25),
            ),
          ),
          ElevatedButton(
            onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (context) => const SecondWindow())),
            child: const Text('Call Second Window'),
          )
        ],
      ),
    );
  }
}