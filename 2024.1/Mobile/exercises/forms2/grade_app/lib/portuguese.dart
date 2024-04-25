import 'package:flutter/material.dart';

class PortugueseWindow extends StatelessWidget {
  const PortugueseWindow({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Portuguese Window'),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            color: Colors.blue,
            width: 400,
            height: 180,
            child: const Text(
              'Se expressarmos gratidão pelo que temos, teremos mais por que expressar gratidão.',
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