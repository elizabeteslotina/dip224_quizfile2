from openpyxl import Workbook, load_workbook
import pandas as pd
data = pd.read_csv("data.csv")

#6
vajag= data[data['industry'] == 'Auxiliary']
max_value = vajag['value'].max()
print(max_value)

#7
skaits= data[data['industry'] == 'Insurance']
count_value = skaits['value'].count()
print(count_value)

#8
vērtība= data[data['industry'] == 'Mining']
average_value = vērtība['value'].mean()
noapaļots=round(average_value)
print(noapaļots)

#9
filtrēts = data[data['industry'] == 'Mining']
top3 = filtrēts['value'].nlargest(3)
min_top3 = top3.min()
print(min_top3)