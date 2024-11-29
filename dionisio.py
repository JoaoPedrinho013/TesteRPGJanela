import apolo
from musicas import dionisioMusica
from imagens import dionisioImagem, carregarImagemDeFundoDionisio, dionisioImagem2, carregarImagemDeFundoDionisio2
from modulos import *
from classes import Jogador, Inimigo


def abrirJanelaDionisio(janela2):
    global imagemDeFundoDionisio
    global janela4
    janela2.withdraw()  # OCULTAR JANELA MENU
    janela4 = Toplevel(janela2)
    janela4.attributes('-fullscreen', False)
    janela4.resizable(False, False)
    janela4.geometry("1000x600")
    janela4.title("BATALHA-DIONISIO")
    # MUSICA
    dionisioMusica()

    def morte():
        init()
        mixer.music.load('morte.mp3')
        mixer.music.set_volume(0.3)
        mixer.music.play()

    # CARREGAR IMAGEM
    imagemDeFundoDionisio = carregarImagemDeFundoDionisio()
    # IMAGEM
    fundoDionisio = dionisioImagem(janela4, imagemDeFundoDionisio)
    batalha_em_andamento = False  # Variável de controle da batalha
    botao_iniciar_clicado = False

    # ENCONTRO COM DIONISIO PRÉ BATALHA
    tituloEncontroFonte = font.Font(family="Impact", size=20, weight="bold")
    tituloEncontro = Label(janela4, text='Dionísio! O deus do vinho, patrono dos bêbados',
                           font=tituloEncontroFonte, bg="black", fg="purple")
    tituloEncontro.place(x=200, y=5)

    def animacao(encontro):
        current_y = 601  # Define a posição inicial do Label
        encontro.place(x=2, y=current_y)
        move_animacao(encontro, current_y)

    def move_animacao(encontro, current_y):
        if current_y > -encontro.winfo_height():  # Verifica se o Label ainda está visível
            encontro.place_configure(y=current_y - 1)  # Move o Label um pixel acima
            encontro.after(0, lambda: move_animacao(encontro,
                                                    current_y - 1))  # Chama a função novamente após um pequeno intervalo
        else:
            encontro.destroy()  # Remove o Label quando a animação terminar
            botaoBatalha()

    encontro_fonte = font.Font(family="Segoe Print", size=18, weight="bold")
    encontro = Label(janela4, text='''Dionísio partiu em sua busca. Com seu poder, ele fez a cabeça de várias
pessoas nas tavernas por onde passou. E foi ajudado por informações, até que
chegou em uma taverna onde o taverneiro conheceu Quíron.
 Ele ouviu boatos que Quíron estava treinando um rapaz desconhecido todos os
dias no "Vale do Conhecimento de Quíron", falaram que ele estava lá quase 
sempre.
 Com essa informação, Dionísio partiu para o vale e em questão de minutos 
estava de frente a sua frente. Lá, ele disse: "Renda-se e venha comigo para o
Olimpo, ou te levarei morto!"
Sorte ou destino?
De qualquer forma, voce já sabia da profecia que Quíron havia
lhe contado e,assim que Dionísio o desafiou.O combate começou ali mesmo, no 
Vale.
 Com seus equipamentos e habilidades à disposição, você precisará lutar para 
defendersua honra e seus objetivos contra um poderoso oponente.
 Este é o momento de mostrar seu valor e sua bravura em batalha!!!''', font=encontro_fonte, bg="black", fg="orange")
    animacao(encontro)

    def botaoRestart():
        botaoRestart = Button(janela4, text="Restart", font=("Times New Roman", 12, "bold"), command=restart,
                              bg="black", fg="red")
        botaoRestart.place(x=930, y=5)

    def restart():
        sleep(10)
        janela4.destroy()
        abrirJanelaDionisio(janela2)

    def botaoAvancar():
        botaoFonte = font.Font(family="Times New Roman", size=12, weight="bold")
        botaoAvancar = Button(janela4, text="AVANÇAR", command=lambda: apolo.abrirJanelaApolo(janela4),
                              font=botaoFonte, bg="black", fg="red")
        botaoAvancar.place(x=905, y=5)

    def botaoBatalha():
        global botao_iniciar
        botao_iniciar = Button(janela4, text="Começar Batalha", font=("Arial", 24),
                               command=lambda: iniciarBatalha(janela2), bg="black", fg="red")
        botao_iniciar.place(x=375, y=300)


    def retanguloTexto():
        # Crie um widget Text na janela principal onde vai aparecer os textos
        global texto
        texto = Text(janela4, font=("Times New Roman", 18, "bold"), bg="black", fg="gray")
        texto.pack()
        texto.place(x=30, y=500, width=930, height=100)
        # Adicione uma barra de rolagem
        scrollbar = Scrollbar(janela4, command=texto.yview)
        scrollbar.place(x=950, y=500, height=100)
        texto.config(yscrollcommand=scrollbar.set)


    def iniciarBatalha(janela):
        global jogador, barra_vida_jogador
        global inimigo, barra_vida_inimigo
        # CARREGAR IMAGEM
        imagemDeFundoDionisio2 = carregarImagemDeFundoDionisio2()
        # IMAGEM
        fundoDionisio2 = dionisioImagem2(janela4, imagemDeFundoDionisio2)
        # ENCONTRO2 COM DIONISIO PRÉ BATALHA
        tituloEncontroFonte = font.Font(family="Impact", size=20, weight="bold")
        tituloEncontro = Label(janela4, text='Dionísio! O deus do vinho, patrono dos bêbados',
                               font=tituloEncontroFonte, bg="black", fg="purple")
        tituloEncontro.place(x=200, y=5)
        jogador = Jogador(Entry(janela).get(), 100, 23, 10)
        inimigo = Inimigo("Dionísio", 45, 30, 5)
        retanguloTexto()
        batalha(jogador, inimigo)
        encontro.destroy()
        # Crie a barra de progresso para a vida do jogador
        barra_vida_jogador = ttk.Progressbar(janela4, orient="horizontal", length=200, mode="determinate")
        barra_vida_jogador["maximum"] = jogador.vida
        barra_vida_jogador["value"] = jogador.vida
        barra_vida_jogador.place(x=50, y=55)

        # Crie a barra de progresso para a vida do inimigo
        barra_vida_inimigo = ttk.Progressbar(janela4, orient="horizontal", length=200, mode="determinate")
        barra_vida_inimigo["maximum"] = inimigo.vida
        barra_vida_inimigo["value"] = inimigo.vida
        barra_vida_inimigo.place(x=50, y=90)

    # FUNCAO DE BATALHA DIONISIO
    def batalha(jogador, dionisio):
        nonlocal batalha_em_andamento  # Referenciar a variável externa
        batalha_em_andamento = True  # Iniciar a batalha
        nonlocal botao_iniciar_clicado  # Referenciar a variável externa
        if not botao_iniciar_clicado:
            botao_iniciar_clicado = True
            botao_iniciar.config(state=DISABLED)  # Desativar o botão "Iniciar Jogo"
        botao_iniciar.destroy()
        global texto
        texto.insert(1.0, "Você está de frente ao Dionísio!!!\n O que deseja fazer? Atacar ou Defender? \n")

        def acao_atacar():
            dano = randint(20, jogador.ataque) - dionisio.defesa
            if dano >= 0:
                dano = dano
            dionisio.vida -= dano
            texto.tag_configure("atacar", foreground="darkorange")
            texto.insert(END, f"\nVocê atacou o {dionisio.nome} e causou dano de {dano}!\n", "atacar")
            texto.yview_moveto(1.0)
            barra_vida_inimigo["value"] = inimigo.vida

            if jogador.vida <= 0:
                texto.tag_configure("morte", foreground="red")
                texto.insert(END, "\nSe foi de americanas...", "morte")
                mixer.music.stop()
                morte()
                batalha_em_andamento = False
                botao_atacar.destroy()
                botao_defender.destroy()

                botaoRestart()
            else:
                turno_dionisio()
                verificar_fim_batalha()

        def acao_defender():
            dano = randint(20, 60) - randint(0, jogador.defesa)
            if dano >= 0:
                dano = dano
            jogador.vida -= dano
            barra_vida_jogador["value"] = jogador.vida
            texto.tag_configure("defender", foreground="darkorange")
            texto.insert(END, f"\nVocê defendeu o ataque de {dionisio.nome} e\n sofreu um dano de {dano}!\n",
                         "defender")
            texto.yview_moveto(1.0)
            if jogador.vida <= 0:
                texto.tag_configure("morte", foreground="red")
                texto.insert(END, "\nSe foi de americanas...", "morte")
                mixer.music.stop()
                morte()
                batalha_em_andamento = False
                botao_atacar.destroy()
                botao_defender.destroy()
                botaoRestart()
            else:
                turno_dionisio()
                verificar_fim_batalha()

        def turno_dionisio():
            if dionisio.vida > 0:
                dano = randint(20, dionisio.ataque) - randint(0, jogador.defesa)
                if dano <= 0:
                    dano = 1
                jogador.vida -= dano
                barra_vida_jogador["value"] = jogador.vida
                texto.insert(END, "Agora é a vez dele\n")
                texto.tag_configure("inimigx", foreground="purple")
                texto.insert(END, f"O {dionisio.nome} atacou você e causou dano de {dano}!", "inimigx")
                verificar_fim_batalha()
                if jogador.vida <= 0:
                    texto.tag_configure("morte", foreground="red")
                    texto.insert(END, "\nSe foi de americanas...", "morte")
                    mixer.music.stop()
                    morte()
                    batalha_em_andamento = False
                    botao_atacar.destroy()
                    botao_defender.destroy()
                    botaoRestart()

        def verificar_fim_batalha():
            nonlocal batalha_em_andamento  # Referenciar a variável externa
            if dionisio.vida <= 0:
                texto.tag_configure("vitoria", foreground="green")
                texto.insert(END, f"Você derrotou o {dionisio.nome}!!! O famoso Deus bêbado!", "vitoria")
                botaoAvancar()
                batalha_em_andamento = False  # Encerrar a batalha
                # Desativar os botões de atacar e defender se a batalha estiver encerrada
            if not batalha_em_andamento:
                botao_atacar.destroy()
                botao_defender.destroy()

        # Botões de ação

        botao_atacar = Button(janela4, text="Atacar", font=("Times New Roman", 37, "bold"), command=acao_atacar,
                              bg="black", fg="green")
        botao_atacar.place(x=525, y=500)

        botao_defender = Button(janela4, text="Defender", font=("Times New Roman", 37, "bold"), command=acao_defender,
                                bg="black", fg="red")
        botao_defender.place(x=715, y=500)

    janela4.protocol("WM_DELETE_WINDOW", lambda: fechar_jogo(janela2))


# FECHAR JOGO
def fechar_jogo(janela2):
    mixer.music.stop()
    janela4.destroy()
    janela2.destroy()
    exit()
