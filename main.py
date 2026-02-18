import cv2
from src.kernelHelper import maske_olustur, rengi_degistir, arka_plani_karart

# Görseli yükle
img = cv2.imread('input/rose.jpeg')

# Maske oluştur
maske, otsu_degeri = maske_olustur(img)
print(f"Otsu'nun hesapladığı eşik değeri: {otsu_degeri}")

# Rengi değiştir
mor_resim = rengi_degistir(img, maske)

# Arka planı karart
sonuc = arka_plani_karart(mor_resim, maske)

# Görselleri göster
cv2.imshow("OTSU MASK", maske)
cv2.imshow("SONUC", sonuc)

cv2.waitKey(0)
cv2.destroyAllWindows()

