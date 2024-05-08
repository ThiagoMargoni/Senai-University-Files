import 'package:flutter/material.dart';
import 'package:sports_app/sport.dart';

class Soccer extends StatefulWidget {
  const Soccer({super.key});

  @override
  State<Soccer> createState() => _SoccerState();
}

class _SoccerState extends State<Soccer> {
  @override
  Widget build(BuildContext context) {
     return Scaffold(
        appBar: AppBar(
          title: const Text('Soccer Page'),
        ),
        body: Stack(
          alignment: Alignment.bottomCenter,
          children: [
            ListView(
              children: [
                Sport('Pelé', 82, 1500),
                Sport('Lionel Messi', 50, 10),
                Sport('Luva de Pedreiro', 20, 99999999),
                const SizedBox(
                  height: 110,
                )
              ],
            )
          ],
        )
    );
  }
}