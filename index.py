idade_minima = 18

print("Bem vindo ao sistema")

nome  = input("Por favor informe a seu nome: ")

idade_usuario = int(input("Por favor informe a sua idade: "))

if idade_usuario >= idade_minima:
    print("Seja bem vindo(a)", nome)
else:
    print(nome, "você ainda não tem idade suficiente para entrar no sistema")