import cv2
import numpy as np
import torch
from torchvision import transforms

class YOLOv3:
    def _init_(self):
        self.model = self.load_model()

    def load_model(self):
        #loading pre-trained YOLOv3 model
        model = cv2.dnn.readNetFromDarknet('yolov4.cfg', 'yolov4.weights')
        model.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        model.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

        return model

    def detect_objects(self, image):
        #preparing image for object detection
        blob = cv2.dnn.blobFromImage(image, 1/255, (416, 416), (0, 0, 0), True, crop=False)
        self.model.setInput(blob)

        #perform forward pass and get the detections
        layer_names = self.model.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in self.model.getUnconnectedOutLayers()]
        outputs = self.model.forward(output_layers)

        return outputs
def track_gaze():
    #instance of YOLOv3 class
    yolo = YOLOv3()

    #initialize the video capture
    cap = cv2.VideoCapture(0)

    while True:
        #reading frame from video capture
        ret, frame = cap.read()

        # Detect
