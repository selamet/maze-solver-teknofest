from cv2 import *
import numpy as np
import sys

np.set_printoptions(threshold=np.nan)
np.set_printoptions(linewidth=150)

img = cv2.imread('deneme.jpg',0)

#img = cv2.resize(img,(34,34))
print(type(img))

satirSutun = np.array(img) #Satır ve sutun sayısına erişiyoruz

satirSayisi = satirSutun.shape[0] # Satır sayısı
sutunSayisi = satirSutun.shape[1] # Sutun Sayısı

dizi=[]
sayac = 0

#def ortancaBul(dizi):
#    ilk_eleman = dizi[0]
#    dizi.reverse()
#    son_eleman = dizi[0]
#    ortanca = (ilk_eleman + son_eleman) // 2
#    return ortanca


for i in range(satirSayisi):

    for j in range (sutunSayisi):
        if img[i][j]==255:
            dizi.append((i,j))



    print('\n')
#ortanca = ortancaBul(dizi)



for i in dizi:
    print(i)
