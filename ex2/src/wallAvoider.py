#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from pdb import set_trace
import numpy as np
class wallAvoider:
    def __init__(self):
        rospy.init_node('wallAvoider')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.sub=rospy.Subscriber('/kobuki/laser/scan',LaserScan,self.subCallback) 
        self.rate = rospy.Rate(2)
        self.move = Twist()

    def subCallback(self,msg):
        # print(msg)
        # find index of right and left:
        # np.count_nonzero(np.array(np.where(np.isinf(x)))<=234)
        # 90 degree is front of robot. 
        msgArray = np.array(msg.ranges)
        # print(msgArray.shape)
        right = msgArray[0:235] 
        center = msgArray[235:485] 
        # left = msgArray[485:] 
        # set_trace()

        if np.any(center<= 1) :
            print("detected on center")
            self.stop()
            self.rotate('left')
        elif np.any(right<= 1):
            print("detected on right")
            self.rotate('left')
        else:
            print("move forward")
            self.moveForward()

    def stop(self):
        self.move.linear.x = 0
        self.move.linear.y = 0
        self.move.linear.z = 0
        self.move.angular.x = 0
        self.move.angular.y = 0
        self.move.angular.z = 0
        self.pub.publish(self.move)

    def moveForward(self):
        self.move.linear.x = 0.5
        self.move.linear.y = 0
        self.move.linear.z = 0
        self.move.angular.x = 0
        self.move.angular.y = 0
        self.move.angular.z = 0
        self.pub.publish(self.move)

    def rotate(self,dir):
        self.move.linear.x = 0
        self.move.linear.y = 0
        self.move.linear.z = 0
        self.move.angular.x = 0
        self.move.angular.y = 0
        self.move.angular.z = -0.5 if dir == 'right' else 0.5
        self.pub.publish(self.move)

if __name__ == '__main__':
    wa = wallAvoider()
    rospy.spin( ) 
    # while not rospy.is_shutdown():
    # pub.publish(move)
    # rate.sleep()


