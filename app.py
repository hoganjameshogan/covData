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
    
    if name not in tidyDict:
        print('%s nope' % (name))
    else :
        if tidyDict[name] >= 1000:
            color = 'red'
        elif tidyDict[name] >= 500 and tidyDict[name] < 1000:
            color = 'orange'
        elif tidyDict[name] >= 100 and tidyDict[name] < 500:
            color = 'yellow'
        elif tidyDict[name] >= 10 and tidyDict[name] < 100:
            color = '#a0beef'
        else :
            color = 'green'    
        # print("%s : %s" % (name, tidyDict[name]))
    return color


worldMap = folium.Map(tiles="cartodbpositron")
fg = folium.FeatureGroup(name="foo")
color="purple"
fg.add_child(folium.GeoJson(data=open("world.json", "r",encoding="utf-8-sig").read(),
style_function= lambda x : {'fillColor':colorFn(x), 'stroke':'black'}))

worldMap.add_child(fg)
worldMap.save("test.html")

webbrowser.open("test.html")