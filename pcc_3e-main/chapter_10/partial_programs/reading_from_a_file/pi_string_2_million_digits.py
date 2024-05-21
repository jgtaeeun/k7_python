from pathlib import Path
import os

print(os.getcwd())

new_path='partial_programs/reading_from_a_file'
os.chdir(new_path)
print("변경된 디렉토리:",os.getcwd())  

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
print(f"pi_million_digits.txt의 행의 갯수:{len(lines)}")


pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(f"pi_million_digits.txt의 요소 갯수: {len(pi_string)}")
print(f"pi_million_digits.txt의 인덱스 0~51까지 출력 후 나머지는 ...처리 : {pi_string[:52]}...")
