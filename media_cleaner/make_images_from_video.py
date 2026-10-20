import os
import cv2

def make_images_from_video(video_path, images_folder_path, save=False):
    # Initialize video capture
    video_path = os.path.join(os.path.dirname(__file__), video_path)
    images_folder_path = os.path.join(os.path.dirname(__file__), images_folder_path)
    final_images_folder_path = os.path.join(images_folder_path, "final")
    os.makedirs(final_images_folder_path, exist_ok=True)
    rimraf = f"rm -rf {images_folder_path}"
    os.system(rimraf)
    os.makedirs(final_images_folder_path, exist_ok=True)
    vidcap = cv2.VideoCapture(video_path)

    # Initialize count and success
    count = 0
    success = True
    frame_rate = int(vidcap.get(cv2.CAP_PROP_FPS))
    skip_frames = frame_rate * 1  # 1 frame every second
    # Total number of frames in the video
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Total duration of the video in seconds
    total_duration = total_frames / frame_rate
    count = 0  # Keep track of which frame you are on

    # Initialize an empty dictionary to hold frame-to-time mapping
    frame_to_time = {}

    while success:
        # Capture frames every 4 frames

        vidcap.set(cv2.CAP_PROP_POS_FRAMES, count)        
        # Capture frame-by-frame
        success, image = vidcap.read()
        if not success:
            break
    
        # Calculate the time in seconds
        time_in_seconds = count / frame_rate

        print(f"Processed {time_in_seconds:.2f} seconds out of {total_duration:.2f} seconds.")


        # Save frame as JPEG file
        frame_path = os.path.join(images_folder_path, f"frame{count}.jpg")
        if save:
            cv2.imwrite(frame_path, image)

        # Store the time mapping
        frame_to_time[frame_path] = time_in_seconds
    
        # Resize image to target dimensions (e.g., 128x128) for model input
        resized_image = None
        if save:
            resized_image = cv2.resize(image, (128, 128))

        # Save the resized image
        model_images_path = os.path.join(final_images_folder_path, f"resized_frame{count}.jpg")
        if resized_image is not None and save:
            cv2.imwrite(model_images_path, resized_image)

        count += skip_frames

    # Release the video capture
    vidcap.release()
    # Print or save the frame-to-time mapping
    print(frame_to_time)
    return final_images_folder_path
