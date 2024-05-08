import 'package:flutter/material.dart';
import 'package:sports_app/sport.dart';

class Basket extends StatefulWidget {
  const Basket({super.key});

  @override
  State<Basket> createState() => _BasketState();
}

class _BasketState extends State<Basket> {
  @override
  Widget build(BuildContext context) {
     return Scaffold(
        appBar: AppBar(
          title: const Text('Basket Page'),
        ),
        body: Stack(
          alignment: Alignment.bottomCenter,
          children: [
            ListView(
              children: [
                Sport('Kevin Durant', 35, 100),
                Sport('Giannis Antetokounmpo', 922, 1000),
                Sport('LeBron James', 39, 99999999),
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