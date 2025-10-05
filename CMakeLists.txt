# Cmake version
cmake_minimum_required(VERSION 3.20)

# Project name
project(ha-log-tutorial)

# Project configuration
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(MAKE_C_COMPILER clang)
set(MAKE_CXX_COMPILER clang++)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Options for the project
option(BUILD_TESTS "Enable building C++ Tests" OFF)

# Find Python
if(NOT DEFINED Python_EXECUTABLE)
    set(Python_FIND_VIRTUALENV FIRST)
    find_package(Python COMPONENTS Interpreter Development REQUIRED)
endif()

# Fetch pybind11
if(NOT DEFINED PYBIND11_CMAKE_DIR)
    execute_process(
        COMMAND ${Python_EXECUTABLE} -c "import pybind11; print(pybind11.get_cmake_dir())"
        OUTPUT_VARIABLE PYBIND11_CMAKE_DIR
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
endif()

message(STATUS "PYBIND11_CMAKE_DIR: ${PYBIND11_CMAKE_DIR}")
if(PYBIND11_CMAKE_DIR)
    list(APPEND CMAKE_PREFIX_PATH ${PYBIND11_CMAKE_DIR})
    message(STATUS "CMAKE_PREFIX_PATH: ${CMAKE_PREFIX_PATH}")
endif()

find_package(pybind11 REQUIRED)

# add lib/
add_subdirectory(lib)

# add spdlog
add_subdirectory(3rdparty/spdlog)

# C++ Unit Tests
if(BUILD_TESTS)
    enable_testing()
    add_subdirectory(${CMAKE_SOURCE_DIR}/tests/cpp)
endif()
