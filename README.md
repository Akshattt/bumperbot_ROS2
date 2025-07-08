# BumperBot – ROS 2 SLAM & Localization Robot
## Features


- 🌍 Real-time 2D SLAM using [`slam_toolbox`](https://github.com/SteveMacenski/slam_toolbox)
- 🧭 AMCL-based global localization with map server
- 🎮 Manual joystick teleoperation
- 🧩 Lifecycle node management via `nav2_lifecycle_manager`
- 🧠 Parameterized using YAML configs for both SLAM and localization
- 🖼️ Visualization in RViz 2 with dynamic frame transforms


## 🚀 Launch Instructions
- open terminal
- go to the workspace using cd workspace/
- Use command given below:
- ros2 launch bumperbot_bringup simulated_robot.launch.py use_slam:=true world_name:=small_house

### How It Works
