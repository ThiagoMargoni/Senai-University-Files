import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  String price = "0";
  TextEditingController value = TextEditingController();
  int? selectop, selectop1;
  double vdolar = 0;
  double veuro = 0;
  double vreais = 0;

  void getBitcoinPrice() async {
    String url = "https://blockchain.info/ticker";
    http.Response res = await http.get(Uri.parse(url));
    Map<String, dynamic> data = json.decode(res.body);

    setState(() {
      price = data['BRL']['buy'].toString().replaceFirst('.', ',');
    });
  }

  convertValue() {
    if (selectop == 0 && selectop1 == 1) {
      setState(() {
        vdolar = double.parse(value.text);
      });
    } else if (selectop == 0 && selectop1 == 3) {
      setState(() {
        vdolar = double.parse(value.text) / 5.01;
      });
    } else if (selectop == 0 && selectop1 == 5) {
      setState(() {
        vdolar = double.parse(value.text) / 5.45;
      });
    } else if (selectop == 2 && selectop1 == 1) {
      setState(() {
        vdolar = double.parse(value.text) * 5.01;
      });
    } else if (selectop == 2 && selectop1 == 3) {
      setState(() {
        vdolar = double.parse(value.text);
      });
    } else if (selectop == 2 && selectop1 == 5) {
      setState(() {
        vdolar = double.parse(value.text) * 0.92;
      });
    } else if (selectop == 3 && selectop1 == 1) {
      setState(() {
        vdolar = double.parse(value.text) * 0.18;
      });
    } else if (selectop == 4 && selectop1 == 3) {
      setState(() {
        vdolar = double.parse(value.text) * 0.91;
      });
    } else if (selectop == 4 && selectop1 == 5) {
      setState(() {
        vdolar = double.parse(value.text);
      });
    } else if (selectop == 4 && selectop1 == 1) {
      setState(() {
        vdolar = double.parse(value.text) * 5.45;
      });
    }
  }

  clean() {
    setState(() {
      vdolar = 0;
      value.text = "";
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          backgroundColor: Colors.blue, title: const Text('Price Consult')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Row(children: <Widget>[
              Expanded(
                child: Container(
                    margin: const EdgeInsets.only(left: 10.0, right: 20.0),
                    child: const Divider(
                      color: Color.fromARGB(255, 197, 149, 4),
                      height: 36,
                    )),
              ),
              const Text(
                "Consult Bitcoin Price",
                style: TextStyle(
                    fontSize: 20, color: Color.fromARGB(255, 189, 143, 8)),
              ),
              Expanded(
                child: Container(
                    margin: const EdgeInsets.only(left: 20.0, right: 10.0),
                    child: const Divider(
                      color: Color.fromARGB(255, 197, 149, 4),
                      height: 36,
                    )),
              ),
            ]),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: Text(
                'Bitcoin Value: R\$ $price',
                style: const TextStyle(fontSize: 20),
              ),
            ),
            ElevatedButton(
                onPressed: getBitcoinPrice,
                child: const Text('Get Bitcoin Price')),
            Row(children: <Widget>[
              Expanded(
                child: Container(
                    margin: const EdgeInsets.only(left: 10.0, right: 20.0),
                    child: const Divider(
                      color: Color.fromARGB(255, 56, 126, 58),
                      height: 36,
                    )),
              ),
              const Text(
                "Convert the Price",
                style: TextStyle(
                    fontSize: 20, color: Color.fromARGB(255, 56, 126, 58)),
              ),
              Expanded(
                child: Container(
                    margin: const EdgeInsets.only(left: 20.0, right: 10.0),
                    child: const Divider(
                      color: Color.fromARGB(255, 56, 126, 58),
                      height: 36,
                    )),
              ),
            ]),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: TextField(
                keyboardType: TextInputType.number,
                decoration: const InputDecoration(
                  labelText: "Type the value to convert",
                  border: OutlineInputBorder()
                ),
                controller: value,
              ),
            ),
            const Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                Text(
                  "From",
                  style: TextStyle(fontSize: 15),
                ),
                Text(
                  "To",
                  style: TextStyle(fontSize: 15),
                ),
              ],
            ),
            Container(
              color: Colors.transparent,
              width: 450,
              height: 150,
              child: Column(
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      Radio(
                          value: 0,
                          groupValue: selectop,
                          onChanged: (value) {
                            setState(() {
                              selectop = value;
                            });
                          }),
                      const Text("R\$"),
                      Radio(
                          value: 1,
                          groupValue: selectop1,
                          onChanged: (value) {
                            setState(() {
                              selectop1 = value;
                            });
                          }),
                      const Text("R\$"),
                    ],
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      Radio(
                          value: 2,
                          groupValue: selectop,
                          onChanged: (value) {
                            setState(() {
                              selectop = value;
                            });
                          }),
                      const Text("Dólar"),
                      Radio(
                          value: 3,
                          groupValue: selectop1,
                          onChanged: (value) {
                            setState(() {
                              selectop1 = value;
                            });
                          }),
                      const Text("Dólar"),
                    ],
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      Radio(
                          value: 4,
                          groupValue: selectop,
                          onChanged: (value) {
                            setState(() {
                              selectop = value;
                            });
                          }),
                      const Text("Euro"),
                      Radio(
                          value: 5,
                          groupValue: selectop1,
                          onChanged: (value) {
                            setState(() {
                              selectop1 = value;
                            });
                          }),
                      const Text("Euro"),
                    ],
                  )
                ],
              ),
            ),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 50),
              child: Text(
                "Converted Value  \$ ${vdolar.toStringAsFixed(2)}",
                style: TextStyle(fontSize: 20),
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                ElevatedButton(onPressed: convertValue, child: const Text("Convert Price")),
                ElevatedButton(onPressed: clean, child: const Text("Clean Text")),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
