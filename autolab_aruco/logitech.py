import numpy as np
import cv2
import pyudev


LEFT_CAM_SERIAL = '864EE09F'
RIGHT_CAM_SERIAL = 'D640145F'


class Camera:
    def __init__(self, cam):
        self.cap = cv2.VideoCapture(self.__get_device_index(cam))
        self.cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
        self.cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)

    def __del__(self):
        self.cap.release()

    @staticmethod
    def __get_device_index(cam):
        serial_number = [LEFT_CAM_SERIAL, RIGHT_CAM_SERIAL][cam == 'right']
        context = pyudev.Context()
        video_devices = context.list_devices(subsystem='video4linux')

        for device in video_devices:
            try:
                parent = device.find_parent('usb', 'usb_device')
            except pyudev.DeviceNotFound:
                continue

            serial = parent.attributes.asstring('serial')
            if serial == serial_number:
                return int(device.sys_name[5:])

    def get_rgb_img(self):
        while True:
            ret, rgb_img = self.cap.read()
            if ret:
                break

        return rgb_img

