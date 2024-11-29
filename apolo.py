import artemis
from musicas import apoloMusica
from imagens import apoloImagem, carregarImagemDeFundoApolo, apoloImagem2, carregarImagemDeFundoApolo2
from modulos import *
from classes import Jogador, Inimigo
from random import randint

def abrirJanelaApolo(janela4):
    global imagemDeFundoApolo
    global janela5
    janela4.withdraw()  # OCULTAR JANELA MENU
    janela5 = Toplevel(janela4)
    janela5.attributes('-fullscreen', False)
    janela5.resizable(False, False)
    janela5.geometry("1000x600")
    janela5.title("BATALHA-APOLO")
    # MUSICA
    apoloMusica()
    def morte():
        init()
        mixer.music.load('morte.mp3')
        mixer.music.set_volume(0.3)
        mixer.music.play()

    # CARREGAR IMAGEM
    imagemDeFundoApolo = carregarImagemDeFundoApolo()
    # IMAGEM
    fundoApolo = apoloImagem(janela5, imagemDeFundoApolo)

    batalha_em_andamento = False  # Variável de controle da batalha
    botao_iniciar_clicado = False

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

#ENCONTRO COM APOLO PRÉ BATALHA
    tituloEncontroFonte = font.Font(family="Impact", size=20, weight="bold")
    tituloEncontro = Label(janela5, text='Apolo! O deus narcisista e do Sol',
                           font=tituloEncontroFonte, bg="black", fg="gold")
    tituloEncontro.place(x=300, y=5)

    encontro_fonte = font.Font(family="Segoe Print", size=23, weight="bold")
    encontro = Label(janela5, text='''A morte de Dionísio deixou Apolo devastado. 
Os dois irmãos eram muito próximos, compartilhavam 
de uma paixão pela música e arte.
 Apolo, o tolo divino, não tinha a mínima capacidade 
intelectual para compreender como um mero semideus poderia
possuir tal quantidade de força e habilidade para 
aniquilar um ser divino como Dionísio. Sua mente limitada
e arrogante se sentiu duplamente enganada, pois além da 
tristeza pela morte de seu irmão, teve que encarar a 
realidade de ser superado por um simples e insignificante 
semideus, cuja presunção o deixou ainda mais irritado. 
Afinal, como poderia alguém tão inferior ousar desafiar um 
ser divino como ele próprio? Essa situação só revela o quão 
patético e fraco Apolo realmente é, incapaz de lidar com 
a verdadeira grandiosidade dos seres humanos.
 Após o luto, a dor de Apolo se transformou em raiva e ele 
jurou vingança, partindo em uma busca pelo assassino. 
Utilizando sua habilidade com o arco e flecha e seus poderes
divinos, Apolo investigou cidades e vilas, vasculhou florestas
e montanhas em busca do semideus.
 Seu desejo por justiça e vingança era insaciável, e nada o 
deteria até que o responsável pelo assassinato de Dionísio 
fosse encontrado e punido pelo seu crime.''', font=encontro_fonte, bg="black", fg="orange")
    animacao(encontro)
    def botaoRestart():
        botaoRestart = Button(janela5, text="Restart", font=("Times New Roman", 12, "bold"), command=restart,
                               bg="black", fg="red")
        botaoRestart.place(x=770, y=250)
    def restart():
        sleep(10)
        janela5.destroy()
        abrirJanelaApolo(janela4)

