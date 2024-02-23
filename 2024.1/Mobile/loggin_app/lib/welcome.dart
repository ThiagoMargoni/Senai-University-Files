import 'package:flutter/material.dart';

class WelcomeWindow extends StatelessWidget {
  const WelcomeWindow({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Welcome Window'),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            alignment: Alignment.center,
            color: Colors.black,
            width: 400,
            height: 180,
            child: const Text(
              'Welcome User!!',
              style: TextStyle(
                fontSize: 40,
                color: Colors.white
              ),
            ),
          ),
          ElevatedButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Logout'),
          )
        ],
      ),
    );
  }
}