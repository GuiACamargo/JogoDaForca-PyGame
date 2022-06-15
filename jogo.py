#Feito por Guilherme Albani Camargo

import pygame

import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox

pygame.init()

#---------Cores---------
rosa95 = (255, 230, 255)
rosa90 = (255, 204, 255)
rosa80 = (255, 153, 255)
rosa70 = (255, 102, 255)
rosa60 = (255, 51, 255)
rosa50 = (255, 0, 255)
rosa40 = (204, 0, 204)
rosa30 = (153, 0, 153)
rosa15 = (77, 0, 77)
preto = (0, 0, 0)
branco = (255, 255, 255)
#<<---------Cores--------->>

#---------Alguns Setups do Pygame---------
pygameDisplay = pygame.display
pygameDisplay.set_caption("Jogo da Forca")
gameDisplay = pygameDisplay.set_mode((1440, 840))
gameEvents = pygame.event
clock = pygame.time.Clock()
gameIcon = pygame.image.load("favicon.ico")
pygameDisplay.set_icon(gameIcon)
#<<---------Alguns Setups do Pygame--------->>

#---------Widgets Functions---------
alfabetoCompleto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"]

def outputDesafiante():
    if textboxDesafiante.getText() != "":
        textboxDesafiante.hide()
        textboxTitleAcimaDesafiante.hide()
        textboxRegistraPalavraChave.show()
        textboxRegistraDica1.show()
        textboxRegistraDica2.show()
        textboxRegistraDica3.show()
        textboxTitleAcimaPalavraChave.show()
        textboxTitleAcimaDica1.show()
        textboxTitleAcimaDica2.show()
        textboxTitleAcimaDica3.show()
        textboxLog.setText("")
    else:
        textboxLog.setText("Não deixe os campos em branco/vazio!")

def outputCompetidor():
    if textboxCompetidor.getText() != "":
        textboxCompetidor.hide()
        textboxTitleAcimaCompetidor.hide()
        textboxLog.setText("")
    else:
        textboxLog.setText("Não deixe os campos em branco/vazio!")

def outputPalavraChave():
    if textboxRegistraPalavraChave.getText() != "":
        textboxRegistraPalavraChave.hide()
        textboxTitleAcimaPalavraChave.hide()
        palavraChave = textboxRegistraPalavraChave.getText().upper()
        asteriscos = list("_" * len(palavraChave))
        textboxAdivinharAPalavra.setText(" ".join(asteriscos))
        textboxLog.setText("")
    else:
        textboxLog.setText("Não deixe os campos em branco/vazio!")
        

errado = []
certo = []
tickets = [1]

