Görüntü işleme (Computer Vision) öğrenme sürecimde yaptığım bu projede, bir görseldeki nesneyi arka plandan ayırmayı ve rengini değiştirmeyi denedim.
Bu kod, kırmızı bir gülü alıyor, arka planını temizliyor ve rengini mora çeviriyor. Bunu yaparken manuel bir eşik değeri (threshold) girmek yerine, Otsu Metodu en uygun değeri otomatik hesaplıyor.

Projenin Amacı

RGB katmanlarını (kanallarını) yönetmek.

Renk farklarını kullanarak nesne tespiti yapmak.

Otsu Thresholding mantığını kavramak.

HSV renk uzayında renk değişimi yapmak.

Kullanılan Kütüphaneler

Projeyi çalıştırmak için şu kütüphanelere ihtiyacınız var:

Python 3

OpenCV (cv2)

NumPy

Gerekli kütüphaneleri indirin:

pip install opencv-python numpy

Proje klasörüne rose.jpeg adında bir görsel ekleyin (veya kod içindeki dosya adını değiştirin).

Kodu çalıştırın.

Örnek Girdi ve Çıktılar
![rose](https://github.com/user-attachments/assets/840bd0d1-db7f-49ff-9fe9-aed246cbf1d2)
<img width="1500" height="1030" alt="image" src="https://github.com/user-attachments/assets/9bbf2ca6-0af0-401f-9283-afe58252661d" />
<img width="1494" height="1039" alt="image" src="https://github.com/user-attachments/assets/884fbcbf-13bb-443c-8435-68c8568be385" />

Kodun Mantığı
Kanalları Ayırma: Resmi Mavi, Yeşil ve Kırmızı (BGR) katmanlarına ayrılması.

Fark Alma: Gül kırmızı olduğu için, Kırmızı (R) kanalı ile Yeşil (G) kanalı arasındaki fark alındı (cv2.subtract). Bu sayede gül, arka plandan daha net ayrıldı.

Otsu ile Eşikleme: Hangi pikselin gül, hangisinin arka plan olduğuna karar vermek için cv2.THRESH_OTSU kullanıldı. Bu yöntem, en uygun eşik değerini (threshold) kendisi buluyor.

Renk Değiştirme: Resmi HSV formatına çevirip, sadece maskelenen (gül olan) alanın rengini (Hue değerini) değiştirildi.

Sonuç: Arka planı siyah yapıp sadece mor renge çevirilen gül ekrana yansıtıldı.
