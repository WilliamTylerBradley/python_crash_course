from pathlib import Path
import json

def get_stored_number(path):
    """Get stored number if available"""
    if path.exists():
        contents = path.read_text()
        number = json.loads(contents)
        return number
    else:
        return None
    
def get_new_number(path):
    """Prompt for a new number"""
    number = input("What is your number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    return number

def get_number():
    """Ask for number"""
    path = Path("python_work/chapter_10/number.json")
    number = get_stored_number(path)
    if number:
        print(f'Your number is {number}')
    else:
        number = get_new_number(path)
        print(f'{number} saved')

get_number()