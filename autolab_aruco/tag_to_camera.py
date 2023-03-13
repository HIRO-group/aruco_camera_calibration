'''
Sample Usage:-
python pose_estimation.py --K_Matrix calibration_matrix.npy --D_Coeff distortion_coefficients.npy --type DICT_5X5_100
'''

import numpy as np
import cv2
import sys
from utils import ARUCO_DICT
import argparse
import time
from autolab_core import RigidTransform
from matplotlib import pyplot as plt

def rvec_tvec_to_transform(rvec, tvec):
    '''
    convert translation and rotation to pose
    '''
    if rvec is None or tvec is None:
        return None

    R = cv2.Rodrigues(rvec)[0]
    t = tvec
    return RigidTransform(R, t, from_frame='tag', to_frame='cam')


def pose_estimation(frame, aruco_dict_type, matrix_coefficients, distortion_coefficients, tag_length):
    '''
    frame - Frame from the video stream
    matrix_coefficients - Intrinsic matrix of the calibrated camera
    distortion_coefficients - Distortion coefficients associated with your camera

    return:-
    frame - The frame with the axis drawn on it
    '''
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.aruco_dict = cv2.aruco.Dictionary_get(aruco_dict_type)
    parameters = cv2.aruco.DetectorParameters_create()

    corners, ids, _ = cv2.aruco.detectMarkers(gray, cv2.aruco_dict, parameters=parameters)

    if len(corners) == 0 or len(ids) == 0:
        raise Exception("No Aruco markers detected in the image!")

    # If markers are detected
    rvec, tvec = None, None
    if len(corners) > 0:
        for i in range(0, len(ids)):
            # Estimate pose of each marker and return the values rvec and tvec---(different from those of camera coefficients)
            rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners[i], tag_length, matrix_coefficients,
                                                                           distortion_coefficients)
            # Draw a square around the markers
            cv2.aruco.drawDetectedMarkers(frame, corners)

            # Draw Axis
            cv2.drawFrameAxes(frame, matrix_coefficients, distortion_coefficients, rvec, tvec, 0.01)
    return frame, rvec, tvec

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--type", type=str, default="DICT_ARUCO_ORIGINAL", help="Type of ArUCo tag to detect")
    ap.add_argument("-i", "--image_path", required=True, help="Path to image containing ArUCo tag to estimate the pose of.")

    args = vars(ap.parse_args())

    if ARUCO_DICT.get(args["type"], None) is None:
        print(f"ArUCo tag type '{args['type']}' is not supported")
        sys.exit(0)

    aruco_dict_type = ARUCO_DICT[args["type"]]

    # load the input image from disk, convert it to grayscale, and detect
    # ArUCo markers in the image
    image = cv2.imread(args["image_path"])

    # Etch ZED parameters (example)
    # k = np.array(
    #     [[1376.21533203125, 0.0, 1113.4146728515625], [0.0, 1376.21533203125, 612.0199584960938], [0.0, 0.0, 1.0]])
    # d = np.array([0.0, 0.0, 0.0, 0.0, 0.0])

    # BWW UR5 RealSense parameters
    k = np.array(
        [[384.793, 0., 324.277],
        [0., 384.422, 241.649],
        [0., 0., 1.]]
    )
    d = np.array([0.0, 0.0, 0.0, 0.0, 0.0])

    # tag dimensions
    l = 0.136

    # display the K and D matrices to confirm they are correct with the user
    print("K Matrix: ")
    print(k)
    print("Distortion Coefficients: ")
    print(d)
    print("Tag length (m):")
    print(l)
    input("Confirm K and D are correct for your camera, and that the tag side length is correct, then press Enter to continue...")
    output, rvec, tvec = pose_estimation(image, aruco_dict_type, k, d, l)
    pose = rvec_tvec_to_transform(rvec, tvec)

    plt.title("Estimated pose")
    plt.imshow(output[..., ::-1])
    plt.show()
    input("Do the drawn axes look correct?")

    print("Calculated RigidTransform", pose)
    # save the RigidTransform to disk
    pose.save('T_tag_cam.tf')
    print("Saved to disk!")
