from pathlib import Path
import json
import os
import plotly.express as px

os.chdir('pcc_3e-main\chapter_16\mapping_global_datasets\partial_programs')

# Read data as a string and convert to a Python object.
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')    #데이터파일을 문자열로 읽음
all_eq_data = json.loads(contents)              #문자열을 파이썬 객체로 변환


#eq_data/eq_data_1_day_m1.geojson 파일 데이터를 눈에 보기 쉽게 정리한 파일 생성-1번 생성하고 난 뒤 주석처리 필수
# path=Path('eq_data/readable_eq_data_1_day_m1.geojson')
# readable_contents=json.dumps(all_eq_data , indent=4)
# path.write_text(readable_contents)


#16.2.3(p.469)
#eq_data_1_day_m1.geojson 파일 데이터 중에서 키 값이 features인 값들을 가지고 온다.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))


#16.2.4(p.470) 지진 규모 추출하기
# mags=[]  #지진규모 리스트
# for eq_dicts in all_eq_dicts:
#     mag=eq_dicts['properties']['mag']
#     mags.append(mag)

# print(mags[:10]) # [1.6, 1.6, 2.2, 3.7, 2.92000008, 1.4, 4.6, 4.5, 1.9, 1.8]

#) 지진 규모, 위치정보 추출하기
mags,lons,lats,eq_titles=[],[],[],[] #지진규모, 경도, 위도 ,지역과 규모 정리한 텍스트 리스트
for eq_dicts in all_eq_dicts:
    mag=eq_dicts['properties']['mag']
    mags.append(mag)
    lon=eq_dicts['geometry']['coordinates'][0]
    lons.append(lon)
    lat=eq_dicts['geometry']['coordinates'][1]
    lats.append(lat)
    eq_title=eq_dicts['properties']['title']
    eq_titles.append(eq_title)

print(f"지진규모: {mags[:10]}")
print(f"경도: {lons[:10]}")
print(f"위도: {lats[:10]}")
print(f"정보: {eq_titles[:10]}")
# print(len(mags), len(lons), len(lats))


#세계지도 그리기
title='Global Earthquakes'
fig=px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                   color=mags, color_continuous_scale='Viridis', labels={'color':'Magnitude'},
                   projection='natural earth' ,hover_name=eq_titles, )     
#scatter_geo(lag='', lon='', title='')함수는 지도위에 산포도를 오버레이로 표시할 수 있다.
#scatter_geo()함수를 가장 단순하게 사용하는 방식은 위도와 경도 리스트를 전달하는 것이다.
#projection='natural earth' 지도 가장자리를 둥글게
#색깔(파랑->노랑) : 지진규모(작음->큼)
fig.show()