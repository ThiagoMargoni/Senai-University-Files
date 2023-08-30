while True:
    n1, n2 = 0,0
    j = 0
    while j < 2:
        num = input(f'Digite o {j+1}º valor (números decimais serão arredondados): ')
        aux = num.replace('.', '')
        aux = aux.replace('-', '')

        if aux.isnumeric():
            if n1 == 0:
                n1 = round(float(num))
            else:
                n2 = round(float(num))    
            j+=1
        else:
            print('Favor Inserir Apenas Números')
    
    string = ''
    if n1 > n2:
        for i in range(n1, n2-1, -1):
            string += f'{i}; '
    else:
        for i in range(n1, n2+1, 1):
            string += f'{i}; '         
    
    print(f'\nContagem: {string}\n')