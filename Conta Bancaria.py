conta = 0
deposito = 0
saque = 0
cont_saque = 0
extrato_deposito = []
extrato_saque = []
while True:
    print("[ 1 ] Desposito \n[ 2 ] Saque \n[ 3 ] Extrato \n[ 4 ] Sair")
    opcao = int(input(">>>>Sua Resposta: "))
    if opcao == 1:
        deposito = float(input("Quanto Você Quer Depositar?: "))
        if deposito <= 0:
            print("Valor Invalido!")
        else:
            conta = conta + deposito
            extrato_deposito.append(deposito)
    elif opcao == 2:
        if cont_saque == 3:
            print("Maxímo de Saque Diários atingidos!")
        else:
            saque = float(input("Qual Valor Você Quer Sacar?[Max=500]: "))
            if saque > 500:
                print("Falha! Valor Acima Do Limite de Saque.")
            elif saque >= 0:
                print("Valor Invalido!")
            else:
                print(f"R${saque} Sacados com Sucesso!")
                cont_saque += 1
                extrato_saque.append(saque)
                conta = conta - saque

