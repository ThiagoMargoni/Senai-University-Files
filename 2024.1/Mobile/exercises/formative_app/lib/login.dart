import 'package:flutter/material.dart';
import 'package:formative_app/create_user.dart';
import 'package:formative_app/list_product.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class Login extends StatefulWidget {
  const Login({super.key});

  @override
  State<Login> createState() => _LoginState();
}

class _LoginState extends State<Login> {
  final TextEditingController _user = TextEditingController();
  final TextEditingController _password = TextEditingController();
  String url = 'http://10.109.83.19:3000/users';

  void makeLogin(login, password, context) async {
    http.Response res = await http.get(Uri.parse(url));
    List data = json.decode(res.body) as List;
    List filteredData = data.where((user) => user['login'] == login && user['password'] == password).toList();

    if(filteredData.isNotEmpty) {
      Navigator.push(context, MaterialPageRoute(builder: (context) => const ListProducts()));
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('User/Password Mismatch'),
          duration: Duration(seconds: 2),
        )
      );
    }
  }

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