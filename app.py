import folium
from folium.map import FeatureGroup
from folium.plugins import MarkerCluster

from geopy.geocoders import ArcGIS
import webbrowser
import pandas as pd
from datetime import datetime, timedelta
import json
import pandas

load = open("world.json", "r",encoding="utf-8-sig").read()

worldMap = folium.Map(tiles="cartodbpositron")
fg = folium.FeatureGroup(name="foo")
fg.add_child(folium.GeoJson(data=load))
worldMap.add_child(fg)
worldMap.save("test.html")

data = pd.read_json(r"cov_02-02-21.json")

dt = (datetime.today().now() - timedelta(days=1))
dtf = dt.strftime("%Y-%m-%d")

tidyArr = []
for item in data:
    for res in data[item]['data']:
        if res['date'] == dtf:
            pair = [data[item]['location'],int(res['new_cases'])]
            outStr = "%s : %s" % (pair[0],pair[1])
            tidyArr.append(pair)
            # print(tidyArr)
            # print(tidyArr[0])

load = [open("world.json", "r",encoding="utf-8-sig").read(), tidyArr]

def conv(arr):
    res = {}
    for i in arr:
        res[str(i[0])] = i[1]
    return res
# print(tidyArr)

tidyDict = conv(tidyArr)
# print(tidyDict)

for key in tidyDict.items():
   print(key)
print('______________________________________________________________\n')

def colorFn(x):
    color = 'white'
    name = x['properties']['NAME']

    #temp fix for mismatching country names
    if name == "Iran (Islamic Republic of)":
            name = "Iran"
    if name == "Lao People's Democratic Republic":
            name = "Laos"
    if name == "The former Yugoslav Republic of Macedonia":
            name = "North Macedonia"
    if name == "Viet Nam":
            name = "Vietnam"        
    if name == "Swaziland":
            name = "Eswatini" 
    if name == "Korea, Republic of":
            name = "South Korea"
    if name == "Republic of Moldova":
            name = "Moldova"
    if name == "Syrian Arab Republic":
            name = "Syria" 
    if name == "Democratic Republic of the Congo":
            name = "Democratic Republic of Congo"      
    if name == "Libyan Arab Jamahiriya":
            name = "Libya" 
    if name == "Czech Republic":
            name = "Czechia"        

    if name not in tidyDict:
        
        print('%s nope' % (name))
    else :
        if tidyDict[name] >= 10000:
            color = '#800000'
        elif tidyDict[name] >= 1000:
            color = '#d47f7f'
        elif tidyDict[name] >= 500 and tidyDict[name] < 1000:
            color = 'orange'
        elif tidyDict[name] >= 100 and tidyDict[name] < 500:
            color = 'yellow'
        elif tidyDict[name] >= 10 and tidyDict[name] < 100:
            color = '#67d7db'
        else :
            color = 'green'    
    return color


worldMap = folium.Map(tiles="cartodbpositron")
fg = folium.FeatureGroup(name="foo")
color="purple"
fg.add_child(folium.GeoJson(data=open("world.json", "r",encoding="utf-8-sig").read(),
style_function= lambda x : {'fillColor':colorFn(x), 'stroke':'black'}))

worldMap.add_child(fg)
worldMap.add_child(folium.LayerControl())

worldMap.save("cov_map.html")

webbrowser.open("cov_map.html")