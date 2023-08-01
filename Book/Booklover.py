import pandas as pd

class booklover:
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    num_books = 0
    
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre

        
    def add_book(self, book_name, rating):
        book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        if not self.has_read(book_name):
            new_book = pd.DataFrame({'book_name': [book_name],'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
            print(book_name, "added to your list")
            return self.num_books
        else:
            print(f"{self.name} has already read '{book_name}'.")
            
    def has_read(self,book_name):
        return book_name in self.book_list['book_name'].values
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
         