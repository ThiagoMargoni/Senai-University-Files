import 'dart:io';

class People {
  String? name;
  int? age;
  String? profession;
  double? salary;

  void show_job(String company, int working_time) =>
      print('Company: $company\nWorking Time: $working_time');
}

void main() {
  People people = People();

  print('Digite a empresa em que trabalha: ');
  String company = stdin.readLineSync()!;

  print('Digite sua carga horária diária: ');
  int working_time = int.parse(stdin.readLineSync()!);

  people.show_job(company, working_time);
}
