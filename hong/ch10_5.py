#visiting폴더/visitors.txt
from pathlib import Path
import os

current_path = os.getcwd()  # 현재 경로 가지고오기
print(current_path)
# os.mkdir(current_path + "/" + 'visit')  # 1번 만들고 주석처리
os.chdir('hong/visit')
print(os.getcwd())
path=Path('visitor.txt')

with open ('visitor.txt', 'w') as file:
    count=0
    while True:
        if count==10 : break
        file.write(input('사용자이름: '))
        file.write('\n')
        count+=1

        
        

