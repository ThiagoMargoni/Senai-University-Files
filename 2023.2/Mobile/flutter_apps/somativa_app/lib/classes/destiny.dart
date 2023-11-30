import 'package:flutter/material.dart';

class Destiny extends StatefulWidget {
  final String name;
  final String img;
  final double dailyValue;
  final double peopleValue;

  const Destiny(this.name, this.img, this.dailyValue, this.peopleValue, {super.key});

  @override
  State<Destiny> createState() => Destiny_State();
}

// ignore: camel_case_types
class Destiny_State extends State<Destiny> {
  
  // ignore: non_constant_identifier_names
  int n_days = 0, n_people = 0;
  double total = 0.0; 

  // ignore: non_constant_identifier_names
  void increment_days() {
    setState(() {
      n_days+=1;
    });
  }

  // ignore: non_constant_identifier_names
  void decrement_days() {
    if(n_days > 0) {
      setState(() {
        n_days-=1;
      });
    }
  }

  // ignore: non_constant_identifier_names
  void increment_people() {
    setState(() {
      n_people+=1;
    });
  }

  // ignore: non_constant_identifier_names
  void decrement_people() {
    if(n_people > 0) {
      setState(() {
        n_people-=1;
      });
    }
  }

  // ignore: non_constant_identifier_names
  void calc_total() {
    setState(() {
      total = (n_people*widget.peopleValue) + (n_days*widget.dailyValue);
    });
  }

  void clear() {
    setState(() {
      total = 0;
      n_days = 0;
      n_people = 0;
    });
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
            '\$ ${widget.dailyValue}/day - \$ ${widget.peopleValue}/people'.replaceAll('.', ','),
            style: TextStyle(color: Colors.red[300], fontSize: 23),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                'Number of Days: $n_days',
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
                    onPressed: () => increment_days(),
                    child: const Icon(Icons.add_outlined),
                  )
                ],
              )
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                'Amount of People: $n_people',
                style: const TextStyle(fontSize: 20),
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Container(
                    margin: const EdgeInsets.only(right: 15),
                    child: ElevatedButton(
                      onPressed: () => decrement_days(),
                      child: const Icon(Icons.remove_outlined),
                    ),
                  ),
                  ElevatedButton(
                    onPressed: () => increment_people(),
                    child: const Icon(Icons.add_outlined),
                  )
                ],
              )
            ],
          ),
          Text(
            'Total: \$ $total'.replaceAll('.', ','),
            style: const TextStyle(fontSize: 25),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                margin: const EdgeInsets.only(right: 20),
                child: ElevatedButton(
                  onPressed: () => clear(),
                  child: const Text('Clear'),
                )
              ),
              ElevatedButton(
                onPressed: () => calc_total(),
                child: const Text('Calc Total'),
              )
            ],
          ),
          // Row(
          //   mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          //   children: [
          //     ElevatedButton(

          //     ),
          //     ElevatedButton(

          //     ),
          //   ],
          // )
        ],
      ),
    );
  }
}