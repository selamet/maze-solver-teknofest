from cv2 import *
import numpy as np


#np.set_printoptions(threshold=np.nan)
#np.set_printoptions(linewidth=3000)
img = cv2.imread('20_20.png',0)
cv2.imshow("Image",img)
#imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,tresh = cv2.threshold(img,128,255,cv2.THRESH_BINARY_INV)
img2,contours,hierarchy = cv2.findContours(tresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
path = np.zeros((img.shape),dtype=np.uint8)
cv2.drawContours(path,contours,0,(255,255,255),cv2.FILLED)
kernel =np.ones((21,21),dtype=np.uint8)
path = cv2.dilate(path,kernel)
path_erode = cv2.erode(path,kernel)
cv2.imshow("dilate",path)
cv2.imwrite('dilate.jpg',path)
cv2.imshow("erode",path_erode)
diff = cv2.absdiff(path,path_erode,path)
satirSutun = np.array(diff) #Satır ve sutun sayısına erişiyoruz
satirSayisi = satirSutun.shape[0] # Satır sayısı
sutunSayisi = satirSutun.shape[1] # Sutun Sayısı
diziIndis=[]
dosya = open('cozum.txt','w')
for i in range(satirSayisi):
    for j in range (sutunSayisi):
        if diff[i][j]==255:
            print("satir: "+(str)(i)+" sutun: "+(str)(j)) # 255 olan değerlerin indislerini buluyoruz.
            degisken = (str)(i)+" "+(str)(j)#string şeklinde değişkenimize atama yapıp dizi içerisinde vermizi tutuyoruz.
            diziIndis.append(degisken)
            dosya.write((str)(i)+" "+(str)(j)+'\n')
#path2 = cv2.resize(path,(50,50))
cv2.imshow("diff",path)
#print(path)
#dosya2 = open('yo.txt','w')
#dosya2.write((str)(path))
#cv2.imwrite('deneme.jpg',path)
cv2.waitKey(0)
