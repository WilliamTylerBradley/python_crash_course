current_users = ['Andy', 'Bob', 'Charlie', 'David', 'Elizabeth']
current_users_lower = [user.lower() for user in current_users]

new_users = ['Zach', 'Yanni', 'Xavier', 'William', 'Elizabeth']

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('Need new user name')
    else:
        print('User name is available')