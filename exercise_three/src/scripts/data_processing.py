#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from exercise_three.msg import custom_msg


def callback(message):
    editted_msg=message.data.replace(', ',': ')
    splitted_msg=editted_msg.split(': ')
    msg_to_publish=custom_msg()
    msg_to_publish.name=splitted_msg[1]
    msg_to_publish.age=int(splitted_msg[3])
    msg_to_publish.height=int(splitted_msg[5])
    
    pub.publish(msg_to_publish)
    
    rospy.loginfo(msg_to_publish.name)
    rospy.loginfo(msg_to_publish.age)
    rospy.loginfo(msg_to_publish.height)
    rospy.loginfo("\n")


rospy.init_node('data_processing')
sub=rospy.Subscriber('raw_data', String, callback)
pub = rospy.Publisher('user_info', custom_msg, queue_size=10)
rate = rospy.Rate(1) # 1 Hz

rospy.spin()
