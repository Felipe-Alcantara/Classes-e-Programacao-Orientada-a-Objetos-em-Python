from classes import Vendedor  # Importação da classe Vendedor do arquivo 'classes'

vendas = 1000  # Definição do número total de vendas
meta = 500  # Definição da meta de vendas

if vendas >= meta:  # Verificação se o número total de vendas é maior ou igual à meta
    print("bateu a meta")  # Impressão da mensagem "bateu a meta" se a condição for verdadeira
else:
    print("Não bateu a meta")  # Impressão da mensagem "Não bateu a meta" se a condição for falsa

Vendedor1 = Vendedor("Lira")  # Instanciação de um objeto da classe Vendedor com o nome "Lira"
Vendedor1.Vendeu(1000)  # Chamada do método Vendeu do objeto Vendedor1 com o número de vendas como argumento
Vendedor1.bateu(600)  # Chamada do método bateu do objeto Vendedor1 com a meta como argumento

print(Vendedor1.nome)  # Impressão do nome do vendedor associado ao objeto Vendedor1

Vendedor2 = Vendedor("Alon")  # Instanciação de um objeto da classe Vendedor com o nome "Alon"
Vendedor2.Vendeu(600)  # Chamada do método Vendeu do objeto Vendedor2 com o número de vendas como argumento
Vendedor2.bateu(600)  # Chamada do método bateu do objeto Vendedor2 com a meta como argumento
