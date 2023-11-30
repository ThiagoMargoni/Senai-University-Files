import 'package:flutter/material.dart';
import 'package:somativa_flutter/classes/destiny.dart';

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
      body: ListView(
        children: const [
          Destiny('Angra dos Reis', 'images/angra.png', 384, 70),
          Destiny('Jericoacoara', 'images/jeri.png', 571, 75),
          Destiny('Arraial do Cabo', 'images/arraial.png', 534, 65),
          Destiny('Florianópolis', 'images/flori.png', 348, 85),
          Destiny('Madri', 'images/madri.png', 401, 85),
          Destiny('Paris', 'images/paris.png', 546, 95),
          Destiny('Orlando', 'images/orlando.png', 616, 105),
          Destiny('Las Vegas', 'images/vegas.png', 504, 110),
          Destiny('Roma', 'images/roma.png', 478, 85),
          Destiny('Chile', 'images/chile.png', 446, 95),
        ],
      ),
    );
  }
}