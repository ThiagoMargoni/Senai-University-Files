import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(
    debugShowCheckedModeBanner: false,
    home: Grade(),
  ));
}

class Grade extends StatefulWidget {
  const Grade({super.key});

  @override
  State<Grade> createState() => _GradeState();
}

class _GradeState extends State<Grade> {
  final TextEditingController _name = TextEditingController();
  final TextEditingController _age = TextEditingController();
  final TextEditingController _address = TextEditingController();
  final TextEditingController _email = TextEditingController();
  final TextEditingController _phone = TextEditingController();
  String name = '', age = '', address = '', email = '', phone = '';

  void _showToast(BuildContext context, String na, String ag, String ad,
      String em, String ph) {
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(
      content: Text(
          'Name: $na\nAge: $ag\nAddress: $ad\nE-mail: $em\nPhone Number: $ph'),
      duration: Duration(seconds: 2),
    ));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('User Information'),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Padding(
            padding: const EdgeInsets.only(left: 32, right: 32),
            child: TextField(
              keyboardType: TextInputType.name,
              decoration: const InputDecoration(labelText: 'Enter Your Name'),
              style: const TextStyle(fontSize: 16),
              controller: _name,
            ),
          ),
          Padding(
            padding: const EdgeInsets.only(left: 32, right: 32),
            child: TextField(
              keyboardType: TextInputType.number,
              decoration: const InputDecoration(labelText: 'Enter Your Age'),
              style: const TextStyle(fontSize: 16),
              controller: _age,
            ),
          ),
          Padding(
            padding: const EdgeInsets.only(left: 32, right: 32),
            child: TextField(
              keyboardType: TextInputType.streetAddress,
              decoration:
                  const InputDecoration(labelText: 'Enter Your Address'),
              style: const TextStyle(fontSize: 16),
              controller: _address,
            ),
          ),
          Padding(
            padding: const EdgeInsets.only(left: 32, right: 32),
            child: TextField(
              keyboardType: TextInputType.emailAddress,
              decoration: const InputDecoration(labelText: 'Enter Your Email'),
              style: const TextStyle(fontSize: 16),
              controller: _email,
            ),
          ),
          Padding(
            padding: const EdgeInsets.only(left: 32, right: 32),
            child: TextField(
              keyboardType: TextInputType.phone,
              decoration:
                  const InputDecoration(labelText: 'Enter Your Phone Number'),
              style: const TextStyle(fontSize: 16),
              controller: _phone,
            ),
          ),
          ElevatedButton(
            onPressed: () {
              setState(() {
                name = _name.text;
                age = _age.text;
                address = _address.text;
                email = _email.text;
                phone = _phone.text;

                _showToast(context, name, age, address, email, phone);
              });
            },
            child: const Text('Save User Information'),
          )
        ],
      ),
    );
  }
}
