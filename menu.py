
import os
from solucao import TabuleiroSolucao, tabuleiro_solucao
from jogador import TabuleiroJogador, tabuleiro_jogador
from vizinhanca import TabuleiroVizinhanca, tabuleiro_vizinhanca

def limpatela():
    os.system("clear"if os.name=="posix" else"cls")

print("\n")
print("|\tBem Vindo ao Campo Minado !!!\t|\n")
print("Para vencer o jogo, encontre todas as bombas presentes no Campo\n")
print("Durante o jogo, voce tera as opções do Menu\n") 
print("Bom Jogo !!!\n")
print("|\t  O que deseja fazer? \t\t|")

while True:
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")   
    print("|\t\t\t\t\t|\n")											
    print("|  1-Ver Tabuleiro     2-Marcar Simbolo |")  	
    print("|\t\t\t\t\t|\n")															    
    print("|  3-Desmarcar Simbolo           4-Sair |")
    print("|\t\t\t\t\t|\n")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")    
    print("\n")
    while True:
        op = int(input("Digite uma Opção: "))		
        print("\n")
        if op < 1 or op > 4:
            print("Opcão Inválida!")
            print("\a")
        else:
            break

    if op == 1:
        limpatela()
        print("Tabuleiro: \n")
        tabuleiro_jogador.MostrarTabuleiroJogador()	
        print("\nMatriz Vizinhanca: \n")
        tabuleiro_vizinhanca.MostrarTabuleiroVizinhanca()
        tabuleiro_solucao.MostrarQtdBombas()
        tabuleiro_jogador.MostrarQtdAcertos()

    elif op == 2:
        limpatela()
        while True:
            x, y = tabuleiro_jogador.Posicao()
            simbolo = tabuleiro_jogador.Simbolo()
            limpatela()
            if tabuleiro_jogador.tabuleiro_escolha[x-1][y-1] == '*' or tabuleiro_jogador.tabuleiro_escolha[x-1][y-1] == '-':
                print('\nPosição já escolhida, escolha outra posição\n')
            else:
                break
        tabuleiro_jogador.ContaAcertos(x, y, simbolo)
        tabuleiro_solucao.MostrarQtdBombas()
        tabuleiro_jogador.MostrarQtdAcertos()
        tabuleiro_jogador.VerificaTabuleiro(x, y, simbolo)
        tabuleiro_jogador.MostrarTabuleiroJogador()		
        print()
        tabuleiro_vizinhanca.MostrarTabuleiroVizinhanca()    
        print()
        if tabuleiro_solucao.bomba == tabuleiro_jogador.acertos:
            limpatela()      
            tabuleiro_jogador.MostrarTabuleiroJogador()		
            print()
            tabuleiro_solucao.MostrarTabuleiroSolucao()
            print("\nVOCÊ GANHOU, PARABÉNS!!!\n") 
            print("\nCaso queira jogar mais uma vez, abra novamente o aquivo!\n")
            print("Até a proxima!!!\n")
            break 

    elif op == 3:
        limpatela()
        x, y = tabuleiro_jogador.Posicao()
        if tabuleiro_solucao.tabuleiro[x-1][y-1] == tabuleiro_jogador.tabuleiro_escolha[x-1][y-1] and tabuleiro_solucao.tabuleiro[x-1][y-1] == '*':	
            tabuleiro_jogador.acertos +=  -1
        limpatela()
        tabuleiro_jogador.Desmarcar(x, y)
        tabuleiro_solucao.MostrarQtdBombas()
        tabuleiro_jogador.MostrarQtdAcertos()
        tabuleiro_jogador.MostrarTabuleiroJogador()		
        print()
        tabuleiro_vizinhanca.MostrarTabuleiroVizinhanca()

    else:
        limpatela()
        print("Solução do Campo Minado\n")
        tabuleiro_solucao.MostrarTabuleiroSolucao()
        print("\n")
        print("Programa Encerrado, até a proxima !!!\n\n")
        break