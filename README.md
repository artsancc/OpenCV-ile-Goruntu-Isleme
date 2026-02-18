Görüntü işleme (Computer Vision) öğrenme sürecimde yaptığım bu projede, bir görseldeki nesneyi arka plandan ayırmayı ve rengini değiştirmeyi denedim.
Bu kod; kırmızı bir gülü alıyor, Otsu Metodu ile otomatik eşikleme yapıyor, Morfolojik İşlemler (Kernel) ile maskeyi pürüzsüzleştiriyor ve son olarak gülün rengini mora çeviriyor. 

Projenin Amacı

RGB katmanlarını (kanallarını) yönetmek.

Renk farklarını kullanarak nesne tespiti yapmak.

Otsu Thresholding mantığını kavramak.

Morfolojik işlemler (Erosion, Dilation, Opening, Closing) ile gürültü temizlemek ve maske iyileştirmek.

HSV renk uzayında manipülasyon yapmak.

Fonksiyonel ve modüler kod yapısı kurmak.

Kullanılan Kütüphaneler

Projeyi çalıştırmak için şu kütüphanelere ihtiyacınız var:

Python 3

OpenCV (cv2)

NumPy

Gerekli kütüphaneleri indirin:

pip install opencv-python numpy

Proje klasörüne rose.jpeg adında bir görsel ekleyin (veya kod içindeki dosya adını değiştirin).

Kodu çalıştırın.

##Input
![rose](https://github.com/user-attachments/assets/840bd0d1-db7f-49ff-9fe9-aed246cbf1d2)

##Output
<img width="1494" height="1034" alt="image" src="https://github.com/user-attachments/assets/7df91cb6-8557-4eb2-98d9-15afbb7f7516" />
<img width="1498" height="1045" alt="image" src="https://github.com/user-attachments/assets/c18462a2-bddb-48fd-923d-0a21195571bf" />

Kodun Mantığı

Proje, src dosyası içerisindeki yardımcı fonksiyonları kullanarak şu adımları izler:

Kanalları Ayırma: Resim Mavi, Yeşil ve Kırmızı (BGR) katmanlarına ayrılır.

Fark Alma: Gül kırmızı ağırlıklı olduğu için, Kırmızı (R) kanalı ile Yeşil (G) kanalı arasındaki fark alınır (cv2.subtract). Bu, gülü arka plandan ayırmanın ilk adımıdır.

Gürültü Azaltma (Blur): Fark görüntüsüne GaussianBlur uygulanarak keskin pikseller yumuşatılır, bu sayede eşikleme daha sağlıklı çalışır.

Otsu ile Eşikleme: Hangi pikselin gül, hangisinin arka plan olduğuna karar vermek için cv2.THRESH_OTSU kullanılır. Bu yöntem, manuel değer girmeden en uygun eşik değerini (threshold) otomatik hesaplar.

Maske İyileştirme (Kernel & Morfolojik İşlemler):

Otsu işlemi sonrası maskede oluşan siyah noktalar (kayıplar) ve dışarıdaki beyaz gürültüler için 3x3'lük bir kernel matrisi oluşturulur.

Closing (Kapama): Gülün içinde oluşan siyah delikleri kapatmak için uygulanır.

Opening (Açma): Gülün etrafındaki istenmeyen küçük beyaz gürültüleri silmek için uygulanır.

Renk Değiştirme: Resim HSV formatına çevrilir ve temizlenen maske kullanılarak sadece gülün olduğu bölgenin "Hue" (Renk) değeri değiştirilir (Mor yapılır).

Sonuç: Arka plan karartılır ve sadece rengi değiştirilmiş, temizlenmiş gül ekrana yansıtılır.
