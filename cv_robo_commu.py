
def detect_pitball():
  rospy.init_node('pitball')
  pub = rospy.Publisher('pitball_detector', Bool, queue_size=10)
  rate = rospy.Rate(2) #send it each 1/2 sec 
  found = False
  while not found:
    #此处省略cv的code 
    found = True
  pub.publish(found) 
  
  
#再写一个subscribe的；pub把found是publish到‘pitball_detector‘这个topic；所以我的小车subscribe这个topic就好了
def pitball_listener():
  rospy.init_node('spinner')
  rospy.Subscribe('pitball_detector', Bool, queue_size=10)
  
  
