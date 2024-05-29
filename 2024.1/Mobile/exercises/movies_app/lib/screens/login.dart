import 'package:flutter/material.dart';
import 'package:movies_app/screens/create_user.dart';
import 'package:movies_app/service/user_service.dart';

class Login extends StatefulWidget {
  const Login({super.key});

  @override
  State<Login> createState() => _LoginState();
}

class _LoginState extends State<Login> {
  final TextEditingController _user = TextEditingController();
  final TextEditingController _password = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Login'),
        backgroundColor: Colors.blue,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: TextField(
                keyboardType: TextInputType.name,
                controller: _user,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(8))),
                  labelText: 'Type your login'
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: TextField(
                keyboardType: TextInputType.text,
                obscureText: true,
                obscuringCharacter: '*',
                controller: _password,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(8))),
                  labelText: 'Type your password'
                ),
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                  child: const Text('Login'),
                  onPressed: () => makeLogin(_user.text, _password.text, context),
                ),
                Container(
                    margin: const EdgeInsets.all(10.0),
                    child: Container()
                ),
                ElevatedButton(
                  child: const Text('Sign up'),
                  onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (context) => const CreateUser()))
                )
              ],
            )
          ],
        ),
      ),
    );
  }
}