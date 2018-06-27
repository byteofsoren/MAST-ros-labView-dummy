#!/usr/bin/env python
# ---------------------------------------------------
#  Created by Magnus S0rensen for the MAST project
#  byteofsoren@gmail.com   june 26 2018
# ---------------------------------------------------

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size = 10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10Hz
    while not rospy.is_shutdown():
        hello_str = "Hello word from the dummy and the time is {}".format(rospy.get_time())
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__== '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        print("An error have ocured")
        pass
