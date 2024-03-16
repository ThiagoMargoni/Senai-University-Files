import 'package:flutter/material.dart';
import 'package:food_list/classes/food.dart';

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Mange Trips',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const Home(),
    );
  }
}

class Home extends StatelessWidget {
  const Home({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('Mange Trips'),
        ),
        body: Stack(
          alignment: Alignment.bottomCenter,
          children: [
            ListView(
              children: [
                Food('Tacos', 'images/taco.jpg', 10),
                Food('Prato Feito', 'images/prato_feito.jpg', 50),
                Food('Hamburguer', 'images/hamburguer.jpg', 30),
                const SizedBox(
                  height: 110,
                )
              ],
            ),
            Container(
              width: 420,
              height: 100,
              color: const Color.fromARGB(255, 203, 198, 198),
            )
          ],
        ));
  }
}