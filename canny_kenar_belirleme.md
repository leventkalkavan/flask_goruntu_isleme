# CANNY KENAR BELİRLEME
Canny kenar belirleme algoritması; görüntüde keskin olarak belirlenmiş kenarları bulmak için John F. Canny tarafından geliştirilmiş ve aşamaları olan bir algoritmadır. Kenar bulmada son derece etkin olarak kullanılan bir algoritmadır. Aşamaları maddeleyecek olursak; Görüntünün gürültülerini azaltmak amacıyla Gaussian çekirdekle konvolüsyon alınarak azaltılır. Gaussian filtre dışında Mean ya da Medyan filtre de kullanılabilir. . Gradyan operatörü uygulanır. Bu şekilde görüntünün Gradyan büyüklüğü ve yönü hesaplanır. Bu işlem için Sobel filtresi en çok kullanılan yöntemdir. Bunun dışında Prewitt ve Robert kenar bulma metotları da mevcuttur. . Kenarlar Non Maxima baskılama kullanılarak incelemeye alınır. . İkili eşikleme uygulanır bu şekilde istenmeyen ayrıntılardan arındırılma işlemi gerçekleştirilir. . Güçlü-zayıf ayrımı yapıldıktan sonra baskılama uygulanır ve asıl kenarlarla görüntüye son hali verilir.
# Mean Filtresi
Mean filtresi alçak geçiren filtre olarak çalışmaktadır. Alçak geçiren filtre belirli bir frekansın üzerinde kalan sinyallerin işlenmesini sağlayan filtredir. Mean filtrenin çalışma mantığı; pencerede bulunan piksel değerinin diğer tüm piksel değerlerinin ortalaması ile değiştirerek çalışır. Pencere genellikle karedir yani matris olarak düşünülürse nxn boyutunda kare matristir.
# Sobel İşleci 
Sayısal bir görüntü, bir fonksiyon olarak değerlendirildiğinde, bir nokta üzerindeki gradyan değerinin, 3×3 komşulukta mümkün olan dört merkezi yönde elde edilebilir. Gradyan değerlerinin vektör toplamları şeklinde oluşturulması düşüncesine dayanmaktadır.

Bu gradyan değerlerinin vektör toplamları; gradyan ölçümleri üzerinde ortalama değer bulunmasını sağlamaktadır. 3×3’lük komşuluk için merkez noktanın gradyan değeri, dik vektör çiftlerinin vektör toplamları olarak bulunmaktadır.
Sobel işlecinde iki adet konvolüsyon çekirdeği yer alır. Bunlar görüntü içerisindeki ani ışık yoğunluk değişimi olan yerlerin belirlenmesini sağlar.
# Prewitt İşleci 
Sobel işleci gibi düşey ve yatay keskinlik sağlamaktadır. Sobel işlece göre daha basittir ama sonucunu değerlendirecek olursak biraz daha gürültü içermektedir.
# Robert İşleci
Görüntü işlemede kullanılan en eski işleçtir. Bu işleçle sadece yatay ya da sadece düşey olarak kenarlar elde edilmektedir. Hızlı ve basit bir uygulamaya sahip olduğundan gerçek zamanlı uygulamalarda çokça tercih edilmektedir.c

Aşağıdaki dosya linkinden daha detaylı bakabilirsiniz.

[Flask İle Canny Kenar Belirleme.docx](https://github.com/leventkalkavan/flask_goruntu_isleme/files/7111915/Flask.Ile.Canny.Kenar.Belirleme.docx)

