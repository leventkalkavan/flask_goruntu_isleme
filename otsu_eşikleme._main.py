from flask import Flask, render_template
from PIL import Image
#Kullanacağımız kütüphaneleri uygulamaya dahil edilir.

app = Flask(__name__)

@app.route("/otsu")
def otsu():
    return render_template("otsu.htm")  

@app.route("/otsu_gri")
def otsu_gri():
    return  render_template("otsu_gri.htm")  

@app.route("/otsu_yeni")
def otsuyeni():
    return render_template("otsu_yeni.htm")  
#HTML sayflarını oluşturduktan sonra template dosyasına atılır. 

if __name__ == "__main__":
    app.run(debug=True)

resim = Image.open("static\img\otsu.jpg")
#resim değişkeninin içerisine belirtilen klasörde bulunan 'otsu' adlı resim dosyası atılır.
newmat = resim.load()
#newmat adlı yeni bir matris oluşturup bunun içerisine resim dosyası yüklenir.
w = resim.size[0]
#w değişkenine resim dosyasının genişlik boyutu atılır. Dosyanın genişliği 640 piksel.
h = resim.size[1]
#h değişkenine resim dosyasının yükseklik boyutu atılır. Dosyanın  yüksekliği 360 piksel
graylist = [[0]*h for x in range (w)]
#graylist adında tanımlanan matrisin boyutu yukarıda alınan resim dosyasının genişlik ve yükseklik değerlerine göre belirlenir.
for x in range (w):
#Otsu metodu gri seviye görüntüler üzerinde çalıştığı için resim dosyasını gri tonlarına çevirmek için iç içe döngü ile matrise çekilir. Böylece her bir piksel birer matris elemanı olacaktır.
     for y in range (h) :
          r,g,b = resim.getpixel((x,y))
#Her pikselde birer r(kırmızı),g(yeşil),b(mavi) değeri bulunmaktadır. Bunlar o piksele renk veren kodlardır. Öncelikle 'getpixel' fonksiyonu ile bu değerleri r,g,b değişkenlerine atılır.
          gray=(int)((r*0.2126)+(g*0.7152)+(b*0.0722))
#Resmi gri yapacak olan sayısal değeri elde etmek için, insan gözünün gama ışınlarını algılama oranlarına göre oluşturulan formül ile alınan katsayıları r,g,b değişkenleriyle çarpılıp toplanır. Böylece resimdeki her piksel için ayrı bir gri renk tonu elde etmiş olunur.
          graylist[x][y] = gray
#graylist matrisinin her elemanına ağırlık toplama yöntemi ile bulunan gri değerleri kaydedilir.
          newmat[x,y]= (gray,gray,gray) 
#Resim dosyasını yüklenen matrisin tüm elemanlarına(piksellerine) ağırlık toplama yöntemine göre bulunan gri renk kodu atılır. Böylece resmin her pikseli renk tonuna göre gri rengini almış olacaktır. Burada kırmızı, yeşil, mavi renk tonlarının hepsine aynı değer atılır. Bu yöntem gri rengini elde etmemizi sağlar.
resim.save("static\img\otsu_gri.jpg")   
 #Artık gri tonlarında olan resmi belirtilen dosyanın içine .jpg uzantılı olarak kaydedilir.  
def histogram(resim):
#Histogram fonksiyonu renklerin görüntü üzerindeki sayısını bulmak için kullanılır. Bu metod bir resim parametresi ile çalışmaktadır.
     width = resim.size[0]
#Parametre olarak alınan  resim dosyasının ilk elemanı olan genişlik boyutunu 'width' değişkenine atılır.
     height = resim.size[1]
#Parametre olarak alınan resim dosyasının ikinci elemanı olan yükseklik boyutunu 'height' değişkenine atılır.
     histogram = [0]*256
#histogram adında bir matris tanımlanır. Bu matris renk sayılarını tutulacağı  grafiktir
     for x  in range(height):
#Görüntünün tüm piksellerini yani matrisin elemanlarını dolaşmak için genişlik ve yükseklik değerleriyle iç içe döngü kullanılır.
          for y in range(width):
               a,b,c = resim.getpixel((y,x))
#resim değişkeninin her pikselinde bulunan sayısal değerleri çekip a,b,c değişkenlerine atılır. Burada gelen değer örnek olarak :(200,200,200) şeklindedir. Çünkü ağırlık toplama yönteminden sonra her pikselde aynı sayısal değer yani aynı tonlar bulunur.
               histogram[a] = histogram[a]+1
#Bulunan üç değerden herhangi birini kullanarak histogramda toplanan renk sayısı bir arttırılır.
     return histogram
#Geri dönüş değeri olan histogramda iç içe döngülerin sonucunda resmin üzerinde bulunan her pikseldeki renk tonunu ayrı ayrı tutulmuş oldu..
def Otsu (resim):
#Otsu algoritmasının kullanılacağı fonksiyon. 'otsu_thrd' adlı metodun resim parametresi ile çalıştırılmaktadır.
     hist = histogram(resim)
 #Otsu metodunun en önemli özelliği olan histogram yani renk sayısını bulmak için ilk olarak parametre olan 'resim' değişkeni histogram fonksiyonuna gönderilir. Geri dönen matris değerini 'hist' adında bir matrise atılır.
     sum_all = 0
