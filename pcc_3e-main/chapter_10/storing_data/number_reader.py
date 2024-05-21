from pathlib import Path
import json
import os
os.chdir('storing_data')
path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)