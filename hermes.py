from imagens import carregarImagemDeFundoHermes, hermesImagem
from musicas import artemisMusica
from modulos import *
from classes import Jogador, Inimigo

perguntaAtual = 0
escolha = []


def abrirJanelaHermes(janela6):
    global imagemDeFundoDionisio
    global janela7
    janela6.withdraw()
    janela7 = Toplevel(janela6)
    janela7.attributes('-fullscreen', False)
    janela7.resizable(False, False)
    janela7.geometry("1000x600")
    janela7.title("BATALHA-HERMES")
    # MUSICA
    artemisMusica()

    def morte():
        init()
        mixer.music.load('morte.mp3')
        mixer.music.set_volume(0.3)
        mixer.music.play()

    # IMAGEM
    imagemDeFundoHermes = carregarImagemDeFundoHermes()
    fundoHermes = hermesImagem(janela7, imagemDeFundoHermes)

    # TITULO HERMES
    tituloEncontroFonte = font.Font(family="Impact", size=20, weight="bold")
    tituloEncontro = Label(janela7, text='Hermes, o deus rapidinho',
                           font=tituloEncontroFonte, bg="black", fg="lightblue")
    tituloEncontro.place(x=300, y=5)

    # Crie um widget Text na janela principal onde vai aparecer os textos
    def retanguloTexto3():
        global texto
        texto = Text(janela7, font=("Impact", 15), bg="black", fg="lightblue")
        texto.pack()
        texto.place(x=30, y=500, width=930, height=100)

        # Adicione uma barra de rolagem
        scrollbar = Scrollbar(janela7, command=texto.yview)
        scrollbar.place(x=950, y=500, height=100)
        texto.config(yscrollcommand=scrollbar.set)

    # PERGUNTAS
    perguntas = [
        "1-Por que você, semideus, deseja matar Zeus e cumprir essa profecia? Qual é a sua motivação?",
        "2-Você acredita que após eliminar os deuses do Olimpo, haverá consequências para o mundo e os mortais?",
        "3-Você sente alguma hesitação ou dúvida em matar os deuses do Olimpo?",
        "4-Você teme que, após matar todos os deuses do Olimpo, você se torne igual ou pior do que eles?",
        "5-Existe alguma relação pessoal entre você e Zeus que motiva o seu desejo de matá-lo?"
    ]
    # ALTERNATIVAS
    alternativas = [
        ["a) Eu quero assumir o controle do Olimpo e restaurar o equilíbrio entre os deuses.",
         "b) Zeus é uma ameaça para o mundo dos mortais e precisa ser detido para evitar mais tragédias.",
         "c) A profecia me obriga a fazer isso, não há escolha."],
        ["a) Sim, tenho medo das consequências, mas acredito que a mudança é necessária.",
         "b) Não, acredito que o mundo se tornará mais seguro e livre de interferências divinas.",
         "c) Não posso prever o futuro, apenas seguir a profecia sem pensar nas consequências."],
        ["a) Sim, cada morte pesa em meu coração, mas sinto que é meu dever cumprir a profecia.",
         "b) Não, não há espaço para sentimentos quando se trata de cumprir a profecia.",
         "c) Não posso permitir que emoções me afetem, independente dos meus sentimentos."],
        ["a) Sim, tenho esse medo, mas sei que devo agir para evitar maiores desastres.",
         "b) Não, acredito que minha causa é justa e não me corromperei como eles.",
         "c) Não importa o que eu sinta ou tema, a profecia é tudo o que importa."],
        ["a) Sim, Zeus causou sofrimento a alguém que amo, e isso me motiva a agir.",
         "b) Não, minha motivação é puramente baseada na profecia e no dever designado.",
         "c) Não importa minhas relações pessoais, só importa o que a profecia requer."]
    ]

    def exibirPerguntas(indice):
        texto.delete(1.0, END)
        texto.tag_configure('cor', foreground='Silver', font=('Impact', 15))
        pergunta = texto.insert(END, perguntas[indice] + "\n")
        for alternativa in alternativas[indice]:
            texto.insert(END, alternativa + '\n', 'cor')

    def salvarEscolha(escolhaClicada):
        escolha.append(escolhaClicada)

    def proximaPergunta():
        global perguntaAtual
        if perguntaAtual < len(perguntas) - 1:
            perguntaAtual += 1
            exibirPerguntas(perguntaAtual)
        else:
            print("Você chegou ao final das perguntas.")
            print("Respostas selecionadas:", escolha)

    retanguloTexto3()

    exibirPerguntas(perguntaAtual)
    # BOTAO PARA ALTERNATIVAS
    botaoA = Button(janela7, text='✔️', bg='lightblue', fg='black', command=lambda: salvarEscolha('a') or
                                                                                    proximaPergunta())
    botaoA.place(x=2, y=525)
    botaoB = Button(janela7, text='✔️', bg='lightblue', fg='black', command=lambda: salvarEscolha('b') or
                                                                                    proximaPergunta())
    botaoB.place(x=2, y=550)
    botaoC = Button(janela7, text='✔️', bg='lightblue', fg='black', command=lambda: salvarEscolha('c') or
                                                                                    proximaPergunta())
    botaoC.place(x=2, y=575)

    # BOTAO AVANCAR
    # def botaoAvancar():
    #     botaoFonte = font.Font(family="Times New Roman", size=12, weight="bold")
    #     botaoAvancar = Button(janela6, text="AVANÇAR", command=lambda: hermes.abrirJanelaHermes(janela6),
    #                             font=botaoFonte, bg="black", fg="red")
    #     botaoAvancar.place(x=900, y=550)
    janela7.protocol("WM_DELETE_WINDOW", lambda: fechar_jogo(janela6))


# FECHAR JOGO
def fechar_jogo(janela6):
    mixer.music.stop()
    janela7.destroy()
    janela6.destroy()
    exit()
