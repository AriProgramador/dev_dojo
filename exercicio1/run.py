import os

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
    os.system("cls")  
    try:
        print("\n^^^^^^^PAINEL DO ELEVADOR^^^^^^^")
        print("1 - escolher andar\n2 - verificar andar\n3 - sair do elevador")
        opcao = int(input("escolha uma operacao: "))

        if opcao == 1:

            x = int(input("selecione o andar desejado: "))
            elev.movimentar(x)
        elif opcao == 2:
            x  = elev.verificar_andar()
        
        elif opcao == 3:
            print("saindo do elevador...")
            break
        else:
            print("operacao inexistente!")

    except ValueError:
        print("caractere invalido! Selecione um andar de 1 a 15\n")

    except AndarInvalidoError as erro:
        print(erro)
        
print(x)