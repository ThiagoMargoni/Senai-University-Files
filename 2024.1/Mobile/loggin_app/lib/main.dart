import 'package:flutter/material.dart';
import 'package:loggin_app/welcome.dart';

void main() {
  runApp(const MaterialApp(
    debugShowCheckedModeBanner: false,
    home: LoginWindow(),
  ));
}

class LoginWindow extends StatefulWidget {
  const LoginWindow({super.key});

  @override
  State<LoginWindow> createState() => _LoginWindowState();
}

class _LoginWindowState extends State<LoginWindow> {

  final TextEditingController _name = TextEditingController();
  final TextEditingController _password = TextEditingController();

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
    return Scaffold(
      appBar: AppBar(
        title: const Text('App Login'),
      ),
      body: Column(
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
          ElevatedButton(
            onPressed: () {
              if(_name.text == 'Thiago' && _password.text == 'Thiago') {
                Navigator.push(context, MaterialPageRoute(builder: (context) => const WelcomeWindow()));
              } else {
                _showToast(context);
              }
            },
            child: const Text('Login'),
          )
        ],
      ),
    );
  }
}
