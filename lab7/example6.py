numbers1 = [2, 3, 4, 20, 5, 5, 15]
numbers2 = [10, 20, 20, 15, 30, 40]
set1 = set(numbers1)
set2 = set(numbers2)
interSet = set()
unionSet = set(numbers1+numbers2)

for i in set1:
    if i in set2:
        interSet.add(i)
        
for j in set2:
    if j in set1:
        interSet.add(j)
        
print(interSet)
print(unionSet)