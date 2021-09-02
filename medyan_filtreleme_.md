# MEDYAN FİLTRELEME 
Medyan filtresi görüntü işlemede çok sık kullanılan filtredir. Görüntülerde gürültü adı verilen, istenmeyen sinyaller bulunmaktadır. Gürültü, görüntüyü kirleten ve görüntü kalitesini düşüren harici kaynaklarda oluşan etkidir. Gürültü bir görüntü içerisinde bir çok farklı kaynaklardan meydana gelebilir. Filtreleme yöntemleri sayesinde görüntüler gürültüden arındırılarak istenilen hale getirilebilir.
Filtreleme yöntemi görsel üzerinde uygulanacaktır. Uygulama sırasında hangi işlemlerin yapıldığı, filtrenin seçimi ve aşamalar anlatılacaktır. Uygulamanın Python dilinde kodlanması da gerçekleştirilecektir.
# Medyan Filtreleme Yöntemi Uygulaması:
Bahsedildiği üzere medyan filtresi en çok tercih edilen algoritmaların başında yer alır ve lineer bir işlem değildir.
Medyan filtreler nonlineer uzaysal filtrelerdir. Maskeyi oluşturan boyuttaki resim piksel değerlerinin küçükten büyüğe sıralanıp ortadaki değeri merkez piksele atama işlemidir.Medyan filtresi bir alçak geçiren filtredir.
Mean filtrelerinin genel çalışma mantığı ise; NxN boyutlu bir matris penceresi içerisinde bir ortalama değer bulmaya çalışarak işlenir. Bunu yaparken görüntü üzerinde gezen bir kayan pencere yöntemi kullanılır. Medyan filtresi mean filtreleri içerisinde en basit olanıdır. Pencere içerisindeki değerlerin aritmetik ortalamasını alır ve bu şekilde büyük atlamaları kaldırmış olur. Filtre uygulandıktan sonra; konumlarından ayrılmış olan pikseller tespit edilerek temizlenmiş olur. Görüntü içerisindeki yerel değişimleri yumuşatmış olur.
# Medyan Filtrelerinin Gerçekleştirdiği İşlemler:
Medyan filtresi için örnek olarak alınan değerler sırasıyla şunlar olsun:
996, 1718, 1002, 993, 1692, 1003
Alınan bu sayıları 3’erli gruplayalım(window size=3 alındı):
1.grup: [996 996 1718]  → Burada 996 sayısının 2 kere kullanılmasının sebebi window size’ın 3 olarak belirlenmiş olmasıdır. 1.grup için medyan=996 O halde 1. Sayı 996’dır. 
2.grup:[ 996, 1718, 1002]  → Sıralanırsa: 996 1002 1718. Bu grup için medyan değeri=1002dir. 2.sayı da 1002 olmuş oldu. 
3.grup:[ 1718, 1002, 993] → Sıralama işleminin ardından medyan değeri=1002. Üçüncü sayı 1002 olmuştur.  
4.grup:[1002 993 1693] → 4.grubun medyanı=1002 bulundu. 4. Sayı=1002 
5.grup:[ 993, 1692, 1003 ] →  Üç sayının medyanı 1003 dür. O halde beşinci sayının yeni değeri 1003 dür.
6. grup: [1692 1003 1003] → 6.grubun medyan değeri. 1003 dür. O halde son sayının yeni değeri 1003 olmuştur. 
Buna göre ilk başta verilmiş olan; 996 1718 1002 993 1692 1003 sayılarının yeni değerleri sırayla aşağıdaki gibi olmuştur.
996 1002 1002 1002 1003 1003 
Yeni elde ettiğimiz değerlerden anlaşılacağı gürültüden kaynaklı 1718 ve 1692 sayıları kaybolmuştur. Yeni değerlerin ortalaması ise 1001,3 dür.
Değerler; ortanca filtre kullanılmadan önce ortalama 1234 idi. Ortanca filtresi kullanımından sonra 1001,3 olmuştur.


Aşağıdaki dosya linkinden detaylı olarak bakabilirsiniz.

[Flask İle Medyan Filtreleme.docx](https://github.com/leventkalkavan/flask_goruntu_isleme/files/7096707/Flask.Ile.Medyan.Filtreleme.docx)


