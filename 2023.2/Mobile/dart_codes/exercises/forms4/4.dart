class People {
  String name = 'Jonathan';
  int age = 18;

  String get Name {
    print(name);
    return this.name;
  }

  int get Age {
    print(age);
    return this.age;
  }

  set Age(int age) {
    if (age >= 18 && age <= 60) {
      age = this.age;
      print('You are an adult');
    } else {
      print('You are not an adult');
    }
  }
}

void main() {
  People people = People();
  people.Name;
  people.Age;
}