#'sum_all' adlı değişkeni toplam indis sayısını tutması için tanımlandı.. İlk değer olarak '0' atandı..
     for t in range(256):
#Histogramdan gelen matris indislerindeki toplam değeri almak için döngü oluşturulur.
          sum_all+=t*hist[t]
     sum_back = 0
#Kendisi ve kendisinden önceki indisteki elemanların değerler toplamını tutacak değişken.
     w_back = 0
#Bulunan eşik değerinden önceki değerler için weight değerini tutacak değişken.
     w_fore =0
#Bulunan  eşik değerinden sonraki değerler için weight değerini tutacak değişken.
     mean_back = 0
#Bulunan eşik değerinden önceki değerler için mean değerini tutacak değişken.
     mean_fore = 0
#Bulunan eşik değerinden sonraki değerler için mean değerini tutacak değişken.
     var_max = 0
#Histogram elemanları arasındaki en yüksek varyans değerini tutacak değişken.
     var_between = 0
#Histogramdaki her renk tonu için sınıflar arası varyans değerini tutacak değişken.
     threshold = 0
#Threshold işlemini yapacak olan yani otsu metodunun asıl amacı olan eşik değerini tutacak değişken.
     total =resim.size[0]*resim.size[1]
#'total' değişkeninde görüntünün genişlik*yükseklik değerleri yani toplam alanı bulunmaktadır.
     for t in range(256):
#Histogram üzerindeki tüm değerleri ulaşmak için döngü oluşturulur.
          w_back +=hist[t]
#Eşik değerinden önceki tüm değerler sırasıyla 'w_back' değişkeninde toplanır.
          if(w_back == 0):
#Mean değerini hesaplarken paydada kullanılacak 'w_back' değerinin 0 olması durumu kontrol edilir. 0 ise döngüde sıradaki değer ile devam edilir.
           continue
          w_fore = total-w_back
#Eşik değerinden sonraki weight değerlerin bulunması için toplam değerinden bulunan  önceki weight değerleri çıkarılır.
          if(w_fore == 0):
#Mean değerini hesaplarken paydada kullanılacak 'w_fore' değerinin 0 olması durumu kontrol edilir. 0 ise döngüde sıradaki değer ile devam edilir.
           continue
          sum_back += t*hist[t]
#Histogramda kendisi ve kendisinden önceki tüm elemanların indisleri ile çarparak toplanır.
          mean_back = sum_back/w_back
#Histogramda kendisinden önce bulunan toplam değerleri kendisinden önceki weight değerlerine bölerek her indis için kendisinden önceki mean değeri hesaplanır.
          mean_fore=(sum_all-sum_back)/w_fore
#Histogramda kendisinden sonra bulunan toplam değerleri kendisinden sonraki weight değerlerine bölerek her indis için kendisinden sonraki mean değerini hesaplanır.
          var_between = w_back * w_fore * (mean_back-mean_fore)**2
#Varyans formülünü kullanarak histogramdaki her eleman için renk tonları arasında varyans hesaplaması yapılır.
          if(var_between>var_max):
#Burada amaç büyük ama en ideal eşik değerini bulmak. Bu yüzden sınıflar arası yani histogramda elemanlarımız arasındaki renk tonlarının varyans değerini hesaplandı. Bu yüzden en yüksek varyans değerine sahip olan elemanı bulunup bulunmadığı kontrol edilir.
            var_max=var_between
#Bulunan  varyans değeri en yüksek ise 'var_max' değişkeninde saklanır.
            threshold = t
#En yüksek varyansa sahip olan histogram elemanının indisini de eşik değeri olarak 'threshold' değişkenine atılır.
          return threshold
#Fonksiyon sonuç olarak ideal bir eşik değeri bulup geri göndermiş olacaktır.
res = Image.open("static\img\otsu_gri.jpg")
#Daha önce kullanılan griye çevrilen resim dosyası tekrar açılır.
otsu_th = Otsu(res)
#Açılan resim dosyasının eşik değerini bulmak için Otsu fonksiyonuna gönderilir. Geri dönen değeri 'otsu_th' değişkenine atılır
otsu_im = res.load()
#Açılan resim dosyasını 'otsu_im' matrisine yüklenir.
print (otsu_th)
#Dönen eşik değerini görmek için ekrana yazdırılır.
for x in range(w):
#İç içe döngü ile en başta kullanılan 'graylist' üzerindeki tüm elemanlara ulaşılır ve her eleman için kontrol gerçekleştirilir.
    for y in range(h):
        if graylist[x][y]<otsu_th:
#Eğer elemanın değeri bulunan eşik değerinden küçük ise resmi yüklediğimiz 'otsu_im'  matrisinin elemanına renk kodu olarak siyah(0,0,0) değeri atılır.
            otsu_im[x,y] =(0,0,0)
            if graylist[x][y]>otsu_th:
#Eğer elemanın değeri bulunan eşik değerinden büyük ise resm yüklediğimiz 'otsu_im' matrisinin elemanına renk kodu olarak beyaz(255,255,255) değerini atılır.
                otsu_im[x,y]=(255,255,255)
res.save("static\img\otsu_yeni.jpg")
#Otsu algoritmasıyla işlenen görüntü, projenin belirtilen adresine kaydedilir.
res.show()        #show fonksiyonu ile görüntü ekrana getirilir.
