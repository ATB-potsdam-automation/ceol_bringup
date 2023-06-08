from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.descriptions import ParameterValue
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
       
    return LaunchDescription([
            
            Node(
                package='ceol_base',
                executable='ceol_node',
                name='ceol_lanarvi',
                output='screen'
                ),

            Node(
                package="tf2_ros",
                executable="static_transform_publisher",
                name="lidar_tf",
                arguments=["0.975565", "-0.000249", "0.959613", "0.0", "0.2617993877991494", "0.0", "base_link", "cloud"]
                ),

            IncludeLaunchDescription(
                PythonLaunchDescriptionSource([
                    PathJoinSubstitution([
                        FindPackageShare('ros2_socketcan'), 'launch',
                        'socket_can_receiver.launch.py'
                    ])
                ]),
            ),

            IncludeLaunchDescription(
                PythonLaunchDescriptionSource([
                    PathJoinSubstitution([
                        FindPackageShare('sick_scan'), 'launch',
                        'sick_mrs_1xxx.launch.py'
                    ])
                ]),
            ),
            
            ]
    )