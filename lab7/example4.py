employees = dict()
employees_name = ""
employees_salary = 0
for i in range(3):
    
	employees_name = input("Type name: ")
	employees_salary = int(input("type salary: "))
	employees.update({employees_name:employees_salary})

print(sorted(employees.items(), key=lambda item: item[1], reverse=True))