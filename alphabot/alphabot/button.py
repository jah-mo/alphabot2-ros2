#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from alphabot.alphabot import Alphabot

class Sensors(Node):
    def __init__(self):
        super().__init__("button_node")

        self.alphabot = Alphabot()
        self.alphabot.init_button()

        self.toggle = False

        self.button_publisher = self.create_publisher(
            Bool,
            "alphabot/toggle",
            10
        )
        self.timer = self.create_timer(0.1, self.talker)

    def talker(self):
        msg = Bool()
        if self.alphabot.get_button_status():
            self.toggle = not self.toggle
        msg.data = self.toggle
        self.button_publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Sensors()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()