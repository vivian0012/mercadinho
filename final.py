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

# Função para retornar o valor do carrinho para o cliente, nome do alimento e seus valores de acordo com o tamanho.
def CarrinhoDeCompra(carrinho, nome, p, m, g):
     print("")
     while True:
        tamanho = input("Qual tamanho você quer? [P, M ou G]: ")
        if(formatarTextto(tamanho) == "P"):
            # Fazendo a incrementação do valor de acordo do tamanho para o carrinho.
            carrinho = carrinho + p
            print(f"Você pediu um {nome} - P no valor de R${p}")
            return carrinho
        elif(formatarTextto(tamanho) == "M"):
            carrinho = carrinho + m
            print(f"Você pediu um {nome} - M no valor de R${m}")
            return carrinho
        elif(formatarTextto(tamanho) == "G"):
            carrinho = carrinho + g
            print(f"Você pediu um {nome} - G no valor de R${g}")
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
            carrinho = CarrinhoDeCompra(carrinho, "Bife Acebolado", 16.00, 18.00, 22.00)
            print("")
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
            carrinho = CarrinhoDeCompra(carrinho, "Filé de Frago", 15.00, 17.00, 21.00)
            print("")
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