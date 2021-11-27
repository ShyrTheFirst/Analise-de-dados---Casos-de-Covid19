import pandas as pd
import matplotlib.pyplot as plt

#plotar planilhas#

planilha = pd.read_excel("casos_covid_1a100.xlsx")

colunas = ["Confirmados","Recuperados","Descartados","Obitos","Sindrome Gripal Total"]
colunas2 = ["Confirmados","Recuperados","Obitos"]

planilha[colunas].plot()
planilha[colunas2].plot.area()
plt.show()
