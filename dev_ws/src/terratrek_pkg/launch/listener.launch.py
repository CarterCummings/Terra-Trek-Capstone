from launch import LaunchDescription
from launch_ros.actions import Node

def generate_description():
    return LaunchDescription({
        Node(
            package='demo_nodes.py',
            executables='listener'
        )
    })