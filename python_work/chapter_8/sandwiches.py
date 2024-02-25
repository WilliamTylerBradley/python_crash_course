def make_sandwich(*item_list):
    """Prints sandwich order"""
    print('Sandwich ordered includes:')
    for item in item_list:
        print(f'- {item}')
    print('')

make_sandwich('ham')
make_sandwich('ham', 'cheese')
make_sandwich('ham', 'cheese', 'mustard')