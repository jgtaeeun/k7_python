#16-8 최근 지진
#json파일 
# path = Path('eq_data/eq_data_1_day_m1.geojson')
# contents = path.read_text(encoding='utf-8')    #데이터파일을 문자열로 읽음
# all_eq_data = json.loads(contents)    
# all_eq_dicts = all_eq_data['features']

#cvs파일
# path = Path('weather_data/sitka_weather_2021_simple.csv')    #2021 총 데이터  avg데이터는 ''이다.
# lines = path.read_text().splitlines()
# reader = csv.reader(lines)
# header_row = next(reader)
# for row in reader:
#     current_date=datetime.strptime(row[2], '%Y-%m-%d')

#그래프
#import mathlib as plt

#지도
# import plotly.express as px

from pathlib import Path
import json
import os
import plotly.express as px

os.chdir('hong')

path=Path('1.0_month.geojson')
contents= path.read_text(encoding='utf-8')    #데이터파일을 문자열로 읽음
all_eq_data = json.loads(contents)  

# path=Path('readable_1.0_month.geojson')
# readable_contents=json.dumps(all_eq_data , indent=4)
# path.write_text(readable_contents)



all_eq_dicts = all_eq_data['features']

mags,lons,lats,places=[],[],[],[]

for eq_dicts in all_eq_dicts:
    try:
     mag=eq_dicts['properties']['mag']
     place=eq_dicts['properties']['place']
     lon=eq_dicts['geometry']['coordinates'][0]
     lat=eq_dicts['geometry']['coordinates'][1]

    except ValueError:
        print('valueerror')
    else:

     mags.append(mag)
     lons.append(lon)
     lats.append(lat)
     places.append(place)


print(f"지진규모: {mags[:10]}")
print(f"경도: {lons[:10]}")
print(f"위도: {lats[:10]}")
print(f"정보: {places[:10]}")
# print(len(mags), len(lons), len(lats))


#세계지도 그리기
title='Global Earthquakes'
fig=px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                   color=mags, color_continuous_scale='Viridis', labels={'color':'Magnitude'},
                    hover_name=places, )     
#scatter_geo(lag='', lon='', title='')함수는 지도위에 산포도를 오버레이로 표시할 수 있다.
#scatter_geo()함수를 가장 단순하게 사용하는 방식은 위도와 경도 리스트를 전달하는 것이다.
#projection='natural earth' 지도 가장자리를 둥글게
#색깔(파랑->노랑) : 지진규모(작음->큼)
fig.show()