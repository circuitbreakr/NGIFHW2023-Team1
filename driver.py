import argparse

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
if ".jpg" in input_path | ".mp4" in input_path | ".png" in input_path:
    todo
else:
    print("Error! Please give a valid mp4, jpg, or png file.")

