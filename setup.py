from setuptools import setup

setup(
    name='autolab_aruco',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/BerkeleyAutomation/aruco_camera_calibration',
    author='Kaushik Shivakumar',
    author_email='kaushiks@berkeley.edu',
    license='MIT',
    packages=['autolab_aruco'],
    install_requires=['opencv-contrib-python',
                      'numpy',
                      'matplotlib'],
    classifiers=[],
)