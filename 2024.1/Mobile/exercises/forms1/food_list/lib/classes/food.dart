import 'package:flutter/material.dart';

double total = 0.0;

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
              child: Text('Total: $total')
            )
          ],
        ));
  }
}

class Food extends StatefulWidget {
  final String name;
  final String img;
  // ignore: non_constant_identifier_names
  final double food_price;

  Food(this.name, this.img, this.food_price, {super.key});

  @override
  State<Food> createState() => Destiny_State();
}

// ignore: camel_case_types
class Destiny_State extends State<Food> {
  // ignore: non_constant_identifier_names
  int n_food = 0;

  // ignore: non_constant_identifier_names
  void increment_food() {
    setState(() {
      n_food += 1;
      total += food_price;
    });
  }

  // ignore: non_constant_identifier_names
  void decrement_days() {
    if (n_food > 0) {
      setState(() {
        n_food -= 1;
        total -= food_price;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(12.0),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          SizedBox(
            width: 393,
            height: 250,
            child: Image.asset(widget.img, fit: BoxFit.fill),
          ),
          Text(
            widget.name,
            style: const TextStyle(fontSize: 30),
          ),
          Text(
            '\$ ${widget.food_price}/unit'.replaceAll('.', ','),
            style: TextStyle(color: Colors.red[300], fontSize: 23),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                'Number of Food: $n_food',
                style: const TextStyle(fontSize: 20),
              ),
              Row(
                children: [
                  Container(
                    margin: const EdgeInsets.only(right: 15),
                    child: ElevatedButton(
                      onPressed: () => decrement_days(),
                      child: const Icon(Icons.remove_outlined),
                    ),
                  ),
                  ElevatedButton(
                    onPressed: () => increment_food(),
                    child: const Icon(Icons.add_outlined),
                  )
                ],
              )
            ],
          ),
        ],
      ),
    );
  }
}
