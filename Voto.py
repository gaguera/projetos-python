idade = int(input("Digite sua idade: "))
genero = input("Você é homem ou mulher? ")


if genero =="Homem" and idade >=18 and idade <71:
    alistamento = input("Você está com o alistamento em dia? ")
    if alistamento == "Não":
        print("Você não pode votar por conta do alistamento")
    if alistamento == "Sim":
        print("Você pode votar, pois está com o alistamento em dia")


if  idade >= 18 and idade < 71 :
    print("Você é obrigado a votar")
else:
    print("Você não é obrigado a votar")