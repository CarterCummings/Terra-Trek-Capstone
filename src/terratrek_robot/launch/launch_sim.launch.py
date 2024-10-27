import os

from ament_index_python.packages import get_package_share_directory # type: ignore

from launch import LaunchDescription 
from launch.actions import IncludeLaunchDescription # type: ignore
from launch.launch_description_sources import PythonLaunchDescriptionSource # type: ignore
from launch.substitutions import LaunchConfiguration,  PathJoinSubstitution # type: ignore
from launch_ros.substitutions import FindPackageShare

import launch_ros.parameter_descriptions

from launch_ros.actions import Node # type: ignore

 

def generate_launch_description():
    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!
 
    use_sim_time = LaunchConfiguration('use_sim_time', default='false') 

    package_name='terratrek_robot' #<--- CHANGE ME

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    gazebo_params_file = os.path.join(get_package_share_directory(package_name),'config','gazebo_params.yaml')

    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
                    launch_arguments={'extra_gazebo_args': '--ros-args --params-file ' + gazebo_params_file}.items()
             )

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'terratrek_robot'],
                        output='screen')

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
    ) 

    controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["skid_cont",
                   "joint_broad",],
    )

    # extender_spawner = Node(
    #     package="controller_manager",
    #     executable="spawner",
    #     parameters=[
    #         launch_ros.parameter_descriptions.ParameterFile(
    #             param_file=os.path.join(get_package_share_directory(package_name),'config','extenders_config.yaml'),
    #             allow_substs=True), {'use_sim_time': True} ], 
    #     arguments=[
    #             "joint_state_controller",
    #             "joint1_position_controller",
    #             "joint2_position_controller",],
    # )

    twist_mux_params = os.path.join(get_package_share_directory(package_name),'config','twist_mux.yaml')
    twist_mux = Node(
            package="twist_mux",
            executable="twist_mux",
            parameters=[twist_mux_params, {'use_sim_time': True}],
            remappings=[('/cmd_vel_out','/skid_cont/cmd_vel_unstamped')]
        )


    joystick = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','joystick.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )    

    # Launch them all!
    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        rviz,
        controller_spawner,
        joystick,
        twist_mux,
        #extender_spawner,
        #position_cont_spawner,
    ])
