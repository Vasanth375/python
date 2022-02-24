import cv2 as cv

img=cv.imread('C:\\Users\\VASANTH\\Hello.png')
det=cv.QRCodeDetector()
val, pts, st_code=det.detectAndDecode(img)
print(val)