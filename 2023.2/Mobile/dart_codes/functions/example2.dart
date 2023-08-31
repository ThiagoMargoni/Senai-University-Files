import 'dart:io';

double calc_salary(double salary, double bonus) {
  salary += (salary * 0.1) + bonus;
  return salary;
}

void main() {
  print('Type your salary in R\$: ');
  double salary = double.parse(stdin.readLineSync()!);
  print('Type your bonus in R\$: ');
  double bonus = double.parse(stdin.readLineSync()!);

  salary = calc_salary(salary, bonus);
  print('Your salary is R\$ $salary');
}
