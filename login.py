Admin_user = "admin"
APassword = "1234"

Username = "user"
Password = "1233"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == Admin_user and Apassword == APassword:
    print("You have successfully logged in as Admin!")

elif username == Username and password == Password:
    print("You have successfully logged in as User!")

else:
    print("Incorrect username or password.")
