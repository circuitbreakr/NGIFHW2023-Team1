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
# potential edge case if someone tries to upload a file called .jpg.wav or any sort of incompatible file that also happens
# to have a compatible file name somewhere in it
if input_path.endswith(".jpg") | input_path.endswith(".png"):
    process_image(input_path)
elif input_path.endswith(".mp4"):
    process_video(input_path)
else:
    print("Error! Please provide a valid mp4, jpg, or png file.")

