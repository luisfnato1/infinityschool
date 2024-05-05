senha = "senha123"
tentativas_totais = 3

for tentativa in range (tentativas_totais):
    tentativa = (input("Digite sua senha:"))
    tentativas_totais -= 1
    if tentativa == senha:
        print ("Seja bem-vindo")
        break
    if tentativas_totais == 0:
        print ("Você esgotou suas tentativas. Celular bloqueado por 5 minutos")

    else: 
        print (f"Senha incorreta. Você tem mais {tentativas_totais} tentativas restantes")


