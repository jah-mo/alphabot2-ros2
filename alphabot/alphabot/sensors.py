#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from alphabot.alphabot import Alphabot

class Sensors(Node):
    def __init__(self):
        super().__init__("sensors_node")

        self.alphabot = Alphabot()
        self.alphabot.init_ir_sensors()

        self.sensor_publisher = self.create_publisher(
            Bool,
            "alphabot/front_sensors",
            10
        )
        self.timer = self.create_timer(0.1, self.talker)

    def talker(self):
        msg = Bool()
        msg.data = self.alphabot.get_ir_sensors_status()
        self.sensor_publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Sensors()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()