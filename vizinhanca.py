
from solucao import TabuleiroSolucao, tabuleiro_solucao

class TabuleiroVizinhanca(TabuleiroSolucao):
    def __init__(self) -> None:
        self.vizinhanca = []
        self.ConstruirVizinhanca()
        
    def ConstruirVizinhanca(self):    
        for i in range(tabuleiro_solucao.nlin):
            self.vizinhanca.append([])
            for j in range(tabuleiro_solucao.ncol):
                self.vizinhanca[i].append(0)

        for i in range(tabuleiro_solucao.nlin):
            for j in range(tabuleiro_solucao.ncol):
                if j == 0:
                    inic = 0
                else:
                    inic = j-1
                    if tabuleiro_solucao.tabuleiro[i][inic] == '*':
                        self.vizinhanca[i][j] += 1

                if j == tabuleiro_solucao.ncol - 1:
                    fim = j
                else:
                    fim = j+1
                    if tabuleiro_solucao.tabuleiro[i][fim] == '*':
                        self.vizinhanca[i][j] += 1

                if i > 0:
                    for k in range(inic, fim+1):
                        if tabuleiro_solucao.tabuleiro[i-1][k] == '*' :	
                            self.vizinhanca[i][j] += 1

                if i < (tabuleiro_solucao.nlin - 1):
                    for k in range(inic, fim+1):
                        if tabuleiro_solucao.tabuleiro[i+1][k] == '*' :	
                            self.vizinhanca[i][j] += 1        

    def MostrarTabuleiroVizinhanca(self):
        for i in range(tabuleiro_solucao.nlin):
            for j in range(tabuleiro_solucao.ncol):
                print(f'{self.vizinhanca[i][j]} ', end='')
            print()

tabuleiro_vizinhanca = TabuleiroVizinhanca()
