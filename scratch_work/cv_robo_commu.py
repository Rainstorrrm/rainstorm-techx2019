##第一个写法，现在看来较复杂
def detect_spitball():
  rospy.init_node('spitball')
  pub = rospy.Publisher('spitball_detector', Bool, queue_size=10)
  rate = rospy.Rate(2) #send it each 1/2 sec 
  found = Bool()
  found = False
  while not found:
    #此处省略cv的code 
    found = True
  pub.publish(found) 
  
#再写一个subscribe的；pub把found是publish到‘spitball_detector‘这个topic；所以我的小车subscribe这个topic就好了
def stop_spinning(found):
  if found
    pub = rospy.Publisher('car/cmd_vel', Twist, queue_size=10)
    rospy.init_node('publisher')
    msg.linear.x = 1500
	  msg.angular.z = 90
	  pub.publish(msg)
  
def spitball_listener():
  rospy.init_node('spinner')
  rospy.Subscribe('spitball_detector', Bool, stop_spinning)
  
  
  
  
##第二个写法：
def 
  while found_spitball()=False:
    spin()
  ##找到了 停下
  msg.linear.x = 1500
  msg.angular.z = 90
  pub.publish(msg)
  time.sleep(0.5)
  msg.linear.x = 1500
  msg.angular.z = 90
  pub.publish(msg)
  time.sleep(0.5)  
