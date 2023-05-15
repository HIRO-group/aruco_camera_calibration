from autolab_core import RigidTransform
import numpy as np
import cv2

# touch the TCP of the robot to each of the corners of the AR tag and list the positions here

# use the corresponding corner names from the AR tag
# these are example values from a calibration run on the UR5
#A = np.array([-326, -576, -22]) / 1000
#B = np.array([-190, -582, -22]) / 1000
#C = np.array([-186, -442, -22]) / 1000
#D = np.array([-323, -441, -22]) / 1000


#A = np.array([0.3401459222565844, -0.3067644761673867, 0.010326842649315271])
#B = np.array([0.5434992902768486, -0.3065149743523112, 0.010237746909775566])
#C = np.array([0.5475899406561999, -0.5105068568141249, 0.00953883888660198])
#D = np.array([0.33977253618036735, -0.5114201759265138, 0.009916084193254515])

#A = np.array([0.36211256484530646, 0.3924946460454836, 0.014952089416435901])
#B = np.array([0.5717560328928705, 0.3777180270051756, 0.008963915103340839])
#C = np.array([0.5524347737254306, 0.1721921271168473, 0.012523811421957506])
#D = np.array([0.3474089461456711, 0.18651941975820172, 0.01361394864389108])
A = np.array([0.36682266381602685, 0.23399668595325093, 0.015502010680355172])
B = np.array([0.5672202638844357, 0.21804397432275377, 0.010020977293024938])
C = np.array([0.5513487359529634, 0.01490699308859976, 0.008264110669820149])
D = np.array([0.343547882299845, 0.03163525114022628, 0.00746049688341581])


# compute the center of the tag
center = (A + B + C + D) / 4

# Compute the orientation of the tag in the robot frame
x_axis_ba = (B - A) / np.linalg.norm(B - A)
x_axis_cd = (C - D) / np.linalg.norm(C - D)
x_axis = (x_axis_ba + x_axis_cd) / 2
x_axis = x_axis / np.linalg.norm(x_axis)  # ensure x_axis is a unit vector

y_axis_da = (D - A) / np.linalg.norm(D - A)
y_axis_cb = (C - B) / np.linalg.norm(C - B)
raw_y_axis = (y_axis_da + y_axis_cb) / 2

# Apply the Gram-Schmidt process to make y_axis orthogonal to x_axis
y_axis = raw_y_axis - x_axis * np.dot(raw_y_axis, x_axis)
y_axis = y_axis / np.linalg.norm(y_axis)  # ensure y_axis is a unit vector

# Now compute z_axis as the cross product of x_axis and y_axis (should be orthogonal)
z_axis = np.cross(x_axis, y_axis)

# Compute the rotation matrix
R = np.array([x_axis, y_axis, z_axis]).T

transform = RigidTransform(R, center, from_frame='tag', to_frame='robot')
print("Calculated transform!")
print(transform)

transform.save("T_tag_robot.tf")

