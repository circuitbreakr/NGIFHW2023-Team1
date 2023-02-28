# NGIFHW2023-Team1
Team 1's project for the [2023 Northrop Grumman Innovation Factory Hack Week](https://www.marksz.org/hackweek/)!

*wip*

## Idea
AI-generated or deepfaked image/video detector

## What it does
`Driver.py` takes in your input, check if it's valid (image/video) or not, then invokes the proper processing method from the processing file!
`Processing.py` uses a model to examine your file and outputs the detected items in the command line!

## How to use
1) Download files
2) Open command line prompt in the folder with driver.py
3) Make sure that you have Python 3.X as well as PyTorch (+ torchvision) and OpenCV (spefically opencv-contrib-python) installed!
3) Run `python driver.py -i <filepath to image or video>` on the command line

## How we made it
Modules we used:
- PyTorch
- OpenCV
Tutorials:
- [Object Detection with Pre-Trained Networks](https://pyimagesearch.com/2021/08/02/pytorch-object-detection-with-pre-trained-networks/)
- 
