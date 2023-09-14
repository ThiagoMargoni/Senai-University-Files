class User {
  String? username;
  String? password;

  String autenticate(username, password) {
    if (username == this.username && password == this.password) {
      return 'Successfully Loged';
    } else {
      return 'Invalide Username/Password';
    }
  }
}

void main() {
  User user = User();

  user.username = 'test';
  user.password = 'test';

  print(user.autenticate('test', 'aaa'));
}
