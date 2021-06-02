# Остановки
# Считать из csv-файла (с http://data.mos.ru/datasets/752) количество остановок, вывести улицу, на которой больше всего остановок.
import pandas as pd

stations = pd.read_csv(open('bus_stops.csv', 'r', encoding='cp1251'), sep=';')
stations_count = stations.groupby(['Street']).size()
stations_count.sort_values(ascending=False, inplace=True)
print(stations_count[1:2])
