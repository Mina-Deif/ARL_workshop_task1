#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def subscriber():
	sub = rospy.Subscriber('raw_data', String, callback)
	rospy.spin()
    
def callback(message):
	editted_msg=message.data.replace(', ',': ')
	splitted_msg=editted_msg.split(': ')
	name=splitted_msg[1]
	age=int(splitted_msg[3])
	height=int(splitted_msg[5])
	rospy.loginfo("%s" %name)	
	rospy.loginfo("%d" %age)
	rospy.loginfo("%d" %height)		

if __name__ == '__main__':
   rospy.init_node('data_processing')
   subscriber()
