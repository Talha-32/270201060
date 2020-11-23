mail = input("your mail adress: ")
mail = mail.lower()
a = mail.index("@")
for i in range(a):
    if(mail[i] == "."):
        mail = mail[:i] + mail[:i + 1]
if mail == "cen113@example.com":
    print("True")
else:
    print("false")    