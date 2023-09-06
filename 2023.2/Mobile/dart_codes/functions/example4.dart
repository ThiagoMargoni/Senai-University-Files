void calc_salary(double salary, Function f) {
  print('Salary R\$ $salary');
  f();
}

void calc_bonus() {
  print('Bonus R\$ 50.0');
}

void main() {
  calc_salary(5000, calc_bonus);
}
