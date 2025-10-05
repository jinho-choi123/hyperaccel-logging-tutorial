set(PYBIND_LIBRARY_NAME calculator)

# Define the csrc directories and files
set(CALCULATOR_CSRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/csrc)
set(THIRD_PARTY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../../3rdparty)
set(CALCULATOR_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/include)


file(
    GLOB_RECURSE CALCULATOR_CXX_CSRC
    "${CALCULATOR_CSRC_DIR}/*.cpp"
)

# Python binding
message(STATUS "PYBIND_LIBRARY_NAME: ${PYBIND_LIBRARY_NAME}")
pybind11_add_module(${PYBIND_LIBRARY_NAME} )
target_sources(${PYBIND_LIBRARY_NAME} PRIVATE ${CALCULATOR_CXX_CSRC})
target_include_directories(${PYBIND_LIBRARY_NAME} PRIVATE ${CALCULATOR_INCLUDE_DIR})
target_include_directories(${PYBIND_LIBRARY_NAME} PRIVATE ${THIRD_PARTY_DIR}/spdlog/include)
