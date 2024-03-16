import 'package:flutter/material.dart';
import 'dart:math';

double height = 50;
double width = 50;
Color color = Colors.blueGrey;
BorderRadiusGeometry borderRadius = BorderRadius.circular(8);

void main() {
  runApp(const AnimationContainer());
}

class AnimationContainer extends StatefulWidget {
  const AnimationContainer({super.key});

  @override
  State<AnimationContainer> createState() => _AnimationContainerState();
}

class _AnimationContainerState extends State<AnimationContainer> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Animation App'),
        ),
        body: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Center(
              child: AnimatedContainer(
                width: width,
                height: height,
                decoration:
                    BoxDecoration(color: color, borderRadius: borderRadius),
                duration: const Duration(seconds: 1),
                curve: Curves.fastOutSlowIn,
              ),
            ),
            FloatingActionButton(
              onPressed: () {
                setState(() {
                  final random = Random();

                  // widget.height = random.nextInt(300).toDouble();
                  // widget.width = random.nextInt(300).toDouble();

                  height = random.nextDouble() * 300;
                  width = random.nextDouble() * 300;

                  color = Color.fromRGBO(random.nextInt(256),
                      random.nextInt(256), random.nextInt(256), 1);

                  borderRadius =
                      BorderRadius.circular(random.nextDouble() * 100);
                });
              },
              child: const Icon(Icons.play_arrow),
            ),
            const SnackBarComponent()
          ],
        ),
      ),
    );
  }
}

class SnackBarComponent extends StatelessWidget {
  const SnackBarComponent({super.key});

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () {
        final snack = SnackBar(
          content: const Text("I'm a Snack Bar"),
          action: SnackBarAction(
            label: 'Undo',
            onPressed: () {},
          ),
        );

        ScaffoldMessenger.of(context).showSnackBar(snack);
      },
      child: const Text('Show Snack Bar'),
    );
  }
}
