import folium
from folium.map import FeatureGroup
from folium.plugins import MarkerCluster

from geopy.geocoders import ArcGIS
import webbrowser
import pandas as pd
from datetime import datetime, timedelta

load = open("world.json", "r",encoding="utf-8-sig").read()

fg = folium.FeatureGroup(name="foo")

worldMap = folium.Map(tiles="cartodbpositron")


fg = folium.FeatureGroup(name="foo")
fg.add_child(folium.GeoJson(data=load))
worldMap.add_child(fg)

worldMap.save("test.html")

webbrowser.open("test.html")

data = pd.read_json(r"cov_02-02-21.json")
# test2 = pd.DataFrame(test)

dt = (datetime.today().now() - timedelta(days=1))
dtf = dt.strftime("%Y-%m-%d")

for item in data:
    
        # print(test[item]['data'][0]['date'])
    for res in data[item]['data']:
            # print(dt)
            # print(res['date'])
        if res['date'] == dtf:
            outStr = "%s : %s" % (data[item]['location'],int(res['new_cases']))
            print(outStr)