from autolab_core import RigidTransform
import numpy as np

tag_to_robot = RigidTransform.load("T_tag_to_robot.tf")
tag_to_cam = RigidTransform.load("T_tag_cam.tf")
print(tag_to_robot)
print(tag_to_cam)

# toy_tag_to_robot = RigidTransform(
#     rotation=np.eye(3),
#     translation=[-0.25625, -0.51025, -0.022  ],
#     from_frame='tag',
#     to_frame='robot'
# )

# toy_tag_to_cam = RigidTransform(
#     # rotation=[
#     #     [ 0.97699  , 0.06273 ,  0.203854],
#     #     [ 0.053781 ,-0.997342 , 0.04915 ],
#     #     [ 0.206395 ,-0.037056, -0.977767]
#     # ],
#     rotation = RigidTransform.y_axis_rotation(5 * np.pi / 180),
#     translation=[-0.039062, -0.061116, 0.8],
#     from_frame='tag',
#     to_frame='cam'
# )

tag_to_cam.rotation = RigidTransform.y_axis_rotation(-1.5 * np.pi / 180)

cam_to_robot = tag_to_robot * tag_to_cam.inverse()
print(cam_to_robot)
cam_to_robot.save("T_cam_to_robot.tf")