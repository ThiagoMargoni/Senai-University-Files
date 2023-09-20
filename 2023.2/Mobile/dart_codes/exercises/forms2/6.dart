import 'dart:io';

class ShoppingCart {
  var itens = [];
  var quantitys = [];
  var unitary_prices = [];

  void add_item(String name, int quantity, double price) {
    this.itens.add(name);
    this.quantitys.add(quantity);
    this.unitary_prices.add(price);

    print('Item adicionado com sucesso');
  }

  void remove_item(int index) {
    this.itens.removeAt(index);
    this.quantitys.removeAt(index);
    this.unitary_prices.removeAt(index);

    print('Item removido com sucesso');
  }

  void calculate_total() {
    double total = 0.0;
    for (var i = 0; i < this.itens.length; i++) {
      total += this.quantitys[i] * this.unitary_prices[i];
    }

    print('Total da compra: R\$ $total');
  }
}

void main() {
  var compra = ShoppingCart();

  while (true) {
    String answer = '';

    while (true) {
      print(
          'Digite o número correspondente a escolha que deseja fazer: \n1 - Adicionar Item\n2 - Remover Item\n3 - Calcular Preço Total');

      answer = stdin.readLineSync()!;

      if (answer == '1' || answer == '2' || answer == '3') {
        break;
      } else {
        print('Digite uma das opções');
      }
    }

    if (answer == '1') {
      print('Digite o nome do item: ');
      var name = stdin.readLineSync()!;

      print('Digite a quantidade de itens: ');
      var quantity = int.parse(stdin.readLineSync()!);

      print('Digite o preço unitário do items: ');
      var price = double.parse(stdin.readLineSync()!);

      compra.add_item(name, quantity, price);
    } else if (answer == '2') {
     if(compra.itens.length > 0) {
      String string = '';
      for (var i = 0; i < compra.itens.length; i++) {
        string += '\n${i + 1} - ${compra.itens[i]}';
      }

      print('Digite o número do item que deseja remover: $string');
      var index = int.parse(stdin.readLineSync()!);

      compra.remove_item(index - 1);
     } else {
      print('Não há itens no carrinho');
     }
    } else {
      compra.calculate_total();
    }

    print('Deseja continuar? (S/N)');
    var res = stdin.readLineSync()!;

    if (res == 'N') {
      break;
    }
  }
}
