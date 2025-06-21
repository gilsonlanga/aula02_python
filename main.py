# Exemplo que causa TypeError

# nome = "Gilson"

# try:
#     resultado = len(nome)
#     print(resultado)
# except TypeError as e:
#     print(e) # Imprime a mensagem de erro

# else:
#     print("tudo ocorreu bem")
# finally:
#     print("O importante é participar")

# numero = int(input("Insira um número: "))
# if isinstance(numero, int):
#     print("A variável é um inteiro")
# else:
#     print("A variável não é um inteiro")

idade = 17
if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Exatamente 18 anos")
else:
    print("Maior de idade")