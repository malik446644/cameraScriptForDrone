import time

new_frame_time = 0
prev_frame_time = 0

def calculateFps():
    global prev_frame_time
    new_frame_time = time.time()
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    return int(fps)