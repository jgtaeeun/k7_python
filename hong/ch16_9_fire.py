from pathlib import Path
import csv
import plotly.express as px
from datetime import datetime
import json


path=Path('world_fires_1_day.csv')
lines=path.read_text().splitlines()
contents=csv.reader(lines)
header_row=next(contents)

#for i , n in enumerate(header_row):
#    print(i, n)
   # 0 latitude  1 longitude 2 brightness
lat_list, lon_list, bright_list = [],[],[]
for r in contents:
    try:
        lat=float(r[0])
        lon=float(r[1])
        bright=float(r[2])
    except ValueError:
        print(f"lat, lon, bright 데이터가 모두 있어야 합니다.")
    else:
        lat_list.append(lat)
        lon_list.append(lon)
        bright_list.append(bright)
title='Global Fire'
fig=px.scatter_geo(lat=lat_list, lon=lon_list, size=bright_list,  title=title,
                color=bright_list, )        

fig.show()