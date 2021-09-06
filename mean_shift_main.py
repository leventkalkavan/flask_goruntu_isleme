from flask import Flask , render_template
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from PIL import Image
import matplotlib.pyplot as plt

#Gerekli kütüphaneleri ekliyoruz.

app = Flask(__name__)

@app.route("/mean")
def anaSayfa():
    return render_template ("/mean.htm")

if __name__ =="__main__":

    app.run(debug=True)

image = Image.open("static\img\mean.jpg")

# Kullanacağımız resmi ‘open’ fonksiyonu ile açıp ‘resim’ değişkenine atıyoruz.

image = np.array(image)

original_shape = image.shape

# Resmin 687x1025 RGB kanallarına ulaşılır.

X = np.reshape(image, [-1, 3])

# Resim düzleştirilir.

plt.imshow(image)

bandwidth = estimate_bandwidth(X, quantile=0.1, n_samples=100)

print(bandwidth)

#Resmimizden (veri noktaları) kullanmak için çekirdek bant genişliğini yazılır.

ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)

ms.fit(X)

#Şimdi X'te saklanan görüntü segmentasyonunu yapmak için görüntü üzerine Meanshift'i çalıştırın.

labels = ms.labels_

print(labels.shape)

cluster_centers = ms.cluster_centers_

print(cluster_centers.shape)

labels_unique = np.unique(labels)

n_clusters_ = len(labels_unique)

print("number of estimated clusters : %d" %n_clusters_)

#Ne yapıldığını anlamak için bazı hata ayıklama bilgileri yazdırın. Görünen bu 4 küme 4 renk verdi. Burası farklı parametrelerle yeniden çalıştırılırsa, farklı sonuçlar bulunabilir.

segmented_image = np.reshape(labels, original_shape[:2])  

# Sadece boyut al, RGB kanallarını görmezden gelinir.

plt.figure(2)

plt.subplot(1, 2, 1)

plt.imshow(image)

plt.axis('off')

plt.imsave("static\img\mean1.jpg",image)

plt.subplot(1, 2, 2)

plt.imshow(segmented_image)

plt.axis('off')

plt.imsave("static\img\mean_yeni.jpg",segmented_image)

#Mean Shift uygulanmış görüntü ve orjinal görüntü klasöre kaydedilir.
