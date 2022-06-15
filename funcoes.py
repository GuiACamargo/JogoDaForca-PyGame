
def permiteMostrarDicas(array):
    if array.count(1) == 1:
        array.remove(1)
    if array.count(2) == 1 and array.count(1) == 0:
        array.remove(2)
    if array.count(3) == 1 and array.count(2) == 0:
        array.remove(3)

def separaEntreCertoEErradoEMudaSpriteDoMeteoro(text, arrayErrado, arrayCerto, palavraChave, contador):
    jaEstaEmErrado = False
    if text in arrayErrado:
        jaEstaEmErrado = True
    if text in palavraChave:
        arrayCerto.append(text)
    elif (jaEstaEmErrado == False):
        contador.append(1)
        arrayErrado.append(text) 

def salvaCompetidorVitoria(palavraChave, nomeCompetidor, nomeDesafiante):
    arquivo = open("registros/banco.txt", "a")
    arquivo.write("Palavra: " + palavraChave + " - Vencedor: Competidor " + nomeCompetidor + ", Perdedor: Desafiante " + nomeDesafiante + "\n")
    arquivo.close()

def salvaDesafianteVitoria(palavraChave, nomeCompetidor, nomeDesafiante):
    arquivo = open("registros/banco.txt", "a")
    arquivo.write("Palavra: " + palavraChave + " - Vencedor: Desafiante " + nomeDesafiante + ", Perdedor: Competidor " + nomeCompetidor + "\n")
    arquivo.close()

def palavraChaveEmListaSemRepetirParaComparar(palavraChave):
    return list(dict.fromkeys(list(palavraChave.getText().upper())))

def listagemBotoes(alfabeto, posicaoY, funcaoBotao):
    posicaoBotaoX = 800
    for letras in alfabeto:
        funcaoBotao(posicaoBotaoX, posicaoY, letras)
        posicaoBotaoX = posicaoBotaoX + 100

def validaRegistros(palavraChave, Dica1, Dica2, Dica3, competidor):
    return palavraChave.getText() != "" and Dica1.getText() != "" and Dica2.getText() != "" and Dica3.getText() != "" and competidor.getText() != ""
    