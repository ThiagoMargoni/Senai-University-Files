import 'package:flutter/cupertino.dart';

class Sport extends StatefulWidget {
  final String name;
  final int age;
  final int rating;

  Sport(this.name, this.age, this.rating, {super.key});

  @override
  State<Sport> createState() => SportState();
}

// ignore: camel_case_types
class SportState extends State<Sport> {
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(12.0),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Text(
            widget.name,
            style: const TextStyle(fontSize: 30),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                'Age: ${widget.age}',
                style: const TextStyle(fontSize: 20),
              ),
              Text(
                'Rating Player: ${widget.rating}',
                style: const TextStyle(fontSize: 20),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
