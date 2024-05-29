import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import 'package:movies_app/screens/list_movies.dart';

const String url = 'http://10.109.83.19:3000/users';

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
        content: Text('An Error Occurred'),
        duration: Duration(seconds: 2),
      )
    );
  }
}

void makeLogin(login, password, context) async {
    http.Response res = await http.get(Uri.parse(url));
    List data = json.decode(res.body) as List;
    List filteredData = data.where((user) => user['login'] == login && user['password'] == password).toList();

    if(filteredData.isNotEmpty) {
      Navigator.push(context, MaterialPageRoute(builder: (context) => const ListMovies()));
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('User/Password Mismatch'),
          duration: Duration(seconds: 2),
        )
      );
    }
  }