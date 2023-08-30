import 'dart:io';

void main() {
  int weekday;
  
  print('Digite o dia da semana em numeral: ');
  weekday = int.parse(stdin.readLineSync()!);

  switch(weekday) {
    case 1: print('Dia da semana é Domingo'); break;
    case 2: print('Dia da semana é Segunda'); break; 
    case 3: print('Dia da semana é Terça'); break; 
    case 4: print('Dia da semana é Quarta'); break; 
    case 5: print('Dia da semana é Quinta'); break; 
    case 6: print('Dia da semana é Sexta'); break; 
    case 7: print('Dia da semana é Sábado'); break; 
    default: print('Dia da semana Inexistente');
  }
}