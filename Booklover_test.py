import unittest
from booklover import booklover


class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`
        
        person = booklover('Jackie','jjf4rp@virginia.edu',"Romance")
        book_name = "Love"
        rating = 9
        
        person.add_book(book_name,rating)
        self.assertIn(book_name, person.book_list['book_name'].values)


    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        person = booklover('Jackie','jjf4rp@virginia.edu',"Romance")
        book_name = "Love"
        rating = 9
        
        person.add_book(book_name, rating)
        person.add_book(book_name, rating)

        # Checking if the book is in the book_list only once
        self.assertEqual(len(person.book_list[person.book_list['book_name'] == book_name]), 1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        
        person = booklover('Jackie','jjf4rp@virginia.edu',"Romance")
        book_name = "Love"
        rating = 9
        
        person.add_book(book_name, rating)

        # Test if the person has read the book (should be True)
        self.assertTrue(person.has_read(book_name))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        person = booklover('Jackie','jjf4rp@virginia.edu',"Romance")
        book_name = "Love"
        self.assertFalse(person.has_read(book_name))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.

        person = booklover('Jackie','jjf4rp@virginia.edu',"Romance")
        book_name = "Love"
        books_data = [("Love ", 10), ("Fun", 2), ("Happiness", 8)]

        # Add books to the person's book list
        for book_name, rating in books_data:
            person.add_book(book_name, rating)

        # Test if num_books matches the expected number of books added
        expected_num_books = len(books_data)
        self.assertEqual(person.num_books_read(), expected_num_books)
        
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        
        
        person = booklover('Jackie','jjf4rp@virginia.edu',"Romance")
        books_data = [("Love ", 10), ("Fun", 2), ("Happiness", 8)]
        for book_name, rating in books_data:
            person.add_book(book_name, rating)

        # Get the favorite books
        favorite_books = person.fav_books()

        # Check if all returned books have rating > 3
        self.assertTrue(all(favorite_books['book_rating'] > 3))

                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)