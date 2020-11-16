userName = input("write your Username: ")
password = input("write your password: ")

if userName == "Talha" and password == "123":
    print("welcome the system!!!")
elif not password:
    print("please write your password")
elif not userName:
    print("please write your username")
else :
    print("Your password or username not true!!!")
