#!/usr/bin/env python
# ---------------------------------------------------
#  Created by Magnus S0rensen for the MAST project
#  byteofsoren@gmail.com   june 26 2018
# ---------------------------------------------------
# ROS - LabView comunitation dummy that emulate the RoboRIO.

import rospy
from std_msgs.msg import String
from ros_labview_dummy.msg import from_rio
from ros_labview.msg import to_rio

# Settings:
subcribe_from_tx2 = 'control_to_rio'
publish_to_tx2 = 'read_rio'

# Globals:
message_from_tx2 = to_rio()
message_to_tx2 = from_rio()
# Create a publisher so data can be sent from the rio to the tx2
pub_handle = rospy.Publisher(publish_to_tx2, data_class=from_rio, queue_size=1)
# Create a subcriber so the it can read the data from the tx2
rospy.init_node(subcribe_from_tx2, anonymous=True)
update_rate = rospy.Rate(100)
set_speed=0
set_steering=0

def send_to_tx2(steering=0, speed=0):
    """Sends return value to the tx2 by publishing

    :steering: steering is a float in degrees
    :speed: speed is a float im m/s
    :returns: None

    """
    message_to_tx2.speed_is = speed
    message_to_tx2.steering_is = steering
    rospy.loginfo(message_to_tx2)
    pub_handle.publish(message_to_tx2)

def read_fom_tx2(data):
    """Subsribing to tx2's information

    :data: TODO
    :returns: TODO

    """
    set_spee = data.set_speed
    set_steering = data.set_steering

def main():
    while not rospy.is_shutdown():
        # Read data from TX2 by subscribing
        rospy.Subscriber(subcribe_from_tx2, to_rio, read_fom_tx2)
        rospy.loginfo("got this from TX2 speed={}, steering={}".format(set_speed, set_steering))
        # Send data to TX2.
        send_to_tx2(3, 5)
        # sleep
        update_rate.sleep()
    pass

if __name__ == "__main__":
    main()
