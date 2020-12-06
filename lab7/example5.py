password = input("Create your password: ")

isValid = False
lowValid = False
upValid=False
digValid = False
wanted = 0

if len(password) >= 8: wanted += 1
for i in password:
	if i.islower() and not lowValid:
		lowValid = True

	elif i.isupper() and not upValid:
		upVal = True

	elif i.isdigit() and not digValid:
		digValid = True

if digValid and lowValid and upValid and wanted == 4:
	print("Valid password... ")

else:
	print("Invalid password... ")