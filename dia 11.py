#projeto do jogo 21
import random
cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #listas das cartas do baralho
usuario = [] #cartas do usuario
temp = [] #cartas temporarias
pc = [] #cartas do oponente
while True:
    pergunta = str(input('Quer jogar 21?[S/N]:  ')).strip().upper()
    usuario.clear()
    pc.clear()
    if pergunta == 'N':
        break
    for v in range(0, 2):
        temp = random.choice(cartas)
        usuario.append(temp)
        del temp
    for v in range(0, 2):
        temp = random.choice(cartas)
        pc.append(temp)
        del temp
    print(f'Cartas do adversario {pc[0]}')
    print(f'Suas cartas {usuario}')
    while True:
        if sum(usuario) < 21:
            adic = str(input(f'A soma das suas cartas é {sum(usuario)}\nDigite X para pegar mais uma carta ou Y para passar a vez: ')).strip().upper()
            if adic == 'X':
                temp = random.choice(cartas)
                usuario.append(temp)
                print(f'Cartas do adversario {pc[0]}')
                print(f'Suas cartas {usuario}')
            elif adic == 'Y':
                if sum(pc) < 17:
                    temp = random.choice(cartas)
                    pc.append(temp)
                elif sum(pc) == 21:
                    print(f'A soma das cartas do seu adversário é {sum(pc)}, você perdeu!')
                    break
                elif sum(pc) > 21:
                    print(f'A soma das cartas do seu adversario é {sum(pc)}, ultrapassando 21, você ganhou!')
                    break
                elif sum(usuario) < sum(pc) and sum(pc) < 21:
                    print(f'A soma das suas cartas é {sum(usuario)} e do seu adversario é {sum(pc)} você perdeu.')
                    break
                elif sum(usuario) > sum(pc) and sum(usuario) < 21:
                    print(f'A soma das suas cartas é {sum(usuario)} e do seu adversario é {sum(pc)} você ganhou.')
                    break
                elif sum(usuario) == sum(pc):
                    print(f'A soma das suas cartas é {sum(usuario)} e do seu adversario é {sum(pc)} resultando em um empate!')
                    break
        elif sum(usuario) == 21:
            print(f'A soma das suas cartas é {sum(usuario)}, você venceu!')
            break
        else:
            print(f'A soma das suas cartas é {sum(usuario)}, você perdeu!')
            break
