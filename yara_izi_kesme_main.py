import cv2
from flask import Flask , render_template

#Gerekli kütüphaneleri ekliyoruz.

app = Flask(__name__)

@app.route("/yara")
def yara():
    return render_template ("/yara.htm")

#HTML sayfasının kodlarını giriyoruz.  

if __name__ =="__main__":

    app.run(debug=True)

image=cv2.imread("yaraizi.jpg")

#Ardından, resmin okunması gerekiyor. Bu cv2.imread (dosya adı, flag) işlevi tarafından yapılır.

height, width = image.shape[:2]

#Görüntünün boyutları üzerinde hareket edilebilmesi için resim ikiye bölünür.

start_row, start_col = int (height * .25), int (width * .30)


end_row, end_col = int (height * .60), int (width * .60)

# Görüntüde kırpılmak istenen boyuta göre değer verilir.

cropped = image [start_row : end_row , start_col : end_col]

#Belirtilen boyutların birbirleri üzerindeki işlemleri görüntünün kesilecek yerlerini belirtir.

cv2.imshow ("Kesilmis Resim", cropped)

#Belirtilen pencerede kesilen  görüntüyü gösterir.

cv2.imwrite("yara-kesme.jpg",cropped)

#Alternatif olarak, değiştirilmiş görüntüyü cv2.imwrite (isim, img) işleviyle de kaydedilebilir.

cv2.waitKey(0)
cv2.destroyAllWindows()

# Eğer cv2.imshow () kullanılırsa, yazılan kod yukarıdaki kodu da içermelidir.
