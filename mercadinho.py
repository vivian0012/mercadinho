# ===================================== ATIVIDADE 2 ===========================
import os
import time

def limpatela():  # FUNÇÃO PARA LIMPAR A TELA
    os.system('cls' if os.name == 'nt' else 'clear')
    
# Função para formatar o texto do usuário:
def formatarTextto(texto):
    textFormatado = texto.upper()
    return textFormatado

# Função para retornar a introdução do código
def introducao():
    print("----- Bem-Vindo a Loja de Marmitas da Vivian Freitas ------------")
    print(20*"-"+ "Cardápio" + "-"* 37)
    print("-"*65)
    print("---|  Tamanho  |  Bife Acebolado(BA)  |  Filé de Frango(FF)  |---")
    print("---|     P     |       R$ 16.00       |       R$ 15.00       |---")
    print("---|     M     |       R$ 18.00       |       R$ 17.00       |---")
    print("---|     G     |       R$ 22.00       |       R$ 21.00       |---")
    print("-"*65)

# Função para dar opções ao sabor Bife Acebolado
def OpcoesBifeAcebolado(carrinho):
     print("")
     while True:
        tamanho = input("Qual tamanho você quer? [P, M ou G]: ")
        if(formatarTextto(tamanho) == "P"):
            valor = 16.00
            carrinho = carrinho + valor
            print(f"Você pediu um Bife Acebolado - P no valor de R${valor}")
            return carrinho
        elif(formatarTextto(tamanho) == "M"):
            valor = 18.00
            carrinho = carrinho + valor
            print(f"Você pediu um Bife Acebolado - M no valor de R${valor}")
            return carrinho
        elif(formatarTextto(tamanho) == "G"):
            valor = 32.00
            carrinho = carrinho + valor
            print(f"Você pediu um Bife Acebolado - G no valor de R${valor}")
            return carrinho
        else:
            limpatela()
            print("Tamanho inválido! Tente novamente!")
            print("VOLTANDO....")
            time.sleep(3)
            limpatela()
            introducao()
            print(f"R$:{carrinho}")

# Função para dar opções ao sabor Filé de Frango
def OpcoesFileDeFrango(carrinho):
     print("")
     while True:
        tamanho = input("Qual tamanho você quer? [P, M ou G]: ")
        if(formatarTextto(tamanho) == "P"):
            valor = 15.00
            carrinho = carrinho + valor
            print(f"Você pediu um Bife Acebolado - P no valor de R${valor}")
            return carrinho
        elif(formatarTextto(tamanho) == "M"):
            valor = 17.00
            carrinho = carrinho + valor
            print(f"Você pediu um Bife Acebolado - M no valor de R${valor}")
            return carrinho
        elif(formatarTextto(tamanho) == "G"):
            valor = 21.00
            carrinho = carrinho + valor
            print(f"Você pediu um Bife Acebolado - G no valor de R${valor}")
            return carrinho
        else:
            limpatela()
            print("Tamanho inválido! Tente novamente!")
            print("VOLTANDO....")
            time.sleep(3)
            limpatela()
            introducao()
            print(f"R$:{carrinho}")      
introducao()
carrinho = 0.0
print(f"R$:{carrinho}")

while True:
    sabor = input("Qual sabor você quer? (BA ou FF): ") 
    
    # Se o sabor for BA:
    if ( formatarTextto(sabor) == "BA"):
            carrinho = OpcoesBifeAcebolado(carrinho)
            resposta = input("Deseja mais alguma coisa? [S/N]: ")
            if(formatarTextto(resposta) == "S" or formatarTextto(resposta) == "SIM"):
                print("VOLTANDO....")
                time.sleep(1)
                limpatela()
                introducao()
                print(f"R$:{carrinho}")
                continue
            else:
                limpatela()
                print(f"Valor total a ser pago: R${carrinho}")
                break
    
    # Se o sabor for FF:
    elif( formatarTextto(sabor) == "FF"):
            carrinho = OpcoesFileDeFrango(carrinho)
            resposta = input("Deseja mais alguma coisa? [S/N]: ")
            if(formatarTextto(resposta) == "S" or formatarTextto(resposta) == "SIM"):
                print("VOLTANDO....")
                time.sleep(1)
                limpatela()
                introducao()
                print(f"R$:{carrinho}")
                continue
            else:
                limpatela()
                print(f"Valor total a ser pago: R${carrinho}")
                break
    
    # Caso não seja nenhum dos dois:
    else:
        print("Sabor Inválido. Tente novamente!")
        print("VOLTANDO....")
        time.sleep(1)
        limpatela()
        introducao()
        print(f"R$:{carrinho}")