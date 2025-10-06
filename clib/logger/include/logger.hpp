#ifndef LOGGER_HPP
#define LOGGER_HPP

#include <spdlog/spdlog.h>

enum class LogLevel {
  TRACE,
  DEBUG,
  INFO,
  ERROR,
};

class Logger {

public:
  __attribute__((no_instrument_function)) static void
  info(const std::string &message);

  __attribute__((no_instrument_function)) static void
  error(const std::string &message);

  __attribute__((no_instrument_function)) static void
  debug(const std::string &message);

  __attribute__((no_instrument_function)) static void
  trace(const std::string &message);
};

#endif
