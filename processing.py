# import the necessary packages
from torchvision.models import detection
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import numpy as np
import torch
import cv2
import time

# set the device we will be using to run the model
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# load the list of categories in the COCO dataset and then generate a
# set of bounding box colors for each class
CLASSES = ('background', 'ai_gen')
# pickle.loads(open(args["labels"], "rb").read())
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# load the model and set it to evaluation mode
model = detection.fasterrcnn_resnet50_fpn(weights='DEFAULT')
in_features = model.roi_heads.box_predictor.cls_score.in_features
model.roi_heads.box_predictor = FastRCNNPredictor(in_features, len(CLASSES))

model.eval()

def process_image(image_filepath): # process a single image
    # load the image from disk
    image = cv2.imread(image_filepath)
    orig = image.copy()

    processed_img = process_frame(image, orig)

    # show the output image
    cv2.imshow("Output", processed_img)
    cv2.waitKey(0)

def process_video(video_filepath): # process a video frame-by-frame
    video = cv2.VideoCapture()
    video.open(video_filepath)
    while(video.isOpened()):  
        tic = time.time()
        ret, frame = video.read()
        orig = frame.copy()

        processed_img = process_frame(frame, orig)

        cv2.imshow("Output", processed_img)
        toc = time.time()
        print("FPS: {:.3f}".format(1/(toc-tic)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()

def process_frame(img, orig): # process one image through the model; code provided by Adrian Rosebrock
    # convert the image from BGR to RGB channel ordering and change the
    # image from channels last to channels first ordering
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.transpose((2, 0, 1))

    # add the batch dimension, scale the raw pixel intensities to the
    # range [0, 1], and convert the image to a floating point tensor
    img = np.expand_dims(img, axis=0)
    img = img / 255.0
    img = torch.FloatTensor(img)

    # send the input to the device and pass the it through the network to
    # get the detections and predictions
    img = img.to(DEVICE)
    detections = model(img)[0]

    # loop over the detections
    for i in range(0, len(detections["boxes"])):
        # extract the confidence (i.e., probability) associated with the
        # prediction
        confidence = detections["scores"][i]

        # filter out weak detections by ensuring the confidence is
        # greater than the minimum confidence
        if confidence > 0.7: # if confidence > args["confidence"]:
            # extract the index of the class label from the detections,
            # then compute the (x, y)-coordinates of the bounding box
            # for the object
            idx = int(detections["labels"][i])
            box = detections["boxes"][i].detach().cpu().numpy()
            (startX, startY, endX, endY) = box.astype("int")

            # display the prediction to our terminal
            label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
            print("[INFO] {}".format(label))

            # draw the bounding box and label on the image
            cv2.rectangle(orig, (startX, startY), (endX, endY),
                COLORS[idx], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(orig, label, (startX, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
    return orig