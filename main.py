def esc(num):
    from random import randint

    comp = randint(1, 3)
    if num == 1:
        if comp == 1:
            print('Você escolheu pedra e o computador pedra. \033[034mEmpate\033[m.')
        elif comp == 2:
            print('Você escolheu pedra e o computador papel. \033[031mVocê perdeu\033[m.')
        else:
            print('Você escolheu pedra e o computador tesoura. \033[36mVocê ganhou!\033[m.')
    elif num == 2:
        if comp == 1:
            print('Você escolheu papel e o computador pedra. \033[36mVocê ganhou!\033[m.')
        elif comp == 2:
            print('Você escolheu papel e o computador papel. \033[034mEmpate\033[m.')
        else:
            print('Você escolheu papel  e o computador tesoura. \033[031mVocê perdeu\033[m.')
    elif num == 3:
        if comp == 1:
            print('Você escolheu tesoura e o computador pedra. \033[031mVocê perdeu\033[m.')
        elif comp == 2:
            print('Você escolheu tesoura e o computador papel. \033[36mVocê ganhou!\033[m.')
        else:
            print('Você escolheu tesoura e o computador tesoura. \033[034mEmpate\033[m.')


escolha = int(input("""Opção:
[1] Pedra
[2] Papel
[3] Tesoura: """))

print(esc(escolha))

