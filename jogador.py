
import sys
from solucao import TabuleiroSolucao, tabuleiro_solucao

class TabuleiroJogador(TabuleiroSolucao):
    def __init__(self) -> None:
        self.tabuleiro_escolha = []
        self.acertos = 0
        for i in range(tabuleiro_solucao.nlin):
            self.tabuleiro_escolha.append([])
            for j in range(tabuleiro_solucao.ncol):
                self.tabuleiro_escolha[i].append('N')

    def MostrarTabuleiroJogador(self):
        for i in range(tabuleiro_solucao.nlin):
            for j in range(tabuleiro_solucao.ncol):
                print(f'{self.tabuleiro_escolha[i][j]} ', end='')
            print()

    def ContaAcertos(self, x, y, simbolo):
        if tabuleiro_solucao.tabuleiro[x-1][y-1] == simbolo and simbolo == '*' and self.tabuleiro_escolha[x-1][y-1] != '*':
            self.acertos += 1

    def MostrarQtdAcertos(self):
        print(f"A quantidade de acertos é: {self.acertos}\n")

    def Posicao(self):
        while True:
            pos_x = int(input(f'Digite a linha onde queira marcar o simbolo (1 - {tabuleiro_solucao.nlin}): '))
            if 1 <= pos_x <= tabuleiro_solucao.nlin:
                break
            else:
                print(f'Índice inválido. Intervalo válido: (1 - {tabuleiro_solucao.nlin})')
        
        while True:
            pos_y = int(input(f'Digite a coluna onde queira marcar o simbolo (1 - {tabuleiro_solucao.ncol}): '))
            if 1 <= pos_y <= tabuleiro_solucao.ncol:
                break
            else:
                print(f'Índice inválido. Intervalo válido: (1 - {tabuleiro_solucao.ncol})')   

        return pos_x, pos_y     
    
    def Simbolo(self):
        while True:
            simbol = input('Digite o Símbolo ( ''*'' -> bomba  || ''-'' -> livre): ')
            if simbol == '*' or simbol == '-':
                break
            else:  
                print('Símbolo inválido, tente novamente')

        return simbol        

    def VerificaTabuleiro(self, x, y, simbolo):
        if tabuleiro_solucao.tabuleiro[x-1][y-1] == simbolo or simbolo == '*':
            self.tabuleiro_escolha[x-1][y-1] = simbolo
        
        if simbolo == '-':
            if tabuleiro_solucao.tabuleiro[x-1][y-1] == '*':
                print("VOCÊ PERDEU!!!\n")
                print("Solucao do Campo Minado\n")
                tabuleiro_solucao.MostrarTabuleiroSolucao()
                print("\nCaso queira jogar mais uma vez, abra novamente o aquivo !\n")
                print("Ate a proxima !!!\n")
                sys.exit()

    def Desmarcar(self, x, y):
        self.tabuleiro_escolha[x-1][y-1] = 'N'

tabuleiro_jogador = TabuleiroJogador()
