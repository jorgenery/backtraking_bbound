import numpy as np
import streamlit as st


# Valida condições do Sodoku
def numero_valido(tabuleiro, linha, coluna, valor):    
    # Verifica se o número não aparece na mesma linha, coluna ou subgrade
    for lc in range(9):
        if tabuleiro[linha][lc] == valor or tabuleiro[lc][coluna] == valor:
            return False
    # Verifica se já existe o numero no mesmo quadrante    
    linha_inicial, coluna_inicial = 3 * (linha // 3), 3 * (coluna // 3)
    for l in range(linha_inicial, linha_inicial + 3):
        for c in range(coluna_inicial, coluna_inicial + 3):
            if tabuleiro[l][c] == valor:
                return False
    return True

# Pega a Proxima Posição Vazia
def pega_vazio(tabuleiro):
    for l in range(9):
        for c in range(9):
            if tabuleiro[l][c] == 0:
                return l, c
    return None      

def pega_default():
    tabuleiro_default = dict()
    tabuleiro_default[(0,0)] = 1
    tabuleiro_default[(0,2)] = 7
    tabuleiro_default[(0,5)] = 6
    tabuleiro_default[(0,6)] = 4
    tabuleiro_default[(0,7)] = 5
    tabuleiro_default[(1,1)] = 2
    tabuleiro_default[(1,2)] = 5
    tabuleiro_default[(1,3)] = 3
    tabuleiro_default[(1,4)] = 4
    tabuleiro_default[(1,8)] = 8
    tabuleiro_default[(2,1)] = 6
    tabuleiro_default[(2,4)] = 1
    tabuleiro_default[(2,7)] = 7
    return tabuleiro_default
    

# Algoritmo backtracking que resolve o sodoku
def resolve_sudoku(tabuleiro):
    empty = pega_vazio(tabuleiro)
    if not empty:
        return True
    linha, coluna = empty
    for valor in range(1, 10):
        if numero_valido(tabuleiro, linha, coluna, valor):
            tabuleiro[linha][coluna] = valor
            if resolve_sudoku(tabuleiro):
                return True
            tabuleiro[linha][coluna] = 0
    return False
# Monta tela de Entrada do Sodoku
def exemplo_sodoku():        
    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)
    col_list = [col1, col2, col3, col4, col5, col6, col7, col8, col9]   
    tabuleiro = np.zeros((9, 9), dtype=int)
    tabuleiro_entradas = []
    st.header("Entrada de dados Sudoku")    
    # Sodoku Exemplo
    tabuleiro_default = pega_default()        
    c = -1
    tabuleiro_entradas = dict()
    for col in col_list:
        c = c + 1 
        with col:
            for l in range(9):
                default = 0
                if (l, c) in tabuleiro_default:
                    default = tabuleiro_default[(l,c)]
                tabuleiro_entradas[(l,c)]=st.number_input(label=" ", label_visibility = "hidden", min_value=0, max_value=9, value=default, key=(l, c))                
    resolve_button = st.button("Resolver Sudoku")        
    if resolve_button:
        tabuleiro_valido = True
        for l in range(9):
            for c in range(9):
                valor = tabuleiro_entradas[(l,c)]
                if valor>0 and not numero_valido(tabuleiro, l, c, valor):
                    tabuleiro_valido = False
                tabuleiro[l][c] = valor
                
        if tabuleiro_valido:
            if resolve_sudoku(tabuleiro):
                st.success("Sudoku solvido!")
            else:
                st.error("Não existe solução para este Sudoku.")
        else:
            st.error("Sodoku de Entrada Invalido.")

    st.write(tabuleiro)