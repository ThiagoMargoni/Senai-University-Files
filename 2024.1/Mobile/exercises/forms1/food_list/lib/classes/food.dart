import 'package:flutter/material.dart';

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
  double total = 0.0;

  // ignore: non_constant_identifier_names
  void increment_food() {
    setState(() {
      n_food += 1;
    });
  }

  // ignore: non_constant_identifier_names
  void decrement_days() {
    if (n_food > 0) {
      setState(() {
        n_food -= 1;
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
