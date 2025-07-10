from time import sleep

conta = 0
deposito = 0
saque = 0
cont_saque = 0
extrato_deposito = []
extrato_saque = []

print()
print(f"=============MENU NUBANK=============\n")

while True:
    sleep(3)
    print("[ 1 ] Desposito \n[ 2 ] Saque \n[ 3 ] Saldo \n[ 4 ] Extrato \n[ 5 ] Sair\n")
    opcao = int(input(">>>>Sua Resposta: "))
    print()

    if opcao == 1:
        deposito = float(input(">>>Quanto Você Quer Depositar?: "))
        print()

        if deposito <= 0:
            print("Valor Invalido!".center(25, "/"))
        else:
            print(f"R${deposito} Depositado Com Sucesso!".center(50, "+"))
            conta += deposito
            extrato_deposito.append(deposito)
        print()

    elif opcao == 2:
        if cont_saque == 3:
            print("Maxímo de Saque Diário atingido!".center(49, "/"))
        else:
            saque = float(input(">>>Qual Valor Você Quer Sacar?[Max=500]: "))
            print()
            
            if saque > conta:
                print("Saldo Insuficiente!".center(29, "/"))
             
            else:
                if saque > 500:
                    print("Falha! Valor Acima Do Limite de Saque".center(50, "/"))
                elif saque <= 0:
                    print("Valor Invalido!".center(25, "/"))
                else:
                    print(f"R${saque} Sacados com Sucesso!".center(50, "+"))
                    cont_saque += 1
                    extrato_saque.append(saque)
                    conta -= saque
                print()
            print()
        print()


    elif opcao == 3:
        print(f"<<<Seu saldo atual é de R${conta}...\n")
        
    elif opcao == 4:
        print(f"<<Depositos Feitos: {extrato_deposito} \n>>Saques Feitos: {extrato_saque}\n")

    elif opcao == 5:
        print(">>>>>>Finalizando...\n")
        sleep(3)
        break

    else:
        print("Opção Invalida! Por favor, Digite Uma Das Alternativas Abaixo\n".center(70, "/"))
    print()
