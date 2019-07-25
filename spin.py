#!/usr/bin/env python

import rospy, time
from geometry_msgs.msg import Twist

def forward(speed,angle,time):
    msg = Twist()
    msg.angular.z = angle
    msg.linear.x = speed
    pub.publish(msg)
    time.sleep(time)
    return

def backward(speed,angle,time):
    msg = Twist()
    msg.angular.z = 90
    msg.linear.x = 

def spin():
    step = 0.4
    step_stop = 1
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
	msg.linear.x = 1420
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
