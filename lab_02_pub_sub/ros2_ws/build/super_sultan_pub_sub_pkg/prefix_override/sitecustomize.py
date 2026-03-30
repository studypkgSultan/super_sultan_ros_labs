import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sultan/ros_labs/super_sultan_ros_labs/lab_02_pub_sub/ros2_ws/install/super_sultan_pub_sub_pkg'
