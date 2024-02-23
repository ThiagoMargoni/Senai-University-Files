import 'package:flutter/material.dart';

void main() {
  runApp(const Home());
}

class Home extends StatelessWidget {
  const Home({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Second App'),
        ),
        body: const Center(
          child: Counter()
        ),
      ),
    );
  }
}

class Counter extends StatefulWidget {
  const Counter({super.key});

  @override
  State<Counter> createState() => _CounterState();
}

class _CounterState extends State<Counter> {

  final TextEditingController _name = TextEditingController();
  final TextEditingController _password = TextEditingController();
  Color boxColor = Colors.blue;

  void _showToast(BuildContext context) {
    ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('User/Password Mismatch'),
          duration: Duration(seconds: 2),
        )
    );
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
      children: [
        Padding(
          padding: const EdgeInsets.only(left: 32, right: 32),
          child: TextField(
            keyboardType: TextInputType.name,
            decoration: const InputDecoration(labelText: 'Enter your name here'),
            style: const TextStyle(fontSize: 16),
            controller: _name,
          ),
        ),
        Padding(
          padding: const EdgeInsets.only(left: 32, right: 32),
          child: TextField(
            keyboardType: TextInputType.text,
            obscureText: true,
            decoration: const InputDecoration(labelText: 'Enter your password here'),
            style: const TextStyle(fontSize: 16),
            controller: _password,
          ),
        ),
        Container(
          color: boxColor,
          width: 150,
          height: 150,
        ),
        ElevatedButton(
          onPressed: () {
            setState(() {
              if(_name.text == 'Thiago' && _password.text == 'Thiago') {
                boxColor = Colors.green;
              } else {
                boxColor = Colors.blue;
                _showToast(context);
              }
            });
          },
          child: const Text('Change color'),
        )
      ],
    );
  }
}
