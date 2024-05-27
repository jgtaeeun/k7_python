from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime



path1=Path('sitka_weather_2021.csv')
lines1=path1.read_text().splitlines()
contents1=csv.reader(lines1)
header_row1=next(contents1)  #  2 DATE  5 PRCP

path2=Path('death_valley_2021_full.csv')
lines2=path2.read_text().splitlines()
contents2=csv.reader(lines2)
header_row2=next(contents2)  #2 DATE 3 PRCP

prcp1, date1=[],[]
prcp2, date2=[],[]

for r in contents1:
    try:
        current_date1=datetime.strptime(r[2], '%Y-%m-%d')
        p1=float(r[5])
    except ValueError:
        print('데이터없음')
    else:
        prcp1.append(p1)
        date1.append(current_date1)

for r in contents2:
    try:
        current_date2=datetime.strptime(r[2], '%Y-%m-%d')
        p2=float(r[3])
    except ValueError:
        print('데이터없음')
    else:
        prcp2.append(p2)
        date2.append(current_date2)


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.set_title('sitka(red) vs death-valley(blue)', fontsize=14)
ax.set_xlabel('date', fontsize=14)
ax.set_ylabel('prcp', fontsize=14)
ax.plot(date1,prcp1 , color='red')
ax.plot(date2,prcp2 , color='blue')
fig.autofmt_xdate()
plt.show()
