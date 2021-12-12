import pandas as pd

OilData = pd.read_csv('static/data/BrentOilPrices.csv', sep=';')
GoldData = pd.read_csv('static/data/GOLDPMGBD228NLBM.csv', sep=';')
SnpData = pd.read_csv('static/data/S&P.csv', sep=';')

SnpData.pop('Unnamed: 2')
SnpData.pop('Unnamed: 3')
SnpData.pop('Unnamed: 4')
SnpData.pop('Unnamed: 5')
SnpData.pop('Unnamed: 6')
SnpData.pop('Unnamed: 7')
SnpData.pop('Unnamed: 8')
OilData.pop('Unnamed: 2')

OilData.rename(columns={'Price': 'OilPrice'}, inplace=True)
SnpData.rename(columns={'S&Pprice': 'SnpIndex'}, inplace=True)

maindatafr = pd.merge(OilData, GoldData, on='Date')
maindatafr = pd.merge(maindatafr, SnpData, on='Date')

def stat(frcolumn):
    maindatafr.GoldPrice = pd.to_numeric(maindatafr.GoldPrice, errors='coerce')
    return 'median - ' + str(frcolumn.median()) + ', mean - '  + str(frcolumn.mean()) + ', std - ' + str(frcolumn.std())

oil_stat = stat(maindatafr.OilPrice)
gold_stat = stat(maindatafr.GoldPrice)
snp_stat = stat(maindatafr.SnpIndex)

tables, titles = [maindatafr.head(10).to_html(classes='data')], maindatafr.columns.values
