# ArUCo-Markers-Pose-Estimation-Generation-Python

Forked from [here.s](https://github.com/GSNCodes/ArUCo-Markers-Pose-Estimation-Generation-Python)

This repository contains all the code you need to generate an ArucoTag,
and estimate the pose of ArucoTags in images. There is also code to obtain the calibration matrix for your, and an example file to compute a transform between the robot and ArUCo marker as used for the surgical thread tracking project.

<img src = 'Images/pose_output_image.png' width=400 height=400>

## 0. Getting Started
Run `git clone https://github.com/BerkeleyAutomation/aruco_camera_calibration`.

## 1. ArUCo Marker Generation
The file `generate_aruco_tags.py` contains the code for ArUCo Marker Generation.
You need to specify the type of marker you want to generate.

The command for running is :-  
`python generate_aruco_tags.py --id 1 --type DICT_5X5_100 --output tags/`
You can find more details on other parameters using `python generate_aruco_tags.py --help`.

You can print out these tags, but make sure that you precisely measure the size of these markers once they are printed for accurate pose estimation.

## 2. Calibration
If intrinsics and distortion coefficients for your camera are known, you may skip this section.

The file `calibration.py` contains the code necessary for calibrating your camera. This step has several pre-requisites. You need to have a folder containing a set of checkerboard images taken using your camera. Make sure that these checkerboard images are of different poses and 
orientation. You need to provide the path to this directory and the size of the square in metres. You can also change the shape of the checkerboard pattern using the parameters given. Make sure this
matches with your checkerboard pattern. This code will generate two numpy files `calibration_matrix.npy` and `distortion_coefficients.npy`. You will need to paste the values from this step into the code for pose estimation.

The command for running is :-  
`python calibration.py --dir calibration_checkerboard/ --square_size 0.024`

You can find more details on other parameters using `python calibration.py --help`.

## 3. Pose Estimation  
The file `pose_estimation.py` contains the code that performs pose estimation after detecting the 
ArUCo markers. You need to specify 
the path to the camera calibration matrix and distortion coefficients obtained from the previous step as well 
as the type for ArUCo marker you want to detect. Note that this code could be easily modified to perform 
pose estimation on images and video files.  

The command for running is :-  
`python pose_estimation.py --K_Matrix calibration_matrix.npy --D_Coeff distortion_coefficients.npy --type DICT_5X5_100`  


You can find more details on other parameters using `python pose_estimation.py --help`  

## Output

<img src ='Images/output_sample.png' width = 400>  

<img src ='Images/pose_output.gif'>

### <ins>Notes</ins>
The `utils.py` contains the ArUCo Markers dictionary and the other utility function to display the detected markers.

Feel free to reach out to me in case of any issues.  
If you find this repo useful in any way please do star ⭐️ it so that others can reap it's benefits as well.

Happy Learning! Keep chasing your dreams!

## References
1. https://docs.opencv.org/4.x/d9/d6d/tutorial_table_of_content_aruco.html
2. https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html
