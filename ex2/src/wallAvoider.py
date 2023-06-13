#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
class wallAvoider:
    def __init__(self):
        rospy.init_node('wallAvoider')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.sub=rospy.Subscriber('/kobuki/laser/scan',LaserScan,self.subCallback) 
        self.rate = rospy.Rate(2)
        self.move = Twist()

    def subCallback(self,msg):
        print(msg)

        self.moveForward()
        self.rate.sleep()

        self.rotate('right')
        self.rate.sleep()

        self.moveForward()
        self.rate.sleep()

        self.rotate('right')
        self.rate.sleep()

        self.stop()
        self.rate.sleep()


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


