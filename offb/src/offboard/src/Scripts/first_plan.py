"""
 * File: offb_node.py
 * Stack and tested in Gazebo Classic 9 SITL
"""

#! /usr/bin/env python2

import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, CommandBoolRequest, SetMode, SetModeRequest
from std_msgs.msg import Int32
current_state = State()

def state_cb(msg):
    global current_state
    current_state = msg

#def waypoint(msg):
#   x_location = msg.pose.position.x
#   y_location = msg.pose.position.y
#   z_location = msg.pose.position.z
#  return x_location,y_location,z_location    
if __name__ == "__main__":
    rospy.init_node("plan1")


#    now_pos_pub = rospy.Subscriber("mavros/local_position/pose",PoseStamped, callback=waypoint)
    local_pos_pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size=10)
    state_sub = rospy.Subscriber("mavros/state", State, callback = state_cb)
    rospy.wait_for_service("/mavros/cmd/arming")
    arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)

    rospy.wait_for_service("/mavros/set_mode")
    set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)


    # Setpoint publishing MUST be faster than 2Hz
    rate = rospy.Rate(20)

    # Wait for Flight Controller connection
    while(not rospy.is_shutdown() and not current_state.connected):
        rate.sleep()
 # init a posestamped actor
    pose = PoseStamped()
    pose.pose.position.x = 0
    pose.pose.position.y = 0
    pose.pose.position.z = 0.6
   

    # Send a few setpoints before starting

    a = input()
    if (a == 1):
        x_1 = 0.44
        y_1 = 1.80

    b = input()
    if(b ==2 ):
        x_2 = 1.42
        y_2 = 0.90
    for i in range(100):
        if(rospy.is_shutdown()):
            break

        local_pos_pub.publish(pose)
        rate.sleep()

        offb_set_mode = SetModeRequest()
        offb_set_mode.custom_mode = 'OFFBOARD'

        arm_cmd = CommandBoolRequest()
        arm_cmd.value = True

        land_set_mode = SetModeRequest()
        land_set_mode.custom_mode = "AUTO.LAND"

        last_req = rospy.Time.now()
        flag   =  0
        while not rospy.is_shutdown():
            if current_state.mode != "OFFBOARD" and (rospy.Time.now() - last_req) > rospy.Duration(5.0):
                if set_mode_client.call(offb_set_mode).mode_sent == True:
                    rospy.loginfo("OFFBOARD enabled")
                last_req = rospy.Time.now()
            elif not current_state.armed and (rospy.Time.now() - last_req) > rospy.Duration(5.0):
                if arming_client.call(arm_cmd).success == True:
