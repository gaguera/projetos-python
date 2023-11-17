import random 

escolha = random.choice(["cara", "coroa"])

numero1 = int(input("escolha um numero de 0 a 10:"))
numero2 = int(input("escolha um numero de 0 a 10:"))

if escolha == "cara":
    if numero1 < numero2:
        print(numero1, "foi o vencedor")

    if numero2 < numero1:
        print(numero2, "foi o vencedor") 
    
    if numero1 == numero2:
        print("empate")

if escolha == "coroa":
    if numero1 > numero2:
        print(numero1, "foi o vencedor")

    if numero2 > numero1:
        print(numero2, "foi o vencedor")

    if numero2 == numero1:
        print("empate")    

print(escolha, "foi o escolhido")