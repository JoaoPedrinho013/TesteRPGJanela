from modulos import *

menuMusica()
# MENU
janela = Tk()
janela.attributes('-fullscreen', False)
janela.resizable(False, False)
janela.geometry("1000x600")
janela.title("MENU")
# Carregar a imagem de fundo
imagens.carregarImagemDeFundoMenu()
# IMAGEM
fundoMenu = imagens.menuImagem(janela)
# TITULO DO JOGO
titulo_fonte = font.Font(family="Times New Roman", size=25, weight="bold")
textoTitulo = Label(janela, text="Odisseia do Ultimo Semideus", font=titulo_fonte, bg="red", fg="black", padx=10
                          , pady=5)
textoTitulo.place(x=285, y=5)
botaoI_fonte = font.Font(family="Times New Roman", size=10, weight="bold")
botaoIniciar = Button(janela, text="JOGAR", command=lambda: introducao.abrirJanelaDoJogo(janela),
                      font=botaoI_fonte, bg="black", fg="red", padx=10)
botaoIniciar.place(x=465, y=510)
botaoR_fonte = font.Font(family="Times New Roman", size=10, weight="bold")
botaoRegras = Button(janela, text="REGRAS DO JOGO", command=lambda: regras.abrirJanelaDasRegras(janela),
                     font=botaoR_fonte, bg="black", fg="red", padx=10)
botaoRegras.place(x=430, y=540)
botaoS_fonte = font.Font(family="Times New Roman", size=10, weight="bold")
botaoSair = Button(janela, text="SAIR", command=partial(sairDoJogo, janela), font=botaoS_fonte, bg="black", fg="red")
botaoSair.place(x=480, y=570)
# RODANDO
janela.mainloop()
