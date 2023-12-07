import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        debugShowCheckedModeBanner: false,
        home: Scaffold(
            appBar: AppBar(title: const Text('Movie App')),
            body: ListView(
              children: const [
                Movie('Vingadores Ultimato',
                    'https://br.web.img3.acsta.net/pictures/19/04/26/17/30/2428965.jpg'),
                Movie('Avatar 2',
                    'https://upload.wikimedia.org/wikipedia/pt/5/54/Avatar_The_Way_of_Water_poster.jpg'),
                Movie('Titanic',
                    'https://upload.wikimedia.org/wikipedia/pt/5/54/Avatar_The_Way_of_Water_poster.jpg'),
                Movie('Coraline',
                    'https://m.media-amazon.com/images/I/911peZ9F14L._AC_UF1000,1000_QL80_.jpg'),
              ],
            )
        )
    );
  }
}

class Movie extends StatelessWidget {
  final String name;
  final String image_link;
  const Movie(this.name, this.image_link, {super.key});

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
                    width: 148,
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
                        print('Like button Pressed');
                      },
                      child: const Icon(Icons.thumb_up)
                  )
                ]),
          )
        ],
      ),
    );
  }
}
