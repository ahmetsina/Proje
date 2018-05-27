# Görüntüden Cinsiyet Tespiti

Bu projede **NKÜ - Çorlu Mühendislik Fakültesi Bilgisayar Mühendisliği 2017-2018 Akademik Dönemi** Proje 1 ve Proje 2 dersinin teorik içerikleri ve uygulamaları yer almaktadır. Güz döneminde işlenen Proje 1 dersindeki işlediğimiz ve üzerinde çalıştığımız konu **öznitelik çıkarımı ve karşılaştırması**ydı. Bu çalışmamızın adımları ve elde edilen sonuçlar aşağıda belirtiliyor. Şu anda bulunduğumuz bahar döneminde, Proje 1 dersinden elde ettiğimiz sonuçlara göre görüntüden cinsiyet tespitini, uygulamaya ve somut bir projeye geçirmeyi planlıyorum.

#### Öznitelik Çıkarımı Ve Karşılaştırılması

Proje 1 dersindeki öznitelik çıkarımı ve karşılaştırma çalışmamız şu şekilde ilerledi. Bu derste kullandığımız ve üzerinde çalıştığımız ortam MatLab uygulamasıydı.

1. **Verilerin Toplanması ve İşlenmesi**
    * Bu konuda çalışma için gerekli veri gerçeğe yakın, farklı insanlara ait ve farklı farklı yüz ifadelerini barındıran **JPG** formatındaki görüntülerdi.
      Tabi bu görüntüleri, daha önceden **Kaggle** sitesinde bir yarışmada kullanılmış ve Youtube'daki Youtuberların videolarından belirli kesitler olan veri setinden hazır olarak elde ettik. 10000 görüntünün 8 binini eğitim, 2 binini de test verisi olarak ikiye ayırdık. Görüntüleri öznitelik çıkarımı işlemine sokmadan önce görüntü üzerinde önişlemler yaptık.

2. **Öznitelik çıkarımı**
    * Önişlemden geçen görüntülerin CNN, HOG ve LBP'ye göre ayrı ayrı öznitelik çıkarımı yaptık. CNN için MathConvNet, HOG ve LBP için ise VLFeat kütüphanesini kullandık.

3. **Eğitim**
    *  Görüntülerin öznitelik çıkarımlarını ve gerçek cinsiyet karşılıklarını SVM sınıflandırıcısı ile sınıflandırma işlemine tabi tuttuk. Bu eğitim işlemi ile belli bir SVM modeli elde ettik.

4. **Test ve Sınıflandırma**
    *  Modelimizi eğitim aşamasından sonra gerçek verileri test etmek üzere öncelikle öznitelik çıkarımı yaptık. Bu özniteliklerin modelimize göre karşılığını bulmak için öznitelik çıkarımlarını tahmin fonksiyonuna dahil edip çıktısını aldık.

5. **Elde Edilen Sonuçlar**
   * Her öznitelik çıkarımı methodu için eğitim ve test işlemlerini gerçekleştirdik. Ve elimizdeki veri setine göre şu şekilde sonuçlara ulaştık.

   | Öznitelik Türü | Başarı Oranı | Öznitelik Kombinasyonu | Başarı Oranı |
   |---| ---|---| :---: |
   | CNN  | %83,30 | CNN + LBP + HOG | % 94,80 |
   | LBP  | %76,60 | **CNN + HOG** | **%94,85** |
   | **HOG**  | **%91,40** | CNN + LBP | 90,10 |
   | | |HOG + LBP | %91,80|

   * Sonuçlara göre tek başına HOG en başarılı öznitelik çıkarımını bize sağlıyor. Çıkarım methodlarıyla tümleştirme yapıldığında ise CNN ve HOG kombinasyonu bize en iyi sonucu döndürüyor.



#### Proje 2 Dersinde ve İzlenecek Adımlar

Proje 1 dersindeki çalışmalar MatLab programı üzerinde prototip olarak yapılmıştı. Bu dönem bunu öncelikle Web üzerinde çalışan bir uygulamaya dökmeyi planlıyorum. Bu yüzden kullanacağım geliştirme ortamı tamamen değişecek. İzleyeceğim adımlar ise şöyle:

1. **Geliştirme Ortamının Kurulması**
    * Python 2.7'nin kurulması (Kullanacağım programlama dili. Hali hazırda şuanki ortamımda mevcut.)
    * JetBrains PyCharm IDE (Python yazarken kullanacağım IDE)
2. **Verileri Tekrardan İşleme**
    * Verilerin Python ortamında tekrardan işlenmesi. Bunun için ham görüntülerin işleme geçirilmemiş halini alıp 64x64px şekline getirerek eğitime hazır hale getireceğim.
3. **Verileri Eğitme ve Model Oluşturma**
    - Görüntülerden HOG ile öznitelik çıkarımı yapacağım. Ve bu çıkardığım verileri CSV formatında kaydedeceğim.
    - Her öznitelik çıkarımına karşılık gelen cinsiyet değerlerini de SVM sınıflandırıcı fonksiyonuyla işleyip SVM sınıflandırıcı modelimi oluşturacağım.
4. **Test Verileri ve Sonuçların İncelenmesi**
    - Bu aşamada test verilerinin öznitelik değerlerini, oluşturduğum SVM sınıflandırıcısında tahminleme yapıp genel başarı oranını yakalamaya çalışacağım.
    - İstenen başarı oranını yakaladığımda arkaplan işlemlerini hazır hale getireceğim.

5. **Flask Uygulamasını Oluşturma**
    - Bu aşamada Python'un micro web uygulamalar için kullanılan Flask kütüphanesi ile basit bir web sayfası oluşturacağım.
    - Sayfada en basitinden resim yükleme formu olacak.
    - Yüklenen resmin arkaplanda öznitelikleri çıkarılıp SVM sınıflandırıcısına sokulacak ve geri dönen sonucu sayfaya yansıtacak.


Eğer projem bu aşamalara gelir, başarılı bir şekilde çalışır ve yeteri kadar zaman olursa bu projeyi **Digital Ocean**'dan aldığım sanal sunucuya yükleyip orada koşturarak sonuç olarak json verisi döndürmeyi planlıyorum.
Böylelikle mobil uygulama yaparken yapacağım post işleminden dönen cevabı direk olarak uygulamada gösterebileceğim.








