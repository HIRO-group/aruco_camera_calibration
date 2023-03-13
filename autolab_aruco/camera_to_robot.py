from autolab_core import RigidTransform
import numpy as np

tag_to_robot = RigidTransform.load("T_tag_robot.tf")
tag_to_cam = RigidTransform.load("T_tag_cam.tf")
# print(tag_to_robot)
# print(tag_to_cam)

tag_to_cam.rotation = RigidTransform.y_axis_rotation(-1.5 * np.pi / 180)

cam_to_robot = tag_to_robot * tag_to_cam.inverse()
print(cam_to_robot)
cam_to_robot.save("T_cam_robot.tf")