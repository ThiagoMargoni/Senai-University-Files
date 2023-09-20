import 'dart:io';

double calc_salary(double gross_salary) {
  return gross_salary - (gross_salary * 0.1) + (gross_salary * 0.2);
}

void main() {
  print('Digite seu salário bruto');
  var gross_salary = double.parse(stdin.readLineSync()!);

  print('Salário líquido: R\$ ${calc_salary(gross_salary)}');
}
