#include "../../include/PX4_realsense_bridge/PX4_realsense_bridge.h"

using namespace bridge;

int main(int argc, char** argv) {
  ros::init(argc, argv, "PX4_realsense_bridge_node");
  ros::NodeHandle nh("~");
  PX4_Realsense_Bridge Bridge(nh);

  ros::spin();

  Bridge.worker_.join();

  return 0;
}
