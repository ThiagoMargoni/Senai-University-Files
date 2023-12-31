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
            appBar: AppBar(title: const Text('Movie App')),
            body: ListView(
              children: const [
                Music('Payphone',
                    'https://cdns-images.dzcdn.net/images/cover/da7418953af2fa393f3038bb80be9edd/350x350.jpg'),
                Music('Ela Partiu',
                    'https://cdns-images.dzcdn.net/images/cover/da7418953af2fa393f3038bb80be9edd/350x350.jpg'),
                Music('Rewrite the Stars',
                    'https://cdns-images.dzcdn.net/images/cover/da7418953af2fa393f3038bb80be9edd/350x350.jpg'),
                Music('Alvorada',
                    'https://cdns-images.dzcdn.net/images/cover/da7418953af2fa393f3038bb80be9edd/350x350.jpg'),
              ],
            )
        )
    );
  }
}

class Music extends StatelessWidget {
  final String name;
  final String image_link;
  const Music(this.name, this.image_link, {super.key});

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
                        print('Saved Music');
                      },
                      child: const Icon(Icons.save)
                  )
                ]),
          )
        ],
      ),
    );
  }
}
