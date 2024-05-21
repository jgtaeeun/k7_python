from pathlib import Path
import os

print(os.getcwd())

new_path='partial_programs/reading_from_a_file'
os.chdir(new_path)
print("변경된 디렉토리:",os.getcwd())  


path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")