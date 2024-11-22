import tkinter as tk
import random

def escolher_palavra():
    palavras = ["MITS", "altair", "programacao", "etec", "tecnologia", "computador", "Ridley", "Microsoft", "Apple", "informatica"]
    return random.choice(palavras).upper()

class JogoDaForca:
    def __init__(self):
        self.palavra_secreta = escolher_palavra()
        self.letras_corretas = ["_" for _ in self.palavra_secreta]
        self.tentativas = 6
        self.letras_erradas = []

    def iniciar_jogo(self):
        self.root = tk.Tk()  # Inicializa a janela principal do Tkinter
        self.root.title("Jogo da Forca")  # Define o título da janela

        # Obtém as dimensões da tela e calcula a posição da janela para centralizá-la
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        largura_janela = 500
        altura_janela = 625
        pos_x = (largura_tela - largura_janela) // 4
        pos_y = (altura_tela - altura_janela) // 2
        self.root.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')

        # Cria um canvas para desenhar a forca e o boneco
        self.canvas = tk.Canvas(self.root, width=300, height=400)
        self.canvas.pack()
        self.canvas.create_line(5, 400, 5, 50)
        self.canvas.create_line(5, 50, 170, 50)
        self.canvas.create_line(170, 50, 170, 100)

        # Cria um label para exibir a palavra com as letras corretas adivinhadas
        self.palavra_label = tk.Label(self.root, text=" ".join(self.letras_corretas), font=("Helvetica", 18))
        self.palavra_label.pack(pady=20)

        # Cria um campo de entrada para o jogador digitar uma letra
        self.letra_entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.letra_entry.pack()
        self.letra_entry.bind("<Return>", self.verificar_letra_evento)  # Associa a tecla Enter ao método verificar_letra_evento

        # Cria um frame para os botões
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=15)

        # Cria o botão "Verificar" e associa ao método verificar_letra
        verificar_button = tk.Button(button_frame, text="Verificar", command=self.verificar_letra)
        verificar_button.pack(side=tk.LEFT)

        # Cria o botão "Jogar Novamente" e associa ao método reinicia_jogo
        jogarDeNovo = tk.Button(button_frame, text="Jogar Novamente", command=self.reinicia_jogo)
        jogarDeNovo.pack(side=tk.RIGHT)

        # Cria um label para exibir mensagens ao jogador (resultados das tentativas)
        self.resultado_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.resultado_label.pack(pady=20)

        # Inicia o loop da interface gráfica
        self.root.mainloop()

    def verificar_letra_evento(self, event):
        self.verificar_letra()  # Chama o método verificar_letra quando a tecla Enter é pressionada

    def verificar_letra(self):
        chute = self.letra_entry.get().upper()  # Obtém a letra digitada e converte para maiúscula
        self.letra_entry.delete(0, tk.END)  # Limpa o campo de entrada

        # Verifica se a entrada é válida (uma única letra)
        if len(chute) != 1 or not chute.isalpha():
            self.resultado_label.config(text="Digite uma única letra válida.")
            return

        # Verifica se a letra já foi tentada
        if chute in self.letras_corretas or chute in self.letras_erradas:
            self.resultado_label.config(text="Você já tentou essa letra. Tente outra.")
            return

        # Verifica se a letra está na palavra secreta
        if chute in self.palavra_secreta:
            for i, letra in enumerate(self.palavra_secreta):
                if letra == chute:
                    self.letras_corretas[i] = letra
            self.resultado_label.config(text="Boa! A letra está na palavra.")
        else:
            self.tentativas -= 1  # Decrementa o número de tentativas
            self.letras_erradas.append(chute)
            self.desenhar_boneco()  # Atualiza o desenho do boneco
            self.resultado_label.config(text="A letra não está na palavra.")

        self.atualizar_palavra()  # Atualiza a exibição da palavra

        # Verifica se o jogo foi ganho ou perdido
        if "_" not in self.letras_corretas:
            self.resultado_label.config(text="Parabéns! Você adivinhou a palavra!")
            self.letra_entry.config(state=tk.DISABLED)
        elif self.tentativas == 0:
            self.resultado_label.config(text=f"Você perdeu! A palavra era: {self.palavra_secreta}")
            self.letra_entry.config(state=tk.DISABLED)

    def atualizar_palavra(self):
        self.palavra_label.config(text=" ".join(self.letras_corretas))  # Atualiza o label da palavra

    def desenhar_boneco(self):
        if self.tentativas == 5:
            self.canvas.create_oval(140, 100, 200, 160)  # Cabeça
        elif self.tentativas == 4:
            self.canvas.create_line(170, 160, 170, 290)  # Corpo
        elif self.tentativas == 3:
            self.canvas.create_line(170, 190, 140, 240)  # Braço esquerdo
        elif self.tentativas == 2:
            self.canvas.create_line(170, 190, 200, 240)  # Braço direito
        elif self.tentativas == 1:
            self.canvas.create_line(170, 290, 140, 345)  # Perna esquerda
        elif self.tentativas == 0:
            self.canvas.create_line(170, 290, 200, 345)  # Perna direita
            self.canvas.create_line(117, 140, 222, 180)  # Linha diagonal do X
            self.canvas.create_line(117, 180, 222, 140)  # Linha diagonal do X

    def reinicia_jogo(self):
        self.palavra_secreta = escolher_palavra()  # Escolhe uma nova palavra secreta
        self.letras_corretas = ["_" for _ in self.palavra_secreta]  # Reinicia as letras corretas
        self.tentativas = 6  # Reinicia as tentativas
        self.letras_erradas = []  # Reinicia as letras erradas
        self.atualizar_palavra()  # Atualiza a exibição da palavra
        self.canvas.delete("all")  # Limpa o canvas
        self.canvas.create_line(5, 400, 5, 50)  # Redesenha a estrutura da forca
        self.canvas.create_line(5, 50, 170, 50)  # Redesenha a estrutura da forca
        self.canvas.create_line(170, 50, 170, 100)  # Redesenha a estrutura da forca
        self.resultado_label.config(text="")  # Limpa o label de resultado
        self.letra_entry.config(state=tk.NORMAL)  # Reativa o campo de entrada