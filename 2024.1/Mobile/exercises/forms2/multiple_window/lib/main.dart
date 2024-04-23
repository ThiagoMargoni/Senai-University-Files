import 'package:flutter/material.dart';
import 'package:multiple_window/window1.dart';
import 'package:multiple_window/window2.dart';
import 'package:multiple_window/window3.dart';
import 'package:multiple_window/window4.dart';
import 'package:multiple_window/window5.dart';

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
        body: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                  onPressed: () => Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => const FirstWindow())),
                  child: const Text('Call Window 1'),
                ),
                ElevatedButton(
                  onPressed: () => Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => const SecondWindow())),
                  child: const Text('Call Window 2'),
                ),
                ElevatedButton(
                  onPressed: () => Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => const ThirdWindow())),
                  child: const Text('Call Window 3'),
                ),
                ElevatedButton(
                  onPressed: () => Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => const FourthWindow())),
                  child: const Text('Call Window 4'),
                ),
                ElevatedButton(
                  onPressed: () => Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => const FifithWindow())),
                  child: const Text('Call Window 5'),
                ),
              ],
            ),
          ],
        ));
  }
}
