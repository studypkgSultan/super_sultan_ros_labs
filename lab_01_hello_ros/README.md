# Лабораторная работа №1: Hello ROS

## Описание
Создание первого ROS 2 пакета и узлов.

## Содержание пакета `super_sultan_study_pkg`
- `first_node.py` — простой узел, выводящий "Hello ROS 2 World!"
- `time_printer.py` — узел с таймером, выводящий текущее время каждые 5 секунд

## Запуск
```bash
cd ~/ros_labs/super_sultan_ros_labs/lab_01_hello_ros
colcon build --packages-select super_sultan_study_pkg
source install/setup.bash
ros2 run super_sultan_study_pkg time_printer
