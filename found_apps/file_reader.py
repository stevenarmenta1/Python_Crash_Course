from pathlib import Path

'''
path = Path('learning_python.txt')
contents = path.read_text().rstrip()
print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)
'''

path = Path('learning_python.txt')
contents = path.read_text().rstrip()

for line in contents.splitlines():
    print(line.replace('Python', 'C'))
