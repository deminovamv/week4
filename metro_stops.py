# Остановки у метро
# Объединить наборы данных из предыдущих задач и посчитать, у какой станции метро больше всего остановок (в радиусе 0.5 км).

import pandas as pd
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r


stations = pd.read_csv(open('bus_stops.csv', 'r', encoding='cp1251'), sep=';')
metro = pd.ExcelFile('metro.xlsx')
metro = metro.parse()

metro_Station = {}
for name,x_m, y_m in zip(metro['NameOfStation'],metro['Longitude_WGS84'], metro['Latitude_WGS84']):
    if not name in metro_Station:
        for  x_s, y_s in zip(stations['Longitude_WGS84'],stations['Latitude_WGS84']):
            distance = haversine(x_m, y_m,x_s, y_s)
            if distance <= 0.5:
                if not name in metro_Station:
                    metro_Station[name] = 1
                else:
                    metro_Station[name] += 1


metro_Station_sort=sorted(metro_Station.items(), key = lambda item: item[1], reverse = True)

print(metro_Station_sort[0][0])
