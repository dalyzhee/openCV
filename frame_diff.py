import cv2

# computing frame difference
def frame_deff(prev_frame, cur_frame, next_frame):
    diff_frames_1 = cv2.absdiff(next_frame, cur_frame)
    diff_frames_2 = cv2.absdiff(cur_frame, prev_frame)
    return cv2.bitwise_and(diff_frames_1, diff_frames_2)

# function to capture current frame
def get_frame(cap, scaling_factor):
    _, frame = cap.read()
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    return gray

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    scaling_factor = 0.5
    # current frame
    prev_frame = get_frame(cap, scaling_factor)
    # next frame
    cur_frame = get_frame(cap, scaling_factor)
    # get next frame
    next_frame = get_frame(cap, scaling_factor)

    # keep reading until esc button press
    while True:
        cv2.imshow('Object Movement', frame_deff(prev_frame, cur_frame, next_frame))
        # updating variables
        prev_frame = cur_frame
        cur_frame = next_frame
        # grab next frame
        next_frame = get_frame(cap, scaling_factor)
        key = cv2.waitKey(10)
        if key == 27:
            break
    
    # close all window
    cv2.destroyAllWindows()
