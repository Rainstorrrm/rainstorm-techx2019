#!/usr/bin/env python

import rospy, time
from geometry_msgs.msg import Twist
length = 0.5

#当投进了，或者已经跑到主人这里了, 
def celebrate():
    pub = rospy.Publisher('car/cmd_vel', Twist, queue_size=10)
    rospy.init_node('publisher')
    
    while not rospy.is_shutdown():
        msg = Twist()
        msg.angular.z = 66
        pub.publish(msg)
        time.sleep(length)
        msg.angular.z = 114
        pub.publish(msg)
        time.sleep(length)
      
if __name__ == '__main__':
    try:
        celebrate()
    except rospy.ROSInterruptException:
        pass
