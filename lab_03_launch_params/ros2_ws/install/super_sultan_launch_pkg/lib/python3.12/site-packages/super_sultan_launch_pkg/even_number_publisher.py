#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_pub')
        
        # Объявляем параметры
        self.declare_parameter('publish_frequency', 10.0)
        self.declare_parameter('overflow_threshold', 100)
        self.declare_parameter('topic_name', '/even_numbers')
        
        # Читаем параметры
        freq = self.get_parameter('publish_frequency').value
        threshold = self.get_parameter('overflow_threshold').value
        topic = self.get_parameter('topic_name').value
        
        self.get_logger().info(f"Starting with freq={freq}Hz, threshold={threshold}, topic={topic}")
        
        # Создаём издателя
        self.publisher = self.create_publisher(Int32, topic, 10)
        self.overflow_pub = self.create_publisher(Int32, '/overflow', 10)
        
        # Таймер
        self.timer = self.create_timer(1.0 / freq, self.timer_callback)
        self.counter = 0
        self.threshold = threshold

    def timer_callback(self):
        msg = Int32()
        msg.data = self.counter
        self.publisher.publish(msg)
        self.get_logger().info(f"Published: {self.counter}")
        
        if self.counter >= self.threshold:
            overflow_msg = Int32()
            overflow_msg.data = self.counter
            self.overflow_pub.publish(overflow_msg)
            self.get_logger().warn(f"!!! OVERFLOW !!! Value: {self.counter}")
            self.counter = 0
        else:
            self.counter += 2

def main(args=None):
    rclpy.init(args=args)
    node = EvenNumberPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