def outputChute(text):
    ###Confere se tudo foi registrado  
    if textboxRegistraPalavraChave.getText() != "" and textboxRegistraDica1.getText() != "" and textboxRegistraDica2.getText() != "" and textboxRegistraDica3.getText() != "" and textboxCompetidor.getText() != "":
        ###Se ouver menos que cinco erros e ainda falta letras para completar a palavra
        if len(errado) < 5 and certo != list(dict.fromkeys(list(textboxRegistraPalavraChave.getText().upper()))):
            textboxLog.setText("")
            ###Coloca a palavra chave em letra maiúscula e separa as letras em listas
            palavraChave = textboxRegistraPalavraChave.getText().upper()
            palavraChave = list(textboxRegistraPalavraChave.getText().upper())
            jaEstaEmErrado = False
            ###Confere se a letra enviada ja está na lista de letras erradas, ou na lista das letras da palavra chave e passa para o proximo sprite do meteoro   
            if text in errado:
                jaEstaEmErrado = True
            if text in palavraChave:
                certo.append(text)
            elif (jaEstaEmErrado == False):
                arrayContadorMeteoro.append(1)
                errado.append(text)     
            
            ###Lógica para o requerimento de dicas
            textboxLetrasErradas.setText(", ".join(errado))
            if tickets.count(1) == 1:
                tickets.remove(1)
            if tickets.count(2) == 1 and tickets.count(1) == 0:
                tickets.remove(2)
            if tickets.count(3) == 1 and tickets.count(2) == 0:
                tickets.remove(3)
            
            #Monta a palavra utilizando o "_" para mostrar quantas letras tem
            textboxAdivinharAPalavra.setText("")
            for letra in palavraChave:
                if letra in certo:
                    textboxAdivinharAPalavra.setText(textboxAdivinharAPalavra.getText() + letra)
                else:
                    textboxAdivinharAPalavra.setText(textboxAdivinharAPalavra.getText() + "_ ")

        ###Se a lista de letras certas for igual a lista das letras da palavra certa, o competidor ganha            
        elif all(item in certo for item in list(dict.fromkeys(list(textboxRegistraPalavraChave.getText().upper())))):
            textboxGanhador.setText("VENCEDOR: " + textboxCompetidor.getText())
            textboxGanhador.show()
            textboxHistorico.show()
            textboxTitleAcimaHistorico.show()
            arquivo = open("registros/banco.txt", "a")
            arquivo.write("Palavra: " + textboxRegistraPalavraChave.getText() + " - Vencedor: Competidor " + textboxCompetidor.getText() + ", Perdedor: Desafiante " + textboxDesafiante.getText() + "\n")
            arquivo.close()
            arquivoR = open("registros/banco.txt", "r")
            linhasArquivo = arquivoR.readlines()
            ultimaLinha = linhasArquivo[len(linhasArquivo) - 2]
            textboxHistorico.setText(ultimaLinha)
            arquivoR.close()

        ###Se a lista de letras certas não for igual a lista das letras da palavra certa, o desafiante ganha
        else:
            errado.append(text)
            textboxGanhador.setText("VENCEDOR: " + textboxDesafiante.getText())
            textboxGanhador.show()
            textboxHistorico.show()
            textboxTitleAcimaHistorico.show()
            arquivo = open("registros/banco.txt", "a")
            arquivo.write("Palavra: " + textboxRegistraPalavraChave.getText() + " - Vencedor: Desafiante " + textboxDesafiante.getText() + ", Perdedor: Competidor " + textboxCompetidor.getText() + "\n")
            arquivo.close()
            arquivoR = open("registros/banco.txt", "r")
            linhasArquivo = arquivoR.readlines()
            ultimaLinha = linhasArquivo[len(linhasArquivo) - 2]
            textboxHistorico.setText(ultimaLinha)
            arquivoR.close()
    ###Avisa no Log de Erros do usuário se faltou preencher algum campo    
    else:
        textboxLog.setText("Preencha todos os campos! (Não deixe vazio!)")

def outputDica1():
    if textboxRegistraDica1.getText() != "":
        textboxRegistraDica1.hide()
        textboxTitleAcimaDica1.hide()
        textboxLog.setText("")
    else:
        textboxLog.setText("Não deixe os campos em branco/vazio!")

def outputDica2():
    if textboxRegistraDica2.getText() != "":
        textboxRegistraDica2.hide()
        textboxTitleAcimaDica2.hide()
        textboxLog.setText("")
    else:
        textboxLog.setText("Não deixe os campos em branco/vazio!")

def outputDica3():
    if textboxRegistraDica3.getText() != "":
        textboxRegistraDica3.hide()
        textboxTitleAcimaDica3.hide()
        textboxLog.setText("")
    else:
        textboxLog.setText("Não deixe os campos em branco/vazio!")

