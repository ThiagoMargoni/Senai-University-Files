abstract class Automobile {
  void name();
  void color();
  void year();
  void belt(bool using);
  void status(bool is_on);
}

class Car implements Automobile {
  void name() {
    print('Palio');
  }

  void color() {
    print('Red');
  }

  void year() {
    print(2020);
  }

  void belt(bool using) {
    if (using == true) {
      print('Using the safety belt');
    } else {
      print('Not using the safety belt');
    }
  }

  void status(bool is_on) {
    if (is_on == true) {
      print('The car is off');
    } else {
      print('The car is on');
    }
  }
}

void main() {
  Car palio = Car();
  palio.name();
  palio.color();
  palio.year();
  palio.belt(true);
  palio.status(true);
}
