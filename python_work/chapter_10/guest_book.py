from pathlib import Path

guest_names = ''

while True:
    guest_name = input('What is your name? ')

    if guest_name == 'quit':
        break
    else:
        guest_names += (guest_name + '\n') 

path = Path('python_work/chapter_10/guest_book.txt')
path.write_text(guest_names)