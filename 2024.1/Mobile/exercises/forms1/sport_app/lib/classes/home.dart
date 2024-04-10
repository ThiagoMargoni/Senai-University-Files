import 'package:flutter/material.dart';
import 'package:sport_app/classes/sport.dart';

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Mange Sports',
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
          title: const Text('Mange Sports'),
        ),
        body: Stack(
          alignment: Alignment.bottomCenter,
          children: [
            ListView(
              children: [
                Sport('Pelé', 'images/pele.jpg', 82, 1500),
                Sport('Lionel Messi', 'images/messi.jpg', 922, 10),
                Sport('Luva de Pedreiro', 'images/luva.jpg', 20, 99999999),
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