import numpy as np
import cv2

def get_hsv_range(bgr_color):
    bgr_array = np.uint8([[bgr_color]])
    hsv_color = cv2.cvtColor(bgr_array, cv2.COLOR_BGR2HSV)

    hue_value = hsv_color[0][0][0]

    if hue_value >= 165:
        lower_hsv = np.array([hue_value - 10, 100, 100], dtype=np.uint8)
        upper_hsv = np.array([180, 255, 255], dtype=np.uint8)
    elif hue_value <= 15:
        lower_hsv = np.array([0, 100, 100], dtype=np.uint8)
        upper_hsv = np.array([hue_value + 10, 255, 255], dtype=np.uint8)
    else:
        lower_hsv = np.array([hue_value - 10, 100, 100], dtype=np.uint8)
        upper_hsv = np.array([hue_value + 10, 255, 255], dtype=np.uint8)

    return lower_hsv, upper_hsv
