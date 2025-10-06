set(PYBIND_LIBRARY_NAME book)
set(LIBRARY_NAME _${PYBIND_LIBRARY_NAME})

# Define the csrc directories and files
set(BOOK_CSRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/csrc)
set(THIRD_PARTY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../../3rdparty)
set(BOOK_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/include)
set(BOOK_PYBIND_CSRC ${BOOK_CSRC_DIR}/binding.cpp)


file(
    GLOB_RECURSE BOOK_CXX_CSRC
    "${BOOK_CSRC_DIR}/*.cpp"
)

list(REMOVE_ITEM BOOK_CXX_CSRC ${BOOK_PYBIND_CSRC})

# Shared library for c++ unit tests
add_library(${LIBRARY_NAME} ${BOOK_CXX_CSRC})
target_include_directories(${LIBRARY_NAME} PUBLIC ${BOOK_INCLUDE_DIR})
target_include_directories(${LIBRARY_NAME} PUBLIC ${THIRD_PARTY_DIR}/spdlog/include)
target_link_libraries(${LIBRARY_NAME} PUBLIC logger)

# Python binding
message(STATUS "PYBIND_LIBRARY_NAME: ${PYBIND_LIBRARY_NAME}")
pybind11_add_module(${PYBIND_LIBRARY_NAME} )
target_sources(${PYBIND_LIBRARY_NAME} PRIVATE ${BOOK_CXX_CSRC} ${BOOK_PYBIND_CSRC})
target_include_directories(${PYBIND_LIBRARY_NAME} PRIVATE ${BOOK_INCLUDE_DIR})
target_include_directories(${PYBIND_LIBRARY_NAME} PUBLIC ${THIRD_PARTY_DIR}/spdlog/include)
target_link_libraries(${PYBIND_LIBRARY_NAME} PUBLIC logger)
