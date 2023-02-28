import argparse
from detect_ai import process_image

# constructs the argument parser to take in a single input path
ap = argparse.ArgumentParser()
ap.add_argument(
    "-i", 
    "--input", 
    type=str,
    help="path to the input image/video"
)
args = ap.parse_args()
input_path = getattr(args, 'input')

# checks if input is a valid video/image file, if not, prints an error message.
if input_path.endswith(".jpg") | input_path.endswith(".png"):
    process_image(input_path)
elif input_path.endswith(".mp4"):
    process_video(input_path)
else:
    print("Error! Please provide a valid mp4, jpg, or png file.")
