#include "book.hpp"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(book, m) {
  py::class_<Book>(m, "Book")
      .def(py::init<>())
      .def("get_book_id", &Book::get_book_id)
      .def("get_book_name", &Book::get_book_name)
      .def("get_book_author", &Book::get_book_author)
      .def("get_book_price", &Book::get_book_price)
      .def("get_book_content", &Book::get_book_content);
}
