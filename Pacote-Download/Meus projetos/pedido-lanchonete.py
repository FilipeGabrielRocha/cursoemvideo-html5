vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
limpar = '\033[m'
a = '='
e = " Bem-vindo ao Rocha's Burguer "
e2 = ' '
fim = "Volte Sempre ao Rocha's Burguer!!"
soma1 = soma2 = soma3 = contlanche = contbebida = contbatata = escolha3 = 0
contlanche1 = contlanche2 = contlanche3 = contlanche4 = contlanche5 = contlanche6 = 0
contbebida1 = contbebida2 = contbebida3 = contbebida4 = 0
contbatata1 = contbatata2 = contbatata3 = contbatata4 = 0
plur1 = plur2 = plur3 = plur4 = plur5 = plur6 = plur7 = plur8 = plur9 = plur10 = plur11 = plur12 = plur13 = plur14 = plur15 = ' '
plur16 = plur17 = plur18 = plur19 = plur20 = plur21 = plur22 = plur23 = plur24 = plur25 = plur26 = plur27 = ' '
print(f"{amarelo}={limpar}" * 60)
print(f'{amarelo}{e:^60}{limpar}')
print(f'{amarelo}={limpar}' * 60)
while e2 not in 'SN':
    e2 = str(input('Posso anotar seu pedido? [S/N] ')).strip().upper()[0]
    if e2 == 'N':
        break
    p1 = float(16.50)
    p2 = float(24.50)
    p3 = float(20.50)
    p4 = float(18.50)
    p5 = float(32.50)
    p6 = float(00.00)
    print(f'''\nOpções de hamburgueres:
    1- X-Salada {a:>10} {verde}R${p1:02.2f}{limpar}
    2- X-EggBacon {a:>8} {verde}R${p2:02.2f}{limpar}
    3- X-Bacon {a:>11} {verde}R${p3:02.2f}{limpar}
    4- X-Egg {a:>13} {verde}R${p4:02.2f}{limpar}
    5- X-Tudo {a:>12} {verde}R${p5:02.2f}{limpar}
    6- Sem Lanche {a:>8} {verde}R${p6:02.2f}{limpar}''')
    while True:
        escolha1 = int(input('Digite o número para escolher: '))
        pergunta1 = ' '
        while pergunta1 not in 'SN':
            pergunta1 = str(input('Quer fazer outro pedido? [S/N] ')).strip().upper()[0]
        if escolha1 == 1:
            valor = p1
            contlanche1 += 1
        if escolha1 == 2:
            valor = p2
            contlanche2 += 1
        if escolha1 == 3:
            valor = p3
            contlanche3 += 1
        if escolha1 == 4:
            valor = p4
            contlanche4 += 1
        if escolha1 == 5:
            valor = p5
            contlanche5 += 1
        if escolha1 == 6:
            valor = p6
            contlanche6 = 0
        soma1 += valor
        contlanche = contlanche1 + contlanche2 + contlanche3 + contlanche4 + contlanche5 + contlanche6
        if pergunta1 == 'N':
            break
    b1 = float(7.50)
    b2 = float(7.50)
    b3 = float(5.00)
    b4 = float(0.00)
    print(f'''\nOpções de bebidas:
    1- Coca-Cola {a:>10} {verde}R${b1:.2f}{limpar}
    2- Guaraná {a:>12} {verde}R${b2:.2f}{limpar}
    3- Suco {a:>15} {verde}R${b3:.2f}{limpar}
    4- Sem Bebida {a:>9} {verde}R${b4:.2f}{limpar}''')
    while True:
        escolha2 = int(input('Digite o número para escolher: '))
        pergunta2 = ' '
        while pergunta2 not in 'SN':
            pergunta2 = str(input('Quer fazer ou pedido? [S/N] ')).strip().upper()[0]
        if escolha2 == 1:
            valor1 = b1
            contbebida1 += 1
        if escolha2 == 2:
            valor1 = b2
            contbebida2 += 1
        if escolha2 == 3:
            valor1 = b3
            contbebida3 += 1
        if escolha2 == 4:
            valor1 = b4
            contbebida4 = 0
        soma2 += valor1
        contbebida = contbebida1 + contbebida2 + contbebida3 + contbebida4
        if pergunta2 == 'N':
            break
    ac1 = float(3.0)
    ac2 = float(2.0)
    ac3 = float(1.0)
    ac4 = float(0.00)
    print(f'''\nOpções do Tamanho da Batata-Frita:
    1- Pequena {a:>12} {verde}R${ac3:.2f}{limpar}
    2- Média {a:>14} {verde}R${ac2:.2f}{limpar}
    3- Grande {a:>13} {verde}R${ac1:.2f}{limpar}
    4- Sem Batata-Frita {a:>3} {verde}R${ac4:.2f}{limpar}''')
    while True:
        escolha3 = int(input('Digite o número para escolher: '))
        pergunta3 = ' '
        while pergunta3 not in 'SN':
            pergunta3 = str(input('Quer fazer outro pedido? [S/N] ')).strip().upper()[0]
        if escolha3 == 1:
            valor2 = ac3
            contbatata1 += 1
        if escolha3 == 2:
            valor2 = ac2
            contbatata2 += 1
        if escolha3 == 3:
            valor2 = ac1
            contbatata3 += 1
        if escolha3 == 4:
            valor2 = ac4
            contbatata4 = 0
        soma3 += valor2
        contbatata = contbatata1 + contbatata2 + contbatata3 + contbatata4
        if pergunta3 == 'N':
            break
    card1 = 'Débito'
    card2 = 'Crédito'
    print(f'''\nOpções de Pagamento:
    1- {amarelo}Débito{limpar}.
    2- {amarelo}Crédito{limpar}.''')
    escolha3 = int(input('Digite o número para escolher: '))
    conta1 = soma1 + soma2 + soma3
    conta2 = contlanche + contbebida + contbatata
    print('=' * 36)
    if conta2 > 1:
        plur1 = 'foram'
        plur2 = 'feitos'
        plur3 = 'pedidos'
    else:
        plur1 = 'foi'
        plur2 = 'feito'
        plur3 = 'pedido'
    print(f'Ao todo {plur1} {plur2} {conta2} {plur3}.')
    if contlanche >= 1:
        print('Lanche:')
        if contlanche1 > 1:
            plur4 = 'Foram'
            plur5 = 'pedidos'
        else:
            plur4 = 'Foi'
            plur5 = 'pedido'
        if contlanche2 > 1:
            plur6 = 'Foram'
            plur7 = 'pedidos'
        else:
            plur6 = 'Foi'
            plur7 = 'pedido'
        if contlanche3 > 1:
            plur8 = 'Foram'
            plur9 = 'pedidos'
        else:
            plur8 = 'Foi'
            plur9 = 'pedido'
        if contlanche4 > 1:
            plur10 = 'Foram'
            plur11 = 'pedidos'
        else:
            plur10 = 'Foi'
            plur11 = 'pedido'
        if contlanche5 > 1:
            plur12 = 'Foram'
            plur13 = 'pedidos'
        else:
            plur12 = 'Foi'
            plur13 = 'pedido'
        if contlanche1 >= 1:
            print(f'{plur4} {contlanche1} {plur5} de X-salada.')
        if contlanche2 >= 1:
            print(f'{plur6} {contlanche2} {plur7} de X-EggBacon.')
        if contlanche3 >= 1:
            print(f'{plur8} {contlanche3} {plur9} de X-Bacon.')
        if contlanche4 >= 1:
            print(f'{plur10} {contlanche4} {plur11} de X-Egg.')
        if contlanche5 >= 1:
            print(f'{plur12} {contlanche5} {plur13} de X-Tudo.')
    else:
        print('Não foi feito pedido de Lanche.')
    if contbebida >= 1:
        print('Bebida:')
        if contbebida1 > 1:
            plur14 = 'Foram'
            plur15 = 'pedidos'
        else:
            plur14 = 'Foi'
            plur15 = 'pedido'
        if contbebida2 > 1:
            plur16 = 'Foram'
            plur17 = 'pedidos'
        else:
            plur16 = 'Foi'
            plur17 = 'pedido'
        if contbebida3 > 1:
            plur18 = 'Foram'
            plur19 = 'pedidos'
        else:
            plur18 = 'Foi'
            plur19 = 'pedido'
        if contbebida4 > 1:
            plur20 = 'Foram'
            plur21 = 'pedidos'
        else:
            plur20 = 'Foi'
            plur21 = 'pedido'
        if contbebida1 >= 1:
            print(f'{plur14} {contbebida1} {plur15} de Coca-Cola.')
        if contbebida2 >= 1:
            print(f'{plur16} {contbebida2} {plur17} de Guaraná.')
        if contbebida3 >= 1:
            print(f'{plur18} {contbebida3} {plur19} de Suco.')
        if contbebida4 >= 1:
            print(f'{plur20} {contbebida4} {plur21} Sem bebida.')
    else:
        print('Não foi feito pedido de Bebida.')
    if contbatata >= 1:
        print('Batata-Frita:')
        if contbatata1 > 1:
            plur22 = 'Foram'
            plur23 = 'pedidos'
        else:
            plur22 = 'Foi'
            plur23 = 'pedido'
        if contbatata2 > 1:
            plur24 = 'Foram'
            plur25 = 'pedidos'
        else:
            plur24 = 'Foi'
            plur25 = 'pedido'
        if contbatata3 > 1:
            plur26 = 'Foram'
            plur27 = 'pedidos'
        else:
            plur26 = 'Foi'
            plur27 = 'pedido'
        if contbatata1 >= 1:
            print(f'{plur22} {contbatata1} {plur23} de Batata-Frita Pequena.')
        if contbatata2 >= 1:
            print(f'{plur24} {contbatata2} {plur25} de Batata-Frita Média.')
        if contbatata3 >= 1:
            print(f'{plur26} {contbatata3} {plur27} de Batata-Frita Grande.')
    else:
        print('Não foi feito pedido de Batata-Frita.')
        print('=' * 36)
    if escolha3 == 1:
        print('=' * 36)
        print(f'Forma de pagamento: {amarelo}Débito{limpar}.')
    else:
        print('=' * 36)
        print(f'Forma de pagamento: {amarelo}Crédito{limpar}.')
    print(f'O valor do seu pedido ficou {verde}R${conta1:.2f}{limpar}')
    print('=' * 36)
print(f'{amarelo}={limpar}' * 36)
print(f'{amarelo}{fim:^36}{limpar}')
print(f'{amarelo}={limpar}' * 36)
