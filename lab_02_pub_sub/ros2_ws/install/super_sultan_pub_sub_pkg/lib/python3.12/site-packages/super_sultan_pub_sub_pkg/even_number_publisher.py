#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_pub')
        # Основной издатель
        self.publisher = self.create_publisher(Int32, '/even_numbers', 10)
        # Издатель для переполнения
        self.overflow_publisher = self.create_publisher(Int32, '/overflow', 10)
        
        timer_period = 0.1  # 10 Гц
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.counter = 0
        self.get_logger().info("Even number publisher started!")

    def timer_callback(self):
        # Публикуем текущее чётное число
        msg = Int32()
        msg.data = self.counter
        self.publisher.publish(msg)
        self.get_logger().info(f"Published: {self.counter}")
        
        # Проверяем на переполнение
        if self.counter >= 100:
            # Публикуем сообщение о переполнении
            overflow_msg = Int32()
            overflow_msg.data = self.counter
            self.overflow_publisher.publish(overflow_msg)
            self.get_logger().warn(f"!!! ПЕРЕПОЛНЕНИЕ !!! Значение: {self.counter}")
            self.counter = 0
        else:
            self.counter += 2

def main(args=None):
    rclpy.init(args=args)
    node = EvenNumberPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
