from utils import read_video, save_video
import os


def main():
    # Read the input video
    video_frames = read_video("input_videos/08fd33_4.mp4")
    # Save the video frames to an output video file
    try:
        os.makedirs("output_videos")
    except os.error:
        pass
    save_video(video_frames, "output_videos/output_video.mp4")


if __name__ == "__main__":
    main()
