# ----------------------------------------------
# RiotFrame Streaming Tool v1
# ----------------------------------------------
# A video streaming tool for art and activist.
# works on Twitch, Youtube, DailyMotion, and any other streameer that accepts rtmp video streams.
#
# Some ideas on how to use it:
# A] Setup am art,  protest or counter programming stream that runs video content 24/7days a week indefinitely.
#    The longer a stream runs, the more the algoryhtm will prioritized it.
# B] Set up multiple instances to stream to a service and take over an entire subject/cateogory: 
#    I.E. Insert name of target subject, hashtag or livesteamer's name 10-20 streams 
#    the same title/name and take over expose their audience to counter programming.
# C] CultureJamming: Stream content people are searching for and mix it with counter programming.
# D] Rat ***ing, stream cloneing , and other advanced trouble can also be done or implemented.
# E] Many more users , but it's up to you how to flex it. 
# 
#
# Instructions:
# 1. Configure the application settings at the top of this script:
#    a. STREAM_URL: Set this to your RTMP stream URL.
#    b. INCLUDE_TEXT_OVERLAY: Set to True to display video titles as text overlays during streaming. 
#       Set to False to disable overlays.
#    c. VIDEO_DIRECTORY: Set this to the path of the folder containing your video files.
#    d. TITLE_FILE: Specify the path to the file containing video titles (one title per line).
#
# 2. Prepare your resources:
#    a. Place your video files in the directory specified in VIDEO_DIRECTORY.
#       Supported formats: .mp4, .mkv, .avi.
#    b. If INCLUDE_TEXT_OVERLAY is True, create a text file (TITLE_FILE) with one title per line.
#       Titles will be displayed as text overlays during their respective videos.
#
# 3. Run the program:
#    a. Use Python 3.6+ to run the script.
#    b. Command: python riotframe.py
#    c. To stop the stream, press Ctrl+C.
#    D. To run it headless in the background run it nohup python riotframe.py &
#
# 4. Features:
#    a. Streams videos sequentially from the specified directory.
#    b. Loops the playlist indefinitely.
#    c. Optional text overlay with titles from the TITLE_FILE.
#    d. Logs streaming activity and errors for troubleshooting.
#
# 5. Customization:
#    a. Adjust FFmpeg settings in the `livestream_files` function to change stream quality or other parameters.
#    b. Modify the logging level (INFO, DEBUG, WARNING, etc.) in the logging configuration.
#
# Requirements:
# - Python 3.6 or newer
# - FFmpeg installed and available in the system PATH
#
# Notes:
# - If no titles are provided or TITLE_FILE is not found, "RIOTFRAME" will be displayed for all videos
#   when text overlay is enabled.
# - The application will automatically loop through all videos in VIDEO_DIRECTORY.
#
# ----------------------------------------------

import os
import subprocess
import logging

# Configuration (set these values at the top of the script)
# Twitch defalt url below
STREAM_URL = "rtmp://ingest.global-contribute.live-video.net/app/" + "ADD YOUR STREAM KEY HERE"
INCLUDE_TEXT_OVERLAY = False  # Set to False if you don't want text overlays
VIDEO_DIRECTORY = "./videos"  # Directory containing the video files
TITLE_FILE = "titles.txt"  # File containing video titles

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_video_files(directory):
    """
    Retrieve all video files from the specified directory.
    """
    logging.info(f"Scanning directory: {directory}")
    video_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(('.mp4', '.mkv', '.avi'))]
    if not video_files:
        logging.warning("No video files found in the directory.")
    return video_files


def get_titles_from_file(title_file):
    """
    Read titles from a text file, each title on a new line.
    """
    try:
        with open(title_file, 'r') as file:
            titles = file.readlines()
        titles = [title.strip() for title in titles]
        logging.info(f"Loaded {len(titles)} titles from {title_file}.")
        return titles
    except FileNotFoundError:
        logging.error(f"Title file {title_file} not found.")
        return []


def livestream_files(video_files, titles, include_text):
    """
    Stream video files sequentially in a loop, optionally adding titles as overlays.
    """
    while True:  # Infinite loop for continuous streaming
        for index, video in enumerate(video_files):
            title = titles[index % len(titles)] if titles else "RIOTFRAME"
            logging.info(f"Starting to stream video: {video} with title: {title if include_text else 'No overlay'}")

            # FFmpeg command
            command = [
                "ffmpeg", "-re", "-i", video,
                "-vcodec", "libx264", "-pix_fmt", "yuv420p",
                "-preset", "medium", "-r", "30", "-g", "48", "-b:v", "2500k",
                "-acodec", "libmp3lame", "-ar", "44100", "-threads", "6",
                "-q:a", "3", "-b:a", "712000", "-bufsize", "512k", "-f", 
                "flv", STREAM_URL,
            ]

            # Add text overlay if enabled
            if include_text:
                command.insert(4, "-vf")
                command.insert(5, f"drawtext=fontsize=40:fontcolor=white:box=1:boxcolor=black@0.8:boxborderw=5: \
                text='{title}':x=(w-text_w)/2:y=h-th-20:enable='1'")

            try:
                # Run the command to stream the video
                subprocess.run(command, check=True)
                logging.info(f"Finished streaming video: {video}")
            except subprocess.CalledProcessError as e:
                logging.error(f"Error streaming video {video}: {e}")
            except KeyboardInterrupt:
                logging.info("Streaming interrupted by user.")
                return  # Exit the loop gracefully
            except Exception as e:
                logging.error(f"Unexpected error: {e}")


def main():
    # Get video files and titles
    video_files = get_video_files(VIDEO_DIRECTORY)
    titles = get_titles_from_file(TITLE_FILE)

    if not video_files:
        logging.error("No video files to stream. Exiting.")
        return

    # Start streaming files
    livestream_files(video_files, titles, INCLUDE_TEXT_OVERLAY)


if __name__ == "__main__":
    main()
