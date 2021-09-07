# HİSTOGRAM ARALIĞI İLE GÖLGE TESPİTİ
Matematiksel olarak histogram; gruplandırılmış bir veri dağılımının sütun grafiğiyle gösterimidir. Görüntüde ise her piksel seviyesini gösteren bir ölçüttür. Histogram grafiklerine bakılarak bir görüntüde parlaklık durumu veya görüntünün tonlamaları hakkında bilgi edinilebilir. Aşağıda görüntüler ve histogram grafiklerinin örnekleri yer almaktadır.

# Histogram Dengeleme
Bir görüntüdeki renk değerlerinin belli bir yerde kümelenmiş olmasından kaynaklanan, renk dağılımı bozukluğunu gidermek için kullanılan bir yöntemdir.
Histogram matematiksel olarak aşağıdaki şekilde gösterilebilir.

→h(rk )=nk
 
rk : k’nıncı parlaklık değeri             nk : k nıncı parlaklık değerinin görüntüdeki sayısı

8-bit parlaklıklı görüntüde 256 gri seviye vardır. Örnek olarak tüm değerler ilk 100 değerde toplanırsa renkleri fark etmek zorlaşmaktadır.
Dönüştürülmüş ve orjinal olan histogramlar grafiklerde görüldüğü üzere olasılık yoğunluğu olarak da gösterebilmektedir.

Görüntü histogramı incelendiğinde ani artışlar ton grup aralıkları olarak ifade edilmektedir. 
Görüntüde var olabilen bu kısımlar gölge olarak belirlenerek gerekli işlemler yapılmaktadır.


Sayısal görüntü işlemede en basit ve en çok kullanılan araçlardan birisi gri seviyesi histogramıdır. 
Bu fonksiyon görüntünün gri seviyesi içeriği hakkında bilgiler elde edilmesini sağlar. Histogramdan elde edilebilecek bazı bilgiler:
Koyu bir görüntünün histogram grafiğinin düşük gri seviye bölgesine yığılacağı açıktır.
Parlak (Açık renk) düzgün bir görüntünün histogram grafiğinin büyük gri seviye bölgesine yığılacağı açıktır.
İyi kontrastlı bir resmin histogram grafiği tüm gri seviye değerlerine eşit yayılmış olduğunu açıklar.


Görüntüdeki gölgenin yumuşatılması için gerçekleştirilecek işlemler bu işlemlerle benzerlik göstermektedir. Yani gölge olarak belirlenen bölgenin yani piksellerin renk değerlerinin görüntünün geneline uyarlanmasıdır.

# Histogram Eşitleme
İdeal olarak Histogram eşitleme; Giriş histogramını, her gri seviyesinde eşit piksel sayısına sahip bir histograma dönüştürme işlemi gibi düşünülebilir. Bu pratikte mümkün değildir. Bu yöntem histogramı dar olan resimler ya da resim içindeki bölgeler için daha iyi sonuç verir. Yani Histogram eşitleme renk değerleri düzgün dağılımlı olmayan resimler için uygun bir görüntü iyileştirme metodudur. Resmin tümüne uygulanabileceği gibi sadece belli bir bölgesine de uygulanabilir. Tüm resme uygulanırsa global histogram eşitleme, resmin belli bir bölgesine uygulandığında ise lokal histogram eşitleme adını alır.
Histogram eşitlemenin özeti olarak;

Görüntüdeki gölgenin yumuşatılması için gerçekleştirilecek işlemler bu işlemlerle benzerlik göstermektedir. Yani gölge olarak belirlenen bölgenin yani piksellerin renk değerlerinin görüntünün geneline uyarlanmasıdır.

Bu formülü uygulama adımlarına dökecek olursak;
 Resmin histogramı bulunur (her gri seviye için piksel sayısı grafiği).

Histogramdan yararlanılarak kümülatif histogram bulunur. Kümülatif   histogram, histogramın her değerinin kendisinden öncekiler ve kendisinin toplamı ile elde edilen değerleri içeren büyüklüktür.

Kümülatif histogram değerleri normalize edilip (toplam piksel sayısına bölünerek), yeni resimde olmasını istediğimiz max. renk değerleri ile çarpılır, çıkan değer tam sayıya yuvarlanır. Böylelikle yeni gri seviye değerleri elde edilmiş olur.

 Eski (Orijinal) gri seviye değerleri ile; 2.adımda elde edilen gri seviye değerleri biribirine karşılık düşürülür ve yeni histogram grafiği çizilir.

n: giriş görüntüsündeki toplam piksel sayısı (n0+n1+…….+nL-1 = n)

nj (nk ): j. gri seviyedeki piksel sayısı

L: mümkün olan (veya istenilen) toplam gri seviye sayısı ( 8 bit renk     derinliğinde 255 v.b)

sk : Daha iyi kontraslı bir görüntü elde etmek için gri seviye dönüşüm değeri.

Amaç; imgedeki düşük görünürlüğü iyileştirmektir.


Aşağıdaki dosya linkinden detaylı olarak bakabilirsiniz.

[Flask ile Histogram Aralığı ile Gölge Tespiti.docx](https://github.com/leventkalkavan/flask_goruntu_isleme/files/7098089/Flask.ile.Histogram.Araligi.ile.Golge.Tespiti.docx)


