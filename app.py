import folium
from folium.map import FeatureGroup
from geopy.geocoders import ArcGIS
import webbrowser
import pandas as pd
from datetime import datetime, timedelta

test = pd.read_json(r"cov_02-02-21.json")
test2 = pd.DataFrame(test)

dt = (datetime.today().now() - timedelta(days=1))
dtf = dt.strftime("%Y-%m-%d")

for item in test:
    if test[item]['location'] == "Ireland" :
        # print(test[item]['data'][0]['date'])
        for res in test[item]['data']:
            # print(dt)
            # print(res['date'])
            if res['date'] == dtf:
                print(dt)
                outStr = "%s : %s" % (dtf,res['new_cases'])
                print(outStr)