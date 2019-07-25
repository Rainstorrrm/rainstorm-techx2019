#!/usr/bin/env python

import rospy, time
from geometry_msgs.msg import Twist

def spin():
    pub = rospy.Publisher('car/cmd_vel', Twist, queue_size=10)
    rospy.init_node('publisher')
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = Twist()
    	msg.angular.z = 66
        pub.publish(msg)
	time.sleep(1)
	msg.linear.x = 1580
	pub.publish(msg)
	time.sleep(1)
	msg.linear.x = 1500
	pub.publish(msg)
	time.sleep(1)
    	msg.angular.z = 90
        pub.publish(msg)
        time.sleep(1)
	msg.angular.z = 114
        pub.publish(msg)
        time.sleep(1)
	msg.linear.x = 1360
	pub.publish(msg)
	time.sleep(1)
        msg.linear.x = 1500
        pub.publish(msg)
        time.sleep(0.5)
	msg.linear.x = 1360
	pub.publish(msg)
	time.sleep(1)
	msg.linear.x = 1500
	pub.publish(msg)
	time.sleep(1)
    	

if __name__ == '__main__':
    try:
        spin()
    except rospy.ROSInterruptException:
        pass
