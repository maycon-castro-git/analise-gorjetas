
# Mini Projeto: Análise de Gorjetas no Restaurante
"""

# Etapa 1: Importar bibliotecas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Estilo dos gráficos
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)


# Etapa 2: Carregar os dados
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)


# Etapa 3: Explorar os dados
print("Primeiras linhas:")
print(df.head())


print("\nInformações da base:")
print(df.info())


print("\nEstatísticas descritivas:")
print(df.describe())


# Etapa 4: Limpeza e preparação
df.columns = df.columns.str.lower().str.replace(' ', '_')


# Etapa 5: Análise Exploratória

# Total de gorjetas por dia

sns.boxplot(x="day", y="tip", data=df)
plt.title("Distribuição das Gorjetas por Dia da Semana")
plt.show()


# Gorjeta em relação ao total da conta
sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex")
plt.title("Gorjeta x Total da Conta")
plt.show()


# Etapa 6: Gorjeta média por sexo
gorjeta_sexo = df.groupby("sex")["tip"].mean()
print("\nGorjeta média por sexo:")
print(gorjeta_sexo)


# Etapa 7: Relacionar gorjeta com fumo no restaurante
sns.violinplot(data=df, x="smoker", y="tip", hue="sex", split=True)
plt.title("Gorjetas por Sexo e Fumante/Não-Fumante")
plt.show()

# Etapa 8: Qual o dia da semana tem a maior média de gorjetas ?

media_dia = df.groupby("day")["tip"].mean().sort_values(ascending=False)
print("Média de gorjetas por dia:")
print(media_dia)

# Grafico de barras medio de gorjetas por dia:

media_dia.plot(kind="bar")
plt.title("Média de Gorjetas por Dia da Semana")
plt.xlabel("Dia da Semana")
plt.ylabel("Média de Gorjetas")
plt.show()

# Etapa 9: Gorjetas dfo tipo de refeição (almoço ou Jatar)

sns.boxplot(x="time", y="tip", data=df)
plt.title("Gorjetas por Tipo de Refeição (Lunch x Dinner)")
plt.show()

gorjeta_tempo = df.groupby("time")["tip"].mean()
print("Gorjeta média por tipo de refeição:")
print(gorjeta_tempo)

# Etapa 10: Clientes fumantes dão mais gorjeta?

gorjeta_fumante = df.groupby("smoker")["tip"].mean()
print("Gorjeta média por habito de fumar:")
print(gorjeta_fumante)

sns.boxplot(x="smoker", y="tip", data=df)
plt.title("Gorjetas por Habito de Fumar")
plt.show()

# Etapa 11: Criando uma nova coluna: porcentagem da gorjeta

df["percentual_gorjeta"] = round((df["tip"] / df["total_bill"]) * 100, 2)
print(df[["total_bill", "tip", "percentual_gorjeta"]].head())

# Gráfico: porcetagem da gorjeta por sexo

sns.violinplot(data=df, x="sex", y="percentual_gorjeta", hue="sex")
plt.title("Porcentagem da Gorjeta por Sexo")
plt.show()