naoPodeJogarNovamenteDica1 = []
naoPodeJogarNovamenteDica2 = []
naoPodeJogarNovamenteDica3 = []
##---------Dicas---------
###Uso de array como método de True ou False (count)
def outputBotaoDica1(textboxRegistraDica, textboxApresentaDicas, log):
    if textboxRegistraDica.getText() != "" and tickets.count(1) == 0 and naoPodeJogarNovamenteDica1.count(5) == 0:
        textboxApresentaDicas.setText("Dica 1: " + textboxRegistraDica.getText().upper())
        log.setText("")
        if naoPodeJogarNovamenteDica1.count(5) == 0:
            naoPodeJogarNovamenteDica1.append(5)
        if tickets.count(2) == 0:
            tickets.append(2)
    elif textboxRegistraDica.getText() == "":
        log.setText("Dica 1 não registrada!")
    elif naoPodeJogarNovamenteDica1.count(5) != 0 and naoPodeJogarNovamenteDica2.count(5) == 0:
        log.setText("Dica 1 já pedida, jogue 1 vez para pedir Dica 2!")
    elif naoPodeJogarNovamenteDica1.count(5) != 0 and naoPodeJogarNovamenteDica2.count(5) != 0:
        log.setText("Dica 1 já pedida!")
    else:
        log.setText("Jogue uma vez para pedir Dica 1!")

def outputBotaoDica2(textboxRegistraDica, textboxApresentaDicas, log):
    if textboxRegistraDica.getText() != "" and tickets.count(2) == 0 and tickets.count(1) == 0 and naoPodeJogarNovamenteDica2.count(5) == 0:
        textboxApresentaDicas.setText("Dica 2: " + textboxRegistraDica.getText().upper())
        log.setText("")
        if naoPodeJogarNovamenteDica2.count(5) == 0:
            naoPodeJogarNovamenteDica2.append(5)
        if tickets.count(3) == 0:
            tickets.append(3)
    elif textboxRegistraDica.getText() == "":
        log.setText("Dica 2 não registrada!")
    elif naoPodeJogarNovamenteDica2.count(5) != 0 and naoPodeJogarNovamenteDica3.count(5) == 0:
        log.setText("Dica 2 já pedida, jogue 1 vez para pedir Dica 3!")
    elif naoPodeJogarNovamenteDica1.count(5) != 0 and naoPodeJogarNovamenteDica3.count(5) != 0:
        log.setText("Dica 2 já pedida!")


def outputBotaoDica3(textboxRegistraDica, textboxApresentaDicas, log):
    if textboxRegistraDica.getText() != "" and tickets.count(3) == 0 and tickets.count(2) == 0 and tickets.count(1) == 0 and naoPodeJogarNovamenteDica3.count(5) == 0:
        textboxApresentaDicas.setText("Dica 3: " + textboxRegistraDica.getText().upper())
        log.setText("")
        if naoPodeJogarNovamenteDica3.count(5) == 0:
            naoPodeJogarNovamenteDica3.append(5)
    elif textboxRegistraDica.getText() == "":
        log.setText("Dica 3 não registrada!")
    elif naoPodeJogarNovamenteDica3.count(5) != 0:
        log.setText("Dica 3 já pedida!")
##<<---------Dicas--------->>

def outputBotaoSair():
    quit()

def outputBotaoReiniciar():
    jogo()

def criarBotaoDica1(x, texto):
    Button(
    gameDisplay,
    x,
    260,
    160,  # Largura
    60,  # Altura

    text = texto,
    fontSize = 36,
    margin = 20,
    inactiveColour = rosa30,
    hoverColour = rosa70,
    pressedColour = rosa40,
    radius = 15,
    shadowDistance = 5,
    
    shadowColour = rosa15,
    textHAlign = "centre",
    textVAlign = "centre",
    textColour = rosa95,
    onClick = lambda: outputBotaoDica1(textboxRegistraDica1, textboxApresentaDicas, textboxLog)
    )

def criarBotaoDica2(x, texto):
    Button(
    gameDisplay,
    x,
    260,
    160,  # Largura
    60,  # Altura

    text = texto,
    fontSize = 36,
    margin = 20,
    inactiveColour = rosa30,
    hoverColour = rosa70,
    pressedColour = rosa40,
    radius = 15,
    shadowDistance = 5,
    
    shadowColour = rosa15,
    textHAlign = "centre",
    textVAlign = "centre",
    textColour = rosa95,
    onClick = lambda: outputBotaoDica2(textboxRegistraDica2, textboxApresentaDicas, textboxLog)
    )

