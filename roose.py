import cv2
import numpy as np

img = cv2.imread('rose.jpeg')
# Görseli katmanlara bölme işlemi
b, g, r = cv2.split(img)
fark = cv2.subtract(r, g)
# Otsu ile eşikleme işlemi
ret, maske = cv2.threshold(fark, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# Otsu'nun hesapladığı sayıyı görmek için
print(f"Otsu'nun hesapladığı eşik değeri: {ret}")
# Kernel ile temizleme işlemi
kernel = np.ones((3,3), np.uint8)
maske = cv2.morphologyEx(maske, cv2.MORPH_CLOSE, kernel, iterations=2)
maske = cv2.morphologyEx(maske, cv2.MORPH_OPEN, kernel, iterations=1)
# Renk değiştirme işlemi
hsv_resim = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv_resim[maske == 255, 0] = 145
mor_resim = cv2.cvtColor(hsv_resim, cv2.COLOR_HSV2BGR)
# Arka planı karartma
sonuc = cv2.bitwise_and(mor_resim, mor_resim, mask=maske)

cv2.imshow('OTSU MASK', maske)
cv2.imshow('SONUC', sonuc)

cv2.waitKey(0)

cv2.destroyAllWindows()
