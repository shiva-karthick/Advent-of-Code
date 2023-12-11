cmake_minimum_required(VERSION 3.22)

project(
  AOC_2023
  VERSION 1.0
  LANGUAGES CXX)

# find_package(Microsoft.GSL CONFIG REQUIRED)

include(FetchContent)

FetchContent_Declare(GSL
    GIT_REPOSITORY "https://github.com/microsoft/GSL"
    GIT_TAG "v4.0.0"
    GIT_SHALLOW ON
)

FetchContent_MakeAvailable(GSL)

# add_library(mylib my_lib.cpp my_lib.hpp)
add_executable(main Day_2a.cpp)

target_link_libraries(main PRIVATE Microsoft.GSL::GSL)
