import random 
jogo = random.choice(["pedra", "papel", "tesoura"])
escolha = input("escolha entre pedra papel ou tesoura:")

if escolha == "pedra":
    print("sua escolha foi", escolha)
    print("a maquina escolheu", jogo)

    if jogo == "pedra":
        print( "empate") 
    if jogo == "papel":
        print("você perdeu!")
    if jogo == "tesoura":
        print("você venceu!")

if escolha == "papel":
    print("sua escolha foi", escolha)
    print("a maquina escolheu", jogo)

    if jogo == "papel":
        print( "empate") 
    if jogo == "pedra":
        print("você venceu!")
    if jogo == "tesoura":
        print("você perdeu!")

if escolha == "tesoura":
    print("sua escolha foi", escolha)
    print("a maquina escolheu", jogo)

    if jogo == "tesoura":
        print( "empate") 
    if jogo == "pedra":
        print("você perdeu!")
    if jogo == "papel":
        print("você venceu!")