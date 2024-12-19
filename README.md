# alphabot2 Pi Ros2 Demo

This demo is using [Ubuntu 24.04 LTS for Raspberry Pi](https://ubuntu.com/download/raspberry-pi/thank-you?version=24.04.1&architecture=desktop-arm64+raspi) and [ROS 2 Jazzy Jalisco](https://docs.ros.org/en/rolling/Releases/Release-Jazzy-Jalisco.html).

## Install
Make sure Ubuntu packages are up to date 
```shell
sudo apt update && sudo apt upgrade
```
and follow the download instructions provided by the [ROS 2 Jazzy documentation](https://docs.ros.org/en/jazzy/Installation.html).

In addition you will need the `python3-lgpio` and the python package `pyinput`

These can be installed with
```shell
sudo apt install python3-rpi-gpio -y
pip install pyinput
```

In all shells you are going to be working in you will need to let the shell know about ros2 commands. To do this type
```shell
source /opt/ros/jazzy/setup.bash
```

To build go into `alphabot/` and run 
```shell
colcon build --symlink-install
source install/setup.bash
```
Nodes are set to be run individually in their own terminals as they are needed. To run a node you need do 

```shell
ros2 run <node_name> <node_function_name>
```

### Credit
Elijah Morgan<br>
Ram Adesara<br>
Zachary Meyner