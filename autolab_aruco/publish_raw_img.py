#!/usr/bin/env python

from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import rospy
import camera_info_manager
from sensor_msgs.msg import CameraInfo
from logitech import Camera
import os
import argparse
import numpy as np


bridge = CvBridge()


def main():
    camera = 'logitech'
    frame_id = 'logitech_frame'

    parser = argparse.ArgumentParser()
    parser.add_argument('--cam')
    args = parser.parse_args()

    cam = Camera(args.cam)

    rospy.init_node("img_publisher", anonymous=True)
    img_pub = rospy.Publisher("/" + camera + "/image", Image,
                              queue_size=10)
    info_pub = rospy.Publisher("/" + camera + "/camera_info", CameraInfo,
                               queue_size=10)


    info_url = 'file:///camera.yaml'  # TODO: fix
    info_manager = camera_info_manager.CameraInfoManager(cname=camera,
                                                         url=info_url,
                                                         namespace=camera)
    info_manager.loadCameraInfo()

    while not rospy.is_shutdown():
        rgb_img = cam.get_rgb_img()

        rate = rospy.Rate(30)
        try:
            # Publish image.
            img_msg = bridge.cv2_to_imgmsg(rgb_img, 'bgr8')
            img_msg.header.stamp = rospy.Time.now()
            img_msg.header.frame_id = frame_id
            img_pub.publish(img_msg)

            info_msg = info_manager.getCameraInfo()
            info_msg.header = img_msg.header
            info_msg.height = 480
            info_msg.width = 640
            info_msg.distortion_model = 'plumb_bob'
            info_msg.D = [0, 0, 0, 0, 0]
            info_msg.K = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            info_msg.R = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            info_msg.P = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            info_pub.publish(info_msg)
        except CvBridgeError as err:
            print(err)

        rate.sleep()

    return


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

