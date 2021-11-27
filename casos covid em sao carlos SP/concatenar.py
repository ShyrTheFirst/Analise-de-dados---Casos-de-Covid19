import pandas as pd

#concatenar as planilhas

planilha1 = pd.read_excel("casos_covid_1a200.xlsx")
planilha2 = pd.read_excel("casos_covid_cont3.xlsx")

planilha_casos = pd.concat([planilha1,planilha2],axis=0)
planilha_casos.to_excel("casos_covid_1a300.xlsx",sheet_name="Casos São Carlos", index=True)
