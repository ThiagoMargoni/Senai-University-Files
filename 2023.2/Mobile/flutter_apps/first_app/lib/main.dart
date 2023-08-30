import 'package:flutter/material.dart';

int cont = 0;

void counterValue(String button) {
  if(button == '+') {
    cont+=1;
  } else {
    cont-=1;
  }

  // ignore: avoid_print
  print('Counter value: $cont');
}

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Container(
        color: Colors.white,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Stack(
              alignment: AlignmentDirectional.center,
              children: [
                Container(color: Colors.red, width: 400, height: 80,),
                Container(
                  color: Colors.blue, 
                  width: 350, 
                  height: 50,
                  alignment: Alignment.center,
                  child: const Text(
                    'Mobile',
                    style: TextStyle(
                      decoration: TextDecoration.none,
                      color: Colors.white,
                      fontSize: 35,
                    )
                  ),
                )
              ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                Container(color: Colors.blue, height: 50, width: 50,),
                Container(color: Colors.green, height: 50, width: 50,),
                Container(color: Colors.red, height: 50, width: 50,),
              ],
            ),
            Container(
              color: Colors.amber,
              height: 50,
              width: 300,
              alignment: Alignment.center,
              child: const Text(
                'Senai',
                style: TextStyle(
                  decoration: TextDecoration.none,
                  color: Colors.black,
                  fontSize: 40
                ),
              ),
            ),
            Column(
              children: [
                ElevatedButton(onPressed: () => print('Button 1'), child: const Text('Button 1')),
                ElevatedButton(onPressed: () => counterValue('+'), child: const Text('Plus Counter')),
                ElevatedButton(onPressed: () => counterValue('-'), child: const Text('Subtract Counter')),
              ],
            )
          ],
        ),
      ),
    );
  }
}