# BOTAO AVANCAR
    def botaoAvancar():

        botaoFonte = font.Font(family="Times New Roman", size=12, weight="bold")
        botaoAvancar = Button(janela5, text="AVANÇAR", command=lambda: artemis.abrirJanelaArtemis(janela5),
                              font=botaoFonte, bg="black", fg="red")
        botaoAvancar.place(x=905, y=5)

    def botaoBatalha():
        global botao_iniciar
        botao_iniciar = Button(janela5, text="Começar Batalha", font=("Arial", 24),
                               command=lambda: iniciarBatalha(janela4), bg="black", fg="red")
        botao_iniciar.place(x=375, y=300)

    def retanguloTexto():
        # Crie um widget Text na janela principal onde vai aparecer os textos
        global texto
        texto = Text(janela5, font=("Times New Roman", 18, "bold"), bg="black", fg="gray")
        texto.pack()
        texto.place(x=30, y=500, width=930, height=100)
        # Adicione uma barra de rolagem
        scrollbar = Scrollbar(janela5, command=texto.yview)
        scrollbar.place(x=950, y=500, height=100)
        texto.config(yscrollcommand=scrollbar.set)

    def iniciarBatalha(janela):
        global jogador, barra_vida_jogador
        global inimigo, barra_vida_inimigo
        # CARREGAR IMAGEM
        imagemDeFundoApolo2 = carregarImagemDeFundoApolo2()
        # IMAGEM
        fundoApolo2 = apoloImagem2(janela5, imagemDeFundoApolo2)
        tituloEncontroFonte = font.Font(family="Impact", size=20, weight="bold")
        tituloEncontro = Label(janela5, text='Apolo! O deus narcisista e do Sol',
                               font=tituloEncontroFonte, bg="black", fg="gold")
        tituloEncontro.place(x=300, y=5)
        jogador = Jogador(Entry(janela).get(), 100, 28, 15)
        inimigo = Inimigo("Apolo", 55, 40, 10)
        retanguloTexto()
        batalha(jogador, inimigo)
        encontro.destroy()
        # Crie a barra de progresso para a vida do jogador
        barra_vida_jogador = ttk.Progressbar(janela5, orient="horizontal", length=200, mode="determinate")
        barra_vida_jogador["maximum"] = jogador.vida
        barra_vida_jogador["value"] = jogador.vida
        barra_vida_jogador.place(x=50, y=55)

        # Crie a barra de progresso para a vida do inimigo
        barra_vida_inimigo = ttk.Progressbar(janela5, orient="horizontal", length=200, mode="determinate")
        barra_vida_inimigo["maximum"] = inimigo.vida
        barra_vida_inimigo["value"] = inimigo.vida
        barra_vida_inimigo.place(x=50, y=90)

    # FUNCAO DE BATALHA APOLO
    def batalha(jogador, apolo):
        nonlocal batalha_em_andamento  # Referenciar a variável externa
        batalha_em_andamento = True  # Iniciar a batalha
        nonlocal botao_iniciar_clicado  # Referenciar a variável externa
        if not botao_iniciar_clicado:
            botao_iniciar_clicado = True
            botao_iniciar.config(state=DISABLED)  # Desativar o botão "Iniciar Jogo"
        botao_iniciar.destroy()

        global texto
        texto.insert(1.0, "Você está de frente ao Apolo!!!\n O que deseja fazer? Atacar ou Defender? \n")

        def acao_atacar():
            dano = randint(25, jogador.ataque) - apolo.defesa
            if dano >= 0:
                dano = dano
            apolo.vida -= dano
            texto.tag_configure("ataque", foreground="darkorange")
            texto.insert(END, f"\nVocê atacou o {apolo.nome} e causou dano de {dano}!\n", "ataque")
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
                turno_apolo()
                verificar_fim_batalha()

        def acao_defender():
            dano = randint(30, 70) - randint(0, jogador.defesa)
            if dano >= 0:
                dano = dano
            jogador.vida -= dano
            barra_vida_jogador["value"] = jogador.vida
            texto.tag_configure("defesa", foreground="darkorange")
            texto.insert(END, f"\nVocê defendeu o ataque de {apolo.nome} e sofreu um dano de {dano}!\n", "defesa")
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
                turno_apolo()
                verificar_fim_batalha()

        def turno_apolo():
            if apolo.vida > 0:
                dano = randint(30, apolo.ataque) - randint(3, jogador.defesa)
                if dano <= 0:
                    dano = 1
                jogador.vida -= dano
                barra_vida_jogador["value"] = jogador.vida
                texto.insert(END, "Agora é a vez dele\n")
                texto.tag_configure("inimigx", foreground="yellow")
                texto.insert(END, f"O {apolo.nome} atacou você e causou dano de {dano}!", "inimigx")
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
            if apolo.vida <= 0:
                texto.tag_configure("eDeTodos", foreground="green")
                texto.insert(END, f"Você derrotou o {apolo.nome}!!! O famoso Deus Sol!", "eDeTodos")
                botaoAvancar()
                batalha_em_andamento = False  # Encerrar a batalha
                # Desativar os botões de atacar e defender se a batalha estiver encerrada
            if not batalha_em_andamento:
                botao_atacar.destroy()
                botao_defender.destroy()

        # Botões de ação

        botao_atacar = Button(janela5, text="Atacar", font=("Times New Roman", 37, "bold"), command=acao_atacar,
                              bg="black", fg="green")
        botao_atacar.place(x=525, y=500)

        botao_defender = Button(janela5, text="Defender", font=("Times New Roman", 37, "bold"), command=acao_defender,
                                bg="black", fg="red")
        botao_defender.place(x=715, y=500)

    janela5.protocol("WM_DELETE_WINDOW", lambda: fechar_jogo(janela4))


# FECHAR JOGO
def fechar_jogo(janela4):
    mixer.music.stop()
    janela5.destroy()
    janela4.destroy()
    exit()