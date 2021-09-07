from matplotlib.pyplot import savefig
import numpy as np
import matplotlib.image as mpimg
from flask import Flask , render_template
import pylab as plt

#numpy kütüphanesi eklendi. 
#Ekrana grafik olarak çizdirmeyi sağlayan pylab kütüphanesinden plt modülü eklendi.
#Görüntünün çok yönlü numpy dizisi olarak alınmasını sağlayan mpimg modülü eklendi.
#Resimlerin kaydolması için matplotlib.pyplot savefig kütüphanesi eklendi.

app = Flask(__name__)

@app.route("/histogram")
def histogram():
    return render_template ("histogram.htm")

@app.route("/histogram_yeni")
def histogram_yeni():
    return render_template ("histogram_yeni.htm")

if __name__ =="__main__":

    app.run(debug=True)

def imhist (im):
#imhist fonksiyonu ile parametre olarak gönderilen görüntünün renk histogramı hesaplanır.
     m,n=im.shape
#Görüntünün numpy dizisi olarak boyutu m,n değişkenlerine atanır.
     h=[0.0]*256
#Histogram değerlerini tutacak h adında 256 elemanlık bir matris tanımlanır.


     for i in range(m):
#Görüntünün boyutu değerince oluşturulan iç içe döngüler ile görüntü üzerinde dolaşılır.
          for j in range(n):
#Görüntünün tüm piksel değerleri için histogram bir arttırılarak histogram matrisi bulunur.
              h[im[i,j]] += 1
#Bulunan histogram değerleri numpy dizisine dönüştürülür ve görüntünün büyüklüğüne bölünür. Böylece ilk adım olan renk aralıklarını toplam boyuta bölerek renk frekansları bulma işlemi gerçekleştirilir.
     return np.array(h) / (m*n)
#Kümülatif olarak tüm histogram değerleri toplanır.
def cumsum(h):
     return [sum(h[:i+1]) for i in range(len(h))]
def histeq(im):
#Histogram eşitleme işlemini yapacak fonksiyon resim parametresi ile çalışmaktadır.
     h=imhist(im)
#Gelen resmin histogram tablosu çıkarılır.
     cdf=np.array(cumsum(h))
#Kümülatif dağılım fonksiyonu hesaplanır ve numpy dizisine dönüştürülür.


     sk=np.uint8(255*cdf)
#Kümülatif dağılım fonksiyonu değerleri kullanılarak görüntünün değerleri 0-255 arasına çekilir yani normalize bir gri değer elde edilir.
     s1,s2=im.shape
 #Görüntünün boyutları alınır.
     new_im=np.zeros_like(im)
#Yeni görüntü için 0'lık bir np dizisi oluşturulmuştur.
     for i in range(0,s1):
#Görüntü boyutu değerince iç içe döngü oluşturulur.
          for j in range(0,s2):
               new_im[i,j]=sk[im[i,j]]
#Görüntüden alınan piksel değerleri ile Kümülatif dağılım fonksiyondan alınan  değerleri eşleyerek yeni görüntünün piksel değerleri elde edilir.
     return new_im
#Elde edilen görüntü geri gönderilir.
img=np.uint(mpimg.imread("static\img\cicek.jpg")*255.0)
#İlk olarak png formatındaki görüntünün matris biçiminde 0-255 değerleri arasına indirgeyerek matris olarak okunur.Okunan görüntünün griye çevirme işlemi için kullanılan katsayılar ile çarparak görüntüyü griye çevrilir ve çevirme işleminden sonra görüntü tekrar normalize olarak 0-255 değerleri arasına çekilir.


img = np.uint8(0.2126 * img[:,:,0]) +\
          np.uint8(0.7152 * img[:,:,1]) +\
          np.uint8(0.0722 * img[:,:,2])
new_img = histeq(img)
#Görüntüyü histeq fonksiyonuna göndererek histogramları eşitlenmiş hali elde edilir.
#Son olarak bu görüntüler ekrana çizdirilir.
plt.subplot(121)
#plt modülünden subplot fonksiyonu ile görüntünün durması gereken nokta seçilir.
plt.imshow(img)
#imshow ile çizdirilecek görüntü gösterilir.
plt.title("Orjinal Resim")
#Yazılacak olan başlık belirlenir.
plt.set_cmap("gray")
#Görüntülerin gri düzeyinde gösterilmesini sağlar.
savefig("static\img\cicek_yeni.jpg")

plt.subplot(122)
plt.imshow(new_img)
plt.title("Histogram Esikleme Yapılan Resim")
plt.set_cmap("gray")
savefig("static\img\cicek_eskileme.jpg")
plt.show()    
