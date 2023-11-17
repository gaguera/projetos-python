peso = float(input("digite o seu peso:"))
altura = float(input("digite sua altura:"))


imc = peso / (altura**2)

print(" O seu imc é", " {:.2f}".format(imc))

sexo = input(" digite o seu sexo (H/M): ").upper()

#upper() serve para deixar tudo o que  usuario digite em maiusculo


if sexo == "H":
    if imc <= 20:
        print("Abaixo do peso")
    elif 20 < imc <= 24.9:
        print("peso normal")
    elif 25 < imc <= 29.9:    
        print("obesidade leve")
    elif 30 < imc <= 39.9:
        print("obesidade moderada")
    else:
        print("obesidade mórbida")


        
elif sexo == "M":
    if imc <= 19:
        print("Abaixo do peso")
    elif 19< imc <= 23.9:
        print("peso normal")
    elif 24 < imc <= 28.9:    
        print("obesidade leve")
    elif 29 < imc <= 38.9:
        print("obesidade moderada")
    else:
        print("obesidade mórbida")
        