#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class TemperatureSensor(Node):
    def __init__(self):
        super().__init__('temperature_sensor')
        
        # Объявляем параметры
        self.declare_parameter('publish_rate', 2.0)
        self.declare_parameter('min_temp', 15.0)
        self.declare_parameter('max_temp', 45.0)
        self.declare_parameter('sensor_name', 'main_sensor')
        
        # Читаем параметры
        rate = self.get_parameter('publish_rate').value
        self.min_temp = self.get_parameter('min_temp').value
        self.max_temp = self.get_parameter('max_temp').value
        self.sensor_name = self.get_parameter('sensor_name').value
        
        # Создаём издателя
        self.publisher = self.create_publisher(Float32, '/temperature', 10)
        
        # Таймер
        timer_period = 1.0 / rate
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.get_logger().info(f"Sensor '{self.sensor_name}' started with rate={rate}Hz, range=[{self.min_temp}, {self.max_temp}]")
    
    def timer_callback(self):
        temperature = random.uniform(self.min_temp, self.max_temp)
        msg = Float32()
        msg.data = temperature
        self.publisher.publish(msg)
        self.get_logger().info(f"Published temperature: {temperature:.2f}°C")

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureSensor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
