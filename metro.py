# Метро
# В этом задании требуется определить, на каких станциях московского метро сейчас идёт ремонт эскалаторов и вывести на экран их названия.

# Файл с данными можно скачать на странице http://data.mos.ru/opendata/624/row/1773539.

import re
from datetime import datetime
import pandas as pd


metro = pd.ExcelFile('metro.xlsx')
df1 = metro.parse()

pattern = r'\d{2}.\d{2}.\d{4}'
current_datetime = datetime.now().date()

st_name = {}
for name, line in zip(df1['NameOfStation'],df1['RepairOfEscalators']):
    line = str(line)
    result = re.findall(pattern, line)
    if  result:   
        repair_date = datetime.strptime(result[1], '%d.%m.%Y').date()
        if repair_date > current_datetime:
            st_name[name] = 1
for key,value in st_name.items():
    print(key)
