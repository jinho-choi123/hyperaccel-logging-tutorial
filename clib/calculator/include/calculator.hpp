#ifndef CALCULATOR_HPP
#define CALCULATOR_HPP

#include <spdlog/spdlog.h>

class Calculator {

public:
  Calculator() = default;

  int add(int a, int b);
  int subtract(int a, int b);
  int multiply(int a, int b);
  int divide(int a, int b);
};

#endif
