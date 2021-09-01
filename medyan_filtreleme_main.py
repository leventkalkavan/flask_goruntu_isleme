from PIL import Image
from flask import Flask,request
from flask.templating import render_template
#gerekli kütüphaneleri ekliyoruz
app = Flask(__name__)

@app.route("/medyan")
def medyan():
    return  render_template ("medyan.htm")  

@app.route("/medyanyeni")
def medyanyeni():
    return render_template ("medyanyeni.htm") 

if __name__ == "__main__":
    app.run(debug=True)


resim = Image.open("static\img\medyanfiltreleme.jpg").convert("RGB")

resim.show(resim)
pix = resim.load()

#resmi load fonksiyonuyla pix değişkenine yüklüyoruz

w = resim.size[0]

 #resmin çözünürlüğünün genişlik boyutunu w ye aktarıyoruz

h = resim.size[1]

#resmin çözünürlüğünün yükseklik boyutunu h ye aktarıyoruz

graylist = [[0]*h for x in range (w)]

#ilk elemanla h'nin w kez çarpımı kadar bir liste oluşturulur.

temparray = [[0]*(h+2) for x in range (w+2)]

#ilk elemanla (h+2)'nin (w+2) kez çarpımı kadar bir liste oluşturulur.

print(resim.getpixel((3,5)))

# belirtilen koordinattaki pixeli yazdırır.

for i in range (w):

    for j in range (h):

        r,g,b = resim.getpixel((i,j))

#'getpixel' fonksiyonu ile renk kodlarını r,g,b değişkenlerine atıyoruz.

        print (r,g,b)

        gray = (int)((r*0.2126)+(g*0.7152)+(b*0.0722)) 

#gray değişkenine gri rengini veren değeri atıyoruz

        graylist[i][j] = gray 

#graylist listesinin her elemanına gray rengini atıyoruz.

        pix [i,j] = (gray,gray,gray)

#yuklenen resmin her elemanına gray değerini atıyoruz

for ni in range (1,w+1):

    for nj in range (1,h+1):
        temparray [ni] [nj]  =  graylist [ni-1] [nj-1]

med = [0]*9

gecici = 0
#med[ ] dizisine komsu piksellerin degerleri yazılıyor 
for m in range(1,w+1):

    for n in range (1,h+1):

        med[0] = temparray[m-1][n-1]

        med[1] = temparray[m-1][n]

        med[2] = temparray[m-1][n+1]

        med[3] = temparray[m][n-1]

        med[4] = temparray[m][n]

        med[5] = temparray[m][n+1]

        med[6] = temparray[m+1][n-1]

        med[7] = temparray[m+1][n]

        med[8] = temparray[m+1][n+1]

#sorted() sıralama fonksiyonudur.
        med = sorted(med)

#value değişkenine dizinin ortanca degeri atanıyor
        value = med[4]
 #resimdeki gürültü miktarını belirler

        pix[m-1,n-1] = (value,value,value)

resim.save("static\img\medyanfiltrelemeyeni.jpg")
resim.show()
