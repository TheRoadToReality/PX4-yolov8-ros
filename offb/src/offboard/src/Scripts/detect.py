#! /usr/bin/env python2
import cv2
import numpy as np
import rospy
from std_msgs.msg import Int32
rospy.init_node('aim_publisher_node')

cap = cv2.VideoCapture(0)

def detect_blue_circle(image):
    # Define the lower and upper boundaries for the blue color in HSV color space
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Threshold the image to get only blue color
    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    
    # Find contours of the blue color
    _,contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Iterate through each contour
    for contour in contours:
        # Calculate the contour area
        area = cv2.contourArea(contour)
        
        # Approximate the contour to a circle
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
        
        # If the contour is a circle and the area is above a certain threshold
        if len(approx) > 6 and area > 100:
            return True
    
    return False

def detect_blue_triangle(image):

    
    # Define the lower and upper boundaries for the blue color in HSV color space

    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([140, 255, 255])
    
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Threshold the image to get only blue color
    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    
    # Find contours of the blue color
    _,contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Iterate through each contour
    for contour in contours:
        # Calculate the contour area
        area = cv2.contourArea(contour)
        
        # Approximate the contour to a polygon with less vertices
        epsilon = 0.03 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        # If the contour is a triangle and the area is above a certain threshold
        if len(approx) == 3 and area > 100:
            return True
    
    return False
def detect_red_triangle(image):
    
    # Define the lower and upper boundaries for the blue color in HSV color space

    redLower = np.array([0,43,46])
    redUpper = np.array([80,255,255])
    
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Threshold the image to get only blue color
    mask = cv2.inRange(hsv_image, redLower, redUpper)
    
    # Find contours of the blue color
    _,contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Iterate through each contour
    for contour in contours:
        # Calculate the contour area
        area = cv2.contourArea(contour)
        
        # Approximate the contour to a polygon with less vertices
        epsilon = 0.03 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        # If the contour is a triangle and the area is above a certain threshold
        if len(approx) == 3 and area > 100:
            return True
    
    return False

red_t_cont = 0
blue_c_cont = 0

while True:
    #read the video frame
    
    ret, frame = cap.read()
    red_t_result = detect_red_triangle(frame)
    print(red_t_result)
    blue_c_result = detect_blue_circle(frame)
    # detect red block
    if red_t_result == True:
        red_t_cont = red_t_cont + 1
        if red_t_cont >= 5:
            break
    if red_t_result == False:
        red_t_cont = 0
    if blue_c_result == True:
        blue_c_cont = blue_c_cont + 1
        if blue_c_cont >= 5:
            break
    if blue_c_result == False:
        blue_c_cont = 0
        
    cv2.imshow("Red Blocks", frame)
    cv2.waitKey(1)
    
    # press "q" to quit loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
aim = None
if red_t_cont >= 5:
    qstr = "red triangle"
    aim = 1 
elif blue_c_cont >= 5:
    qstr = "blue circle"
    aim = 2
aim_publisher = rospy.Publisher("aim", Int32, queue_size=10)
rate = rospy.Rate(1)
print("success detect"+ qstr)
while not rospy.is_shutdown():
    aim_publisher.publish(aim)
    rate.sleep()
