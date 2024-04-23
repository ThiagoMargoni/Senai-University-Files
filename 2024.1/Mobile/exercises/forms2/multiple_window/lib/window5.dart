import 'package:flutter/material.dart';

class FifithWindow extends StatelessWidget {
  const FifithWindow({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Fifith Window'),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            color: Colors.green,
            width: 400,
            height: 180,
            child: const Text(
              'Com o coração cheio de gratidão, sei que sou capaz de superar qualquer obstáculo que a vida apresentar!',
              style: TextStyle(
                fontSize: 25,
                color: Colors.white
              ),
            ),
          ),
          ElevatedButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Call Home'),
          )
        ],
      ),
    );
  }
}