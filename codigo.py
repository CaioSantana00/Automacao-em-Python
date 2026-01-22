# Blibliotecas necessárias:
# pip install pyautogui 
# pip install pandas             
# pip install openpyxl

import pyautogui
import time

# Tempo de espera entre todas as ações
pyautogui.PAUSE = 0.5  

# Variáveis
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Sumário das funções:
# pyautogui.click("texto")         -> Clica com o mouse
# pyautogui.write("texto")         -> Escreve o texto
# pyautogui.press("enter")         -> Pressiona a tecla enter
# pyautogui.hotkey("ctrl", "c")    -> Atalho de teclado


# PASSO A PASSO DO PROGRAMA
#  - Entrar no sistema da empresa

# 1° Abrir o navegador 
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click( x=634, y=591)  
pyautogui.write(link)
pyautogui.press("enter")

# 2° Fazer login no sistema
time.sleep(4)
pyautogui.click(x=810, y=467)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("impressionador123")
pyautogui.press("enter")
time.sleep(3) # pausa para aguardar a pagina carregar 

# 3° Acessar base de dados dos produtos 
import pandas

tabela = pandas.read_csv("Produtos.csv")
print(tabela)

for linha in tabela.index:
    # 4° Cadastrar Produtos    
    #  -> Código do produto 
    pyautogui.click(x=917, y=337) 
    codigo = str (tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # -> Marca do produto   
    marca = str (tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    # -> Tipo do produto
    tipo = str (tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # -> Categoria do produto
    categoria = str ( tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # -> Preço unitário do produto
    preço = str (tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preço)
    pyautogui.press("tab")

    # -> Custo do produto
    custo = str (tabela.loc[linha, "custo"])
    pyautogui.write(custo)      
    pyautogui.press("tab")

    # -> observações do produto
    obs = str (tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2) 

    #voltar para inicio da tela             
    pyautogui.scroll(1000) 













