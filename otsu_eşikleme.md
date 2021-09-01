# OTSU EŞİKLEME METODU
  Adını geliştiricisi Nobuyuki Otsu’dan alan yöntem gri tonlamalı bir görüntüyü monokroma dönüştürmek için kullanılan yaygın bir görüntü işleme görevidir. Yöntem sadece renklerin görüntü üzerinde kaçar defa bulunduğuna bakar.Gri seviyedeki bir görüntüyü ikili seviyeye dönüştürülerek kullanılabilecek en uygun eşik değerinin tespitini sağlar.Bu yöntemde, renklerin görüntü üzerinde var olma sayısına bakıldığı için uygulamaların eşik belirleme adımına geçmeden önce renk histogramı hesaplanır ve tüm hesaplamalar bu histogram üzerinden yapılır. Otsu algoritması histogramda eşikleme yapılabilecek en uygun konumun bulunması için kullanılır.
Otsu algoritmasında histogramın her bir elemanını eşik gibi düşünerek her biri için “weight”,mean” ve ”variance” diye tabir edilen veriler hem eşikten önce(background) hem de eşikten sonrası(foreground) için hesaplanır.
Her bir eleman eşik kabul edilerek her bir eleman için hesaplamalar yapılacağı için belirlenen elemandan öncesi eşik öncesi(background),belirlenen elemandan sonrası eşik sonrası(foreground) olarak adlandırılır. 
Detaylı olarak aşağıdaki dosyadan bakabilirsiniz.

[Flaskla Otsu Eşikleme Yöntemi.docx](https://github.com/leventkalkavan/flask_goruntu_isleme/files/7090999/Flaskla.Otsu.Esikleme.Yontemi.docx)
