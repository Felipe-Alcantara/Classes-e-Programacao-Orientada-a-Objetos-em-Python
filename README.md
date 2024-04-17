# Classes-e-Programacao-Orientada-a-Objetos-em-Python
 Esses dois códigos estão relacionados à gestão de vendas e avaliação de desempenho de vendedores. O primeiro define uma classe chamada Vendedor com métodos para registrar vendas e verificar se um vendedor atingiu uma meta específica. Já o segundo código instancia objetos dessa classe, simula vendas para esses vendedores e verifica se atingiram suas metas de vendas. Em resumo, esses códigos trabalham juntos para modelar o desempenho de vendedores em relação a metas de vendas.

## Descrição do Projeto

Este projeto consiste em um sistema simples de gestão de vendas e avaliação de desempenho de vendedores. O projeto é composto por dois arquivos:

### 1. `classes.py`

Este arquivo contém a definição de uma classe Python chamada `Vendedor`. A classe `Vendedor` possui os seguintes métodos:

- `__init__(self, nome)`: Este método inicializa um objeto `Vendedor` com um nome específico e define o número inicial de vendas como zero.
  
- `Vendeu(self, vendas)`: Este método atualiza o número de vendas de um vendedor para um valor especificado.
  
- `bateu(self, meta)`: Este método verifica se o número de vendas de um vendedor atingiu ou ultrapassou uma meta especificada. Ele imprime uma mensagem indicando se o vendedor atingiu a meta ou não.

### 2. `main.py`

Este arquivo contém o código principal que utiliza a classe `Vendedor` definida no arquivo `classes.py`. O código realiza as seguintes operações:

1. Define o número total de vendas (`vendas`) e uma meta de vendas (`meta`).
  
2. Verifica se o número total de vendas atingiu ou ultrapassou a meta e imprime uma mensagem correspondente.

3. Instancia dois objetos da classe `Vendedor`, atribui vendas específicas a cada um e verifica se cada vendedor atingiu a meta.

Este projeto pode ser útil em várias situações, especialmente para empresas que desejam acompanhar o desempenho de seus vendedores e garantir que eles atinjam suas metas de vendas. Algumas maneiras pelas quais esse projeto pode ser útil incluem:

1. **Avaliação de Desempenho**: Permite avaliar objetivamente o desempenho de cada vendedor em relação às metas de vendas estabelecidas.

2. **Identificação de Vendedores de Destaque**: Ajuda a identificar vendedores que consistentemente superam suas metas de vendas, reconhecendo e recompensando seu bom desempenho.

3. **Planejamento de Recursos**: Facilita o planejamento de recursos e estratégias de vendas com base no desempenho histórico dos vendedores.

4. **Motivação da Equipe**: Serve como uma ferramenta de motivação para a equipe de vendas, incentivando-os a trabalhar em direção às metas estabelecidas.

5. **Tomada de Decisões**: Fornece insights valiosos para a tomada de decisões relacionadas à alocação de recursos, treinamento de pessoal e definição de novas metas.

Este projeto pode ajudar as empresas a otimizar suas operações de vendas, melhorar o desempenho da equipe e alcançar maior sucesso comercial.