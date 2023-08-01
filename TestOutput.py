import Book

from Book.Booklover import booklover 

book_name = "The Great Gatsby"
rating = 10
person = booklover('Jackie','jjf4rp@virginia.edu',"Romance")
person.add_book(book_name,rating)


person.book_list

num_books_read = person.num_books_read()

print(num_books_read,"= number of books you have read " )