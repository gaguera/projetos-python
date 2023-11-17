nome = input("digite o seu nome: ")

nota1 = float(input("digite sua nota do primeiro bimestre:"))
nota2 = float(input("digite sua nota do segundo bimestre:"))
nota3 = float(input("digite sua nota do terceiro bimestre:"))
nota4 = float(input("digite sua nota do quarto bimestre:"))

media = (nota1 + nota2 + nota3 + nota4)/4

print(nome, "sua media final é:", media)

if media >= 7:
    print("aprovado")
    
else: 
    print("reprovado")


# if - se (condição necessariamente verdadeira)
# else - se não (negação do if)
# else não tem condição