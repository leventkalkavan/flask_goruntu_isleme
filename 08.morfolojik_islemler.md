# MORFOLOJİK İŞLEMLER
 Biyolojinin canlıların şekil ve yapıları ile ilgilenen dalına morfoloji (biçim bilim) adı verilmektedir. Matematiksel morfoloji ise temel küme işlemlerine dayanan, imgedeki sınırlar (borders), iskelet (skeleton) gibi yapıların tanımlanması ve çıkartılması, gürültü giderimi, bölütleme gibi uygulamalar için gerekli bir araçtır. İmge işlemede genellikle, morfolojik süzgeçleme, inceltme (thinning), budama (pruning) gibi ön/son işlem olarak da sıkça kullanılırlar. Gri tonlu imgeler üzerinde de yapılabileceği gibi, genellikle ikili imgeler üzerinde yapılan işlemlerdir.Uygulama alanları : 
Görüntülerin ön işlenmesinde ya da son işlenmesi adımlarında
Sınır, kenar gibi görüntü bileşenlerinin ayrıştırılmasında
İkili Morfolojik İşlemler
İkili görüntülerde her pikselin (x,y) değeri 0 veya 1 olabilir. İkili görüntü genellikle siyah ve beyaz olarak görülür.Temel ikili morfolojik işlemler :
genleşme işlemi,aşınma işlemi,açma işlemi,kapama işlemi.

# Genleşme İşlemi
İkili imgedeki nesneyi büyütmeye ya da kalınlaştırmaya yarayan morfolojik işlemdir.Sayısal bir imgeyi genişletmek imgeyi yapısal elemanla kesiştiği bölümler kadar büyütmektir. İşlenecek imgenin her bir pikseli, yapısal elemanın merkez noktasına oturtularak genleşme işlemi yapılmaktadır. Kalınlaştırma işleminin nasıl yapılacağını yapısal eleman belirler. Genleşme işlemi uygulanmış bir imgede, imge içerisindeki deliklerin ve boşlukların doldurulması ve köşe noktasının yumuşaması gözlenir.

# Aşınma İşlemi
İkili imgedeki nesneyi küçültmeye ya da inceltmeye yarayan morfolojik işlemdir. Aşınma işlemi tam anlamıyla olmasa da bir bakıma genleşme işleminin tersi gibidir. İmge içerisindeki nesneler ufalır, delik varsa genişler, bağlı nesneler ayrılma eğilimi gösterir.

# Açma İşlemi
İmge üzerinde aşınma işleminin hemen ardından genleşme işlenmesi uygulanması sonucu açma işlemi elde edilir. İmge içerisindeki nesneler ve nesneler arasındaki boşluklar yapısal elemanın büyüklüğüne göre temizlenir. İmge üzerinde kalan nesneler orijinal imgedeki şekillerinden biraz daha küçük hale gelir. Açma işlemi ile birbirine yakın iki nesne imgede fazla değişime sebebiyet vermeden ayrılmış olurlar.

# Kapama İşlemi
İmge üzerinde genleşme işleminin hemen ardından aşınma işleminin uygulanması sonucu kapama işlemi elde edilir. Dolayısıyla birbirine yakın iki nesne imgede fazla değişiklik yapılmadan birbirine bağlanmış olur. Kapama işlemi sonunda imge içerisindeki noktalar birbirlerini kapatırlar, imgedeki ana hatlar daha da dolgunlaşır. Genleşme işlemine benzer bir şekilde kapama işleminde de birbirine yakın olan noktalar arasındaki boşluklar dolar ve noktalar birleşir. İmge üzerinde kalan nesneler, orijinal imgedeki şekillerine bürünürler.

Aşağıdaki dosya linkinden detaylı olarak bakabilirsiniz.

[Flask İle Morfolojik İşlemler.docx](https://github.com/leventkalkavan/flask_goruntu_isleme/files/7114488/Flask.Ile.Morfolojik.Islemler.docx)
