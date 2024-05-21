from pathlib import Path
import json
import os
os.chdir('storing_data')

path=Path('username2.json')
if path.exists():
    contents=path.read_text()
    username=json.loads(contents)
    print(f"읽기={username}")
else :
    username=input('이름은?')
    contents=json.dumps(username)
    path.write_text(contents)
    print(f"이름 입력됨{username}")
