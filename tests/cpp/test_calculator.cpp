#include "calculator.hpp"
#include "logger.hpp"
#include <gtest/gtest.h>

TEST(CalculatorTest, Add) {
  Logger::info("CalculatorTest, Add");
  Calculator calculator;
  EXPECT_EQ(calculator.add(1, 2), 3);
}

TEST(CalculatorTest, Subtract) {
  Logger::info("CalculatorTest, Subtract");
  Calculator calculator;
  EXPECT_EQ(calculator.subtract(1, 2), -1);
}

TEST(CalculatorTest, Multiply) {
  Logger::info("CalculatorTest, Multiply");
  Calculator calculator;
  EXPECT_EQ(calculator.multiply(1, 2), 2);
}

TEST(CalculatorTest, Divide) {
  Logger::info("CalculatorTest, Divide");
  Calculator calculator;
  EXPECT_EQ(calculator.divide(6, 2), 3);
}
