import 'package:flutter/material.dart';

class SecondWindow extends StatelessWidget {
  const SecondWindow({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Second Window'),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            color: Colors.red,
            width: 400,
            height: 180,
            child: const Text(
              'Tela 2',
              style: TextStyle(
                fontSize: 25
              ),
            ),
          ),
          ElevatedButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Call First Window'),
          )
        ],
      ),
    );
  }
}