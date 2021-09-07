# HSV RENK UZAYI
 RGB renk uzayı genel olarak kullanılan renk uzayıdır. Bu renk uzayında üç ana bileşen kullanılır.Görüntü r, g, b yani kırmızı, yeşil, mavi renk kodları üzerine tanımlanır. Her piksel bu renk kodlarına göre ara değerler alır. Böylece renkli bir resim elde edilir.
HSV renk uzayı ise Hue(Renk), Saturation(Doygunluk) ve Value(Parlaklık) terimleri ile rengi tanımlar.RGB de renklerin karışımı kullanılmasına karşın HSV de renk, doygunluk ve parlaklık değerleri kullanılır. Doygunluk rengin canlılığını belirlerken parlaklık rengin aydınlığını ifade eder. Örneğin; HSV uzayında siyah renk için renk ve doygunluk değerleri 0 ile 255 arasında herhangi bir değer alabilirken  parlaklık değeri sıfırdır. Beyaz renkte ise parlaklık değeri 255’tir. Buna göre herhangi bir bilgisayarlı görme/görüntü işleme uygulamasında belirli renkteki bir nesneyi ayırt etmek istenirse HSV renk uzayını kullanmak daha elverişlidir. Çünkü RGB renk uzayında eşik değeri için kullanılan filtreler yerine burada sadece Hue bileşeni ile eşik değeri belirlenebilir. Böylelikle daha net renkler elde edilebilir.
 HSV renk uzayı 1978 yılında Alvy Ray Smith tarafından RGB uzayına göre insan görme sistemine daha benzer bir yapı oluşturmak amacıyla tanımlandı. Şekil 1’de görüleceği üzere H değeri 0-360° arasında değişirken renklerin öz değerleri değişir. Ancak H sabit olarak seçilir ve diğer değerler (S-V) 0-100 arasında değiştirilirse aynı rengin farklı doygunluk ve parlaklıktaki değerleri elde edilir. Bu özelliğinden dolayı HSV renk temelli ayırma işlemlerinde sıklıkla tercih edilir. İki uzay arasındaki dönüşüm doğrusal olmayan bir bağlantı ile gerçekleştirilir.

# HSI RENK UZAYI
RGB, CMY gibi renk uzayları insan gözünün renk alma yapısındadır. İnsan beyninde renkler tanınırken ya da birbiri ile karşılaştırılırken bu modellerin kullanımı zordur.
Bu nedenle bu tür çalışmalarda renk özü (hue-H), doygunluk (saturation-S) ve şiddet (intensity-I) tanımlamaları kullanılır. Bu bileşenlerden oluşan modele de HSI (hue, saturation, intensity) renk modeli adı verilir.
Sonuçta söyleyebiliriz ki, RGB renk modeli renk oluşturma için idealdir (örn;
monitör) fakat betimlemede kötüdür. HSI renk modeli ise renge bağlı tanımlamada çok iyidir.

# YUV RENK UZAYI
 PAL, NTSC, SECAM kompozit renkli video standartlarında kullanılır.

 Y, ışıklılık (luma); U ve V renklilik (chrominance) bileşenleridir.
 YUV bileşenleri RGB’den türetilir.

 Y, ortalama parlaklığı veren ve R, G, B bileşenlerinin ağırlıklı ortalaması ile
 elde edilen ışıklılık bileşeni; U, mavi bileşeninden Y’nin; V, kırmızı
 bileşeninden Y nin çıkarılması ile elde edilen fark bileşenleridir.
 
Aşağıdaki dosya linkinden daha detaylı bakabilirsiniz.

[Flask ile HSV,HSI,YUV .docx](https://github.com/leventkalkavan/flask_goruntu_isleme/files/7097107/Flask.ile.HSV.HSI.YUV.docx)
