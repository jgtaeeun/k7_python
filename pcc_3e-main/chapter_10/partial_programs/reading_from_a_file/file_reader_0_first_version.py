from pathlib import Path
import os 
# print("현재 작업 디렉토리:",os.getcwd())    #최근에 연 폴더에서 파일을 찾는다. /vscode를 chapter_10파일로 열었을 때
# #<built-in function getcwd>
# # PS C:\python_work\pcc_3e-main\chapter_10> 

new_path='partial_programs/reading_from_a_file'
os.chdir(new_path)
print("변경된 디렉토리:",os.getcwd())   

# path = Path('partial_programs/reading_from_a_file/pi_digits.txt')
path = Path('pi_digits.txt')
contents = path.read_text()
contents=contents.rstrip().lstrip()
print(contents)
# 3.1415926535
#   8979323846
#   2643383279

# lines=contents.splitlines()
# for line in lines:
#     print(f"각 줄은 = {line}")

# 각 줄은 = 3.1415926535
# 각 줄은 =   8979323846
# 각 줄은 =   2643383279
# print(contents)

lines=contents.splitlines()
pi_string=''
for line in lines:
    pi_string+=line
print(pi_string)
print(len(pi_string))
#3.1415926535  8979323846  2643383279
# 36
lines=contents.splitlines()
pi_string=''
for line in lines:
    pi_string+=line.lstrip()
print(pi_string)
print(len(pi_string))
# 3.141592653589793238462643383279
# 32

