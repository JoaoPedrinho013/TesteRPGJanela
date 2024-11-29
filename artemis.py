import hermes
from musicas import artemisMusica
from imagens import artemisImagem, imagemDeFundoArtemis, carregarImagemDeFundoArtemis, artemisImagem2, \
    imagemDeFundoArtemis2, carregarImagemDeFundoArtemis2
from modulos import *
from classes import Jogador, Inimigo


def abrirJanelaArtemis(janela5):
    global imagemDeFundoDionisio
    global janela6
    janela5.withdraw()  # OCULTAR JANELA MENU
    janela6 = Toplevel(janela5)
    janela6.attributes('-fullscreen', False)
    janela6.resizable(False, False)
    janela6.geometry("1000x600")
    janela6.title("BATALHA-ARTEMIS")
    # MUSICA
    artemisMusica()

    def morte():
        init()
        mixer.music.load('morte.mp3')
        mixer.music.set_volume(0.3)
        mixer.music.play()

    # CARREGAR IMAGEM
    imagemDeFundoArtemis = carregarImagemDeFundoArtemis()
    # IMAGEM
    fundoDionisio = artemisImagem(janela6, imagemDeFundoArtemis)

    batalha_em_andamento = False  # Variável de controle da batalha
    botao_iniciar_clicado = False

    # Crie um widget Text na janela principal onde vai aparecer os textos
    def retanguloTexto3():
        global texto
        texto = Text(janela6, font=("Times New Roman", 18, "bold"), bg="black", fg="gray")
        texto.pack()
        texto.place(x=30, y=500, width=930, height=100)

        # Adicione uma barra de rolagem
        scrollbar = Scrollbar(janela6, command=texto.yview)
        scrollbar.place(x=950, y=500, height=100)
        texto.config(yscrollcommand=scrollbar.set)

    def iniciarBatalha3(janela):
        global jogador, barra_vida_jogador
        global inimigo, barra_vida_inimigo
        # CARREGAR IMAGEM
        imagemDeFundoArtemis2 = carregarImagemDeFundoArtemis2()
        # IMAGEM
        fundoDionisio = artemisImagem2(janela6, imagemDeFundoArtemis2)
        # ENCONTRO2 COM ARTEMIS PRÉ BATALHA
        tituloEncontroFonte = font.Font(family="Impact", size=20, weight="bold")
        tituloEncontro = Label(janela6, text='Artemis! A deus caça e do Lua',
                               font=tituloEncontroFonte, bg="black", fg="silver")
        tituloEncontro.place(x=300, y=5)
        jogador = Jogador(Entry(janela).get(), 150, 31, 20)
        inimigo = Inimigo("Artemis", 65, 50, 15)
        retanguloTexto3()
        batalha(jogador, inimigo)
        encontro.destroy()

        # Crie a barra de progresso para a vida do jogador
        barra_vida_jogador = ttk.Progressbar(janela6, orient="horizontal", length=200, mode="determinate")
        barra_vida_jogador["maximum"] = jogador.vida
        barra_vida_jogador["value"] = jogador.vida
        barra_vida_jogador.place(x=50, y=55)

        # Crie a barra de progresso para a vida do inimigo
        barra_vida_inimigo = ttk.Progressbar(janela6, orient="horizontal", length=200, mode="determinate")
        barra_vida_inimigo["maximum"] = inimigo.vida
        barra_vida_inimigo["value"] = inimigo.vida
        barra_vida_inimigo.place(x=50, y=90)

    # ENCONTRO COM ARTEMIS PRÉ BATALHA
    tituloEncontroFonte = font.Font(family="Impact", size=20, weight="bold")
    tituloEncontro = Label(janela6, text='Artemis! A deus caça e do Lua',
                           font=tituloEncontroFonte, bg="black", fg="silver")
    tituloEncontro.place(x=300, y=5)

    encontro_fonte = font.Font(family="Times New Roman", size=12, weight="bold")
    encontro = Label(janela6, text='''texto introdução''', font=encontro_fonte, bg="black", fg="orange")
    encontro.place(x=2, y=45)

    def botaoRestart():
        botaoRestart = Button(janela6, text="Restart", font=("Times New Roman", 12, "bold"), command=restart,
                              bg="black", fg="red")
        botaoRestart.place(x=770, y=250)

    def restart():
        sleep(10)
        janela6.destroy()
        abrirJanelaArtemis(janela5)

    #BOTAO AVANCAR
    def botaoAvancar():
        botaoFonte = font.Font(family="Times New Roman", size=12, weight="bold")
        botaoAvancar = Button(janela6, text="AVANÇAR", command=lambda: hermes.abrirJanelaHermes(janela6),
                                font=botaoFonte, bg="black", fg="red")
        botaoAvancar.place(x=905, y=5)

    # FUNCAO DE BATALHA ARTEMIS
    def batalha(jogador, artemis):
        nonlocal batalha_em_andamento  # Referenciar a variável externa
        batalha_em_andamento = True  # Iniciar a batalha
        nonlocal botao_iniciar_clicado  # Referenciar a variável externa
        if not botao_iniciar_clicado:
            botao_iniciar_clicado = True
            botao_iniciar.config(state=DISABLED)  # Desativar o botão "Iniciar Jogo"
        botao_iniciar.destroy()
        texto.insert(1.0, "Você está de frente a Artemis!!!\n O que deseja fazer? Atacar ou Defender? \n")

        def acao_atacar():
            dano = randint(28, jogador.ataque) - artemis.defesa
            if dano >= 0:
                dano = dano
            artemis.vida -= dano
            texto.tag_configure("atacar", foreground="darkorange")
            texto.insert(END, f"\nVocê atacou a {artemis.nome} e causou dano de {dano}!\n", "atacar")
            texto.yview_moveto(1.0)
            barra_vida_inimigo["value"] = inimigo.vida
            if jogador.vida <= 0:
                texto.tag_configure("morte", foreground="red")
                texto.insert(END, "\nSe foi de americanas...", "morte")
                batalha_em_andamento = False
                botao_atacar.destroy()
                botao_defender.destroy()
                mixer.music.stop()
                morte()
                botaoRestart()
            else:
                turno_artemis()
                verificar_fim_batalha()

        def acao_defender():
            dano = randint(40, 80) - randint(0, jogador.defesa)
            if dano >= 0:
                dano = dano
            jogador.vida -= dano
            barra_vida_jogador["value"] = jogador.vida
            texto.tag_configure("defender", foreground="darkorange")
            texto.insert(END, f"\nVocê defendeu o ataque da {artemis.nome} e sofreu um dano de {dano}!\n",
                         "defender")
            texto.yview_moveto(1.0)

            if jogador.vida <= 0:
                texto.tag_configure("morte", foreground="red")
                texto.insert(END, "\nSe foi de americanas...", "morte")
                batalha_em_andamento = False
                botao_atacar.destroy()
                botao_defender.destroy()
                mixer.music.stop()
                morte()
                botaoRestart()
            else:
                turno_artemis()
                verificar_fim_batalha()

        def turno_artemis():
            if artemis.vida > 0:
                dano = randint(30, artemis.ataque) - randint(6, jogador.defesa)
                if dano <= 0:
                    dano = 1
                jogador.vida -= dano
                barra_vida_jogador["value"] = jogador.vida
                texto.insert(END, "Agora é a vez dela\n")
                texto.tag_configure("inimigx", foreground="silver")
                texto.insert(END, f"A {artemis.nome} atacou você e causou dano de {dano}!", "inimigx")
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
            if artemis.vida <= 0:
                texto.tag_configure("vitoria", foreground="green")
                texto.insert(END, f"Você derrotou a {artemis.nome}!!! A Deus caçadora!", "vitoria")
                botaoAvancar()
                batalha_em_andamento = False  # Encerrar a batalha
                # Desativar os botões de atacar e defender se a batalha estiver encerrada
            if not batalha_em_andamento:
                botao_atacar.destroy()
                botao_defender.destroy()

        # Botões de ação

        botao_atacar = Button(janela6, text="Atacar", font=("Times New Roman", 37, "bold"), command=acao_atacar,
                              bg="black", fg="green")
        botao_atacar.place(x=525, y=500)

        botao_defender = Button(janela6, text="Defender", font=("Times New Roman", 37, "bold"), command=acao_defender,
                                bg="black", fg="red")
        botao_defender.place(x=715, y=500)

    botao_iniciar = Button(janela6, text="Começar Batalha", font=("Arial", 24),
                           command=lambda: iniciarBatalha3(janela5), bg="black", fg="red")
    botao_iniciar.place(x=375, y=300)

    janela6.protocol("WM_DELETE_WINDOW", lambda: fechar_jogo(janela5))


# FECHAR JOGO
def fechar_jogo(janela5):
    mixer.music.stop()
    janela6.destroy()
    janela5.destroy()
    exit()