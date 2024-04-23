import 'package:flutter/material.dart';

class ListItems extends StatefulWidget {
  const ListItems({super.key});

  @override
  State<ListItems> createState() => _ListItemsState();
}

class _ListItemsState extends State<ListItems> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('List Items'),
        ),
        body: Stack(
          alignment: Alignment.center,
          children: [
            ListView(
              children: [
                Item('- Sopa'),
                Item('- Mostarda'),
                Item('- Ketchup'),
                Item('- Sal'),
                Item('- Vinagre'),
                Item('- Pão'),
                Item('- Leite'),
                Item('- Macarrão'),
                Item('- Granola'),
                Item('- Sorvete'),
                Item('- Arroz'),
                Item('- Feijão')
              ],
            )
          ],
        )
    );
  }
}

class Item extends StatefulWidget {
  final String name;

  Item(this.name, {super.key});

  @override
  State<Item> createState() => ItemState();
}

class ItemState extends State<Item> {
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(12.0),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Text(
            widget.name,
            style: const TextStyle(fontSize: 30),
          )
        ],
      ),
    );
  }
}