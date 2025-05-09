cmake_minimum_required(VERSION 3.5)
project(sick_safetyscanners2)

# Default to C99
if (NOT CMAKE_C_STANDARD)
    set(CMAKE_C_STANDARD 99)
endif ()

# Default to C++14
if (NOT CMAKE_CXX_STANDARD)
    set(CMAKE_CXX_STANDARD 14)
endif ()

if (CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
endif ()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(Boost REQUIRED COMPONENTS chrono)
find_package(diagnostic_updater REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_lifecycle REQUIRED)
find_package(lifecycle_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(sick_safetyscanners_base REQUIRED)
find_package(sick_safetyscanners2_interfaces REQUIRED)
find_package(rclcpp_components REQUIRED)
find_package(laser_geometry REQUIRED)

set(dependencies
        diagnostic_updater
        rclcpp
        rclcpp_lifecycle
        rclcpp_components
        lifecycle_msgs
        sensor_msgs
        sick_safetyscanners_base
        sick_safetyscanners2_interfaces
        laser_geometry
)

add_library(sick_ros2_component SHARED 
        src/sick_safetyscanners2_node.cpp
        src/SickSafetyscannersRos2.cpp
        src/SickSafetyscanners.cpp
        src/utils/MessageCreator.cpp)

rclcpp_components_register_node(
        sick_ros2_component
        PLUGIN "sick::SickSafetyscannersRos2"
        EXECUTABLE "sick_safetyscanners2_node"
)

target_link_libraries(sick_ros2_component
        sick_safetyscanners_base::sick_safetyscanners_base
        ${Boost_LIBRARIES})

ament_target_dependencies(sick_ros2_component ${dependencies}
)

target_include_directories(sick_ros2_component PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>)

install(DIRECTORY
        launch description rviz
        DESTINATION share/${PROJECT_NAME}/
)

install(TARGETS sick_safetyscanners2_node
        EXPORT export_${PROJECT_NAME}
        DESTINATION lib/${PROJECT_NAME})

if (BUILD_TESTING)
    find_package(ament_lint_auto REQUIRED)
    # the following line skips the linter which checks for copyrights
    # uncomment the line when a copyright and license is not present in all source files
    #set(ament_cmake_copyright_FOUND TRUE)
    # the following line skips cpplint (only works in a git repo)
    # uncomment the line when this package is not in a git repo
    #set(ament_cmake_cpplint_FOUND TRUE)
    ament_lint_auto_find_test_dependencies()
endif ()

#TODO lookup what this does
# For message creation,if used in this message
ament_export_dependencies(${dependencies})


install(TARGETS sick_ros2_component
        EXPORT export_sick_ros2_component
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        RUNTIME DESTINATION bin
)
ament_export_targets(export_sick_ros2_component)

ament_package()
