from ha_hello.lib.book import Book


def test_book_init():
    book = Book()
    assert book is not None


def test_book_print_book(capsys):
    book = Book()
    book_id = book.get_book_id()
    assert book_id == 1


def test_book_print_book_name(capsys):
    book = Book()
    book_name = book.get_book_name()
    assert book_name == 2


def test_book_print_book_author(capsys):
    book = Book()
    book_author = book.get_book_author()
    assert book_author == 3


def test_book_print_book_price(capsys):
    book = Book()
    book_price = book.get_book_price()
    assert book_price == 4
