from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import json

path = Path('sitka_weather_2021.csv')
lines=path.read_text().splitlines()
contents=csv.reader(lines)
header_row=next(contents)

#for i, n in enumerate(header_row):
#    print(i, n)
  #  2 DATE 5 PRCP

dates, prcp_list=[],[]

for r in contents:
    try:
        current_date=datetime.strptime(r[2], '%Y-%m-%d')
        prcp=float(r[5])
    except ValueError:
        print(f"{current_date}의 데이터가 없습니다.")
    else:
        dates.append(current_date)
        prcp_list.append(prcp)

plt.style.use('seaborn-v0_8')
fig, ax =plt.subplots()
ax.set_title("sitka's weather", fontsize=20)
ax.set_xlabel('date', fontsize=14)
ax.set_ylabel('prcp', fontsize=14)
ax.plot(dates,prcp_list , color='blue')
fig.autofmt_xdate()
plt.show()
