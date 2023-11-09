import 'package:flutter/material.dart';

//flutter build apk --release to generate the exe

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Aplicativo Tarefas'),
        ),
        body: const Column(children: [
          Task("Aprender Flutter",
              "https://cdn-images-1.medium.com/v2/resize:fit:1024/0*vowtRZE_wvyVA7CB"),
          Task(" Jogar video game",
              "https://a-static.mlcdn.com.br/800x560/console-sony-playstation-5-825gb-marvels-spider-man-2-limited-edition/magazineluiza/237808200/7c0d5369fd416119d04202e4eb5513a0.jpg"),
          Task("Estudar",
              "https://img.imageboss.me/revista-cdn/cdn/6161/2264a8d4f17f8ee3f56155468163979b38eefbbf.jpg?1515696991"),
          Task("Jogar futebol",
              "https://conteudo.imguol.com.br/c/esporte/15/2022/12/18/messi-com-o-trofeu-da-copa-do-mundo-no-qatar-1671394673199_v2_900x506.jpg"),
        ]),
      ),
    );
  }
}

class Task extends StatefulWidget {
  final String task;
  final String img;

  const Task(this.task, this.img, {super.key});

  @override
  State<Task> createState() => _TaskState();
}

class _TaskState extends State<Task> {
  double level = 0;

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.white,
      child: Stack(
        children: [
          Container(
            color: Colors.blue,
            height: 140,
            child: LinearProgressIndicator(
              color: Colors.white,
              value: level,
            ),
          ),
          Container(
            color: Colors.white,
            height: 100,
            child: Column(
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container(
                      color: Colors.grey,
                      height: 100,
                      width: 80,
                      child: Image.network(
                        widget.img,
                        fit: BoxFit.fill,
                      ),
                    ),
                    Text(
                      widget.task,
                      style: const TextStyle(fontSize: 22),
                    ),
                    SizedBox(
                      height: 52,
                      width: 52,
                      child: ElevatedButton(
                          onPressed: () {
                            setState(() {
                              level++;
                              print('Level: $level');
                            });
                          },
                          child: const Column(
                            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [Icon(Icons.arrow_drop_up), Text('Up')],
                          )),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
