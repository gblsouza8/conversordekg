# Programa que converte KG para as outras unidades de medidas de peso...

def conversor(valor):

    # Converte para as outras unidades de medidas
    grama = valor*1000
    miligrama = valor*1e+6
    stone = valor/6.35
    libra = valor*2.205
    onca = valor*35.274

    # Exibe o resultado
    print(valor, "kg (s) convertido para:\nGramas:", grama, "\nMiligramas:", miligrama, "\nStone:", stone, "\nLibras:", libra, "\nOnça:", onca);
    rodarNovamente()
    
    
    
 # Pede ao usuário para inserir o valor que deseja converter (em kg)
 
def __init__():
    valor =  int(input("Insira aqui o valor (em kg) que você deseja converter: "))
    conversor(valor)
    
def rodarNovamente():
        escolha = int(input("Deseja converter outro valor?\n1. Sim\n2. Não\n"))
        if (escolha == 1):
            print("Iniciando o programa novamente...")
            __init__()
        elif (escolha == 2):
            print("Tudo bem! finalizando o programa...")
            exit()
        else:
            print("Escolha inválida... por favor, escolha uma opção válida.")
            rodarNovamente()
            
            
__init__()