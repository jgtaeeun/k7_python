#austin csv 파일을 읽어와서 그래프 그리기
from pathlib import Path
import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime
import json

os.chdir('hong')

path=Path('austin_weather_2024.csv')
lines=path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# for index, column in enumerate(header_row):
#     print(index, column)
# 5 DATE
# 18 TMAX
# 20 TMIN

dates, tmaxs, tmins=[],[],[]

for row in reader:
    try:
         current_date=datetime.strptime(row[5], '%Y-%m-%d')
         tmax=int(row[18])
         tmin=int(row[20])
    except ValueError:
            print(f"{current_date}의 데이터가 없다.")
    else:
         dates.append(current_date)
         tmaxs.append(tmax)
         tmins.append(tmin)

# #그림 그리기
plt.style.use('seaborn-v0_8')
fig, ax =plt.subplots()
ax.set_title("austin's information", fontsize=20)
ax.set_xlabel('date', fontsize=14)
ax.set_ylabel('temperature', fontsize=14)
ax.plot(dates, tmaxs , color='red')
ax.plot(dates, tmins , color='blue')
ax.fill_between(dates, tmaxs,tmins, facecolor='yellow', alpha=0.5)
fig.autofmt_xdate()
plt.show()
