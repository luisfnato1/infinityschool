#Prova 02 - Escreva um programa em python que pergunte ao usuário a velocidade de um carro. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado e o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.

velocidade = int(input("Qual a velocidade sua na Av. Paralela ontem de noite?"))
velocidade_adicional = (velocidade - 80)

if velocidade > 80:
    print(f'Você ultrapassou o limite de velocidade em {velocidade_adicional}')
    print(f'Assim, você deverá pagar {velocidade_adicional*20} de multa ao DETRAN')