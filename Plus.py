    # metodosDoControleRemoto:
    # - PassarDeCanal
    # - MexerNoVolume
    # - AbrirANetflix
    # - DesligarATV

class ControleRemoto:
    def __init__(self, color, altura, profundidade, largura, material) -> None:
        self.color = color
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
        self.material = material

    def Passar_Canal(self, botao):
        if botao == "+":
            print("Aumentar o canal")
        elif botao == "-":
            print("Diminuir canal")
                        
controle_Remoto = ControleRemoto("Black", "10cm", "2cm", "2cm", "plastico")
print(controle_Remoto.color)
controle_Remoto.Passar_Canal("-")

controle_Remoto2 = ControleRemoto("Cinza", "10cm", "2cm", "2cm", "plastico")
print(controle_Remoto2.color)