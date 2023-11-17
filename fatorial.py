
numero = int(input("digite um numero e verifique se ele é fatorial:"))
valor = 1

while numero > 1:
    valor = valor * numero
    numero = numero - 1

print(" fatorial é igual a",valor)