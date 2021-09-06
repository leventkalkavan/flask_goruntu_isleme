from flask import Flask , render_template
import cv2
import numpy as np

app = Flask(__name__)

@app.route("/asinma")
def asinma():
    return render_template("asinma.htm")

@app.route("/genlesme")
def genlesme():
    return render_template ("genlesme.htm")

@app.route("/gri_asinma_genlesme")
def gri_asinma_genlesme():
    return render_template ("gri_asinma_genlesme.htm")

@app.route("/acilma")
def acilma():
    return render_template ("acilma.htm")    

@app.route("/kapama")
def kapama():
    return render_template ("kapama.htm")      

if __name__ =="__main__":

    app.run(debug=True)
    
img=cv2.imread("static\img\morfolojik.png",0)

#Ardından, resmin okunması gerekiyor. Bu cv2.imread (dosya adı, flag) işlevi tarafından yapılır. Flag = 0 gri tonlamalı bir görüntüyü döndürür.

kernel=np.ones((5,5),np.uint8)

#Morfolojik işlem için yapılandırma elemanı aşağıdaki kod kullanılarak oluşturulur.Şimdi gri tonlamalı görüntüde morfolojik işlemler yapacağız.

dilation=cv2.dilate(img,kernel,iterations=1)

#Bunun için cv2.dilate () işlevini kullanıyoruz.

cv2.imshow("genlesmis resim", dilation)

#Değişiklikleri görmek ve karşılaştırmak için değiştirilmiş resmi görüntüleyebiliriz. Bunun için cv2.imshow (windowName, img) işlevini kullanıyoruz. Örneğin, aşınmış görüntüyü görmek istiyorsanız, bu kod kullanılır.

cv2.imwrite("static\img\morfolojik_genlesme.jpg",dilation)

#Alternatif olarak, değiştirilmiş görüntüyü cv2.imwrite (isim, img) işleviyle de kaydedebiliriz.

cv2.waitKey(0)
cv2.destroyAllWindows()

# Eğer cv2.imshow () kullanılırsa, yazılan kod yukarıdaki kodu da içermelidir.

img=cv2.imread("static\img\morfolojik.png",0)

#Ardından, resmin okunması gerekiyor. Bu cv2.imread (dosya adı, bayrak) işlevi tarafından yapılır. Flag = 0 gri tonlamalı bir görüntüyü döndürür.

kernel=np.ones((5,5),np.uint8)

#Morfolojik işlem için yapılandırma elemanı aşağıdaki kod kullanılarak oluşturulur.Şimdi gri tonlamalı görüntüde morfolojik işlemler yapacağız.

erosion=cv2.erode(img,kernel,iterations=1)

#Bunun için cv2.erode () işlevini kullanıyoruz.

cv2.imshow("asinmis resim",erosion)

#Değişiklikleri görmek ve karşılaştırmak için değiştirilmiş resmi görüntüleyebiliriz. Bunun için cv2.imshow (windowName, img) işlevini kullanıyoruz. Örneğin, aşınmış görüntüyü görmek istiyorsanız, bu kod kullanılır.

cv2.imwrite("static\img\morfolojik_asinma.jpg",erosion)

#Alternatif olarak, değiştirilmiş görüntüyü cv2.imwrite (isim, img) işleviyle de kaydedebiliriz.

cv2.waitKey(0)
cv2.destroyAllWindows()

# Eğer cv2.imshow () kullanılırsa, yazılan kod yukarıdaki kodu da içermelidir.

img=cv2.imread("static\img\acma.png",0)

#Ardından, resmin okunması gerekiyor. Bu cv2.imread (dosya adı, bayrak) işlevi tarafından yapılır. Flag = 0 gri tonlamalı bir görüntüyü döndürür.

kernel=np.ones((5,5),np.uint8)

#Morfolojik işlem için yapılandırma elemanı aşağıdaki kod kullanılarak oluşturulur.Şimdi gri tonlamalı görüntüde morfolojik işlemler yapacağız.

opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

#Bunun için cv2.erode () işlevini kullanıyoruz.

cv2.imshow("acilmis resim",opening)

#Değişiklikleri görmek ve karşılaştırmak için değiştirilmiş resmi görüntüleyebiliriz. Bunun için cv2.imshow (windowName, img) işlevini kullanıyoruz. Örneğin, aşınmış görüntüyü görmek istiyorsanız, bu kod kullanılır.

cv2.imwrite("static\img\morfolojik_acilma.jpg",opening)

#Alternatif olarak, değiştirilmiş görüntüyü cv2.imwrite (isim, img) işleviyle de kaydedebiliriz.

cv2.waitKey(0)
cv2.destroyAllWindows()

# Eğer cv2.imshow () kullanılırsa, yazılan kod yukarıdaki kodu da içermelidir.

img=cv2.imread("static\img\kapama.png",0)

#Ardından, resmin okunması gerekiyor. Bu cv2.imread (dosya adı, bayrak) işlevi tarafından yapılır. Flag = 0 gri tonlamalı bir görüntüyü döndürür.

kernel=np.ones((5,5),np.uint8)

#Morfolojik işlem için yapılandırma elemanı aşağıdaki kod kullanılarak oluşturulur.Şimdi gri tonlamalı görüntüde morfolojik işlemler yapacağız.

closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

#Bunun için cv2.erode () işlevini kullanıyoruz.

cv2.imshow("kapanmis resim",closing)

#Değişiklikleri görmek ve karşılaştırmak için değiştirilmiş resmi görüntüleyebiliriz. Bunun için cv2.imshow (windowName, img) işlevini kullanıyoruz. Örneğin, aşınmış görüntüyü görmek istiyorsanız, bu kod kullanılır.

cv2.imwrite("static\img\morfolojik_kapanma.jpg",closing)

#Alternatif olarak, değiştirilmiş görüntüyü cv2.imwrite (isim, img) işleviyle de kaydedebiliriz.

cv2.waitKey(0)
cv2.destroyAllWindows()

# Eğer cv2.imshow () kullanılırsa, yazılan kod yukarıdaki kodu da içermelidir.

#GRİ AŞINMA İŞLEMİ (import cv2 import numpy as np ,kütüphaneleri aynı)

img=cv2.imread("static\img\canny_gray.bmp",0)

kernel=np.ones((5,5),np.uint8)

erosion=cv2.erode(img,kernel,iterations=1)

cv2.imshow("asinmis resim",erosion)

cv2.imwrite("static\img\gri_asinma.jpg",erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()

#GRİ GENLEŞME İŞLEMİ (import cv2 import numpy as np ,kütüphaneleri aynı)

img=cv2.imread("static\img\canny_gray.bmp",0)

kernel=np.ones((5,5),np.uint8)

dilation=cv2.dilate(img,kernel,iterations=1)

cv2.imshow("asinmis resim", dilation)

cv2.imwrite("static\img\gri_genlesme.jpg",dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
