#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Объявляем аргумент mode
    mode_arg = DeclareLaunchArgument(
        'mode',
        default_value='normal',
        description='Режим работы: fast, slow, normal'
    )
    
    # Получаем значение mode
    mode = LaunchConfiguration('mode')
    
    # Создаём launch описание
    ld = LaunchDescription()
    ld.add_action(mode_arg)
    
    # Добавляем listener всегда (он не зависит от режима)
    ld.add_action(Node(
        package='super_sultan_launch_pkg',
        executable='overflow_listener',
        name='overflow_listener',
        output='screen',
    ))
    
    # Добавляем publisher в зависимости от режима
    # Используем Node с разными именами и условиями
    
    # Для fast режима
    fast_node = Node(
        package='super_sultan_launch_pkg',
        executable='even_number_publisher',
        name='even_pub_fast',
        output='screen',
        parameters=[
            {'publish_frequency': 20.0},
            {'overflow_threshold': 50},
            {'topic_name': '/even_numbers_fast'},
        ],
    )
    
    # Для slow режима
    slow_node = Node(
        package='super_sultan_launch_pkg',
        executable='even_number_publisher',
        name='even_pub_slow',
        output='screen',
        parameters=[
            {'publish_frequency': 5.0},
            {'overflow_threshold': 150},
            {'topic_name': '/even_numbers_slow'},
        ],
    )
    
    # Для normal режима
    normal_node = Node(
        package='super_sultan_launch_pkg',
        executable='even_number_publisher',
        name='even_pub_normal',
        output='screen',
        parameters=[
            {'publish_frequency': 8.0},
            {'overflow_threshold': 80},
            {'topic_name': '/even_numbers'},
        ],
    )
    
    # Здесь проще всего — запустить все три узла с разными именами
    # Тогда не нужно возиться с условиями, и вы сможете тестировать все режимы одновременно
    ld.add_action(normal_node)
    ld.add_action(fast_node)
    ld.add_action(slow_node)
    
    return ld
