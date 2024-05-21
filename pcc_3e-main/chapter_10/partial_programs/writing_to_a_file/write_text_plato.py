from pathlib import Path
import os


print(f"현재경로={os.getcwd()}")

# 파일 생성 및 쓰기
with open('example.txt', 'w') as file: #file변수는 open된  파일 객체이므로 file.write_text()이 없다. =>file.write ()
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")
 
 
print("File created and written successfully.")

path=Path('example.txt')
path.write_text('if file open with Path, file can use write_text()') #덮어쓰기

# 파일에 내용 추가하기
with open('example.txt', 'a') as file:
    file.write("Adding a new line.\n")
    file.write("Appending another line.\n")

with path.open('a', encoding='UTF-8') as file:
    file.write('path객체로 파일에 내용 추가 및 유니코드로 인코딩')



# print("Content appended to the file successfully.")

# # 새로운 파일 생성하기
try:
    with open('new_file.txt', 'x') as file:
        file.write("This is a newly created file.\n")
    print("New file created and written successfully.")
except FileExistsError:
    print("File already exists.")


