correct_login = 'test'
correct_password = 12345

login = input('Login: ')
login = str(login)
password = input('Parol: ')
password = int(password)


if login == correct_login and password == correct_password:
    print('Xos Geldiniz')
    
elif login == '':
    print('Login daxil etmediniz')

elif login != correct_login and password == correct_password:
    print('Login yalnisdir')

elif password != correct_password and login == correct_login:
    print('Parol yalnisdir')

elif login != correct_login and password != correct_password:
    print('Login ve Parol yalnisdir')