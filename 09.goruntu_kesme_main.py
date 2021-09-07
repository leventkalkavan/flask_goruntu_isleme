from flask import Flask , render_template
import cv2
#Yukarıdaki fonksiyonları ve yapısal elemanı oluşturmak için cv2 paketini içe aktarmalıdır.
app = Flask(__name__)

@app.route("/kesme")
def kesme():
    return render_template ("kesme.htm")

if __name__ =="__main__":

    app.run(debug=True)
    
image=cv2.imread("static\img\kesme.jpg")

#Ardından, resmin okunması gerekiyor. Bu cv2.imread (dosya adı, flag) işlevi tarafından yapılır.

height, width = image.shape[:2]

#Görüntünün boyutları üzerinde hareket edilebilmesi için resim ikiye bölünür.

start_row, start_col = int (height * .07), int (width * .42)


end_row, end_col = int (height * .90), int (width * .90)

# Görüntüde kırpılmak istenen boyuta göre değer verilir.

cropped = image [start_row : end_row , start_col : end_col]

#Belirtilen boyutların birbirleri üzerindeki işlemleri görüntünün kesilecek yerlerini belirtir.

cv2.imshow ("Kesilmis Resim", cropped)

#Belirtilen pencerede kesilen  görüntüyü gösterir.

cv2.imwrite("static\img\kesme_yeni.jpg",cropped)

#Alternatif olarak, değiştirilmiş görüntüyü cv2.imwrite (isim, img) işleviyle de kaydedilebilir.

cv2.waitKey(0)
cv2.destroyAllWindows()

# Eğer cv2.imshow () kullanılırsa, yazılan kod yukarıdaki kodu da içermelidir
