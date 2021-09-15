#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32


def callback(message):
    editted_msg=message.data.replace(', ',': ')
    splitted_msg=editted_msg.split(': ')
    name=splitted_msg[1]
    age=int(splitted_msg[3])
    height=int(splitted_msg[5])
    
    pub_name.publish(name)
    pub_age.publish(age)
    pub_height.publish(height)
    
    rospy.loginfo(name)
    rospy.loginfo(age)
    rospy.loginfo(height)
    rospy.loginfo("\n")

rospy.init_node('data_processing')
sub=rospy.Subscriber('raw_data', String, callback)
pub_name = rospy.Publisher('name', String, queue_size=10)
pub_age = rospy.Publisher('age', Int32, queue_size=10)
pub_height = rospy.Publisher('height', Int32, queue_size=10)
rate = rospy.Rate(1) # 1 Hz

rospy.spin()


    
    
