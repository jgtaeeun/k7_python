from pathlib import Path
import os
new_path='partial_programs/reading_from_a_file'
os.chdir(new_path)
 
path = Path('pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)