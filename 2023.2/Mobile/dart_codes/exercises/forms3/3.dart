import 'dart:io';

class User {
  String login;
  String password;

  User(this.login, this.password);

  void authenticate() {
    if (this.login == 'adm' && this.password == '123') {
      print('Logado com Sucesso');
    } else {
      print('Usuário/Senha Incorretos');
    }
  }
}

void main() {
  print('Digite seu login: ');
  var login = stdin.readLineSync()!;

  print('Digite sua senha: ');
  var password = stdin.readLineSync()!;

  User user = User(login, password);

  user.authenticate();
}
