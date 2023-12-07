import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        debugShowCheckedModeBanner: false,
        home: Scaffold(
            appBar: AppBar(title: const Text('Subject App')),
            body: ListView(
              children: const [
                Subject('Mobile',
                    'https://coodesh.com/blog/wp-content/uploads/2021/10/mobile-flutter-1-1152x648.jpg'),
                Subject('Web',
                    'https://camo.githubusercontent.com/660d0a0371b579bc2104685019915e6342731d482276c6689a298dbc2c21bb36/687474703a2f2f692e696d6775722e636f6d2f735933497042452e706e673f31'),
                Subject('IoT',
                    'https://play-lh.googleusercontent.com/rbiJLPyRpzFpP8C688ebkG9AV1vpej4E2F3BBbMlYwqHxHGixsyBr62Gyeg_jIattOE'),
                Subject('IA and Big Data',
                    'https://play-lh.googleusercontent.com/rbiJLPyRpzFpP8C688ebkG9AV1vpej4E2F3BBbMlYwqHxHGixsyBr62Gyeg_jIattOE'),
              ],
            )
        )
    );
  }
}

class Subject extends StatelessWidget {
  final String name;
  final String image_link;
  const Subject(this.name, this.image_link, {super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.white,
      child: Stack(
        children: [
          Container(
            color: Colors.blue,
            height: 140,
          ),
          Container(
            color: Colors.white,
            height: 100,
            child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Container(
                    color: Colors.grey,
                    height: 100,
                    width: 100,
                    child: Image.network(
                      image_link,
                      fit: BoxFit.fill,
                    ),
                  ),
                  Text(
                    name,
                    style: const TextStyle(fontSize: 22),
                  ),
                  ElevatedButton(
                      onPressed: () {
                        print('View button Pressed');
                      },
                      child: const Icon(Icons.remove_red_eye)
                  )
                ]),
          )
        ],
      ),
    );
  }
}
