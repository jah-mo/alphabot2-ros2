import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from pynput import keyboard

class KeyPressNode(Node):
    def __init__(self):
        super().__init__('keyboard_node')

        self.keyboard_publisher = self.create_publisher(
            Int32,
            'keyboard/key_press',
            10
        )

        # Start the pynput listener
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        self.listener.start()


    def on_press(self, key):
        msg = Int32()
        if key == keyboard.Key.space:
            msg.data = 0
        elif key.char == 'w':
            msg.data = 1
        elif key.char == 'a':
            msg.data = 2
        elif key.char == 's':
            msg.data = 3
        elif key.char == 'd':
            msg.data = 4
        else:
            msg.data = 5

        self.keyboard_publisher.publish(msg)

    def on_release(self, key):
        msg = Int32()
        msg.data = 5
        self.keyboard_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = KeyPressNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.listener.stop()  # Stop pynput listener when shutting down
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()