import os

with open("example.txt", encoding='UTF-8') as file:
  data = file.read()
  print(data)


directory = os.getcwd()
print(directory)  #C:\python_work\pcc_3e-main\chapter_10\partial_programs\writing_to_a_file
flist = os.listdir(directory) #현재디렉토리가 있는 곳의 내부 디렉토리들을 리스트로 출력
print(flist) #['example.txt', 'new_file.txt', 'plato_fileread.py', 'programming.txt', 'write_message_0_first_version.py', 'write_message_1_multiple_lines.py', 'write_text_plato.py']