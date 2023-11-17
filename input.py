from datetime import date
anoAtual = date.today().year

nome = input("nome: ")
ano_nascimento = int (input("ano de nascimento: "))

print("olá meu nome é", nome, " Eu tenho",ano_nascimento, "anos")
print(ano_nascimento)
print("olá meu nome é", nome, )
print("olá meu nome é", nome, ". eu tenho" , anoAtual - ano_nascimento, "anos")
print("ano que vem eu faço" , anoAtual - ano_nascimento + 1, "anos")
print("há 10 anos atras eu tinha" , anoAtual - ano_nascimento - 10, "anos")
print("eu nasci em ",ano_nascimento)