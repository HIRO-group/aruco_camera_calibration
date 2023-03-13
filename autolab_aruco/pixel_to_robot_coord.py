import numpy as np
from autolab_core import RigidTransform

def pixel_depth_to_robot_coord(pixel_x, pixel_y, depth, cam_to_robot, k):
    # TODO (undistortion)

    pixel_homog = np.array([pixel_x, pixel_y, 1.0])
    pixel_homog = np.expand_dims(pixel_homog, axis=1)
    pixel_homog = np.matmul(np.linalg.inv(k), pixel_homog)

    pixel_homog = pixel_homog * depth
    pixel_homog = np.append(pixel_homog, 1.0)
    pixel_homog = np.expand_dims(pixel_homog, axis=1)

    return cam_to_robot.matrix @ pixel_homog

if __name__ == "__main__":
    # TODO (read from file)
    cam_to_robot = RigidTransform.load("T_cam_robot.tf")

    k = np.array(
        [[384.793, 0., 324.277],
        [0., 384.422, 241.649],
        [0., 0., 1.]]
    )
    pixel_x = 0
    pixel_y = 0
    depth = 1.0
    print(pixel_depth_to_robot_coord(pixel_x, pixel_y, depth, cam_to_robot, k))