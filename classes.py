class Vendedor():
    def __init__(self, nome):  # Definição do método de inicialização (__init__) da classe Vendedor
        self.nome = nome  # Atribuição do nome do vendedor ao atributo 'nome' da instância
        self.vendas = 0  # Inicialização do atributo 'vendas' com o valor zero
    
    def Vendeu(self, vendas):  # Definição do método 'Vendeu' da classe Vendedor
        self.vendas = vendas  # Atribuição do número de vendas fornecido ao atributo 'vendas' da instância
    
    def bateu(self, meta):  # Definição do método 'bateu' da classe Vendedor
        if self.vendas >= meta:  # Verificação se o número de vendas é maior ou igual à meta
            print(self.nome, "Bateu a meta")  # Impressão do nome do vendedor seguido da mensagem "Bateu a meta" caso ele tenha atingido ou ultrapassado a meta
        else:
            print(self.nome, "Não bateu")  # Impressão do nome do vendedor seguido da mensagem "Não bateu" caso ele não tenha atingido a meta