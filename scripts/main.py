#!/usr/bin/env python
# ---------------------------------------------------
#  Created by Magnus S0rensen for the MAST project
#  byteofsoren@gmail.com   june 26 2018
# ---------------------------------------------------
# ROS - LabView comunitation dummy that emulate the RoboRIO.

import rospy
from std_msgs.msg import String
from ros_labview_dummy import from_rio
from ros_labviw import to_rio

# Settings:
subcribe_from_tx2 = 'control_to_rio'
publish_to_tx2 = 'read_rio'

# Globals:
message_from_tx2 = to_rio()
message_to_tx2 = from_rio()
# Create a publisher so data can be sent from the rio to the tx2
pub_handle = rospy.Publisher(publish_to_tx2, data_class=from_rio)
update_rate = rospy.Rate(100)
# Create a subcriber so the it can read the data from the tx2
rospy.init_node(subcribe_from_tx2, anonymous=True)
set_speed=0
set_steering=0

def main():
    pass

if __name__ == "__main__":
    main()
