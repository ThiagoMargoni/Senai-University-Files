class Animal {
  String name;
  double age;
  String color;
  String type;

  Animal(this.name, this.age, this.color, this.type);

  void weight(double weight) => print('The weight of ${name} is ${weight} kg');

  void sleep() => print('The ${name} slept');

  void wake() => print('the ${name} wake up');
}

abstract class Feed {
  void separateIngredients();
  void takeBowl();
  void prepareFood();
}

class Dog extends Animal implements Feed {
  Dog(String name, double age, String color, String type)
      : super(name, age, color, type);

  @override
  void separateIngredients() =>
      print('Separating the ingredients for ${name} food');

  @override
  void takeBowl() => print('Taking the bowl for put the ${name} food');

  @override
  void prepareFood() => print('Preparing food to feed the ${name}');

  void sleep() => super.sleep();

  void wake() => super.wake();

  void weight(double weight) => super.weight(weight);
}

class Bird extends Animal implements Feed {
  Bird(String name, double age, String color, String type)
      : super(name, age, color, type);

  @override
  void separateIngredients() =>
      print('Separating the ingredients for ${name} food');

  @override
  void takeBowl() => print('Taking the bowl for put the ${name} food');

  @override
  void prepareFood() => print('Preparing food to feed the ${name}');

  void sleep() => super.sleep();

  void wake() => super.wake();

  void weight(double weight) => super.weight(weight);
}

class Tiger extends Animal implements Feed {
  Tiger(String name, double age, String color, String type)
      : super(name, age, color, type);

  @override
  void separateIngredients() =>
      print('Separating the ingredients for ${name} food');

  @override
  void takeBowl() => print('Taking the bowl for put the ${name} food');

  @override
  void prepareFood() => print('Preparing food to feed the ${name}');

  void sleep() => super.sleep();

  void wake() => super.wake();

  void weight(double weight) => super.weight(weight);
}

class Fish extends Animal implements Feed {
  Fish(String name, double age, String color, String type)
      : super(name, age, color, type);

  @override
  void separateIngredients() =>
      print('Separating the ingredients for ${name} food');

  @override
  void takeBowl() => print('Taking the bowl for put the ${name} food');

  @override
  void prepareFood() => print('Preparing food to feed the ${name}');

  void sleep() => super.sleep();

  void wake() => super.wake();

  void weight(double weight) => super.weight(weight);
}

void main() {
  Fish clownfish = Fish('Jony', 2, 'Orange', 'ClownFish');

  clownfish.separateIngredients();
  clownfish.sleep();
  clownfish.takeBowl();
  clownfish.wake();
  clownfish.prepareFood();
  clownfish.weight(1);
}
