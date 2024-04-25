import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:formative_app/list_product.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class CreateProduct extends StatefulWidget {
  const CreateProduct({super.key});

  @override
  State<CreateProduct> createState() => _CreateProductState();
}

class _CreateProductState extends State<CreateProduct> {

  String url = 'http://10.109.83.19:3000/products';
  final TextEditingController _name = TextEditingController();
  final TextEditingController _price = TextEditingController();
  final TextEditingController _quantity = TextEditingController();

  void createProduct(name, price, quantity, context) async {
    http.Response res = await http.post(
      Uri.parse(url),
      headers: {
        'Content-Type': 'application/json; charset=UTF-8'
      },
      body: jsonEncode({ "name": name, "price": price, "qt": quantity})
    );

    if(res.statusCode == 201) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Product Create Successfully'),
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
                controller: _name,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(8))),
                  labelText: 'Type the Product Name'
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: TextField(
                keyboardType: const TextInputType.numberWithOptions(decimal: true),
                controller: _price,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(8))),
                  labelText: 'Type the Product Price'
                ),
                inputFormatters: [ FilteringTextInputFormatter.allow(RegExp(r'^[0-9]+.?[0-9]*')) ]
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: TextField(
                keyboardType: TextInputType.number,
                controller: _quantity,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(8))),
                  labelText: 'Type the Quantity in the Stock'
                ),
                inputFormatters: [ FilteringTextInputFormatter.digitsOnly ]
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                  child: const Text('Create Product'),
                  onPressed: () => createProduct(_name.text, _price.text, _quantity.text, context),
                ),
                Container(
                    margin: const EdgeInsets.all(10.0),
                    child: Container()
                ),
                ElevatedButton(
                  child: const Text('List Products'),
                  onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (context) => const ListProducts()))
                )
              ],
            )
          ],
        ),
      ),
    );
  }
}