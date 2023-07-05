import cv2
import argparse
from logitech import Camera


parser = argparse.ArgumentParser()
parser.add_argument('--cam')
args = parser.parse_args()

cam = Camera(args.cam)

cv2.namedWindow("test")

while True:
    
    frame = cam.get_rgb_img()
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "{}_frame.png".format(args.cam)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

cv2.destroyAllWindows()

