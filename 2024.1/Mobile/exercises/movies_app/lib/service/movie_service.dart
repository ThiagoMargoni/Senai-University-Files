import 'package:http/http.dart' as http;
import 'dart:convert';

const String url =
    'https://raw.githubusercontent.com/danielvieira95/DESM-2/master/filmes.json';

class Movies {
  // ignore: non_constant_identifier_names
  final String name, image, duration, release_year, stars;
  Movies(this.name, this.image, this.duration, this.release_year, this.stars);
}

Future<List<Movies>> getMovies() async {
  List<Movies> movies = [];

  http.Response res = await http.get(Uri.parse(url),
      headers: {'Content-Type': 'application/json; charset=utf-8'});

  if (res.statusCode == 200) {
    for (Map i in json.decode(utf8.decode(res.bodyBytes))) {
      movies.add(Movies(i['nome'], i['imagem'], i['duração'],
          i['ano de lançamento'], i['nota']));
    }
  }

  return movies;
}
