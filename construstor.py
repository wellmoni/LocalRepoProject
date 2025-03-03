class Book:
    def __init__(self, title, author, year):
        """
        Constructor to initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor to clean up and print a message upon object deletion.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation for the Book instance.

        Returns:
            str: A user-friendly string representation of the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation of the Book instance.

        Returns:
            str: A string that can recreate the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Example usage
if __name__ == "__main__":
    # Create a book instance
    my_book = Book("To Kill a Mockingbird", "Harper Lee", 1960)

   
    print(str(my_book))  # Output: To Kill a Mockingbird by Harper Lee, published in 1960

   
    print(repr(my_book))  # Output: Book('To Kill a Mockingbird', 'Harper Lee', 1960)

  
    del my_book


class Book:
    def __init__(self, title, author):
        """
        Initialize a base Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.

        Args:
            title (str): The title of the eBook.
            author (str): The author of the eBook.
            file_size (int): The size of the eBook file in MB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} [EBook - {self.file_size}MB]"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} [PrintBook - {self.page_count} pages]"


class Library:
    def __init__(self):
        """
        Initialize a Library instance with an empty collection of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Add a book (Book, EBook, or PrintBook) to the library.

        Args:
            book (Book): An instance of Book, EBook, or PrintBook.
        """
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        """
        Print the details of all books in the library.
        """
        if not self.books:
            print("The library is empty.")
        else:
            print("Library Collection:")
            for book in self.books:
                print(f"  - {book}")
