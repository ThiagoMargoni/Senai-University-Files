import 'package:flutter/material.dart';

void main() {
  runApp(const Home());
}

class Home extends StatelessWidget {
  const Home({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
          appBar: AppBar(
            title: const Text('First App'),
          ),
          body: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                Container(
                  color: Colors.blue,
                  height: 100,
                  width: 100,
                ),
                Container(
                  color: Colors.red,
                  height: 100,
                  width: 100,
                ),
                ElevatedButton(
                  onPressed: () {
                    print('Pressed');
                  },
                  child: const Text('Click to Print'),
                )
              ],
            ),
          )),
    );
  }
}
