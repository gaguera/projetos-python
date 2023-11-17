import random

numero = random.randint(0,100)

ImparPar = input("escolha entre par ou impar:")

print(f"o numero sorteado foi {numero}")

# quando o f é usado, podemos colocar a variavel detro da string usando a chave({})

if (ImparPar == "par" and numero % 2 == 0) or (ImparPar == "impar" and  numero % 2 != 0):
    print("você acertou")
else:
    print("você errou") 
