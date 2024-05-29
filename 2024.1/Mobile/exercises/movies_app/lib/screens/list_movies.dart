import 'package:flutter/material.dart';

import 'package:movies_app/service/movie_service.dart';

class ListMovies extends StatefulWidget {
  const ListMovies({super.key});

  @override
  State<ListMovies> createState() => _ListMoviesState();
}

class _ListMoviesState extends State<ListMovies> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('List Products'),
        backgroundColor: Colors.blue,
      ),
      body: FutureBuilder(
        future: getMovies(),
        builder: (context, AsyncSnapshot<List<Movies>> snapshot) {
          return ListView.builder(
              itemCount: snapshot.data?.length ?? 0,
              itemBuilder: (context, index) {
                return Card(
                  child: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: [
                        Text(
                            'Movie Name: ${snapshot.data![index].name.toString()}'),
                        Text(
                            'Movie Image: ${snapshot.data![index].image.toString()}'),
                        Text(
                            'Movie Duration: ${snapshot.data![index].duration.toString()}'),
                        Text(
                            'Movie Release Year: ${snapshot.data![index].release_year.toString()}'),
                        Text(
                            'Movie Stars: ${snapshot.data![index].stars.toString()}'),
                      ],
                    ),
                  ),
                );
              }
            );
        },
      )
    );
  }
}