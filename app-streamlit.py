import numpy as np
import streamlit as st

from backtrack_sodoku import exemplo_sodoku
from branch_and_bound_mochila import exemplo_branch_and_bound


# Exibe Documentos
def exibir_arquivo_md(nome_arquivo):
    try:
        with open(nome_arquivo, 'r',encoding='utf-8') as arquivo:
            conteudo = str(arquivo.read())
            return conteudo
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return ""
    
# Monta Tela Inicial        
def main():
    st.set_page_config(page_title="Sudoku Solver", layout="wide")    
    st.title("Exemplos de Algoritmos")
    menu = ["Introdução"
            ,"Sobre Backtraking"
            , "Implementação Backtraking"
            , "Exemplo Backtraking"           
            , "Sobre Branch and Bound"
            , "Implementação Branch and Bound"
            , "Exemplo Branch and Bound"
            ]
    with st.sidebar:
        st.markdown("""
### Instituto de Computação – Universidade Federal da Bahia (UFBA)
* Diciplina: Introdução a Algoritmos
* Professor: Professor Felipe Fernandes
        """)
    choice = st.sidebar.selectbox("Menu", menu)    
    # Using object notation    
    if choice == "Sobre Backtraking":
        st.markdown(exibir_arquivo_md("sobre_backtracking.md"))
    elif choice == "introdução":
        st.markdown(exibir_arquivo_md("introdução.md"))
    elif choice == "Implementação Backtraking":
        st.markdown(exibir_arquivo_md("sobre_implementação_backtracking.md"))
    elif choice == "Exemplo Backtraking":
        exemplo_sodoku()    
    elif choice == "Sobre Branch and Bound":
        st.markdown(exibir_arquivo_md("sobre_branch_and_bound.md"))
    elif choice == "Implementação Branch and Bound":
        st.markdown(exibir_arquivo_md("sobre_implementação_branch_and_bound.md"))
    elif choice == "Exemplo Branch and Bound":
        exemplo_branch_and_bound()
    else:
        st.markdown(exibir_arquivo_md("introdução.md"))
    with st.sidebar:
        st.markdown("""
### Grupo 03
- Jorge Santos Nery Filho 
- Napoleão José Da Conceição Santana 
- Wesley Silva das Virgens
- Vitor Ferreira Trioschi Guerra
- Juliana Maria Oliveira dos Santos
        """)

if __name__ == "__main__":
    main()

