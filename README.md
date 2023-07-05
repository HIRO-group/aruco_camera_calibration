See the calibration guide [here](https://github.com/HIRO-group/aruco_camera_calibration/wiki/Calibration-Guide).

---

# ArUCo-Markers-Pose-Estimation-Generation-Python

Forked from [here.](https://github.com/GSNCodes/ArUCo-Markers-Pose-Estimation-Generation-Python)

This repository contains all the code you need to generate an ArucoTag, estimate the pose of ArucoTags in images, estimate the pose of the tag in the robot frame, and calculate a camera-to-robot transform.

<img src = 'autolab_aruco/Images/pose_output_image.png' width=400 height=400>

## 0. Getting Started
Run `git clone https://github.com/BerkeleyAutomation/aruco_camera_calibration`. Then, `cd aruco_camera_calibration` and then run `pip install -e .` to install the dependencies.

## 1. ArUCo Marker Generation
The file `generate_aruco_tags.py` contains the code for ArUCo Marker Generation.
You need to specify the type of marker you want to generate.

The command for running is :-  
`python generate_aruco_tags.py --id 1 --type DICT_5X5_100 --output tags/`
You can find more details on other parameters using `python generate_aruco_tags.py --help`.

You can print out these tags, but make sure that you precisely measure the size of these markers once they are printed for accurate pose estimation (and input them into the next script.)

## 2. Finding Camera Intrinsics
If intrinsics and distortion coefficients for your camera are known, you may skip this section. You may be able to find ways to obtain these for each model of camera by looking at the `BerkeleyAutomation/perception` repo or searching them up.

The file `find_camera_intrinsics.py` contains the code necessary for calibrating your camera. This step has several pre-requisites. You need to have a folder containing a set of checkerboard images taken using your camera. Make sure that these checkerboard images are of different poses and orientation. You need to provide the path to this directory and the size of the square in metres. You can also change the shape of the checkerboard pattern using the parameters given. Make sure this matches with your checkerboard pattern. You will need to paste the values from this step into the code for pose estimation.

The command for running is :-  
`python find_camera_intrinsics.py --dir calibration_checkerboard/ --square_size 0.024`

You can find more details on other parameters using `python calibration.py --help`.

## 3. Tag Pose Estimation
Enter your values for k and d (camera intrinsics) as well as the tag side length into the code and then run this code. The file `tag_to_camera.py` contains the code that performs pose estimation after detecting the ArUCo markers. You need to specify the path to an image to run this on. This will print the transform and generate a file called `T_tag_cam.tf`.

The command for running is :-  
`python autolab_aruco/tag_pose_estimation.py -i path/to/image.png`  

## 4. Robot to Camera Transform
There are still missing pieces if you wish to calculate the transform between the robot and camera. The most common way of doing this is by touching the robot tooltip to the four corners of the tag and recording the tooltip translations relative to the robot frame in `tag_to_camera.py`. This will print the transform and generate a file called `T_tag_cam.tf`.

## 5. Camera to Robot Transform
To get the camera to robot transform, run `camera_to_robot.py`, which will load in the transforms generated previously and output `T_cam_robot.tf`.

## 6. Example Point Projection
See `pixel_to_robot_coord.py` for an example on how to convert a pixel coordinate (with depth information) to a workspace coordinate. 

## Output

<img src ='autolab_aruco/Images/output_sample.png' width = 400>  

<img src ='autolab_aruco/Images/pose_output.gif'>

### <ins>Notes</ins>
The `utils.py` contains the ArUCo Markers dictionary and the other utility function to display the detected markers.

Feel free to reach out to me in case of any issues.  
If you find this repo useful in any way please do star ⭐️ it so that others can reap it's benefits as well.

Happy Learning! Keep chasing your dreams!

## References
1. https://docs.opencv.org/4.x/d9/d6d/tutorial_table_of_content_aruco.html
2. https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html
