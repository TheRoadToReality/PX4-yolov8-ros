* AutoDrone-px4
# 基于ROS的自主无人机框架
![image](https://github.com/TheRoadToReality/AutoDrone-px4/blob/main/assets/logo.png#pic_center)
# 硬件架构
```bash
主控:px4(STM32F427Vit6)
ROS算法/视觉运行平台:Nvidia Jetson NX
VIO: T265
动力套:Tmotor 
机械结构：x450
协处理器：ESP32-microROS
```
![image](https://github.com/TheRoadToReality/AutoDrone-px4/blob/main/assets/drone_v1.png#pic_center)
## Dependencies
* Ros:
```bash
wget http://fishros.com/install -O fishros && . fishros

```
* Python-ROS:
* For Ubuntu 18.04 and Under version
```bash
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo apt install python-rosdep
sudo rosdep init
rosdep update
rosversion -d
```
*For Ubnutu 20.04 and above version
```bash
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
```
* librealsense: 
```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE
sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo $(lsb_release -cs) main" -u
sudo apt-get install librealsense2-utils
sudo apt-get install librealsense2-dev
```


## Installation
安装ROS1

1. 安装catkin工具链:

   ```bash
   sudo apt install python-catkin-tools

   ```

1. 克隆这个仓库

   ```bash
   git clone  https://github.com/TheRoadToReality/AutoDrone-px4.git
   cd AutoDrone-px4/catkin_ws
   catkin clean

   ```

1. 安装 MAVROS
   * Kinetic(Ubuntu 16.04)
     ```bash
     sudo apt install ros-kinetic-mavros ros-kinetic-mavros-extras
     ```
   * Melodic(Ubuntu 18.04)
     ```bash
     sudo apt install ros-melodic-mavros ros-melodic-mavros-extras
     ```
   * Noetic(Ubuntu 20.04)
     ```
     sudo apt install ros-noetic-mavros ros-noetic-mavros-extras
1. 安装地理信息图集 [GeographicLib] 
   ```bash
   wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh
   sudo bash ./install_geographiclib_datasets.sh   
   ```

1. Install the [realsense2_camera] 在ROS中启动T265:
   * Kinetic(Ubuntu 16.04)
   ```bash
   sudo apt install ros-Kinedic-realsense2-camera
   ```
   * Melodic(Ubuntu 18.04)
   ```bash
   sudo apt install ros-melodic-realsense2-camera
   ```
   * Noetic(Ubuntu 20.04)
   ```bash
   sudo apt install ros-noetic-realsense2-camera ros-noetic-cv-bridge libopencv-dev

   ```

1. 安装ROS点云库 (PCL):

   * Melodic
     ```bash
     sudo apt install ros-melodic-pcl-ros
     ```
   * Kinetic
     ```bash
     sudo apt install ros-kinetic-pcl-ros
     ```
   * Noetic
     ```bash
     sudo apt install ros-noetic-pcl-ros

1. 编译这个package:

   ```bash
   cd ~/Autodrone_px4/catkin_ws
   catkin build px4_realsense_bridge
   ```

1. 启动ROS节点:

   ```bash
   source ./devel/catkin_ws/devel/setup.bash
   roslaunch px4_realsense_bridge bridge_mavros.launch
   ```
1. 启动外部控制文件:
   ```bash
   cd /Autodrone_px4/offboard
   catkin build
   Run
   ```
# 功能介绍
* 自主跟踪（已完成）
* 自主避障（已完成）
* 路径规划（已完成）
* 外部机械臂（待开发）
* T265_VIO SLAM（已完成）
* 激光雷达SLAM（待开发）
* 集群算法（已完成）
* 示教模式<无人机飞到曾经飞过的位置>(已完成)
* 迁移到自制飞控(开发中..)
* 增加中....
