#include "book.hpp"
#include "logger.hpp"

int Book::get_book_id() {
  Logger::info("Book::get_book_id() called");
  return 1;
}

int Book::get_book_name() {
  Logger::info("Book::get_book_name() called");
  return 2;
}

int Book::get_book_author() {
  Logger::info("Book::get_book_author() called");
  return 3;
}

int Book::get_book_price() {
  Logger::info("Book::get_book_price() called");
  return 4;
}

int Book::get_book_content() {
  Logger::info("Book::get_book_content() called");
  return 5;
}
