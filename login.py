
print('user account creation\n')

username= input('enter username \n')
password= input('enter password\n')
if username == 'admin' and password == 'admin':
    print('account has been created successfully\n')

    print('login now !!')

username2 = input ('enter username:\n')
password2 = input ('enter password:\n')
if username==username2 and password==password2:
    print('welcome ',username)
else: print('invalid username or password\n')


