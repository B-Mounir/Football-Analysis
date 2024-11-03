import cv2


def read_video(video_path):
    """
    Reads a video from the specified file path and returns its frames.

    Args:x@
        video_path (str): The path to the video file.

    Returns:
        list: A list of frames, where each frame is represented as a numpy array.
    """
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames


def save_video(output_frames, output_path):
    """
    Saves a list of video frames to a video file.

    Args:
        output_frames (list of numpy.ndarray): List of frames to be saved as a video. Each frame should be a numpy array.
        output_path (str): Path where the output video file will be saved.

    Returns:
        None
    """
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(
        output_path,
        fourcc,
        24,
        (output_frames[0].shape[1], output_frames[0].shape[0]),
    )
    for frame in output_frames:
        out.write(frame)
    out.release()
