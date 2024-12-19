#!/usr/bin/env python3
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool, Int32
from alphabot.alphabot import Alphabot

class Motors(Node):

    def __init__(self):
        super().__init__("motors_node")

        self.alphabot = Alphabot()
        self.alphabot.init_motors()

        self.toggled = False
        self.use_keyboard = False

        self.sensor_subscriber = self.create_subscription(
            Bool,
            "alphabot/front_sensors",
            self.sensor_listener,
            10
        )

        self.button_subscriber = self.create_subscription(
            Bool,
            "alphabot/toggle",
            self.button_listener,
            10
        )

        self.keyboard_subscriber = self.create_subscription(
            Int32,
            "keyboard/key_press",
            self.keyboard_listener,
            10
        )
        
    def sensor_listener(self, msg):
        blocked = msg.data
        if blocked and self.toggled and not self.use_keyboard:
            self.alphabot.stop()
            time.sleep(1)
            self.alphabot.move_backward(50)
            time.sleep(2)
            self.alphabot.stop()
            time.sleep(1)
            self.alphabot.turn_left(30)
            time.sleep(1)
            self.alphabot.stop()
            time.sleep(1)
            self.alphabot.move_forward(50)

    def button_listener(self, msg):
        self.toggled = msg.data
        if self.toggled and not self.use_keyboard:
            self.alphabot.move_forward(50)
        else:
            self.alphabot.stop()

    def keyboard_listener(self, msg):
        key = msg.data
        if key == 0:
            self.use_keyboard = not self.use_keyboard

        if self.use_keyboard:
            if key == 1:
                self.alphabot.move_forward(50)
            elif key == 2:
                self.alphabot.turn_left(30)
            elif key == 3:
                self.alphabot.move_backward(50)
            elif key == 4:
                self.alphabot.turn_right(30)
            elif key == 5:
                self.alphabot.stop()
            else:
                pass

def main(args=None):
    rclpy.init(args=args)
    node = Motors()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()