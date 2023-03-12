from autolab_core import RigidTransform
import numpy as np
import cv2

# use the corresponding corner names from the AR tag
# these are example values from a calibration run on the UR5
A = np.array([-326, -576, -22]) / 1000
B = np.array([-190, -582, -22]) / 1000
C = np.array([-186, -442, -22]) / 1000
D = np.array([-323, -441, -22]) / 1000

# compute the center of the tag
center = (A + B + C + D) / 4

# compute the orientation of the tag in the robot frame
x_axis_ba = (B - A) / np.linalg.norm(B - A)
x_axis_cd = (C - D) / np.linalg.norm(C - D)
x_axis = (x_axis_ba + x_axis_cd) / 2

y_axis_da = (D - A) / np.linalg.norm(D - A)
y_axis_cb = (C - B) / np.linalg.norm(C - B)
y_axis = (y_axis_da + y_axis_cb) / 2

z_axis = np.cross(x_axis, y_axis_da)

# compute the rotation matrix
R = np.array([x_axis, y_axis, z_axis]).T

transform = RigidTransform(R, center, from_frame='tag', to_frame='robot')
print("Calculated transform!")
print(transform)

transform.save("T_tag_to_robot.tf")