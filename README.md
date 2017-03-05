# KYCUBYO
Bu dökümantasyon KYCUBYO içinde kullanılacak olan araçları, editörleri, yazılım dillerini, kütüphaneleri Türkçe olarak açıklamak ve KYCUBYO içinde bu teknolojiler ile ilgili kimlerin deneyimli olduğunu belirtmek için yazılmıştır.

Dökümantasyon içerisinde karar kılınan herşey [issuelar](https://github.com/Yengas/KYCUBYO/issues?utf8=%E2%9C%93&q=) ile takip edilip, ortak bir karar alındıktan sonra eklenmiştir. Burada bulunan herhangi bir karar ile ilgili sorunuz var ise, veya deneyimli kişiler listesine eklenmek istiyorsanız, issue açarak takip edilebilir bir şekilde isteğinizi belirtebilirsinniz.

Bu proje üzerinde [haftalık olarak yaptıklarımız](https://github.com/Yengas/KYCUBYO/issues?utf8=%E2%9C%93&q=label%3A%22Haftan%C4%B1n%20%C3%96zeti%22%20)'ın özeti ve kulübe yeni katılan arkadaşları yönlendirmek için rehber niteliğinde dökümanlarda bulabilirsiniz.

## Döküman İçerikleri
[//]: # (TOCSTART)
- Proje Geliştirme
	- [Mesajlaşma Uygulamaları](./Proje Geliştirme/Mesajlaşma Uygulamaları)
		- [Slack](./Proje Geliştirme/Mesajlaşma Uygulamaları/Slack.md)
	- [Proje Takip ve Yönetimi](./Proje Geliştirme/Proje Takip ve Yönetimi)
		- [Github Issues](./Proje Geliştirme/Proje Takip ve Yönetimi/Github Issues.md)
	- [Versiyon Kontrol](./Proje Geliştirme/Versiyon Kontrol)
		- [Uzak Depolama](./Proje Geliştirme/Versiyon Kontrol/Uzak Depolama)
			- [Github](./Proje Geliştirme/Versiyon Kontrol/Uzak Depolama/Github)
				- [Student Pack](./Proje Geliştirme/Versiyon Kontrol/Uzak Depolama/Github/Student Pack.md)
		- [Git](./Proje Geliştirme/Versiyon Kontrol/Git.md)
- Yazılım Geliştirme Araçları
	- [Editörler](./Yazılım Geliştirme Araçları/Editörler)
		- [Jetbrains](./Yazılım Geliştirme Araçları/Editörler/Jetbrains)
			- [Öğrenci Hesabı](./Yazılım Geliştirme Araçları/Editörler/Jetbrains/Öğrenci Hesabı.md)
		- [Vim](./Yazılım Geliştirme Araçları/Editörler/Vim.md)
	- [Sanallaştırma ve Konteyner Teknolojileri](./Yazılım Geliştirme Araçları/Sanallaştırma ve Konteyner Teknolojileri)
		- [Docker](./Yazılım Geliştirme Araçları/Sanallaştırma ve Konteyner Teknolojileri/Docker.md)
		- [Virtualbox](./Yazılım Geliştirme Araçları/Sanallaştırma ve Konteyner Teknolojileri/Virtualbox.md)
[//]: # (TOCEND)

## Dökümanın düzenlenmesi, ekleme yapılması
Bu döküman üzerinde verilen herhangi bir karar ile ilgili düzenleme yapmak veya yeni bir teknoloji eklemek isterseniz, ilk önce bir issue açmanız veya varolan bir issue'ya yorum eklemeniz gerekmektedir.

### Döküman Düzeni
Dökümanda verilen her bir karar ve kullanılan teknoloji, klasör yapısı kullanarak kategorilendirilmiştir. Klasörler kategoriyi açıklayan bir README.md dosyası bulundurmak zorundadır. Eklemek istediğiniz karar ile ilgili ek döküman veya dosya(konfigürasyon vb.) bulundurmak isterseniz, bu karar için bir klasör oluşturup, karar ile ilgili detayları README.md dosyasında yazabilirsiniz.

### İçerik Düzeni
Her bir karar bu kararı vermek için kullanılan issue'ya, ve ilgili teknoloji üzerinde deneyimli kişilere bir referans içermek zorundadır.

### Örnek Döküman Düzeni
```
.
├── İşletim Sistemleri
├── Proje Geliştirme                 # Proje Geliştirme kategorisinde verilen kararlar
│   ├── Mesajlaşma Uygulamaları
│   ├── Proje Takip ve Yönetimi
│   └── Versiyon Kontrol             # Proje Geliştirmenin bir alt kategorisi, Versiyon Kontrol ile ilgili kararlar
│       ├── README.md                # Versiyon Kontrol kategorisini açıklayan bir yazı
│       ├── Git.md                   # Git kararını açıklayan bir yazı, ilgili issue ve deneyimli kişiler
│       └── Uzak Depolama
│           ├── README.md            # Uzak Depolama kategorisini açıklayan bir yazı
│           └── Github
│               ├── README.md        # Github kararını açıklayan bir yazı, ilgili issue ve deneyimli kişiler
│               └── Student Pack.md  # Github ile ilgili ek bir döküman
├── Yazılım Dilleri
├── Yazılım Geliştirme Araçları
│   └── Editörler
└── README.md                        # Bu dökümanı açıklayan bir yazı ve dökümanın yönetimi/düzeni hakkında bilgiler
```


