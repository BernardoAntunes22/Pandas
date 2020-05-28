import pandas as pd

df = pd.read_csv("pokemon.csv", encoding='unicode_escape')

df['count'] = 1


# Mostrar os dados todos
def mostrar():
    print(df)


# Agrupar contabilizar por tipos
def agrupar():
    n = df.groupby(['Type 1', 'Type 2']).count()['count']
    print(n)


# ordenar por tipo e HP
def ordenar():
    v = df.sort_values(['Type 1', 'HP'], ascending=[1, 0])
    print(v)


pd.set_option('display.max_columns', None)
pd.set_option("max_rows", None)

if __name__ == '__main__':

    n = 1
    while n != 0:
        print('Ordenar os dados: 1\n')
        print('Agrupar os dados: 2\n')
        print('Mostra os dados: 3\n')
        n = int(input('Qual é a opção que pretende: '))
        if n == 1:
            ordenar()
        elif n == 2:
            agrupar()
        elif n == 3:
            mostrar()
        elif n == 0:
            break
        else:
            print('Opção inválida!')
