#include "logger.hpp"

__attribute__((no_instrument_function)) void
Logger::info(const std::string &message) {
  spdlog::info(message);
}

__attribute__((no_instrument_function)) void
Logger::error(const std::string &message) {
  spdlog::error(message);
}

__attribute__((no_instrument_function)) void
Logger::debug(const std::string &message) {
  spdlog::debug(message);
}

__attribute__((no_instrument_function)) void
Logger::trace(const std::string &message) {
  spdlog::trace(message);
}
