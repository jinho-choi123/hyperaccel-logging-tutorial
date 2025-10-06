set(PYBIND_LIBRARY_NAME calculator)
set(LIBRARY_NAME _${PYBIND_LIBRARY_NAME})

# Define the csrc directories and files
set(CALCULATOR_CSRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/csrc)
set(THIRD_PARTY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../../3rdparty)
set(CALCULATOR_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/include)
set(CALCULATOR_PYBIND_CSRC ${CALCULATOR_CSRC_DIR}/binding.cpp)

file(
    GLOB_RECURSE CALCULATOR_CXX_CSRC
    "${CALCULATOR_CSRC_DIR}/*.cpp"
)
list(REMOVE_ITEM CALCULATOR_CXX_CSRC ${CALCULATOR_PYBIND_CSRC})


# Shared library for c++ unit tests
add_library(${LIBRARY_NAME} ${CALCULATOR_CXX_CSRC})
target_include_directories(${LIBRARY_NAME} PUBLIC ${CALCULATOR_INCLUDE_DIR})
target_include_directories(${LIBRARY_NAME} PUBLIC ${THIRD_PARTY_DIR}/spdlog/include)
target_link_libraries(${LIBRARY_NAME} PUBLIC logger)

# Python binding
message(STATUS "PYBIND_LIBRARY_NAME: ${PYBIND_LIBRARY_NAME}")
pybind11_add_module(${PYBIND_LIBRARY_NAME} )
target_sources(${PYBIND_LIBRARY_NAME} PRIVATE ${CALCULATOR_CXX_CSRC} ${CALCULATOR_PYBIND_CSRC})
target_include_directories(${PYBIND_LIBRARY_NAME} PRIVATE ${CALCULATOR_INCLUDE_DIR})
target_include_directories(${PYBIND_LIBRARY_NAME} PUBLIC ${THIRD_PARTY_DIR}/spdlog/include)
target_link_libraries(${PYBIND_LIBRARY_NAME} PUBLIC logger)
