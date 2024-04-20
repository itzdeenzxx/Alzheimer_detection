import cv2

class VideoPlayer:
    def __init__(self):
        pass
    
    def insert_video(self, frame, video_path):
        # Open the video to insert
        video_to_insert = cv2.VideoCapture(video_path)

        # Read a frame from the video to insert
        ret, frame_insert = video_to_insert.read()
        
        if not ret or frame_insert is None:
            # Handle case where frame couldn't be read
            print("Error: Failed to read frame from the video.")
            
        
        # Resize the frame to match the dimensions of the main frame
        # frame_insert_resized = cv2.resize(frame_insert, (frame.shape[1], frame.shape[0]))

        # Insert the video frame into the main frame
        # frame[0:frame_insert_resized.shape[0], 0:frame_insert_resized.shape[1]] = frame_insert_resized
        frame[0:frame_insert.shape[0], 0:frame_insert.shape[1]] = frame_insert
