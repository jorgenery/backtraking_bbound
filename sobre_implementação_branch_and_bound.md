## Implementação
Vamos considerar abaixo o problema da mochila 0/1 para entender Branch and Bound. 

### Parâmetros
items: Uma lista de objetos da classe Item, onde cada objeto representa um item com peso e valor.
capacidade: A capacidade total da mochila.

### Objetivo
O objetivo é encontrar a combinação de itens que maximiza o valor total na mochila, sem exceder a capacidade.

### Teste de Validação
Se chegarmos a um ponto em que uma solução já não é viável, não há necessidade de continuar a explorar Se o melhor na subárvore for pior que o melhor atual, podemos simplesmente ignorar este nó e suas subárvores

### Condição de Parada
Quando todos os itens são considerados e todas as capacidades possíveis são examinadas.

### Retorno
O retorno lista de itens da mochila

### Algoritmo:
        class Item:
            def __init__(self, id, peso, valor):
                self.id = id
                self.peso = peso
                self.valor = valor

        def mochila_dynamic(items, capacidade):
            n = len(items)
            matriz_de_posibilidades = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]
            escolhido = [[False for _ in range(capacidade + 1)] for _ in range(n + 1)]

            for i in range(1, n + 1):
                for w in range(capacidade + 1):
                    if items[i - 1].peso <= w:
                        sem_este_item = matriz_de_posibilidades[i - 1][w]
                        com_este_item = matriz_de_posibilidades[i - 1][w - items[i - 1].peso] + items[i - 1].valor

                        if com_este_item > sem_este_item:
                            matriz_de_posibilidades[i][w] = com_este_item
                            escolhido[i][w] = True
                        else:
                            matriz_de_posibilidades[i][w] = sem_este_item
                    else:
                        matriz_de_posibilidades[i][w] = matriz_de_posibilidades[i - 1][w]

            items_escolhidos = []
            w = capacidade
            valor_na_mochila = 0
            peso_na_mochila = 0
            for i in range(n, 0, -1):
                if escolhido[i][w]:
                    items_escolhidos.append(items[i - 1])
                    valor_na_mochila = valor_na_mochila + items[i-1].valor
                    peso_na_mochila = peso_na_mochila + items[i-1].peso
                    w -= items[i - 1].peso

            return peso_na_mochila, valor_na_mochila, items_escolhidos