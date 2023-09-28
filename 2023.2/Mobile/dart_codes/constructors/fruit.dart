class Food {
  String? name;
  String? flavor;
  double? weight;

  Food(this.name, this.flavor, this.weight);

  void return_name() {
    print('Name: ${this.name}');
  }
}

class Fruit extends Food {
  int? harvest_day;
  Fruit(String name, String flavor, double weight, int harvest_day)
      : super(name, flavor, weight);

  void return_name() => super.return_name();
}
