cmake_minimum_required(VERSION 3.26)
project(c_practical C)

set(CMAKE_C_STANDARD 11)

file(GLOB_RECURSE sources CONFIGURE_DEPENDS "./*.c")
foreach (file_path ${sources})
    string(REPLACE ".c" "" file_path_no_ext ${file_path})
    get_filename_component(file_name ${file_path_no_ext} NAME)
    add_executable(${file_name} ${file_path})
endforeach ()
