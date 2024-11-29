from pygame import init, mixer
from modulos import *

# MUSICA MENU
def menuMusica():
    global menuMusica
    init()
    mixer.music.load('CDZ.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play()
    #    duracao = MP3('cdz.mp3').info.length
    #    Timer(duracao, menuMusica).start()
# MUSICA REGRAS
def regrasMusica():
    init()
    mixer.music.load('NRT_BIRD.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play()
    #     duracao = MP3('ns.mp3').info.length
    #     Timer(duracao, regrasMusica).start()
# MUSICA INTRODUCAO
def introducaoMusica():
    init()
    mixer.music.load('DBZ.mp3')
    mixer.music.set_volume(0.4)
    mixer.music.play()
    #     duracao = MP3('dbz.mp3').info.length
    #     Timer(duracao, introducaoMusica).start()
# MUSICA DIONISO
def dionisioMusica():
    init()
    mixer.music.load('NRT.mp3')
    mixer.music.set_volume(0.3)
    mixer.music.play()
    #    duracao = MP3('yh.mp3').info.length
    #    Timer(duracao, dionisioMusica).start()

# MUSICA APOLO
def apoloMusica():
    init()
    mixer.music.load('YYH.mp3')
    mixer.music.set_volume(0.3)
    mixer.music.play()
# MUSICA ARTEMIS

def artemisMusica():
    init()
    mixer.music.load('chala.mp3')
    mixer.music.set_volume(0.3)
    mixer.music.play()
