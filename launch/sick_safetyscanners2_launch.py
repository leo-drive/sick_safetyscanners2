from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    ld = LaunchDescription()

    ld.add_action(ComposableNodeContainer(
        name="sick_safetyscanners2_container",
        namespace="sick_safetyscanners2",
        package="rclcpp_components",
        executable="component_container",

        composable_node_descriptions=[
            ComposableNode(
                package="sick_safetyscanners2",
                plugin="sick::SickSafetyscannersRos2",
                name="sick_safetyscanners2_node",
                parameters=[
                {"frame_id": "scan",
                    "sensor_ip": "192.168.1.2",
                    "host_ip": "192.168.1.1",
                    "interface_ip": "0.0.0.0",
                    "host_udp_port": 0,
                    "channel": 0,
                    "channel_enabled": True,
                    "skip": 0,
                    "angle_start": 0.0,
                    "angle_end": 0.0,
                    "time_offset": 0.0,
                    "general_system_state": True,
                    "derived_settings": True,
                    "measurement_data": True,
                    "intrusion_data": True,
                    "application_io_data": True,
                    "use_persistent_config": False,
                    "min_intensities": 0.0}
                ]
            )
        ],
        output="screen",
        emulate_tty=True,
    ))
    return ld