def criarBotaoDica3(x, texto):
    Button(
    gameDisplay,
    x,
    260,
    160,  # Largura
    60,  # Altura

    text = texto,
    fontSize = 36,
    margin = 20,
    inactiveColour = rosa30,
    hoverColour = rosa70,
    pressedColour = rosa40,
    radius = 15,
    shadowDistance = 5,
    
    shadowColour = rosa15,
    textHAlign = "centre",
    textVAlign = "centre",
    textColour = rosa95,
    onClick = lambda: outputBotaoDica3(textboxRegistraDica3, textboxApresentaDicas, textboxLog)
    )

def criarBotaoReiniciar(x, y, texto):
    Button(
    gameDisplay,
    x,
    y,
    130,  # Largura
    50,  # Altura

    text = texto,
    fontSize = 32,
    margin = 20,
    inactiveColour = (202, 155, 204),
    hoverColour = rosa90,
    pressedColour = rosa80,
    radius = 15,
    shadowDistance = 5,
    shadowColour = rosa15,
    textHAlign = "centre",
    textVAlign = "centre",
    textColour = rosa15,
    onClick = lambda: outputBotaoReiniciar()
    )

def criarBotaoSair(x, y, texto):
    Button(
    gameDisplay,
    x,
    y,
    130,  # Largura
    50,  # Altura

    text = texto,
    fontSize = 32,
    margin = 20,
    inactiveColour = (202, 155, 204),
    hoverColour = rosa90,
    pressedColour = rosa80,
    radius = 15,
    shadowDistance = 5,
    shadowColour = rosa15,
    textHAlign = "centre",
    textVAlign = "centre",
    textColour = rosa15,
    onClick = lambda: outputBotaoSair()
    )

def criarBotao(x, y, texto):
    Button(
    gameDisplay,
    x,
    y,
    80,  # Largura
    50,  # Altura

    text = texto,
    fontSize = 32,
    margin = 20,
    inactiveColour = rosa95,
    hoverColour = rosa90,
    pressedColour = rosa80,
    radius = 15,
    shadowDistance = 5,
    shadowColour = rosa15,
    textHAlign = "centre",
    textVAlign = "centre",
    textColour = rosa15,
    onClick = lambda: outputChute(texto)
    )

def listagemBotoes(alfabeto, posicaoY):
    posicaoBotaoX = 800
    for letras in alfabeto:
        criarBotao(posicaoBotaoX, posicaoY, letras)
        posicaoBotaoX = posicaoBotaoX + 100
#<<---------Widgets Functions--------->>

#---------Botões---------
alfabeto1 = ["A", "B", "C", "D", "E", "F"]
alfabeto2 = ["G", "H", "I", "J", "K", "L"]
alfabeto3 = ["M", "N", "O", "P", "Q", "R"]
alfabeto4 = ["S", "T", "U", "V", "W", "X"]

listagemBotoes(alfabeto1, 345)
listagemBotoes(alfabeto2, 415)
listagemBotoes(alfabeto3, 485)
listagemBotoes(alfabeto4, 555)
criarBotao(1000, 625, "Y")
criarBotao(1100, 625, "Z")

criarBotaoDica1(815, "Dica 1")
criarBotaoDica2(1008, "Dica 2")
criarBotaoDica3(1201, "Dica 3")

criarBotaoReiniciar(725, 750, "REINICIAR")
criarBotaoSair(865, 750, "SAIR")
#<<---------Botões--------->>

#---------Textos---------
#Nomes dos jogadores
textboxDesafiante = TextBox(gameDisplay, 790, 185, 270, 50, fontSize = 36, borderColour = rosa40,
                    textColour = rosa15, onSubmit = outputDesafiante, radius = -10, borderThickness = 5, colour = rosa95)

textboxCompetidor = TextBox(gameDisplay, 1120, 185, 270, 50, fontSize = 36, borderColour = rosa40,
                    textColour = rosa15, onSubmit = outputCompetidor, radius = -10, borderThickness = 5, colour = rosa95)
                    
