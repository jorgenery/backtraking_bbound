import streamlit as st


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

class Item:
    def __init__(self, id, peso, valor):
        self.id = id
        self.peso = peso
        self.valor = valor

def exemplo_branch_and_bound():
    st.title("Problema da Mochila")

    num_items = st.number_input("Numero de Itens:", min_value=1, value=4)
    capacidade = st.number_input("Capacidade Mochila:", min_value=1, value=10)

    items = []
    for i in range(num_items):
        id = i + 1
        peso = st.number_input(f"Peso Item {id}:", min_value=1)
        valor = st.number_input(f"Valor do Item {id}:", min_value=1)
        items.append(Item(id, peso, valor))

    if st.button("Resolver"):
        peso_mochila, valor_mochila, items_selecionados = mochila_dynamic(items, capacidade)
        st.write("----")
        st.write(f"## Peso da Mochila = {peso_mochila} Kg")
        st.write(f"## Valor na Mochila = {valor_mochila}")        
        st.write("### Itens Selecionados:")
        for item in items_selecionados:
            st.write(f"- Item {item.id} (Peso: {item.peso}, Valor: {item.valor})")
        st.write("----")