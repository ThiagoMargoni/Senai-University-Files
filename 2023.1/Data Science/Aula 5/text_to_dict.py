data = {
    'session': [],
    'right': [],
    'politic': [],
    'statistic': []
}

string = '''Pessoal 9 9,0 9
Pessoal 9 6,5 9
Pessoal 9 9,0 8
Pessoal 9 6,0 8
Pessoal 9 6,5 9
Pessoal 9 6,5 10
Pessoal 9 9,0 8
Técnica 9 6,0 8
Técnica 9 9,0 9
Técnica 9 9,0 8
Técnica 9 7,0 10
Técnica 9 5,5 7
Técnica 9 6,0 7
Técnica 9 8,0 9
Vendas 9 7,0 8
Vendas 9 9,0 7
Vendas 9 10,0 8
Vendas 9 5,5 9
Vendas 9 7,0 2
Vendas 9 6,0 7
Vendas 9 6,5 7
Vendas 9 6,0 8
Vendas 9 9,0 9
Vendas 9 6,5 8
Vendas 9 7,0 7'''

listString = string.split(sep='\n')

for i in listString:
    newString = i.split(sep=' ')

    i = 0
    for x in newString:
        match i:
            case 0: data['session'].append(f'{x}')
            case 1: data['right'].append(int(x))
            case 2: data['politic'].append(float(x.replace(',', '.')))
            case 3: data['statistic'].append(int(x))
        i+=1