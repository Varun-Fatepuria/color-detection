import cv2
from PIL import Image
from util import get_hsv_range

yellow_bgr = [0, 255, 255]  
camera = cv2.VideoCapture(0)

while True:
    is_frame_read, video_frame = camera.read()
    if not is_frame_read:
        break

    hsv_frame = cv2.cvtColor(video_frame, cv2.COLOR_BGR2HSV)
    lower_bound, upper_bound = get_hsv_range(color=yellow_bgr)
    color_mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
    
    pil_mask = Image.fromarray(color_mask).convert('L')
    bounding_box = pil_mask.getbbox()

    if bounding_box is not None:
        top_left_x, top_left_y, bottom_right_x, bottom_right_y = bounding_box
        video_frame = cv2.rectangle(
            video_frame,
            (top_left_x, top_left_y),
            (bottom_right_x, bottom_right_y),
            (0, 255, 0),
            5
        )

    cv2.imshow('Detected Yellow Object', video_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
