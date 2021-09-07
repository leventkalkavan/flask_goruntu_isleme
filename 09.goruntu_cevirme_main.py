from flask import Flask , render_template
import cv2

#Yukarıdaki fonksiyonları ve yapısal elemanı oluşturmak için cv2 paketini içe aktarmalıdır.

app = Flask(__name__)

@app.route("/goruntucevirme")
def goruntucevirme():
    return render_template ("goruntucevirme.htm")

if __name__ =="__main__":

    app.run(debug=True)

import cv2

#Yukarıdaki fonksiyonları ve yapısal elemanı oluşturmak için cv2 paketini içe aktarmalıdır.

image=cv2.imread("static\img\rotate.jpg")

#Ardından, resmin okunması gerekiyor. Bu cv2.imread (dosya adı, flag) işlevi tarafından yapılır.

height, width = image.shape[:2]

#Görüntüyü merkezin etrafında döndürmek için resim ikiye bölünür.

rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2),180, .9)

#2D rotasyonun bir affine matrisini hesaplar.Sırasıyla gelen değerler kaynak görüntüdeki dönüş merkezi, derece cinsinden dönme açısı, izotropik ölçek faktörü.

rotated_image = cv2.warpAffine(image, rotation_matrix,(width,height))

#Bir resme afine dönüşümü uygular. Sırasıyla değerler giriş görüntüsü, dönüşüm matrisi, çıktı görüntüsünün boyutunu belirtir.

cv2.imshow ("Rotate imag", rotated_image)

#Belirtilen pencerede bir görüntü gösterir.

cv2.imwrite("static\img\rotate_yeni.jpg",rotated_image)

#Alternatif olarak, değiştirilmiş görüntüyü cv2.imwrite (isim, img) işleviyle de kaydedilebilir.

cv2.waitKey(0)
cv2.destroyAllWindows()

# Eğer cv2.imshow () kullanılırsa, yazılan kod yukarıdaki kodu da içermelidir.
