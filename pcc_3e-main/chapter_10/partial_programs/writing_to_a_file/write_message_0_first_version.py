from pathlib import Path
import os

print(f"현재경로={os.getcwd()}")  #C:\python_work\pcc_3e-main\chapter_10\partial_programs\writing_to_a_file

path = Path('programming.txt')
path.write_text("I like programming.")

