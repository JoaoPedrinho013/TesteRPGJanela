from modulos import *
# MENU IMAGEM
imagemDeFundoMenu = None
def carregarImagemDeFundoMenu():
    global imagemDeFundoMenu
    imagemDeFundoMenu = PhotoImage(file='menu.png')
def menuImagem(janela):
    global imagemDeFundoMenu
    imagemDeFundoMenu = PhotoImage(file='menu.png')
    fundoMenu = Label(janela, image=imagemDeFundoMenu)
    fundoMenu.place(x=0, y=0, relwidth=1, relheight=1)
    return fundoMenu

# REGRAS IMAGEM
imagemDeFundoRegras = None
def carregarImagemDeFundoRegras():
    global imagemDeFundoRegras
    imagemDeFundoRegras = PhotoImage(file='regras.png')
    return imagemDeFundoRegras

def regrasImagem(janela3, imagemDeFundoRegras):
    fundoRegras = Label(janela3, image=imagemDeFundoRegras)
    fundoRegras.place(x=0, y=0, relwidth=1, relheight=1)
    return fundoRegras

# DIONISIO IMAGEM
imagemDeFundoDionisio = None
def carregarImagemDeFundoDionisio():
    global imagemDeFundoDionisio
    imagemDeFundoDionisio = PhotoImage(file='dionisio.png')
    return imagemDeFundoDionisio

def dionisioImagem(janela4, imagemDeFundoDionisio):
    fundoDionisio = Label(janela4, image=imagemDeFundoDionisio)
    fundoDionisio.place(x=0, y=0, relwidth=1, relheight=1)
    return fundoDionisio

# DIONISIO2 IMAGEM
imagemDeFundoDionisio2 = None
def carregarImagemDeFundoDionisio2():
    global imagemDeFundoDionisio2
    imagemDeFundoDionisio2 = PhotoImage(file='dionisio2.png')
    return imagemDeFundoDionisio2

def dionisioImagem2(janela4, imagemDeFundoDionisio2):
    fundoDionisio2 = Label(janela4, image=imagemDeFundoDionisio2)
    fundoDionisio2.place(x=0, y=0, relwidth=1, relheight=1)
    return fundoDionisio2

# APOLO IMAGEM
imagemDeFundoApolo = None
def carregarImagemDeFundoApolo():
    global imagemDeFundoApolo
    imagemDeFundoApolo = PhotoImage(file='apolo.png')
    return imagemDeFundoApolo

def apoloImagem(janela5, imagemDeFundoApolo):
    fundoApolo = Label(janela5, image=imagemDeFundoApolo)
    fundoApolo.place(x=0, y=0, relwidth=1, relheight=1)
    return fundoApolo

# APOLO2 IMAGEM
imagemDeFundoApolo2 = None
def carregarImagemDeFundoApolo2():
    global imagemDeFundoApolo2
    imagemDeFundoApolo2 = PhotoImage(file='apolo2.png')
    return imagemDeFundoApolo2

def apoloImagem2(janela5, imagemDeFundoApolo2):
    fundoApolo2 = Label(janela5, image=imagemDeFundoApolo2)
    fundoApolo2.place(x=0, y=0, relwidth=1, relheight=1)
    return fundoApolo2

# ARTEMIS IMAGEM
imagemDeFundoArtemis = None
def carregarImagemDeFundoArtemis():
    global imagemDeFundoArtemis
    imagemDeFundoArtemis = PhotoImage(file='artemis.png')
    return imagemDeFundoArtemis
def artemisImagem(janela6, imagemDeFundoArtemis):
    fundoArtemis = Label(janela6, image=imagemDeFundoArtemis)
    fundoArtemis.place(x=0, y=0, relwidth=1, relheight=1)
    return fundoArtemis

# ARTEMIS2 BATALHA IMAGEM
imagemDeFundoArtemis2 = None
def carregarImagemDeFundoArtemis2():
    global imagemDeFundoArtemis
    imagemDeFundoArtemis = PhotoImage(file='artemis2.png')
    return imagemDeFundoArtemis
def artemisImagem2(janela6, imagemDeFundoArtemis):
    fundoArtemis = Label(janela6, image=imagemDeFundoArtemis)
    fundoArtemis.place(x=0, y=0, relwidth=1, relheight=1)
    return fundoArtemis
#HERMER IMAGEM
imagemDeFundoHermes = None
def carregarImagemDeFundoHermes():
    global imagemDeFundoHermes
    imagemDeFundoHermes = PhotoImage(file='hermes.png')
    return imagemDeFundoHermes
def hermesImagem(janela6, imagemDeFundoHermes):
    fundoHermes = Label(janela6, image=imagemDeFundoHermes)
    fundoHermes.place(x=0, y=0, relwidth=1, relheight=1)
    return fundoHermes

# INTRODUCAO IMAGEM
imagemDeFundoIntroducao = None
def carregarImagemDeFundoIntroducao():
    global imagemDeFundoIntroducao
    imagemDeFundoIntroducao = PhotoImage(file='jogo.png')
    return imagemDeFundoIntroducao

def introducaoImagem(janela2, imagemDeFundoIntroducao):
    fundoIntroducao = Label(janela2, image=imagemDeFundoIntroducao)
    fundoIntroducao.place(x=0, y=0, relwidth=1, relheight=1)
    return fundoIntroducao