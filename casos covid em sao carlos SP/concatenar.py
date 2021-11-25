import pandas as pd

#concatenar as planilhas

planilha1 = pd.read_excel("casos_covid.xlsx")
planilha2 = pd.read_excel("casos_covid_cont.xlsx")

planilha_casos = pd.concat([planilha1,planilha2],axis=0)
planilha_casos.to_excel("casos_covid_FINAL.xlsx",sheet_name="Casos São Carlos", index=True)
