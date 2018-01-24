from darkflow.net.build import TFNet
import cv2

options = {"model": "./cfg/yolo.cfg","load": "./yolo.weights","threshold": 0.4, "gpu": 0.0}

tfnet = TFNet(options)

imgcv = cv2.imread("./images/sample1.jpg")
result = tfnet.return_predict(imgcv)
print(result)