from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
#Importando biblioteca kivy para conseguir usar interface grafica

class JogoDaVelha(App):
    def build(self):
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.turno = 'X'
        self.vitorias_x = 0
        self.vitorias_o = 0
#inicializando matrizes e variaveis

        layout = GridLayout(rows=3,cols=1) #fazendo o layout da inteface grafica com 1 coluna pra tudo ficar alinhado e 3 linhas para colocar, a vez, os pontos e o tabuleiro

        self.status_label = Label(font_size=30, size_hint_y=None, #aqui é a vez de quem vai ser formatando o texto
                                  text_size=(None, None), halign='center', valign='top')
        layout.add_widget(self.status_label) #adicionando o status para a primeira linha do layout


        self.contador_label = Label(font_size=20, text=f'Vitórias X: {self.vitorias_x}, Vitórias O: {self.vitorias_o}'
                                    ,size_hint_y=None, halign='center', valign='top')
        layout.add_widget(self.contador_label)
        #aqui é o contador de vitórias e adicionando ele ao layout, ja com o texto e com as variaveis

        self.atualizar_status('Novo jogo! Turno do jogador X')

        self.tabuleiro_layout = GridLayout(rows=3, cols=3)
        for row in range(3):
            for col in range(3):
                button = Button(font_size=40)
                button.bind(on_press=self.fazer_jogada)
                button.row = row
                button.col = col
                self.tabuleiro_layout.add_widget(button)
        layout.add_widget(self.tabuleiro_layout)

        return layout

    def fazer_jogada(self, instance):
        row, col = instance.row, instance.col

        if self.tabuleiro[row][col] == ' ':
            instance.text = self.turno
            self.tabuleiro[row][col] = self.turno

            # Adicionando cores aos botões
            if self.turno == 'X':
                instance.background_color = (1, 0, 0, 1)  # Vermelho
            else:
                instance.background_color = (0, 0, 1, 1)  # Azul

            if self.verificar_vencedor():
                self.atualizar_status(f'O jogador {self.turno} venceu!')
                if self.turno == 'X':
                    self.vitorias_x += 1
                else:
                    self.vitorias_o += 1
                self.atualizar_contador()
                self.resetar_jogo()
            elif self.verificar_empate():
                self.atualizar_status('Empate!')
                self.resetar_jogo()
            else:
                self.turno = 'O' if self.turno == 'X' else 'X'
                self.atualizar_status(f'Turno do jogador {self.turno}')

    def verificar_vencedor(self):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != ' ':
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != ' ':
                return True
            if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != ' ':
                return True
            if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ' ':
                return True
        return False

    def verificar_empate(self):
        for row in self.tabuleiro:
            if ' ' in row:
                return False
        return True

    def resetar_jogo(self):
        for widget in self.tabuleiro_layout.children:
            if isinstance(widget, Button):
                widget.text = ''
                widget.background_color = (1, 1, 1, 1)  # Resetando a cor para branco
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.turno = 'X'
        self.atualizar_status('Novo jogo! Turno do jogador X')

    def atualizar_status(self, texto):
        self.status_label.text = texto

    def atualizar_contador(self):
        self.contador_label.text = f'Vitórias X: {self.vitorias_x}, Vitórias O: {self.vitorias_o}'


if __name__ == '__main__':
    JogoDaVelha().run()
