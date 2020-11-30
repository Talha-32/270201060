books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = dict()
for i in range(len(books)):
    t = ((len(books[i]),len(set(books[i]))))
    book_dict.update({books[i]:t})
print(":", book_dict)