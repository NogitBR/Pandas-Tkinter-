import pandas as pd
from datetime import date
from tkinter import *

hoje = date.today()
ano = date.today().year

# print(df.iloc[1]) >> CARACTERRISTICAS DA ROW
# print(df.loc[df['NOME'] == 'pedro']) >> SOH ONDE TEM 'PEDRO' NO NOME
# print(df.sort_values('nome')) >> PRINT EM RELACAO AO NOME DA ORDEM ALFABETICA
# print(df.sort_values('NOME', ascending=False)) # ORDEM ALFABETIA AO CONTRARIO
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed'] >> SOMANDO
# df = df.drop(columns=['Name']) >> DROP DO NAME, NAO APARECE MAIS
# df.iloc[:, 3:10].sum(axis=0) >> soma apartir do 3 ate o 9(10 nao incluso), axis=0 eh esquerda direita, axis=1 eh cima baixo
# print(df.columns.values) >> lista de  colunas
#list(df.columns.values) >> lista de colunas em arrays
# df.reset_index(drop=True) >> reseta o index, o drop tira o index antigo
#df.loc[fd[COLUNA] == CONDICAO, COLUNAMUDAR] = VALORNOVODACOLUNAMUDAR
#df.loc[fd['Type1']] == 'Fire', 'Legendary'] = True
#print(df.head(5))


root = Tk()
root.geometry("400x300")



myLabel = Label(root, text="Nome:", font = "Helvetica 15")
myLabel.pack()
enome = Entry(root, width=20, font = "Helvetica 20 ",justify="center")
enome.pack()


myLabel = Label(root, text="Idade:", font = "Helvetica 15")
myLabel.pack()
eidade = Entry(root, width=20, font = "Helvetica 20 ",justify="center")
eidade.pack()


myLabel = Label(root, text="Valor:", font = "Helvetica 15")
myLabel.pack()
evalor = Entry(root, width=20, font = "Helvetica 20 ",justify="center")
evalor.pack()

labelError = Label(root, text='')
labelError.pack()

def adicionar():


    nome = enome.get()
    idade = eidade.get()
    valor = evalor.get()

    if nome == '' or idade == '' or valor == '':
        labelError.config(text='Preencha todos os campos!')
        return



    diadehoje = str(hoje)
    try:
        df = pd.read_csv('projeto.csv')
        print('Encontrei!')
    except:
        df = pd.DataFrame({'DIA': [],
                           'NOME': [],
                           'IDADE': [],
                           'VALOR': []})
        print('Nao encontrei! Criando arquivo')
    try:
        df2 = pd.DataFrame({
            "NOME": [nome],
            "IDADE": [idade],
            "VALOR": [valor],
            "DIA": [diadehoje]
        })
        novo = pd.concat([df, df2], ignore_index=True)
        novo.to_csv('projeto.csv', index=False)

        ##LIMPANDO ENTRADA DE TEXTOS
        enome.delete(0, END)
        eidade.delete(0, END)
        evalor.delete(0, END)

        #LOG PARA O USUARIO
        labelError.config(text='Criado com sucesso!')
    except PermissionError:

        print('Permissao Negada! Verifique se o programa esta fechado!')

        labelError.config(text='Permissao negada! Verifique se o excel esta fechado')



myButton = Button(root, text="Adicionar!", command=adicionar)
myButton.pack()





root.mainloop()
