import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class CreateUser extends StatefulWidget {
  const CreateUser({super.key});

  @override
  State<CreateUser> createState() => _CreateUserState();
}

class _CreateUserState extends State<CreateUser> {
  final TextEditingController _user = TextEditingController();
  final TextEditingController _password = TextEditingController();
  String url = 'http://10.109.83.19:3000/users';

  void createUser(login, password, context) async {
    http.Response res = await http.post(
      Uri.parse(url),
      headers: {
        'Content-Type': 'application/json; charset=UTF-8'
      },
      body: jsonEncode({ "login": login, "password": password })
    );

    if(res.statusCode == 201) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('User Create Successfully'),
          duration: Duration(seconds: 2),
        )
      );
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('An Error Ocorred'),
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
                  child: const Text('Create User'),
                  onPressed: () => createUser(_user.text, _password.text, context),
                ),
                Container(
                    margin: const EdgeInsets.all(10.0),
                    child: Container()
                ),
                ElevatedButton(
                  child: const Text('Login'),
                  onPressed: () => Navigator.pop(context)
                )
              ],
            )
          ],
        ),
      ),
    );
  }
}