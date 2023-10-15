cmake_minimum_required(VERSION 3.26)
project(c_practical_file C)

set(CMAKE_C_STANDARD 11)

add_executable(c_practical_file src/main.c)

file(GLOB_RECURSE sources CONFIGURE_DEPENDS "src/*.c")
foreach (file_path ${sources})
    string(REPLACE ".c" "" file_path_no_ext ${file_path})
    get_filename_component(file_name ${file_path_no_ext} NAME)
    add_executable(${file_name} ${file_path})
endforeach ()
