import sys


class tranformacao:
    def __init__(self, mensagem, primo):
        self.mensagem = mensagem
        self.primo = primo

    def transMensagem(self):
        mensagemByte = self.mensagem.encode() #transforma pra byte
        mensagemInt = int.from_bytes(mensagemByte, "big") #tranforma de byte pra int
        mensagemBin = bin(mensagemInt) #tranformar em binario
        mensagemBin = mensagemBin[2:] #retirar a representaçao de binario
        primoBin = bin(self.primo)
        primoBin = primoBin[2:] #retirar a representaçao de binario
        return mensagemBin, primoBin

class mensagemClass():

    def __init__(self, mensagemBin, primoBin):
        self.mensagemBin = mensagemBin
        self.primoBin = primoBin

    def divMensagem(self):
        tamPrimo = len(self.primoBin)
        lista = []
        tamLista = len(self.mensagemBin)
        #achar o mod pra preencher com 0 na esquerda
        mod = tamLista % tamPrimo
        completar = tamPrimo - mod

        #encontrar a quantidade de iteracoes
        tamLista = (tamLista + completar)/tamPrimo
        tamLista = int(tamLista)

        #tranformar em string para trabalhar mais facil
        self.mensagemBin = str(self.mensagemBin)

        #completa a esquerda com 0
        self.mensagemBin = (completar*'0') + self.mensagemBin

        #separa a string com a mensagem em binario em uma lista
        for i in range (tamLista):
            lista.append(self.mensagemBin[0:tamPrimo])
            self.mensagemBin = self.mensagemBin[tamPrimo:]

        return lista




class curvaEliptca():
    def __init__ (self, lista):
        self.lista = lista


    def encontrarPontos(self):
        listaPontos = []
        qntLista = len(self.lista)
        print(qntLista)
        #quantidade de numeros na lista é par
        if((qntLista%2)==0):
            i = 0;
            while(i<qntLista):
                listaPontos.append([lista[i],lista[i+1]])
                i+=2

            return listaPontos


        else:
            print("impar")
            return self.lista


mensagem = "21"
primo = 7
lista = []
listaP = []

x = tranformacao(mensagem, primo)
mensagemBin, primoBin = x.transMensagem()

print(mensagemBin)

y = mensagemClass(mensagemBin, primoBin)
lista = y.divMensagem()

z = curvaEliptca(lista)
listaP = z.encontrarPontos()

print(listaP)
