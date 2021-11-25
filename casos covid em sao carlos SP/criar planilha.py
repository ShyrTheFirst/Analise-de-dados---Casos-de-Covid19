import pandas as pd


data_data_publi = []
data_num_boletim = []
data_conf = []
data_rec = []
data_descart = []
data_obito = []
data_gripe_total = []

recebendo_data = True
while recebendo_data:
    print("Inserir novas informações: ")
    data_publi = input("Insira a data de publicação: ")
    data_data_publi.append(data_publi)
    num_boletim = input("Insira o numero do boletim: ")
    data_num_boletim.append(num_boletim)
    conf = input("Insira o numero de confirmados: ")
    data_conf.append(conf)
    rec = input("Insira o numero de recuperados: ")
    data_rec.append(rec)
    descart = input("Insira o numero de descartados: ")
    data_descart.append(descart)
    obito = input("Insira o numero de obitos: ")
    data_obito.append(obito)
    gripe_total = input("Numero de casos gripais totais: ")
    data_gripe_total.append(gripe_total)
    continuar = input("Deseja Continuar? S/N ")
    if continuar == "S" or continuar == "s":
        pass
    else:
        recebendo_data = False


casos_covid_df = pd.DataFrame(
    {"Numero Boletim":data_num_boletim,
     "Confirmados":data_conf,
     "Recuperados":data_rec,
     "Descartados":data_descart,
     "Obitos":data_obito,
     "Sindrome Gripal Total":data_gripe_total},
    index=data_data_publi)

casos_covid_df.to_excel("casos_covid_cont.xlsx",sheet_name="Casos São Carlos", index=True)


