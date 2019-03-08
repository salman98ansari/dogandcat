import cv2

img=cv2.imread("C:\\Users\\Salman\\Documents\\machinelearning\\srk.jpg",1)
print(img)
#resize=cv2.resize(img , (int(img.shape[1]/2),int(img.shape[0]/2)) )
#cv2.imshow("salman",resize)
cv2.imshow("srk",img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
