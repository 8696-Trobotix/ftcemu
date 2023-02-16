cmake_minimum_required (VERSION 3.11)

# FTXUI TUI Library
include(FetchContent)

set(FETCHCONTENT_UPDATES_DISCONNECTED TRUE)
FetchContent_Declare(ftxui
  GIT_REPOSITORY https://github.com/ArthurSonzogni/ftxui
  GIT_TAG v4.0.0
)

FetchContent_GetProperties(ftxui)
if(NOT ftxui_POPULATED)
  FetchContent_Populate(ftxui)
  add_subdirectory(${ftxui_SOURCE_DIR} ${ftxui_BINARY_DIR} EXCLUDE_FROM_ALL)
endif()
# FTXUI

project(tui
  LANGUAGES CXX
  VERSION 1.0.0
)

add_executable(tui tui/src/tui.cpp)
target_include_directories(tui PRIVATE include)

target_link_libraries(tui
  PRIVATE ftxui::screen
  PRIVATE ftxui::dom
  PRIVATE ftxui::component
)

string(APPEND CMAKE_CXX_FLAGS " -Wall -Wextra -pedantic -std=c++17") 
# string(APPEND CMAKE_EXE_LINKER_FLAGS " -O3")
