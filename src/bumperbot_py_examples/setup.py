from setuptools import setup

package_name = 'bumperbot_py_examples'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='antonio.brandi@outlook.it',
    description='ROS 2 Code Examples',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_publisher = bumperbot_py_examples.simple_publisher:main',
            'simple_subscriber = bumperbot_py_examples.simple_subscriber:main',
            'simple_parameter = bumperbot_py_examples.simple_parameter:main',
            'simple_turtlesim_kinematics = bumperbot_py_examples.simple_turtlesim_kinematics:main',
            'simple_service_server = bumperbot_py_examples.simple_service_server:main',
            'simple_service_client = bumperbot_py_examples.simple_service_client:main',
            'simple_tf_kinematics = bumperbot_py_examples.simple_tf_kinematics:main',
            'simple_action_server = bumperbot_py_examples.simple_action_server:main',
            'simple_action_client = bumperbot_py_examples.simple_action_client:main',
            'simple_qos_publisher = bumperbot_py_examples.simple_qos_publisher:main',
            'simple_qos_subscriber = bumperbot_py_examples.simple_qos_subscriber:main',
        ],
    },
)