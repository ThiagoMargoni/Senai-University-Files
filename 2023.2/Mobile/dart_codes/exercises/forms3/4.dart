import 'dart:io';

class Client {
  String name;
  String job;
  double value_in_account;

  Client(this.name, this.job, this.value_in_account);

  void make_transations(String type, double value) {
    if (this.value_in_account >= value) {
      this.value_in_account -= value;
      print('$type realizado com sucesso');
    } else {
      print(
          'Você não pode fazer o $type por conter saldo insuficiente!');
    }

    print(
        '${this.name}, que é ${this.job}, têm agora saldo de R\$ ${this.value_in_account}');
  }
}

void main() {
  print('Digite seu nome: ');
  var name = stdin.readLineSync()!;

  print('Digite sua profissão: ');
  var job = stdin.readLineSync()!;

  print('Digite o saldo na sua conta: ');
  var value_in_account = double.parse(stdin.readLineSync()!);

  Client client = Client(name, job, value_in_account);

  while (true) {
    String type = '', res = '';

    while (true) {
      print(
          'Digite o número da transação abaixo que deseja fazer: \n1 - Saque\n2 - Pix\n3 - Empréstimos\n4 - Transferências');

      res = stdin.readLineSync()!;

      if (res == '1' || res == '2' || res == '3' || res == '4') {
        break;
      } else {
        print('Digite uma das opções');
      }
    }

    switch (res) {
      case '1':
        type = 'Saque';
      case '2':
        type = 'Pix';
      case '3':
        type = 'Empréstimo';
      case '4':
        type = 'Extrato';
    }

    print('Digite o valor da transação: ');
    var value = double.parse(stdin.readLineSync()!);
    client.make_transations(type, value);

    print('Deseja continuar? (S/N)');
    var aux = stdin.readLineSync()!;

    if (aux.toUpperCase() == 'N') {
      break;
    }
  }
}
