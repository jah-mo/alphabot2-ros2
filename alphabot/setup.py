from setuptools import find_packages, setup

package_name = 'alphabot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "sensors_node = alphabot.sensors:main",
            "motors_node = alphabot.motors:main",
            "button_node = alphabot.button:main",
            "keyboard_node = alphabot.keyboard:main",
        ],
    },
)
