from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import json


path=Path('sanfran_data.csv')
lines=path.read_text().splitlines()
contents=csv.reader(lines)
header_row=next(contents)

maxtem, mintem, dates=[],[],[]

#for i, t in enumerate(header_row):
 #   print(i, t)
  # 1 NAME 5 DATE 14 TMAX  16 TMIN
for r in contents:
    try:
        current_time=datetime.strptime(r[5], '%Y-%m-%d')
        maxt = int(r[14])
        mint = int(r[16])
    except ValueError:
        print(f"{current_time}날짜의 데이터가 없습니다.")
    else:
        maxtem.append(maxt)
        mintem.append(mint)
        dates.append(current_time)


plt.style.use('seaborn-v0_8')
fig, ax =plt.subplots()
ax.set_title("sanfransico's information", fontsize=20)
ax.set_xlabel('date', fontsize=14)
ax.set_ylabel('temperature', fontsize=14)
ax.plot(dates, maxtem , color='red')
ax.plot(dates, mintem , color='blue')
ax.fill_between(dates, maxtem,mintem, facecolor='yellow', alpha=0.5)
fig.autofmt_xdate()
plt.show()
