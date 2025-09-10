from pathlib import Path

def read_text(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"Sorry, the file {path} does not exist.")
        pass
    else: 
        print(contents)

filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
    path = Path(filename)
    read_text(path) # call the function to run for each of the files
