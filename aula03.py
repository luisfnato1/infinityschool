# Exercício de revisão 1 - Pedir 3 valores ao usuário e retornar-los em valores decrescente

# idade_pai = input("Digite aqui a idade do seu pai")
# idade_mae = input("Digite aqui a idade da sua mãe")
# idade_irma = input("Digite aqui a idade da sua irmã")

# if idade_pai > idade_mae and idade_pai>idade_irma:
#     if idade_mae > idade_irma:
#             print (idade_pai, idade_mae, idade_irma)
# if idade_pai > idade_mae and idade_pai>idade_irma:
#     if idade_irma> idade_mae:
#             print (idade_pai, idade_irma, idade_mae)
# elif idade_mae>idade_irma and idade_mae>idade_pai:
#       if idade_pai>idade_irma:
#             print(idade_mae, idade_pai, idade_irma)
# elif idade_mae>idade_irma and idade_mae>idade_pai:
#       if idade_irma>idade_pai:
#             print(idade_mae, idade_irma, idade_pai)
# elif idade_irma>idade_pai and idade_irma>idade_mae:
#       if idade_mae>idade_pai:
#             print(idade_irma,idade_mae,idade_pai)
# elif idade_irma>idade_pai and idade_irma>idade_mae:
#       if idade_pai>idade_mae:
#             print(idade_irma,idade_pai,idade_mae)
# else:
#       print ("As idades são iguais")

# contador = 10
# while (contador > 0):
#     print(contador)
#     contador = contador - 1
# print ("Fim da contagem regressiva")

# Exercício Aula 1 - Crie um loop while que imprima os números pares de 2 a 10.

# contador = 1
# while (contador < 11):
#     if contador % 2 == 0:
#         print (contador)
#     contador = contador + 1
# print ("fim do números pares")

# Exercício aula 2 - Implemente um jogo em que o usuário tenta adivinhar um número aleatório entre 1 e 20, dando dicas se a tentativa é muito alta ou muito baixa.

# idade_irma = 19
# tentativa = 0 

# while tentativa != idade_irma:
#     tentativa = int(input("Tente adivinhar aqui a idade da minha irmã"))
#     if tentativa > idade_irma:
#         print ("A idade da minha irmã é menor")
#     if tentativa < idade_irma:
#         print ("A idade da minha irmã é maior")
# print (f'Perfeito! A idade da minha irmã é {idade_irma} anos')

# numero = 18
# tentativa = 0
# while tentativa != numero:
#     tentativa = int(input("Tente adivinhar aqui um número entre 0 a 20"))
#     if tentativa / numero > 0.5 and tentativa < 20 and tentativa != numero:
#         print ("Você está perto")
#     elif tentativa / numero <= 0.5 and tentativa< 20:
#         print ("Você ainda está longe")
#     elif tentativa >= 20:
#         print ("O número deve estar entre 0 e 20")
#     elif tentativa == numero:
#         break
# print ("Parabéns você acertou")

# Atividade prática - Crie um programa que solicite ao usuário adivinhar um número entre 1 e 100, dando dicas se a tentativa é muito alta, muito baixa ou correta. Adicione um limite de tentativas.

# numero = 80 
# tentativas_max = 4
# tentativa = 0 

# while tentativa != numero and tentativas_max > 0:
#     tentativa = int(input("Tente adivinhar aqui um número entre 0 a 100"))
#     tentativas_max -= 1
#     if tentativa > numero and tentativas_max != 0:
#         print (f'O número é menor e você ainda tem {tentativas_max} tentativas')
#     elif tentativa < numero and tentativas_max != 0:
#         print (f'O número é maior e você ainda tem {tentativas_max} tentativas')
# if tentativa == numero:
#     print ("Parabéns você acertou")
# else: 
#     print (f'Suas tentativas acabaram. O número era {numero}')

# Atividade prática - Crie um programa que solicite números inteiros. O programa deve continuar solicitando os números até que a soma dos números pares seja maior que 50. Ao ultrapassar esse limite, o programa deve exibir a toma total e encerrar

soma_par = 0
limite = 50 

while soma_par < limite:
    numero = int(input("Digite um número:"))
    if numero % 2 == 0:
        soma_par += numero
if soma_par == limite:
    print ("A soma dos números pares é 50")
else:
    print (f'A soma ultrapassou o limite de {limite} na soma de números pares. Soma final: {soma_par}')