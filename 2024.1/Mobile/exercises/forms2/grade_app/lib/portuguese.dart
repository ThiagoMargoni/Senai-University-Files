import 'package:flutter/material.dart';

class Portuguese extends StatefulWidget {
  const Portuguese({super.key});

  @override
  State<Portuguese> createState() => _PortugueseState();
}

class _PortugueseState extends State<Portuguese> {

  final _studentController = TextEditingController();
  final _firstGrade = TextEditingController();
  final _secondGrade = TextEditingController();
  final _thirdGrade = TextEditingController();
  final _fourthGrade = TextEditingController();
  String text = 'Mean Will Appear Here!';
  double mean = 0.0;
  
  void calcMean() {
    setState(() {
      mean = (double.parse(_firstGrade.text)+double.parse(_secondGrade.text)+double.parse(_thirdGrade.text)+double.parse(_fourthGrade.text))/4;
      text = "${_studentController.text}'s Mean: $mean";
    });
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Portuguese Grade'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: TextField(
                controller: _studentController,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  hintText: 'Type the Student Name: '
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: TextField(
                controller: _firstGrade,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  hintText: 'Type the First Grade: ',
                ),
                keyboardType: TextInputType.number,
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: TextField(
                controller: _secondGrade,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  hintText: 'Type the Second Grade: ',
                ),
                keyboardType: TextInputType.number,
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: TextField(
                controller: _thirdGrade,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  hintText: 'Type the Third Grade: ',
                ),
                keyboardType: TextInputType.number,
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: TextField(
                controller: _fourthGrade,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  hintText: 'Type the Fourth Grade: ',
                ),
                keyboardType: TextInputType.number,
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: ElevatedButton(
                onPressed: calcMean,
                child: const Text('Calc Mean'),
              ),
            ),
            Text(text)
          ],
        ),
      )
    );
  }
}