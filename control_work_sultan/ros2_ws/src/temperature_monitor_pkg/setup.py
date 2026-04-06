from setuptools import setup
import os
from glob import glob

package_name = 'temperature_monitor_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Sultan',
    maintainer_email='sultan@example.com',
    description='Temperature monitoring system for ROS 2',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temperature_sensor = temperature_monitor_pkg.temperature_sensor:main',
            'temperature_monitor = temperature_monitor_pkg.temperature_monitor:main',
        ],
    },
)
