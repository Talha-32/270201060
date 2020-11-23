midterm1 = 0
midterm2 = 0
final = 0

students = [[50,90,60],[15,60,75],[99,95,91]]
successfullStudents = []

for grades in students:
    midterm1 = grades[0]
    midterm2 = grades[1]
    final = grades[2]
    
    avarage = (float(midterm1)*0.3) + (float(midterm2)*0.3) + (float(final)*0.4)
    
    if(avarage > 90):
        successfullStudents.append(grades)
    
    
        
for i in successfullStudents:
    print(i)