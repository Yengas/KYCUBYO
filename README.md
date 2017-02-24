# KYCUBYO
Bu dökümantasyon KYCUBYO içinde kullanılacak olan araçları, editörleri, yazılım dillerini, kütüphaneleri Türkçe olarak açıklamak ve KYCUBYO içinde bu teknolojiler ile ilgili kimlerin deneyimli olduğunu belirtmek için yazılmıştır.

Dökümantasyon içerisinde karar kılınan herşey issuelar ile takip edilip, ortak bir karar alındıktan sonra eklenmiştir. Burada bulunan herhangi bir karar ile ilgili sorunuz var ise, issue açarak takip edilebilir bir şekilde sorunuzu belirtebilirsinniz.

## Projenin düzenlenmesi, ekleme yapılması
Bu proje üzerinde verilen herhangi bir karar ile ilgili düzenleme yapmak veya yeni bir teknoloji eklemek isterseniz, ilk önce bir issue açmanız veya varolan bir issue'ya yorum eklemeniz gerekmektedir.

### Proje Düzeni
Projede verilen her bir karar ve kullanılan teknoloji, klasör yapısı kullanarak kategorilendirilmiştir. Klasörler kategoriyi açıklayan bir README.md dosyası bulundurmak zorundadır. Eklemek istediğiniz karar ile ilgili ek döküman veya dosya(konfigürasyon vb.) bulundurmak isterseniz, bu karar için bir klasör oluşturup, karar ile ilgili detayları README.md dosyasında yazabilirsiniz.

### İçerik Düzeni
Her bir karar bu kararı vermek için kullanılan issue'ya, ve ilgili teknoloji üzerinde deneyimli kişilere bir referans içermek zorundadır.

### Örnek Proje Düzeni
```
.
├── İşletim Sistemleri
├── Proje Geliştirme                 # Proje Geliştirme kategorisinde verilen kararlar
│   ├── Mesajlaşma Uygulamaları
│   ├── Proje Takip ve Yönetimi
│   └── Versiyon Kontrol             # Proje Geliştirmenin bir alt kategorisi, Versiyon Kontrol ile ilgili kararlar
│       ├── Git.md                   # Git kararını açıklayan bir yazı, ilgili issue ve deneyimli kişiler
│       └── Uzak Depolama
│           └── Github
│               ├── README.md        # Github kararını açıklayan bir yazı, ilgili issue ve deneyimli kişiler
│               └── Student Pack.md  # Github ile ilgili ek bir döküman
├── Yazılım Dilleri
├── Yazılım Geliştirme Araçları
│   └── Editörler
└── README.md                        # Bu projeyi açıklayan bir yazı ve projenin yönetimi/düzeni hakkında bilgiler
```
