#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node

def generate_launch_description():
    rate_arg = DeclareLaunchArgument('rate', default_value='2.0', description='Publication rate in Hz')
    warning_temp_arg = DeclareLaunchArgument('warning_temp', default_value='35.0', description='Warning threshold in °C')
    critical_temp_arg = DeclareLaunchArgument('critical_temp', default_value='40.0', description='Critical threshold in °C')
    mode_arg = DeclareLaunchArgument('mode', default_value='normal', description='Mode: normal or test')
    
    rate = LaunchConfiguration('rate')
    warning_temp = LaunchConfiguration('warning_temp')
    critical_temp = LaunchConfiguration('critical_temp')
    mode = LaunchConfiguration('mode')
    
    actual_rate = PythonExpression(["4.0 if '", mode, "' == 'test' else ", rate])
    actual_warning = PythonExpression(["30.0 if '", mode, "' == 'test' else ", warning_temp])
    actual_critical = PythonExpression(["38.0 if '", mode, "' == 'test' else ", critical_temp])
    
    return LaunchDescription([
        rate_arg,
        warning_temp_arg,
        critical_temp_arg,
        mode_arg,
        
        Node(
            package='temperature_monitor_pkg',
            executable='temperature_sensor',
            name='temperature_sensor',
            output='screen',
            parameters=[
                {'publish_rate': actual_rate},
                {'min_temp': 15.0},
                {'max_temp': 45.0},
                {'sensor_name': 'main_sensor'}
            ]
        ),
        
        Node(
            package='temperature_monitor_pkg',
            executable='temperature_monitor',
            name='temperature_monitor',
            output='screen',
            parameters=[
                {'warning_threshold': actual_warning},
                {'critical_threshold': actual_critical}
            ]
        ),
    ])
