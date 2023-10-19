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
        home: Scaffold(
            appBar: AppBar(title: const Text('To-Do App')),
            body: const Column(
              children: [
                Task('Learn Flutter',
                    'https://cdn-images-1.medium.com/v2/resize:fit:1200/1*5-aoK8IBmXve5whBQM90GA.png'),
                Task('Study',
                    'https://wallpapers.com/images/featured/study-pictures-6ovzato85a4dtczb.jpg'),
                Task('Buy Food',
                    'https://media.product.which.co.uk/prod/images/original/ff4550b67ea3-uk-shopping-trolley.jpg'),
                Task('Clean the Room',
                    'https://yorlenyscleaningservice.com/wp-content/uploads/2021/07/Why-is-cleaning-your-bedroom-important.jpg'),
              ],
            )));
  }
}

class Task extends StatelessWidget {
  final String task;
  final String image_link;
  const Task(this.task, this.image_link, {super.key});

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
                children: [
                  Container(
                    color: Colors.grey,
                    height: 100,
                    width: 80,
                    child: Image.network(
                      image_link,
                      fit: BoxFit.fill,
                    ),
                  ),
                  Text(
                    task,
                    style: const TextStyle(fontSize: 22),
                  ),
                  ElevatedButton(
                      onPressed: () {
                        print('Button Pressed');
                      },
                      child: const Icon(Icons.arrow_drop_up))
                ]),
          )
        ],
      ),
    );
  }
}
