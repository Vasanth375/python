import argparse
import cv2
import pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path= args["C:\\Users\\VASANTH\\mycode\\python\\Pro's\\ColorDetection\\Color.png"]

#Reading image with opencv
img = cv2.imread(img_path)

#Reading csv file with pandas and giving names to each column
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('C:\Game\color.cv', names=index, header=None)