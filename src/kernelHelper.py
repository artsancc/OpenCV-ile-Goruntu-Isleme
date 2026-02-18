import cv2
import numpy as np

def maske_olustur(img):
    # Kanallara ayır
    b, g, r = cv2.split(img)

    # R-G farkı
    fark = cv2.subtract(r, g)

    # Gürültü azaltma
    fark_blur = cv2.GaussianBlur(fark, (5,5), 0)

    # Otsu threshold
    ret, maske = cv2.threshold(fark_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Morfolojik işlemler
    kernel = np.ones((3,3), np.uint8)
    maske = cv2.morphologyEx(maske, cv2.MORPH_CLOSE, kernel, iterations=2)
    maske = cv2.morphologyEx(maske, cv2.MORPH_OPEN, kernel, iterations=1)

    return maske, ret


def rengi_degistir(img, maske):
    hsv_resim = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Mor renk tonu
    hsv_resim[maske == 255, 0] = 145

    mor_resim = cv2.cvtColor(hsv_resim, cv2.COLOR_HSV2BGR)
    return mor_resim


def arka_plani_karart(img, maske):
    sonuc = cv2.bitwise_and(img, img, mask=maske)
    return sonuc
