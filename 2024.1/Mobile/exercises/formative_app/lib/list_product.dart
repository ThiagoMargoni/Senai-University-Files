import 'package:flutter/material.dart';
import 'package:formative_app/create_product.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class Products {
  final String id, name, price, qt;
  Products(this.id, this.name, this.price, this.qt);
}

class ListProducts extends StatefulWidget {
  const ListProducts({super.key});

  @override
  State<ListProducts> createState() => _ListProductsState();
}

class _ListProductsState extends State<ListProducts> {
  String url = 'http://10.109.83.19:3000/products';
  List<Products> products = [];

  Future<List<Products>> getProducts() async {
    products = [];
    http.Response res = await http.get(Uri.parse(url),
        headers: {'Content-Type': 'application/json; charset=utf-8'});

    if (res.statusCode == 200) {
      for (Map i in json.decode(utf8.decode(res.bodyBytes))) {
        products.add(Products(i['id'], i['name'], i['price'], i['qt']));
      }
    }

    return products;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('List Products'),
        backgroundColor: Colors.blue,
      ),
      body: FutureBuilder(
        future: getProducts(),
        builder: (context, AsyncSnapshot<List<Products>> snapshot) {
          return ListView.builder(
              itemCount: products.length,
              itemBuilder: (context, index) {
                return Card(
                  child: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: [
                        Text(
                            'Product Id: ${snapshot.data![index].id.toString()}'),
                        Text(
                            'Product Name: ${snapshot.data![index].name.toString()}'),
                        Text(
                            'Product Price: ${snapshot.data![index].price.toString()}'),
                        Text(
                            'Product Quantity: ${snapshot.data![index].qt.toString()}'),
                      ],
                    ),
                  ),
                );
              }
            );
        },
      ),
      floatingActionButton: FloatingActionButton(
          backgroundColor: Colors.blue,
          tooltip: 'Create Product',
          onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (context) => const CreateProduct())),
          child: const Icon(Icons.add, color: Colors.white, size: 28),
      ),
    );
  }
}
