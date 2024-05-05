soma = 0 
quantidade = 0

while True:
    numero = int(input("Digite um número inteiro"))
    if numero == 0:
        break
    soma = soma + numero
    quantidade += 1
print (f'A soma dos números é {soma}')
print (f'A quantidade de números inteiros digitados é {quantidade}')
print (f'A média dos números digitados é {soma/quantidade}')