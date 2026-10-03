import random
import os
tabuleiro = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_tabuleiro():
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}\n{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}\n{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")

def verificar_vitoria(simbolo):
    linhas_vitoria = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]# Conjuntos de opções para vitória
    for a,b,c in linhas_vitoria:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == simbolo: # Se as linhas vitorias forem igual ao simbolo = vitoria
            return True
    return False

ganhar = False
vez = True
print("1- PLAYER vs PLAYER\n2- PLAYER vs BOT")
opcao = input("")
if opcao == "2":
    while ganhar == False:
        if vez != False:
            mostrar_tabuleiro()
            jogada_player = input("Digite um número para fazer a jogada: ")
            if jogada_player.isdigit(): # isdigit verifica se digitou um número correto

                posicao = int(jogada_player) - 1 # transforma oque o jogador digitou em inteiro e subtrai 1 pois começa em 0 o indice
                if 0 <= posicao <= 8 and tabuleiro[posicao] not in ["X", "O"]:
                    tabuleiro[posicao] = "X"

                    if verificar_vitoria("X"):
                        clear_console()

                        mostrar_tabuleiro()
                        print("Você ganhou.")
                        ganhar = True
                
                    elif all(casa in ["X", "O"] for casa in tabuleiro): # se todas casas forem preenchidas, empate.
                        clear_console()
                        verificar_vitoria()
                        print("Deu velha, empate.")
                        ganhar = True
                    else:
                        vez = False

                else:
                    clear_console()
                    print("Jogada inválida, escolha um número livre")
                    continue
            else:
                clear_console()
                print("Apenas número")
                continue

        elif vez == False:
            clear_console()
            posicao_livre = [int(x) - 1 for x in tabuleiro if x not in ["X", "O"]] ## verifica as posiçoes livres
            jogada_computador = random.choice(posicao_livre) # opção aleatoria do bot

            tabuleiro[jogada_computador] = "O"

            if verificar_vitoria("O"):
                mostrar_tabuleiro()
                print("Você perdeu.")
                ganhar = True
            elif all(casa in ["X", "O"] for casa in tabuleiro): # mesma verificação de empate
                verificar_vitoria()
                print("Deu velha, empate.")
                ganhar = True
            else:
                vez = True
elif opcao == "1":
    vez_jogador = True
    while ganhar == False:
            mostrar_tabuleiro()
            jogada_player = input("Digite um número para fazer a jogada: ")
            if vez_jogador == True:
                simbolo = "X"
            elif vez_jogador != True:
                simbolo = "O"
            if jogada_player.isdigit():

                posicao = int(jogada_player) - 1 # subtrai 1 pelo indice que começa por 0
                if 0 <= posicao <= 8 and tabuleiro[posicao] not in ["X", "O"]:
                    tabuleiro[posicao] = simbolo
                    if vez_jogador == True:
                        vez_jogador = False
                    elif vez_jogador == False:
                        vez_jogador = True
                

                    if verificar_vitoria(simbolo):
                        clear_console()

                        mostrar_tabuleiro()
                        
                        print(f"Jogador do simbolo '{simbolo}' ganhou.")
                        ganhar = True
                
                    elif all(casa in ["X", "O"] for casa in tabuleiro):
                        clear_console()

                        verificar_vitoria(simbolo)
                        mostrar_tabuleiro()
                        print("Deu velha, empate.")
                        ganhar = True

                else:
                    clear_console()
                    print("Jogada inválida, escolha um número livre")
                    continue
            else:
                clear_console()
                print("Apenas número")
                continue