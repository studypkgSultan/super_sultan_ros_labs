from setuptools import find_packages, setup

package_name = 'super_sultan_pub_sub_pkg'

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
    maintainer='sultan',
    maintainer_email='Sultan.zharmukhambetov@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'talker = super_sultan_pub_sub_pkg.talker:main',
            'listener = super_sultan_pub_sub_pkg.listener:main',
            'even_pub = super_sultan_pub_sub_pkg.even_number_publisher:main',
            'overflow_listener = super_sultan_pub_sub_pkg.overflow_listener:main',
        ],
    },
)
