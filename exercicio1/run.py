class AndarInvalidoError(Exception):
    pass

class Elevador:
    def __init__(self, qntd_andares):
        self.quantidade = qntd_andares
        self.terreo = 1
        self.andar_atual = self.terreo

    def movimentar(self, andar):
        if andar <= self.quantidade and andar >= self.terreo:
            self.andar_atual = andar
            print(f"indo para {self.andar_atual} andar...")

        else:
            raise AndarInvalidoError("andar indisponivel!")
    
    def verificar_andar(self):
        if self.andar_atual == self.terreo:
            print("voce esta no terreo!")

        else:
            print(f"voce esta no {self.andar_atual} andar")

elev = Elevador(15)

while True:  
    try:
        print("^^^^^^^PAINEL DO ELEVADOR^^^^^^^")
        x = int(input("selecione o andar desejado: "))
        elev.movimentar(x)
        break
    except ValueError:
        print("caractere invalido! Selecione um andar de 1 a 15")

    except AndarInvalidoError as erro:
        print(erro)
        
