from pathlib import Path
import json

"""
fav_num = input("What is your favorite number? ")

path = Path('users_fav_num.json')
contents = json.dumps(fav_num)
path.write_text(contents)


path = Path('users_fav_num.json')
contents = path.read_text()
num = json.loads(contents)

print(f"I know your favorite number! It's {num}.")
"""

path = Path('users_fav_num.json')
if path.exists():
    contents = path.read_text()
    num = json.loads(contents)
    print(f"I know your favorite number! It's {num}.")
else:
    fav_num = input("What is your favorite number? ")
    contents = json.dumps(fav_num)
    path.write_text(contents)
