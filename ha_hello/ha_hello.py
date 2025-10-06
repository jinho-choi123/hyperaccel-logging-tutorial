from loguru import logger

from ha_hello.lib.book import Book
from ha_hello.lib.calculator import Calculator


class HaSecretWeapon:
    def __init__(self):
        self.calculator = Calculator()
        logger.info("Calculator initialized")
        self.book = Book()
        logger.info("Book initialized")

        logger.info("HaSecretWeapon initialized")

    def add(self, a, b):
        logger.info("HaSecretWeapon::add() called")
        logger.debug(f"HaSecretWeapon::add({a}, {b}) called")
        return self.calculator.add(a, b)

    def get_book_id(self):
        logger.info("HaSecretWeapon::get_book_id() called")
        logger.debug("HaSecretWeapon::get_book_id() called")
        return self.book.get_book_id()

    def get_book_name(self):
        logger.info("HaSecretWeapon::get_book_name() called")
        logger.debug("HaSecretWeapon::get_book_name() called")
        return self.book.get_book_name()

    def get_book_author(self):
        logger.info("HaSecretWeapon::get_book_author() called")
        logger.debug("HaSecretWeapon::get_book_author() called")
        return self.book.get_book_author()

    def get_book_price(self):
        logger.info("HaSecretWeapon::get_book_price() called")
        logger.debug("HaSecretWeapon::get_book_price() called")
        return self.book.get_book_price()

    def get_book_content(self):
        logger.info("HaSecretWeapon::get_book_content() called")
        logger.debug("HaSecretWeapon::get_book_content() called")
        return self.book.get_book_content()
