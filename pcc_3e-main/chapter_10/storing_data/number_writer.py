from pathlib import Path
import json
import os
os.chdir('storing_data')

numbers = [1,2,3,4,5]

path = Path('numbers.json')
contents = json.dumps(numbers)   #json.dumps() :JSON 문자열로 변환
path.write_text(contents)