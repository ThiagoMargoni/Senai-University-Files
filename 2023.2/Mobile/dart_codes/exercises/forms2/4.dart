import 'dart:io';

double value_in_account = 1500.00;

void make_transations(String type, String pronoun, double value) {
  if (value_in_account >= value) {
    value_in_account -= value;
    print('$type realizad$pronoun com sucesso');
  } else {
    print('Você não pode fazer $pronoun $type por conter saldo insuficiente!');
  }

  print('Saldo Atual: R\$ $value_in_account');
}

void call_menu() {
  String type = '', pronoun = '', res = '';

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
      pronoun = 'o';
    case '2':
      type = 'Pix';
      pronoun = 'o';
    case '3':
      type = 'Empréstimo';
      pronoun = 'o';
    case '4':
      type = 'Transferência';
      pronoun = 'a';
  }

  print('Digite o valor da transação: ');
  var value = double.parse(stdin.readLineSync()!);

  make_transations(type, pronoun, value);
}

void main() {
  while (true) {
    call_menu();

    print('Deseja continuar? (S/N)');
    var res = stdin.readLineSync()!;

    if (res == 'N') {
      break;
    }
  }
}
