from pathlib import Path
import os
new_path='partial_programs/reading_from_a_file'
os.chdir(new_path)
print("변경된 디렉토리:",os.getcwd())  

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
  print(line)
