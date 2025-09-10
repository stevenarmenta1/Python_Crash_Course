from pathlib import Path

def count_words(path):
    '''Counts the amount of times the word 'the ' appears in a text'''
    try: 
        contents = path.read_text(encoding='UTF-8')
    except FileNotFoundError:
        pass
    else:
        words = contents.lower()
        the_count = words.count('the ')
        print(f"The number of times 'the ' appears in {path} is {the_count}")

filenames = ['Frankenstein.txt']

for filename in filenames:
    path = Path(filename)
    count_words(path)