textboxTitleAcimaDesafiante = TextBox(gameDisplay, 800, 147, 250, 35, fontSize = 28, borderColour = rosa30,
                    textColour = rosa15, radius = 13, borderThickness = 4, colour = rosa90)

textboxTitleAcimaCompetidor = TextBox(gameDisplay, 1130, 147, 250, 35, fontSize = 28, borderColour = rosa30,
                    textColour = rosa15, radius = 13, borderThickness = 4, colour = rosa90)

textboxGanhador = TextBox(gameDisplay, 40, 10, 1360, 165, fontSize = 120, borderColour = (29, 11, 46),
                    textColour = rosa95, radius = 30, borderThickness = 15, colour = (52, 39, 64))
#FIM / Nomes dos jogadores

#PopUp para o desafiante preencher
textboxRegistraPalavraChave = TextBox(gameDisplay, 500, 110, 260, 30, fontSize = 24, borderColour = rosa15,
                    textColour = rosa30, onSubmit = outputPalavraChave, radius = 10, borderThickness = 3, colour = rosa95)

textboxRegistraDica1 = TextBox(gameDisplay, 500, 160, 260, 30, fontSize = 24, borderColour = rosa15,
                    textColour = rosa30, onSubmit = outputDica1, radius = 10, borderThickness = 3, colour = rosa95)

textboxRegistraDica2 = TextBox(gameDisplay, 500, 210, 260, 30, fontSize = 24, borderColour = rosa15,
                    textColour = rosa30, onSubmit = outputDica2, radius = 10, borderThickness = 3, colour = rosa95)

textboxRegistraDica3 = TextBox(gameDisplay, 500, 260, 260, 30, fontSize = 24, borderColour = rosa15,
                    textColour = rosa30, onSubmit = outputDica3, radius = 10, borderThickness = 3, colour = rosa95)

textboxTitleAcimaPalavraChave = TextBox(gameDisplay, 528, 93, 200, 20, fontSize = 17, borderColour = preto,
                    textColour = rosa30, radius = 3, borderThickness = 3, colour = rosa95)

textboxTitleAcimaDica1 = TextBox(gameDisplay, 528, 143, 200, 20, fontSize = 17, borderColour = preto,
                    textColour = rosa30, radius = 3, borderThickness = 3, colour = rosa95)

textboxTitleAcimaDica2 = TextBox(gameDisplay, 528, 193, 200, 20, fontSize = 17, borderColour = preto,
                    textColour = rosa30, radius = 3, borderThickness = 3, colour = rosa95)

textboxTitleAcimaDica3 = TextBox(gameDisplay, 528, 243, 200, 20, fontSize = 17, borderColour = preto,
                    textColour = rosa30, radius = 3, borderThickness = 3, colour = rosa95)
#FIM / PopUp para o desafiante preencher

#Campo onde a palavra vai sendo completada e a dica
textboxAdivinharAPalavra = TextBox(gameDisplay, 105, 410, 550, 65, fontSize = 45, borderColour = (29, 11, 46),
                    textColour = rosa95, radius = 10, borderThickness = 5, colour = (52, 39, 64))

textboxApresentaDicas = TextBox(gameDisplay, 155, 505, 450, 50, fontSize = 30, borderColour = (29, 11, 46),
                    textColour = rosa95, radius = 10, borderThickness = 5, colour = (78, 56, 98))

textboxTitleAcimaApresentaDicas = TextBox(gameDisplay, 275, 490, 200, 30, fontSize = 26, borderColour = (29, 11, 46),
                    textColour = rosa95, radius = 10, borderThickness = 5, colour = (152, 90, 154))
#FIM / Campo onde a palavra vai sendo completada

#Campo onde aparece as letras chutadas erradas
textboxLetrasErradas = TextBox(gameDisplay, 40, 745, 680, 60, fontSize = 38, borderColour = (29, 11, 46),
                    textColour = rosa95, radius = 10, borderThickness = 5, colour = (152, 90, 154))

