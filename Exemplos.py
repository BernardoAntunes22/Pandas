import pandas as pd

df = pd.read_csv("pokemon.csv", encoding='unicode_escape')

df['count'] = 1

#Mostrar os dados todos
def mostrar():
    print(df)
#Agrupar contabilizar por tipos
def agrupar():
    n = df.groupby(['Type 1', 'Type 2']).count()['count']
    print(n)
#ordenar por tipo e HP
def ordenar():
    v = df.sort_values(['Type 1', 'HP'], ascending=[1,0])
    print(v)

pd.set_option('display.max_columns', None)
pd.set_option("max_rows", None)

if __name__ == '__main__':
    #ordenar()
    #agrupar()
    #mostrar()
