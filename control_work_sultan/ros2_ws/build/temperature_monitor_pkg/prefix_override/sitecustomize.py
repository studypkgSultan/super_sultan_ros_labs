import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sultan/ros_labs/super_sultan_ros_labs/control_work_sultan/ros2_ws/install/temperature_monitor_pkg'
