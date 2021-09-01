from flask import Flask,request, render_template 
import PIL
from PIL import Image

app = Flask(__name__)

@app.route("/agirliktoplama")
def agirliktoplama():
    return render_template("agirliktoplama.htm")  

@app.route("/agirliktoplamayeni")
def agirliktoplamayeni():
    return  render_template("agirliktoplamayeni.htm")  


if __name__ == "__main__":
    app.run(debug=True)

resim = Image.open("static\img\manzara.jpg").convert("RGB")

resim.show(resim)
yuklenen = resim.load()

genislik = resim.size[0]

yukseklik = resim.size[1]

for i in range (genislik):
    
    for j in range(yukseklik):
        r, g, b = resim.getpixel((i, j)) 
        
        gray = (int) ((r*0.2126)+(g*0.7152)+(b*0.0722))    
       
        yuklenen[i, j] = (gray, gray, gray)


resim.save("static\img\manzara_yeni.jpg")

resim.show(resim)