textboxTitleAcimaLetrasErradas = TextBox(gameDisplay, 40, 710, 200, 30, fontSize = 26, borderColour = (29, 11, 46),
                    textColour = rosa95, radius = 10, borderThickness = 5, colour = (152, 90, 154))
#FIM / Campo onde aparece as letras chutadas erradas

#Campo onde aparece os erros do usuário
textboxLog = TextBox(gameDisplay, 1005, 745, 400, 60, fontSize = 26, borderColour = (29, 11, 46),
                    textColour = rosa95, radius = 10, borderThickness = 5, colour = (152, 90, 154))

textboxTitleAcimaLog = TextBox(gameDisplay, 1175, 710, 225, 30, fontSize = 26, borderColour = (29, 11, 46),
                    textColour = rosa95, radius = 10, borderThickness = 5, colour = (152, 90, 154))
#FIM / Campo onde aparece os erros do usuário

#Campo do histórico
textboxHistorico = TextBox(gameDisplay, 55, 600, 650, 60, fontSize = 24, borderColour = (29, 11, 46),
                    textColour = rosa15, radius = 10, borderThickness = 3, colour = (rosa80))

textboxTitleAcimaHistorico = TextBox(gameDisplay, 275, 585, 200, 30, fontSize = 26, borderColour = (29, 11, 46),
                    textColour = rosa95, radius = 10, borderThickness = 4, colour = (152, 90, 154))
#FIM / Campo do histórico
#<<---------Textos--------->>

#---------Título---------
fontTitulo = pygame.font.SysFont('freesansbold.ttf', 70)
imgFontTitulo = fontTitulo.render("Jogo da Forca (Salve o Planeta)", True, rosa90)
#<<---------Título--------->>

#---------Imagens---------
tamanhoBg = (1440, 960)
bg = pygame.image.load("assets/fundo.png")
bg = pygame.transform.scale(bg, tamanhoBg)

tamanhoPlaneta = (180, 180)
planeta = pygame.image.load("assets/planetaRoxo.png")
planeta = pygame.transform.scale(planeta, tamanhoPlaneta)

tamanhoExplosao = (620, 550)
explosao = pygame.image.load("assets/explosao.png")
explosao = pygame.transform.scale(explosao, tamanhoExplosao)

imagensMeteoro = []
for i in range(1, 6):
    imgMeteoro = pygame.image.load("assets/meteoro" + str(i) + ".png")
    imagensMeteoro.append(imgMeteoro)

imagensMeteoro[0] = pygame.transform.rotate(imagensMeteoro[0], 180.0)
imagensMeteoro[0] = pygame.transform.scale(imagensMeteoro[0], (60, 60))
imagensMeteoro[1] = pygame.transform.flip(imagensMeteoro[1], True, False)
imagensMeteoro[2] = pygame.transform.flip(imagensMeteoro[2], True, False)
imagensMeteoro[3] = pygame.transform.flip(imagensMeteoro[3], True, False)
imagensMeteoro[4] = pygame.transform.flip(imagensMeteoro[4], True, False)
imagensMeteoro[4] = pygame.transform.scale(imagensMeteoro[4], (165, 160))
imagensMeteoro.append(pygame.image.load("assets/meteoro5.png"))
imagensMeteoro[5] = pygame.transform.flip(imagensMeteoro[4], True, False)
imagensMeteoro[5] = pygame.transform.scale(imagensMeteoro[4], (165, 160))


arrayContadorMeteoro = []
#<<---------Imagens--------->>

#---------Configurações das TextBox---------
textboxTitleAcimaDesafiante.disable()
textboxTitleAcimaCompetidor.disable()
textboxTitleAcimaPalavraChave.disable()
textboxTitleAcimaDica1.disable()
textboxTitleAcimaDica2.disable()
textboxTitleAcimaDica3.disable()
textboxAdivinharAPalavra.disable()
textboxApresentaDicas.disable()
textboxTitleAcimaApresentaDicas.disable()
textboxLetrasErradas.disable()
textboxTitleAcimaLetrasErradas.disable()
textboxLog.disable()
textboxTitleAcimaLog.disable()
textboxGanhador.disable()
textboxHistorico.disable()
textboxTitleAcimaHistorico.disable()

