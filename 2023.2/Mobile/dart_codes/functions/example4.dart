void calc_salary(double salary, Function f) {
  print('Salary R\$ $salary');
  f();
}

double calc_salary2(double salary, double desc, Function f) {
  f();
  return salary -= salary * desc;
}

void show_message() {
  print('Payment day ');
}

void calc_bonus() {
  print('Bonus R\$ 50.0');
}

void main() {
  // calc_salary(5000, calc_bonus);
  double salary = calc_salary2(500, 0.1, show_message);
  print('Salary: $salary');
}
