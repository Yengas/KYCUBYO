# KYCUBYO
Bu dökümantasyon KYCUBYO içinde kullanılacak olan araçları, editörleri, yazılım dillerini, kütüphaneleri Türkçe olarak açıklamak ve KYCUBYO içinde bu teknolojiler ile ilgili kimlerin deneyimli olduğunu belirtmek için yazılmıştır.

Dökümantasyon içerisinde karar kılınan her şey [issuelar](https://github.com/Yengas/KYCUBYO/issues?utf8=%E2%9C%93&q=) ile takip edilip, ortak bir karar alındıktan sonra eklenmiştir. Burada bulunan herhangi bir karar ile ilgili sorunuz var ise, veya deneyimli kişiler listesine eklenmek istiyorsanız, issue açarak takip edilebilir bir şekilde isteğinizi belirtebilirsiniz.

Bu proje üzerinde [haftalık olarak yaptıklarımız](https://github.com/Yengas/KYCUBYO/issues?utf8=%E2%9C%93&q=label%3A%22Haftan%C4%B1n%20%C3%96zeti%22%20)'ın özeti ve kulübe yeni katılan arkadaşları yönlendirmek için rehber niteliğinde dökümanlarda bulabilirsiniz.

## Döküman İçerikleri
[//]: # (TOCSTART)

- Proje Geliştirme
	- [Mesajlaşma Uygulamaları](./Proje%20Geli%C5%9Ftirme/Mesajla%C5%9Fma%20Uygulamalar%C4%B1)
		- [Slack](./Proje%20Geli%C5%9Ftirme/Mesajla%C5%9Fma%20Uygulamalar%C4%B1/Slack.md)
	- [Proje Takip ve Yönetimi](./Proje%20Geli%C5%9Ftirme/Proje%20Takip%20ve%20Y%C3%B6netimi)
		- [Github Issues](./Proje%20Geli%C5%9Ftirme/Proje%20Takip%20ve%20Y%C3%B6netimi/Github%20Issues.md)
	- [Proje Yayınlama](./Proje%20Geli%C5%9Ftirme/Proje%20Yay%C4%B1nlama)
		- [DigitalOcean](./Proje%20Geli%C5%9Ftirme/Proje%20Yay%C4%B1nlama/DigitalOcean.md)
	- [Versiyon Kontrol](./Proje%20Geli%C5%9Ftirme/Versiyon%20Kontrol)
		- [Uzak Depolama](./Proje%20Geli%C5%9Ftirme/Versiyon%20Kontrol/Uzak%20Depolama)
			- [Github](./Proje%20Geli%C5%9Ftirme/Versiyon%20Kontrol/Uzak%20Depolama/Github)
				- [Student Pack](./Proje%20Geli%C5%9Ftirme/Versiyon%20Kontrol/Uzak%20Depolama/Github/Student%20Pack.md)
		- [Git](./Proje%20Geli%C5%9Ftirme/Versiyon%20Kontrol/Git.md)
- Yazılım Geliştirme Araçları
	- [Editörler](./Yaz%C4%B1l%C4%B1m%20Geli%C5%9Ftirme%20Ara%C3%A7lar%C4%B1/Edit%C3%B6rler)
		- [Jetbrains](./Yaz%C4%B1l%C4%B1m%20Geli%C5%9Ftirme%20Ara%C3%A7lar%C4%B1/Edit%C3%B6rler/Jetbrains)
			- [Öğrenci Hesabı](./Yaz%C4%B1l%C4%B1m%20Geli%C5%9Ftirme%20Ara%C3%A7lar%C4%B1/Edit%C3%B6rler/Jetbrains/%C3%96%C4%9Frenci%20Hesab%C4%B1.md)
		- [Vim](./Yaz%C4%B1l%C4%B1m%20Geli%C5%9Ftirme%20Ara%C3%A7lar%C4%B1/Edit%C3%B6rler/Vim.md)
	- [Sanallaştırma ve Konteyner Teknolojileri](./Yaz%C4%B1l%C4%B1m%20Geli%C5%9Ftirme%20Ara%C3%A7lar%C4%B1/Sanalla%C5%9Ft%C4%B1rma%20ve%20Konteyner%20Teknolojileri)
		- [Docker](./Yaz%C4%B1l%C4%B1m%20Geli%C5%9Ftirme%20Ara%C3%A7lar%C4%B1/Sanalla%C5%9Ft%C4%B1rma%20ve%20Konteyner%20Teknolojileri/Docker.md)
		- [Virtualbox](./Yaz%C4%B1l%C4%B1m%20Geli%C5%9Ftirme%20Ara%C3%A7lar%C4%B1/Sanalla%C5%9Ft%C4%B1rma%20ve%20Konteyner%20Teknolojileri/Virtualbox.md)

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

