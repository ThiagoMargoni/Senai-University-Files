class House {
  String? color;
  double? price;

  void open_door() {
    print('Door Open');
  }

  void open_window() {
    print('Window Open');
  }

  void open_house(bool open) {
    if (open == false) {
      this.open_window();
      this.open_door();
    } else {
      print('Window Closed');
      print('Door Closed');
    }
  }
}

void main() {
  House myHouse = House();
  myHouse.color = 'Blue';
  myHouse.price = 1249343.00;

  print(
      'The house color is ${myHouse.color} and the price is ${myHouse.price}');

  myHouse.open_door();
  myHouse.open_window();
  myHouse.open_house(true);

  House house2 = House();
  house2.color = 'Red';
  print(house2);
}
