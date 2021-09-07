from flask import Flask, render_template
from PIL import Image
import math

app = Flask(__name__)

@app.route("/HSV")
def HSV():
    return render_template("HSV.htm")

@app.route("/HSV_yeni")
def HSV_yeni():
    return render_template("HSV_yeni.htm.")

@app.route("/HSI")
def HSI():
    return render_template("HSI.htm")

@app.route('/HSI_yeni')
def HSI_yeni():
   return render_template("HSI_yeni.htm") 

@app.route("/YUV")
def YUV():
    return render_template ("YUV.htm")

@app.route('/YUV_yeni')
def YUV_yeni():
   return render_template ("YUV_yeni.htm")



if __name__ == "__main__":
    app.run(debug=True)   

def  rgbtohsv (r, g, b):
#Kullanılan fonksiyon 'rgbtohsv' adında int türünde 'r,g,b' adlı üç parametre ile kullanmaktadır.
    r, g, b = r/255.0, g/255.0, b/255.0
#Alınan r,g,b değişkenlerini normalize hale getirmek için yani 0-1 değerleri arasına almak için her değişken 255 sayısına bölünür.
    Cmax = max (r, g, b)
#Yeni değerleri hesaplanan r,g,b değişkenleri arasından en büyük olanı bulunup 'Cmax' değişkenine atılır.
    Cmin = min (r, g, b)
#Yeni değerleri hesaplanan r,g,b değişkenleri arasından en küçük olanı bulunup 'Cmin' değişkenine atılır.
    delta = Cmax - Cmin
#Formülde belirtilen delta değişkeninin hesaplanması için en büyük değerden en küçük değer çıkarılır. Böylece orta bir değer hesaplanır.
    if delta == 0:
#Hue bileşenini bulmak; yani 'h' değişkeni için, eğer en küçük ve en büyük değer eşit ise hue(renk) bileşenine '0' değeri atanır.
        h = 0
    elif Cmax == r:
#Eğer bulunan en büyük değer r(kırmızı) değişkenine eşitse formüldeki denklem uygulanır. En son 360 ile mod işlemi yapılmasının nedeni raporda belirtildiği gibi Hue bileşeni derece cinsinden değer almaktadır. Bu yüzden 360 üzerinden mod alınarak derecesi hesaplanır.
        h = (60 * ((g-b)/delta)) % 360
    elif Cmax == g:
#Eğer bulunan en büyük değer g(yeşil) değişkenine eşitse formüldeki denklem uygulanır. Burada +2 kullanılmasının nedeni 360 derecelik Hue bileşeninde yeşil renginin başlangıç açısı 120 derecesine denk gelmektedir.(Şekil 1.2 de gösterilmiştir.)
        h = (60 * ((b-r)/delta) + 2) % 360
    elif Cmax == b:
#Eğer bulunan en büyük değer b(mavi) değişkenine eşitse formüldeki denklem uygulanır. Burada +4 kullanılmasının nedeni 360 derecelik Hue bileşeninde mavi renginin başlangıç açısı 240 derecesine denk gelmektedir.(Şekil 1.2 de gösterilmiştir.)
        h = (60 * ((r-g)/delta) + 4) % 360
    if Cmax == 0:
#Saturation bileşenini bulmak; yani 's' değişkeni için, eğer 'Cmax' en büyük değişkenimiz '0' ise s değişkenine 0 değeri atılır..
        s = 0
    else:
        s = delta/Cmax
#Değilse formülde gösterildiği gibi, bulunan delta değişkeni en büyük değere bölünür.
    v = Cmax
#Value bileşenini en büyük değer oluşturmaktadır.
    h=int(h)
#Son olarak görüntüdeki piksel değerleri int türünde olduğundan tüm değişkenlere tür dönüşümü yapılır.
    s=int(s)
    v=int(v)
    return h, s, v
    #Tür dönüşümü yapılan değerler geri gönderilir.
resim=Image.open("static\img\HSV.jpg")
#resim değişkeninin içerisine belirtilen klasörde bulunan 'HSV.jpg' adlı resim dosyası atılır.
resim_pix = resim.load()
#resim_pix adlı yeni bir matris oluşturup bunun içerisine resim dosyası yüklenir.
w=resim.size[0]
#w değişkenine resim dosyasının genişlik boyutu atılır. Dosyanın genişliği 640 piksel.
hg=resim.size[1]
#hg değişkenine resim dosyasının yükseklik boyutu atılır. Dosyanın yüksekliği 360 piksel.
for i in range(w):
#Görüntünün tüm piksellerinde bulunan renk kodlarını almak için iç içe döngü oluşturulur.
    for j in range(hg):
        r, g, b = resim.getpixel((i, j))
 #Her pikselde birer r(kırmızı),g(yeşil),b(mavi) değeri bulunmaktadır. Bunlar o piksele renk veren kodlardır. Öncelikle 'getpixel' fonksiyonu ile bu değerleri r,g,b değişkenlerine atılır.
        h, s, v = rgbtohsv(r, g, b)
#Alınan r,g,b değişkenler rgbtohsv fonksiyonuna gönderilir. Bu fonksiyonun geri dönüşü üç parametre olacaktır. Bunlar da h,s,v değişkenlerinde saklanır.
        resim_pix[i,j] = (h, s, v)
