
class TabuleiroSolucao:
    def __init__(self, nome_arquivo) -> None:
        self.tabuleiro = []
        self.bomba = 0
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read().split('\n')
            dimensao = conteudo[0].split()
            self.nlin = int(dimensao[0])
            self.ncol = int(dimensao[1])
            for _ in conteudo[1:]:
                self.tabuleiro.append(list(_))
        self.ContaBomba()

    def ContaBomba(self):
        for linha in self.tabuleiro:
            self.bomba += linha.count('*')

    def MostrarTabuleiroSolucao(self):
        for i in range(self.nlin):
            for j in range(self.ncol):
                print(f'{self.tabuleiro[i][j]} ', end='')
            print()

    def MostrarQtdBombas(self):
        print(f"\nA quantidade de bombas é: {self.bomba}\n")

tabuleiro_solucao = TabuleiroSolucao('jogo.txt')
