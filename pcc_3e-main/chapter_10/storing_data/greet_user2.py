from pathlib import Path
import json
import os
os.chdir('storing_data')



path = Path('username.json')
content=json.dumps('seonjae')
path.write_text(content)