textboxRegistraPalavraChave.hide()
textboxRegistraDica1.hide()
textboxRegistraDica2.hide()
textboxRegistraDica3.hide()
textboxTitleAcimaPalavraChave.hide()
textboxTitleAcimaDica1.hide()
textboxTitleAcimaDica2.hide()
textboxTitleAcimaDica3.hide()
textboxGanhador.hide()
textboxHistorico.hide()
textboxTitleAcimaHistorico.hide()

textboxTitleAcimaApresentaDicas.setText("          Dica Atual")
textboxTitleAcimaLetrasErradas.setText(" Letras Erradas: ")
textboxTitleAcimaDesafiante.setText("     Nome do Desafiante")
textboxTitleAcimaCompetidor.setText("    Nome do Competidor")
textboxTitleAcimaPalavraChave.setText("                   Palavra-Chave")
textboxTitleAcimaDica1.setText("                          Dica 1")
textboxTitleAcimaDica2.setText("                          Dica 2")
textboxTitleAcimaDica3.setText("                          Dica 3")
textboxTitleAcimaLog.setText(" Log de Erros do Usuário:")
textboxTitleAcimaHistorico.setText("   Último Histórico")
#<<---------Configurações das TextBox---------

#---------Jogo---------
def jogo():
    textboxRegistraPalavraChave.hide()
    textboxRegistraDica1.hide()
    textboxRegistraDica2.hide()
    textboxRegistraDica3.hide()
    textboxTitleAcimaPalavraChave.hide()
    textboxTitleAcimaDica1.hide()
    textboxTitleAcimaDica2.hide()
    textboxTitleAcimaDica3.hide()
    textboxDesafiante.show()
    textboxCompetidor.show()
    textboxTitleAcimaCompetidor.show()
    textboxTitleAcimaDesafiante.show()
    textboxRegistraDica1.setText("")
    textboxRegistraDica2.setText("")
    textboxRegistraDica3.setText("")
    textboxLog.setText("")
    textboxRegistraPalavraChave.setText("")
    textboxHistorico.setText("")
    textboxCompetidor.setText("")
    textboxDesafiante.setText("")
    textboxLog.setText("")
    textboxLetrasErradas.setText("")
    textboxApresentaDicas.setText("")
    textboxGanhador.setText("")
    naoPodeJogarNovamenteDica1.clear()
    naoPodeJogarNovamenteDica2.clear()
    naoPodeJogarNovamenteDica3.clear()
    errado.clear()
    certo.clear()
    tickets.clear()
    tickets.append(1)
    arrayContadorMeteoro.clear()
    errado.clear()
    certo.clear()
    naoPodeJogarNovamenteDica1.clear()
    naoPodeJogarNovamenteDica2.clear()
    naoPodeJogarNovamenteDica3.clear()
    textboxAdivinharAPalavra.setText("")
    textboxGanhador.hide()
    textboxTitleAcimaHistorico.hide()
    textboxHistorico.hide()

run = True
while run:
    statusMeteoro = len(arrayContadorMeteoro)
    clock.tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                jogo()
                pygameDisplay.update()

    gameDisplay.blit(bg, (0, 0))
    gameDisplay.blit(imagensMeteoro[statusMeteoro], (210, 165))
    gameDisplay.blit(planeta, (365, 215))  
    if statusMeteoro == 5:
        textboxGanhador.setText("VENCEDOR: " + textboxDesafiante.getText())
        textboxGanhador.show()
        gameDisplay.blit(explosao, (200, 65))
    gameDisplay.blit(imgFontTitulo, (390, 30))
    pygame_widgets.update(events)
    pygameDisplay.update()

#<<---------Jogo--------->>