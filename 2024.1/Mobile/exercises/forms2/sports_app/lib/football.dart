import 'package:flutter/material.dart';
import 'package:sports_app/sport.dart';

class Football extends StatefulWidget {
  const Football({super.key});

  @override
  State<Football> createState() => _BasketState();
}

class _BasketState extends State<Football> {
  @override
  Widget build(BuildContext context) {
     return Scaffold(
        appBar: AppBar(
          title: const Text('Football Page'),
        ),
        body: Stack(
          alignment: Alignment.bottomCenter,
          children: [
            ListView(
              children: [
                Sport('Patrick Mahomes', 27, 100),
                Sport('Jalen Hurts', 25, 1000),
                Sport('Joe Burrow', 26, 99999999),
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