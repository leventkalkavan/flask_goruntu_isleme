# Python ile Ağırlık Toplama Yöntemi Uygulaması:
Uygulamada renkli bir resmi gri tonlarına dönüştüreceğiz. Python dilinde resim dosyaları üzerinde işlem yapabilmek için “Image” kütüphanesini projeye dahil edilmelidir. Python dili için bu tür grafik kütüphanelerini içine bulunduran “PIL” paketini indirebilir. Bunun için terminalden “pip3 install pillow” komutunu yazarak ‘PIL’ paketini indiriyoruz. PyCharmda Python Projesi açarak kodlar yazılabilir.

Bu uygulamada ekranda görüntü alabilmek için “resim.show()” metodu kullanılır.Bu metodun çalışabilmesi için bir görüntüleme programına ihtiyaç vardır.
Griye dönüştürülecek resim PyCharmda Python projelerinin olduğu dosyanın içindeki venv klasöründe bulunmalıdır.Örneğin;
/home/gorountuisleme/PycharmProjects/deneme/venv. Bu sayede resmin adı kullanılarak resim çağrılabilir.Fakat resim ile dosya aynı klasörde değilse resmin olduğu yerin adresi kod parçasının ilgili kısmına yazılır.

# Flask ile Ağırlık Toplama Kodu:
Uygulamanın çalışması için gerekli olan from flask import Flask, request , render_template kütüphanelerini ekliyoruz. Ardından çalışma dosyamızın olduğu dizide templates isimli klasör oluşturuyoruz. Ardından HTML sayfalarınızı bu klasöre koyuyoruz. Örneğin agirliktoplama.html gibi sayfalarınızı bu klasöre koyup HTML sayfalarına gerekli kodlamaları yapıyoruz. Son olarak uygulamayı çalıştırdıktan sonra karşımıza çıkan linkten uygulamamıyı HTML sayfaları üzerinde görebiliriz.
[Flask Ağırlık Toplama.docx](https://github.com/leventkalkavan/flask_goruntu_isleme/files/7089424/Flask.Agirlik.Toplama.docx)


