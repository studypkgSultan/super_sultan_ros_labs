#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class TemperatureMonitor(Node):
    def __init__(self):
        super().__init__('temperature_monitor')
        
        self.declare_parameter('warning_threshold', 35.0)
        self.declare_parameter('critical_threshold', 40.0)
        
        self.warning_threshold = self.get_parameter('warning_threshold').value
        self.critical_threshold = self.get_parameter('critical_threshold').value
        
        self.subscription = self.create_subscription(
            Float32,
            '/temperature',
            self.callback,
            10
        )
        
        self.get_logger().info(f"Monitor started with warning={self.warning_threshold}°C, critical={self.critical_threshold}°C")
    
    def callback(self, msg):
        temp = msg.data
        
        if temp > self.critical_threshold:
            self.get_logger().error(f"CRITICAL! Temperature {temp:.2f}°C exceeds {self.critical_threshold}°C!")
        elif temp > self.warning_threshold:
            self.get_logger().warn(f"Warning! Temperature {temp:.2f}°C exceeds {self.warning_threshold}°C!")
        else:
            self.get_logger().info(f"Temperature OK: {temp:.2f}°C")

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
