import cv2
import numpy as np

# function to capture current frame
def get_frame(cap, scaling_factor):
    _, frame = cap.read()
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    return frame

if __name__=='__main__':
    cap = cv2.VideoCapture(0)
    scaling_factor = 0.5
    while True:
        frame = get_frame(cap, scaling_factor)
        # color conversion from rgb to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower = np.array([0, 70, 60])
        upper = np.array([50, 150, 255])
        mask = cv2.inRange(hsv, lower, upper)
        image_bitwise_and = cv2.bitwise_and(frame, frame, mask=mask)
        image_median_blurred = cv2.medianBlur(image_bitwise_and, 5)
        cv2.imshow('Input', frame)
        cv2.imshow('Output', image_median_blurred)

        c = cv2.waitKey(10)
        if c==27:
            break
    # close all window
    cv2.destroyAllWindows()
