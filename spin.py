#!/usr/bin/env python

import rospy, time
from geometry_msgs.msg import Twist
forward_speed = 1600
backward_speed = 1440
stop_time = 0.1

def forward_right(time):
    msg = Twist()
    msg.angular.z = 66
    msg.linear.x = forward_speed
    pub.publish(msg)
    time.sleep(time)
    msg.angular.z = 90
    return

#refresh is for preparing to go backward because the the robocar has to back twice to actually back
def refresh():
    msg = Twist()
    msg.angular.z = 90
    msg.linear.x = 1420    

def backward_left(time):
    msg = Twist()
    msg.angular.z = 90
    msg.linear.x = 1420   
    pub.publish(msg)
    time.sleep(0.1)
#now it is actually going back
    msg.angular.z = 114
    msg.linear.x = backward_speed
    pub.publish(msg)
    time.sleep(time)
    msg.angular.z = 90
    return

def spin():
    backward_time = 1
    forward_time = 1
    pub = rospy.Publisher('car/cmd_vel', Twist, queue_size=10)
    rospy.init_node('publisher')
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = Twist()
    	msg.angular.z = 66
        pub.publish(msg)
	time.sleep(step)
	msg.linear.x = 1600
	pub.publish(msg)
	time.sleep(step)
	msg.linear.x = 1500
	msg.angular.z = 90
	pub.publish(msg)
	time.sleep(step_stop)
	msg.angular.z = 114
        pub.publish(msg)
        time.sleep(step)
	msg.linear.x = 1460
	pub.publish(msg)
	time.sleep(0.1)
        msg.linear.x = 1500
        pub.publish(msg)
        time.sleep(0.1)
	msg.linear.x = 1460
	pub.publish(msg)
	time.sleep(1)
	msg.linear.x = 1500
	msg.angular.z = 90
	pub.publish(msg)
	time.sleep(1)
    	

if __name__ == '__main__':
    try:
        spin()
    except rospy.ROSInterruptException:
        pass
