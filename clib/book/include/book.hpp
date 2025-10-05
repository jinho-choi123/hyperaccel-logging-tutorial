#ifndef BOOK_HPP
#define BOOK_HPP

#include <spdlog/spdlog.h>

class Book {

public:
  Book() = default;

  int get_book_id();

  int get_book_name();

  int get_book_author();

  int get_book_price();

  int get_book_content();
};

#endif
