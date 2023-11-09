import 'package:flutter/material.dart';

void main() {
  runApp(const StatefulApp());
}

class StatefulApp extends StatefulWidget {
  const StatefulApp({super.key});

  @override
  State<StatefulApp> createState() => _StatefulAppState();
}

class _StatefulAppState extends State<StatefulApp> {
  String _msg = 'Standard Text';
  Color color = Colors.indigo;
  @override

  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Stateful Widget App'),
        ),
        body: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              color: color,
              width: 500,
              height: 200,
              alignment: Alignment.center,
              child: Text(
                _msg, 
                style: const TextStyle(
                  fontSize: 35,
                  color: Colors.limeAccent
                )
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                ElevatedButton(
                  onPressed: () {
                    setState(() {
                      _msg = 'Button 1 Clicked';
                      color = Colors.indigoAccent;
                    });
                  },
                  style: ButtonStyle(
                    backgroundColor: MaterialStateProperty.all(Colors.indigoAccent),
                  ),
                  child: const Text(
                    'Click 1',
                    style: TextStyle(),
                  ),
                ),
                ElevatedButton(
                  onPressed: () {
                    setState(() {
                      _msg = 'Button 2 Clicked';
                      color = Colors.purple;
                    });
                  },
                  style: ButtonStyle(
                    backgroundColor: MaterialStateProperty.all(Colors.purple),
                  ),
                  child: const Text(
                    'Click 2',
                    style: TextStyle(),
                  ),
                ),
                ElevatedButton(
                  onPressed: () {
                    setState(() {
                      _msg = 'Button 3 Clicked';
                      color = Colors.deepPurple;
                    });
                  },
                  style: ButtonStyle(
                    backgroundColor: MaterialStateProperty.all(Colors.deepPurple),
                  ),
                  child: const Text(
                    'Click 3',
                    style: TextStyle(),
                  ),
                ),
              ],
            )
          ],
        ),
      ),
    );
  }
}