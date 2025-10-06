from ha_hello.lib.book import Book


def main():
    book = Book()
    book_id = book.get_book_id()
    book_name = book.get_book_name()
    book_author = book.get_book_author()
    book_price = book.get_book_price()
    book_content = book.get_book_content()


if __name__ == "__main__":
    main()
