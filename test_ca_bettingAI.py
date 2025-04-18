import ca
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


transfer = ca.CA()
myPath_file = "C://Users//stefa//3AInformatica_Prjs//009.sensors_data_analysis//3AAI//data_analysis//ex02//datasets//bettingAI_prov_ageclass.csv"
# hair_eye = pd.read_csv(".\datasets\hair_eye.csv", index_col=0)
bettingAI = pd.read_csv(myPath_file, index_col=0)

print(bettingAI.head())

transfer.fit(bettingAI)
print('centered correspondence matrix:')
print(transfer.centr_corrspnd_mat_)

print('Pearson residual:')
print(transfer.pearson_resd_)

pcs_row, pcs_col = \
    transfer.get_princpl_coords_df(row_categories=bettingAI.index,
                                   col_categories=bettingAI.columns)
print('Principal coordinates of row variables in DataFrame:')
print(pcs_row)
print(pcs_col)


fig, ax = plt.subplots()
sns.regplot(x='Dim 0', y='Dim 1', data=pcs_row, fit_reg=False, ax=ax)
sns.regplot(x='Dim 0', y='Dim 1', data=pcs_col, fit_reg=False, ax=ax)
for i, txt in enumerate(list(bettingAI.index)):
    ax.annotate(txt + ' eyes',
                (pcs_row.iloc[i]['Dim 0'], pcs_row.iloc[i]['Dim 1']))
for i, txt in enumerate(list(bettingAI.columns)):
    ax.annotate(txt + ' hair',
                (pcs_col.iloc[i]['Dim 0'], pcs_col.iloc[i]['Dim 1']))
ax.set_xlabel('Dim 0')
ax.set_ylabel('Dim 1')
plt.show()
