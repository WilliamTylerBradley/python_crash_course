from pathlib import Path

guest_name = input('What is your name? ')

path = Path('python_work/chapter_10/guest.txt')
path.write_text(guest_name)