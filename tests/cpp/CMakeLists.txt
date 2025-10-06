enable_testing()

# set all the source files
file(GLOB_RECURSE TEST_CPP_SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp")

add_executable(cpp_unit_tests ${TEST_CPP_SOURCES})
target_link_libraries(cpp_unit_tests GTest::gtest_main)
target_link_libraries(cpp_unit_tests _calculator)
target_link_libraries(cpp_unit_tests _book)
target_link_libraries(cpp_unit_tests logger)


include(GoogleTest)
gtest_discover_tests(cpp_unit_tests)
