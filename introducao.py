import musicas
from dionisio import abrirJanelaDionisio
from modulos import *
from tkinter import *
from imagens import carregarImagemDeFundoIntroducao, introducaoImagem

# FUNÇÃO JANELA DO JOGO
def abrirJanelaDoJogo(janela):
    janela.withdraw()  # OCULTAR JANELA MENU
    janela2: Toplevel = Toplevel(janela)
    janela2.geometry("1000x600")
    janela2.attributes('-fullscreen', False)
    janela2.resizable(False, False)
    janela2.title("INTRODUCAO")

#MUSICA
    musicas.introducaoMusica()

#IMAGEM
    imagemDeFundoIntroducao = carregarImagemDeFundoIntroducao()#CARREGAR IMAGEM
    fundoIntroducao = introducaoImagem(janela2, imagemDeFundoIntroducao)

# FUNCAO FECHAR O X VERMELHO
    def fechar_jogo(janela):
        janela2.destroy()
        janela.destroy()

#BOTAO VOLTAR
    botao_fonte = font.Font(family="Times New Roman", size=12, weight="bold")
    botaoVoltar2 = Button(janela2, text="VOLTAR", command=partial(voltarJanelaDoMenu2, janela2, janela), font=botao_fonte, bg="black", fg="red")
    botaoVoltar2.place(x=915, y=5)
    janela2.protocol("WM_DELETE_WINDOW", lambda: fechar_jogo(janela))

#BOTAO AVANÇAR
    def botaoAvancar():
        botaoI_fonte = font.Font(family="Times New Roman", size=12, weight="bold")
        botaoAvancar = Button(janela2, text="AVANÇAR", command=lambda: abrirJanelaDionisio(janela2),
                          font=botaoI_fonte, bg="black", fg="red", padx=10)
        botaoAvancar.place(x=885,   y=562)

# BOAS-VINDAS JANELA 2
    boas_vindas_fonte = font.Font(family="Impact", size=25, weight="bold")
    boas_vindas = Label(janela2, text="Seja bem-vindo(a) ao melhor RPG de texto do mundo!", font=boas_vindas_fonte,
                        bg="black", fg="red")
    boas_vindas.place(x=130, y=5)

    def pergunta():
    # INTRODUCAO QUIRON
        iQuiron_fonte = font.Font(family="Times New Roman", size=22, weight="bold")
        iQuiron = Label(janela2, text="Olá eu sou o Quíron treinador de heróis!\nDiga-me seu nome?", font=iQuiron_fonte,
                        bg="black", fg="gray")
        iQuiron.place(x=130, y=530)
    # ENTRY PARA RECEBER A ENTRADA DO USUARIO
        entrada = Entry(janela2)
        entrada.place(x=630, y=530)

    # NOME JOGADOR
        def exibir_pergunta():
            global nome_jogador
            nome_jogador = entrada.get().title().strip()

            if nome_jogador == "":
                boas_vindas2.configure(text="Por favor, digite seu nome para continuar.")
                return
            else:
                introducao()
            # Ocultar a pergunta
            iQuiron.place_forget()
            entrada.place_forget()
            botaoEnviar.place_forget()
            boas_vindas2.place_forget()
            #  return resposta
    # Adicione um botao chamar a funçao da pergunta
        botaoEnvinhar_fonte = font.Font(family="Times New Roman", size=20, weight="bold")
        botaoEnviar = Button(janela2, text="Enviar", command=exibir_pergunta, font=botaoEnvinhar_fonte
                                    , fg="red", bg="black")
        botaoEnviar.place(x=640, y=549)

        boas_vindas2_fonte = font.Font(family="Times New Roman", size=19, weight="bold")
        boas_vindas2 = Label(janela2, text="", font=boas_vindas2_fonte, fg="red", bg="black")
        boas_vindas2.place(x=130, y=562)

    pergunta()
    def animacao(introducao):
        current_y = 601  # Define a posição inicial do Label
        introducao.place(x=2, y=current_y)
        move_animacao(introducao, current_y)

    def move_animacao(introducao, current_y):
        if current_y > -introducao.winfo_height():  # Verifica se o Label ainda está visível
            introducao.place_configure(y=current_y - 1)  # Move o Label um pixel acima
            introducao.after(0, lambda: move_animacao(introducao,
                                                      current_y - 1))  # Chama a função novamente após um pequeno intervalo
        else:
            introducao.destroy()  # Remove o Label quando a animação terminar
            botaoAvancar()

    def introducao():
    # INTRODUCAO

        introducao_fonte = font.Font(family="Segoe Print", size=19, weight="bold")
        introducao = Label(janela2, text=f"""Seja bem-vindo(a), {nome_jogador}
    Em um mundo de mitologia grega, heróis lutam contra a escuridão para
    restaurar a paz e a ordem. O caminho está repleto de perigos e você
    é o último com sangue divino para enfrentar essa jornada épica.
    Empunhe sua espada e vença os desafios para se tornar uma lenda e
    salvar a Grécia antiga!!!
    Gaia, a mãe terra, havia tido uma visão terrível. Uma profecia 
    que a deixou em pânico e incerteza. Ela viu o último semideus, nascido 
    com o poder de acabar com o Olimpo, começando por Dionísio, o deus do 
    vinho e da loucura.
    Zeus, ao ouvir a profecia de Gaia sobre o último semideus que possuía
    o poder de destruir o Olimpo, ordenou que Dionísio, o deus do vinho e da 
    loucura, que saísse em busca do ultimo semideus. Dionísio partiu em busca 
    dele, contando com a sua habilidade do de enlouquecer seus oponentes 
    para facilitar a captura. No entanto, o que eles não esperavam era 
    que o aliado de Gaia, Quíron já havia o encontrado e fariam de tudo 
    para protegê-lo.""", font=introducao_fonte, bg="black", fg="orange")
        introducao.place(x=5, y=380)
        animacao(introducao)


# FUNÇÃO VOLTAR AO MENU
def voltarJanelaDoMenu2(janela2, janela):
    mixer.music.stop()
    janela2.destroy()
    janela.deiconify()
    musicas.menuMusica()
    janela.focus_set()
# FUNÇÃO SAIR DO JOGO
def sairDoJogo(janela):
    janela.destroy()