#!/usr/bin/env python
import rospy
from std_msgs.msg import String

name=input("Enter name")
age=int(input("Enter age"))
height=int(input("Enter height"))

def publisher():
	pub = rospy.Publisher('raw_data', String, queue_size=10)
    
	rate = rospy.Rate(1) # 1 Hz
	msg_to_publish = String()
    
    
    
	while not rospy.is_shutdown():
		string_to_publish = "name: %s, age: %d, height: %d" %(name,age,height) 
		msg_to_publish.data = string_to_publish
		pub.publish(msg_to_publish)
		rospy.loginfo(string_to_publish)
        
		rate.sleep()

if __name__ == '__main__':
	rospy.init_node('user_info_driver')
	publisher()
