cmake_minimum_required(VERSION 3.26.0)
project(ASCII_Converter)

set(OpenCV_DIR "C:\\Users\\mrexh\\opencv\\build\\x64\\vc16\\lib")
find_package(OpenCV REQUIRED)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

include_directories(${OpenCV_INCLUDE_DIRS})
include_directories("C:\\Users\\mrexh\\opencv\\build\\include")
add_executable(ASCII_Converter convert-to-ascii.cpp)
target_link_libraries(ASCII_Converter ${OpenCV_LIBS_DEBUG})
