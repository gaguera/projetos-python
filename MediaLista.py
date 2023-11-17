notas = []

while len(notas)<4:

    entrada = input("digite suas notas:")

    digitadas = entrada.split()

    if len(notas) + len(digitadas) <= 4:
        i = 0
        while i < len(digitadas):
            notas.append(float(digitadas[i]))
            i += 1

print("notas digitadas", notas)

media = sum(notas) / len(notas)
print("media das notas:", media)



