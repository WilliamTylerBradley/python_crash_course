print('Give me two numbers and I will add them.')
print('Enter \'q\' to quit.')

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('\nSecond number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print('Those might not have been numbers.')
    else:
        print(answer)