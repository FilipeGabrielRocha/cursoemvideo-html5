xi = []
fi = []
num1 = []
num2 = []
novaxi = []
n = somaxi = somaxifi = somaxi_media = 0
while True:
    print('''ESCOLHA OS MÉTODOS
    [ 1 ] MÉDIA AMOSTRAL (X)
    [ 2 ] VARIÂNCIA AMOSTRAL (s²)
    [ 3 ] DESVIO-PADRÃO AMOSTRAL (S)
    [ 0 ] PARAR O PROGRAMA''')
    escolha = int(input('Escolha o método: '))
    if escolha == 1:
        print('''O exercício tem:
    [ 1 ] Xi
    [ 2 ] Xi e Fi
    [ 3 ] Ponto Médio com fi
    [ 4 ] Ponto Médio sem fi''')
        pergunta1 = int(input('Escolha o modo: '))
        if pergunta1 == 1: #XI
            while True:
                xi.append(float(input('Digite o número: ')))
                n += 1
                pergunta = ' '
                while pergunta not in 'SN':
                    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
                if pergunta == 'N':
                    break
            for num in range(0, len(xi)):
                somaxi += xi[num]
            x = somaxi / n
            print('==' * 30)
            print(f'A Média Amostral é {x:.3f}')
            print('==' * 30)
        elif pergunta1 == 2: #XI E FI
            while True:
                xi.append(float(input('Digite o xi: ')))
                fi.append(float(input('Digite o fi: ')))
                pergunta = ' '
                while pergunta not in 'SN':
                    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
                if pergunta == 'N':
                    break
            for pos in range(0, len(fi)):
                n += fi[pos]
            for pos in range(0, len(xi)):
                mult = xi[pos] * fi[pos]
                somaxifi += mult
            x = somaxifi / n
            print('==' * 30)
            print(f'A Média Amostral é {x:.3f}')
            print('==' * 30)
        elif pergunta1 == 3: #PONTO MÉDIO COM FI
            while True:
                num1.append(float(input('1° Número: ')))
                num2.append(float(input('2° Número: ')))
                fi.append(float(input('Digite o fi: ')))
                pergunta = ' '
                while pergunta not in 'SN':
                    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
                if pergunta == 'N':
                    break
            for pos in range(0, len(fi)):
                n += fi[pos]
            for pos in range(0, len(num1)):
                div = (num1[pos] + num2[pos]) / 2
                xi.append(div)
            for pos in range(0, len(fi)):
                mult = xi[pos] * fi[pos]
                somaxifi += mult
            x = somaxifi / n
            print('==' * 30)
            print(f'A Média Amostral é {x:.3f}')
            print('==' * 30)
        else:
            while True:
                num1.append(float(input('1° Número: ')))
                num2.append(float(input('2° Número: ')))
                pergunta = ' '
                while pergunta not in 'SN':
                    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
                if pergunta == 'N':
                    break
            for pos in range(0, len(num1)):
                div = (num1[pos] + num2[pos]) / 2
                xi.append(div)
            for pos in range(0, len(xi)):
                somaxi += xi[pos]
            n = float(input('Qual o valor de n: '))
            x = somaxi / n
            print('==' * 30)
            print(f'A Média Amostral é X= {x:.3f}')
            print('==' * 30)
    elif escolha == 2:
        print('''ESCOLHA OS MÉTODOS:
        [ 1 ] COM Fi
        [ 2 ] SEM Fi''')
        pergunta2 = int(input('Escolha o modo: '))
        if pergunta2 == 1:
            for pos in range(0, len(xi)):
                xi_media = ((xi[pos] - x) ** 2) * fi[pos]
                somaxi_media += xi_media
            s_2 = somaxi_media / (n - 1)
            print('==' * 30)
            print(f'A Variância Amostral é S²= {s_2:.3f}')
            print('==' * 30)
        else:
            for pos in range(0, len(xi)):
                xi_media = ((xi[pos] - x) ** 2)
                somaxi_media += xi_media
            s_2 = somaxi_media / (n - 1)
            print('==' * 30)
            print(f'A Variância Amostral é S²= {s_2:.3f}')
            print('==' * 30)
    elif escolha == 3:
        print('''ESCOLHA OS MÉTODOS:
        [ 1 ] COM Fi
        [ 2 ] SEM Fi''')
        pergunta3 = int(input('Escolha o modo: '))
        if pergunta3 == 1:
            s = s_2 ** (1/2)
            print('==' * 30)
            print(f'A Desvio-Padrão Amostral é S= {s:.3f}')
            print('==' * 30)
        elif pergunta3 == 2:
            s = s_2 ** (1 / 2)
            print('==' * 30)
            print(f'A Desvio-Padrão Amostral é S= {s:.3f}')
            print('==' * 30)
    if escolha == 0:
        break
