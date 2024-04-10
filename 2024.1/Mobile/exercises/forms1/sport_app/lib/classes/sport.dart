import 'package:flutter/cupertino.dart';

class Sport extends StatefulWidget {
  final String name;
  final String img;
  final int goals;
  final int age;

  Sport(this.name, this.img, this.age, this.goals, {super.key});

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
          SizedBox(
            width: 393,
            height: 250,
            child: Image.asset(widget.img, fit: BoxFit.fill),
          ),
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
                'Goals Scored: ${widget.goals}',
                style: const TextStyle(fontSize: 20),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
