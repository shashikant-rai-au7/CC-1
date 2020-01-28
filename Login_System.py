Username = input('Enter Your Username ')
Password = input('Enter Your Password ')
if Username == "Priyesh" and Password == "password":
    print('Entered the System')
elif Username != "Priyesh" and Password == "password":
    print('Username Doesnot Exist')
elif Username == "Priyesh" and Password != "password":
    print('Passwords donot match')