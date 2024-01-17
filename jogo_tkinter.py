
from tkinter import *
from tkinter import messagebox
import random
import sys

class Tabuleiro:
    def __init__(self, nlin, ncol, bombas) -> None:
        self.nlin = nlin
        self.ncol = ncol
        self.bombas = bombas
        self.acertos = 0
        self.solucao = [['-' for _ in range(ncol)] for _ in range(nlin)]
        self.bombas_colocadas = 0
        self.CriandoTabuleiro()

        # Distribui as bombas aleatoriamente
        #total_bombas = round(0.2 * board[0] * board[1])
    def CriandoTabuleiro(self):
        while self.bombas_colocadas < self.bombas:
            linha = random.randint(0, self.nlin - 1)
            coluna = random.randint(0, self.ncol - 1)
            if self.solucao[linha][coluna] != '💣':
                self.solucao[linha][coluna] = '💣'
                self.bombas_colocadas += 1

    def verificarVitoria(self, interface):
        if self.acertos == self.nlin * self.ncol - self.bombas:
            messagebox.showinfo("Fim de Jogo", "Parabéns, Você venceu!!!")
            interface.destroy()
            sys.exit()
        else:
            return None

    def ChecarSeTemBomba(self, botaoAtual, matriz, interface):
        botaoAtual_x = -1
        botaoAtual_y = -1
        for i, listaBotoes in enumerate(matriz):
            for j in range(len(listaBotoes)):
                if matriz[i][j] == botaoAtual:
                    botaoAtual_x = j
                    botaoAtual_y = i
        
        botaoAtual['state'] = DISABLED
        if self.solucao[botaoAtual_x][botaoAtual_y] == '💣':
            botaoAtual['text'] = '💣'
            messagebox.showinfo("Fim de Jogo", "Você atingiu uma bomba! Fim de jogo.")
            interface.destroy()
            sys.exit()
        else:
            self.acertos += 1
            botaoAtual['text'] = tabuleiro_vizinhanca.vizinhanca[botaoAtual_x][botaoAtual_y]
            info_celulas_restantes['text'] = f'Células Restantes: {self.nlin * self.ncol - self.bombas - self.acertos}'
            self.verificarVitoria(interface)
         
class Vizinhanca(Tabuleiro):
    def __init__(self) -> None:
        self.vizinhanca = [[0 for _ in range(tabuleiro_solucao.ncol)] for _ in range(tabuleiro_solucao.nlin)]
        self.CriarVizinhanca()

    def CriarVizinhanca(self):    
        for i in range(tabuleiro_solucao.nlin):
            for j in range(tabuleiro_solucao.ncol):
                if j == 0:
                    inic = 0
                else:
                    inic = j-1
                    if tabuleiro_solucao.solucao[i][inic] == '💣':
                        self.vizinhanca[i][j] += 1

                if j == tabuleiro_solucao.ncol - 1:
                    fim = j
                else:
                    fim = j+1
                    if tabuleiro_solucao.solucao[i][fim] == '💣':
                        self.vizinhanca[i][j] += 1

                if i > 0:
                    for k in range(inic, fim+1):
                        if tabuleiro_solucao.solucao[i-1][k] == '💣' :	
                            self.vizinhanca[i][j] += 1

                if i < tabuleiro_solucao.nlin - 1:
                    for k in range(inic, fim+1):
                        if tabuleiro_solucao.solucao[i+1][k] == '💣' :	
                            self.vizinhanca[i][j] += 1    

class Interface:
    def __init__(self, window, tabuleiro: Tabuleiro) -> None:
        self.window = window
        self.tabuleiro = tabuleiro
        self.tamanhobotao = 32
        self.x = tabuleiro.nlin * self.tamanhobotao
        self.y = tabuleiro.ncol * self.tamanhobotao
        self.matriz = []
        self.CriarInterface()
    
    def CriarInterface(self):
        for linha in range(self.tabuleiro.nlin):
            linhaBotao = []
            for coluna in range(self.tabuleiro.ncol):
                novobotao = Button(self.window)
                novobotao['command'] = lambda novobotao = novobotao: self.tabuleiro.ChecarSeTemBomba(novobotao, self.matriz, self.window)
                posY = coluna * self.tamanhobotao
                posX = linha * self.tamanhobotao
                novobotao.place(x=posX, y=posY, height=self.tamanhobotao, width=self.tamanhobotao)
                linhaBotao.append(novobotao)
            
            self.matriz.append(linhaBotao)

           
if __name__ == "__main__":
    dimensao = [5, 5]
    qntdBombas = round(dimensao[0] * dimensao[1] * 0.3)
    tabuleiro_solucao = Tabuleiro(dimensao[0], dimensao[1], qntdBombas)
    tabuleiro_vizinhanca = Vizinhanca()

    window = Tk()
    window.title("Campo Minado")
    interface = Interface(window, tabuleiro_solucao)
    window.geometry(f'{interface.x}x{interface.y}')

    window2 = Tk()
    window2.title('Informações do Jogo')

    info_bombas = Label(window2, text=f'Quantidade de bombas: {qntdBombas}')
    info_bombas.grid(column=0, row=0, padx=10, pady=10)

    info_celulas_restantes = Label(window2, text=f'Células Restantes: {dimensao[0] * dimensao[1] - qntdBombas - tabuleiro_solucao.acertos}')
    info_celulas_restantes.grid(column=0, row=1, padx=5, pady=5)

    window.mainloop()
    window2.mainloop()