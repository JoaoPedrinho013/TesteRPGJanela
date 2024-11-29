from modulos import *
# FUNÇÃO JANELA DAS REGRAS
def abrirJanelaDasRegras(janela):
    global imagemDeFundoRegra
    janela.withdraw()  # OCULTAR JANELA MENU
    janela3 = Toplevel(janela)
    janela3.attributes('-fullscreen', False)
    janela3.resizable(False, False)
    janela3.geometry("1000x600")
    janela3.title("REGRAS")
# MUSICA
    regrasMusica()
# CARREGAR IMAGEM
    imagemDeFundoRegras = carregarImagemDeFundoRegras()
# IMAGEM
    fundoRegras = regrasImagem(janela3, imagemDeFundoRegras)

# FUNCAO FECHAR O X VERMELHO
    def fechar_jogo(janela):
        janela3.destroy()
        janela.destroy()

    botaoV3_fonte = font.Font(family="Times New Roman", size=11, weight="bold")
    botaoVoltar = Button(janela3, text="VOLTAR", command=lambda: voltarJanelaDoMenu(janela3, janela),
                         font=botaoV3_fonte, bg="black", fg="red")
    botaoVoltar.place(x=0, y=0)
    janela3.protocol("WM_DELETE_WINDOW", lambda: fechar_jogo(janela))
# FUNÇÃO VOLTAR AO MENU
def voltarJanelaDoMenu(janela3, janela):
    mixer.music.stop()
    janela3.destroy()
    janela.deiconify()
    menuMusica()
    janela.focus_set()