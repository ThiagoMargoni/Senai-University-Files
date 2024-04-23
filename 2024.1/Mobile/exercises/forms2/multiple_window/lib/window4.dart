import 'package:flutter/material.dart';

class FourthWindow extends StatelessWidget {
  const FourthWindow({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Fourth Window'),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            color: Colors.deepOrangeAccent,
            width: 400,
            height: 180,
            child: const Text(
              'Tenho uma profunda gratidão por cada lição que aprendi no passado. Afinal, foram elas que me permitiram chegar até aqui!',
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