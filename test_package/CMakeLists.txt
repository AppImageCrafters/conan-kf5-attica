cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

find_package(KF5Attica)
find_package(Qt5 COMPONENTS Core REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example KF5::Attica Qt5::Core)