#Fonksiyondan elde edilen  h,s,v değerleri görüntünün uygun piksellerine yeni değer olarak atılır.
resim.save("static\img\HSV_yeni.jpg")
#Oluşan görüntü yeni adıyla belirtilen klasöre kaydedilir.
resim.show()
#Görüntü ekranda gösterilir.
def  rgbtohsi (R, G, B):
#Kullanılan fonksiyon 'rgbtohsi' adında int türünde 'r,g,b' adlı üç parametre ile kullanmaktadır.

  r = R / 255
  g = G / 255  #Değerler normalize hale getirilir.
  b = B / 255

  num=0.5*((r-g)+(r-b))
  den=((r-g)*(r-g)+(r-b)*(g-b))**(0.5) #Formül uygulanır.

  if(b<=g):
     # h [0,pi] aralığında
     if den != 0:
         h = math.acos(num / (den))
     else:
         h = 0

  elif(b>g):
      # h [pi,2pi] aralığında
      if den!=0:
          h=(2*math.pi)-math.acos(num/den)
      else:
          h=0
  s=1-(3*min(r,g,b)/(r+g+b)) #s değeri
  i=(r+g+b)/3                #i değeri

  return int(h*180/math.pi), int(s*100), int(i*255)
  #Tür dönüşümü yapılan değerler geri gönderilir.
resim=Image.open("static\img\HSI.jpg").convert("RGB")
#resim değişkeninin içerisine belirtilen klasörde bulunan 'HSV.jpg' adlı resim dosyası atılır.
resim_pix = resim.load()
#resim_pix adlı yeni bir matris oluşturup bunun içerisine resim dosyası yüklenir.
w=resim.size[0]
#w değişkenine resim dosyasının genişlik boyutunu atılır. Dosyanın genişliği 640 piksel.
hg=resim.size[1]
#hg değişkenine resim dosyasının yükseklik boyutunu atılır. Dosyanın yüksekliği 360 piksel.
for i in range(w):
#Görüntünün tüm piksellerinde bulunan renk kodlarını almak için iç içe döngü oluşturulur.
  for j in range(hg):
      r, g, b = resim.getpixel((i, j))
#Her pikselde birer r(kırmızı),g(yeşil),b(mavi) değeri bulunmaktadır. Bunlar o piksele renk veren kodlardır. Öncelikle 'getpixel' fonksiyonu ile bu değerleri r,g,b değişkenlerine atılır.
      h, s, v = rgbtohsi(r, g, b)
#Alınan r,g,b değişkenler rgbtohsi fonksiyonuna gönderilir. Bu fonksiyonun geri dönüşü üç parametre olacaktır. Bunlar da h,s,v değişkenlerinde saklanır.
      resim_pix[i,j] = (h, s, v)
#Fonksiyondan elde edilen  h,s,i değerleri görüntünün uygun piksellerine yeni değer olarak atılır.
resim.save("static\img\HSI_yeni.jpg")
#Oluşan görüntü yeni adıyla belirtilen klasöre kaydedilir.
resim.show()
#Görüntü ekranda gösterilir.
def  rgbtoyuv (R, G, B):
  r=R/255
  g=G/255 #Değerler normalize hale getirilir.
  b=B/255

  Y=(0.299*r)+(0.587*g)+(0.114*b)
  U=0.492*(b-Y)
  V=0.877*(r-Y)

  return int(Y*255),int(U*255),int(V*255) # y,u,v değerleri 255 ile çarpılarak resim üzerinde gösterilir.
  #Tür dönüşümü yapılan değerler geri gönderilir.
resim=Image.open("static\img\YUV.jpg").convert("RGB")
#resim değişkeninin içerisine belirtilen klasörde bulunan 'HSV.jpg' adlı resim dosyası atılır.
resim_pix = resim.load()
#resim_pix adlı yeni bir matris oluşturup bunun içerisine resim dosyası yüklenir.
w=resim.size[0]
#w değişkenine resim dosyasının genişlik boyutunu atılır. Dosyanın genişliği 640 piksel.
hg=resim.size[1]
#hg değişkenine resim dosyasının yükseklik boyutunu atılır. Dosyanın yüksekliği 360 piksel.
for i in range(w):
#Görüntünün tüm piksellerinde bulunan renk kodlarını almak için iç içe döngü oluşturulur.
  for j in range(hg):
      r, g, b = resim.getpixel((i, j))
#Her pikselde birer r(kırmızı),g(yeşil),b(mavi) değeri bulunmaktadır. Bunlar o piksele renk veren kodlardır. Öncelikle 'getpixel' fonksiyonu ile bu değerleri r,g,b değişkenlerine atılır.
      h, s, v = rgbtoyuv(r, g, b)
#Alınan r,g,b değişkenler rgbtoyuv fonksiyonuna gönderilir. Bu fonksiyonun geri dönüşü üç parametre olacaktır. Bunlar da y,u,v değişkenlerinde saklanır.
      resim_pix[i,j] = (h, s, v)
#Fonksiyondan elde edilen  y,u,v değerleri görüntünün uygun piksellerine yeni değer olarak atılır.
resim.save("static\img\YUV_yeni.jpg")
#Oluşan görüntü yeni adıyla belirtilen klasöre kaydedilir.
resim.show()
#Görüntü ekranda gösterilir.

