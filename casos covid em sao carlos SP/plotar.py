import pandas as pd
import matplotlib.pyplot as plt

#plotar planilhas#

planilha = pd.read_excel("casos_covid.xlsx")

colunas = ["Confirmados","Recuperados","Descartados","Obitos","Sindrome Gripal Total"]

planilha[colunas].plot()
plt.show()
