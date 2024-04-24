class caneca():
    formato = "Cilíndrico, com alça"

    def __init__(self, nome, logo, cor, status) -> None:
        self.logo = logo
        self.cor = cor
        self.nome = nome
        self.status_disponíveis = ["Cheia", "Vazia"]
        self.status = status
        
    def encher(self):
        if self.status in self.status_disponíveis and self.status == "Vazia":
            self.status = "Cheia"
            print("A caneca está cheia agora")
        else:
            print("já está cheia")


    def beber(self):
        print(f"Estou bebendo da caneca: {self.nome}")
        self.status = "Vazia"
        print(f"A caneca: {self.nome} agora está: {self.status}")

class CanecaLondrina(caneca):
    def __init__(self) -> None:
        self.nome = "Caneca Londrina"
        self.logo = "Cidade de Londres"
        self.cor = "Branca"
        self.status = "Vazia"
        self.bebida = "Chá"

caneca1 = caneca("Canequinha", "Logo", "Branca", "Cheia")
caneca2 = CanecaLondrina()
caneca3 = caneca("Caneca ByLearner", "Foguete da ByLearn", "Branca", "Cheia")

print(f"A caneca: {caneca2.nome}, possui a logo: {caneca2.logo}")
print(f"A caneca: {caneca3.nome}, possui a logo: {caneca3.logo}")

print(caneca1.status)

caneca3.beber()
caneca3.encher()

caneca2.beber()