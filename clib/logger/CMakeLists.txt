set(LOGGER_LIBRARY_NAME logger)

# Define the csrc directories and files
set(LOGGER_CSRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/csrc)
set(THIRD_PARTY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../../3rdparty)
set(LOGGER_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/include)

file(
    GLOB_RECURSE LOGGER_CXX_CSRC
    "${LOGGER_CSRC_DIR}/*.cpp"
)

add_library(${LOGGER_LIBRARY_NAME} ${LOGGER_CXX_CSRC})
target_include_directories(${LOGGER_LIBRARY_NAME} PUBLIC ${LOGGER_INCLUDE_DIR})
target_include_directories(${LOGGER_LIBRARY_NAME} PUBLIC ${THIRD_PARTY_DIR}/spdlog/include)
target_link_libraries(${LOGGER_LIBRARY_NAME} PUBLIC spdlog)
