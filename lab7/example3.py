books =  ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", "ENDER'S GAME"]
books_dict = dict()
book_len = 0
unique_len= 0
for i in range(len(books)):
	book_len = len(books[i])
	unique_len = len(set(books[i]))
	tup = (book_len, unique_len, (book_len+unique_len)/2)
	books_dict.update({books[i]: tup})
print(books_dict)
