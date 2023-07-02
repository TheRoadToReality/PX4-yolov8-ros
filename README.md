# AutoDrone-px4
#基于ROS的无人机自动飞行
![image](https://github.com/TheRoadToReality/AutoDrone-px4/blob/main/assets/logo.png)

# VIO (Visual Inertial Odometry)
这个包使用t265作为视觉里程计
## Dependencies
* Ros:
```bash
wget http://fishros.com/install -O fishros && . fishros

```
* Python-ROS:
```bash
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo apt install python-rosdep
sudo rosdep init
rosdep update
rosversion -d
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
   git clone https://github.com/dbaldwin/VIO.git
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
   ```bash
   sudo apt install ros-melodic-realsense2-camera
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
   cd /文件名/catkin_ws
   catkin build px4_realsense_bridge
   ```

1. 启动ROS节点:

   ```bash
   source ~/文件名/catkin_ws/devel/setup.bash
   roslaunch px4_realsense_bridge bridge_mavros.launch
   ```
1. 启动外部控制文件:
   ```bash
   cd /文件名/offb
   catkin build
   Run the Scripts in Script/
   ```
