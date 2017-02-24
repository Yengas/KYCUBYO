# Docker
Docker yürütmek istediğiniz işlemleri, kullandığınız makineden bağımsız sanal bir ortamda çalıştırmanızı sağlar. Bu sayede bir proje üzerinde çalışan iki kişi; tamamen farklı işletim sistemi ve donanım kullansa bile, uygulamanız aynı makinede çalışıyormuş gibi davranır. Bu projede bir sorun ortaya çıktığında; "bende çalışıyor" gibi sorunların ortadan kalkmasına sebep olur.

Aynı zamanda Docker aracılığı ile bir projenin çalışması için gerekli olan tüm gereksinimleri tanımlayabileceğiniz için, takım arkadaşlarınızın bilgisayarında Docker yüklü olduğu durumda, onlara istediğiniz proje'nin kodunu atıp, anında çalıştırıp denemelerini sağlayabilirsiniz.

Bu durumda, her KYÇUBYO öğrencisinin bilgisayarına çalıştıkları proje başına 1-2 yazılım dili compilerı/interpreter'ı, birden fazla veritabanı kurmak yerine sadece Docker kurarak, bilgisayarlarını temiz tutmalarını sağlayabiliyoruz.

## Docker Kurulumu
İşletim sisteminize göre Docker kurulumu değişebilir. Eğer Windows 10+ kullanıyorsanız ve işlemcinizde Hyper-V varsa, kurulum yapmak ve kullanım oldukca basit olacak. Eğer Windows'un daha eski versiyonlarını kullanıyorsanız, veya bilgisayarınızda Hyper-V yoksa kurulum yine aynı derecede kolay fakat kullanım daha kompleks hale geliyor.

Linux kullanıyorsanız hiç düşünmenize gerek yok, Docker kurmak 5 dakikadan fazla zamanınızı almayacak.

### Docker Windows 10+ Kurulumu
[Bu url'yi](https://docs.docker.com/docker-for-windows/install/) kullanarak Docker'ın son stable(istikrarlı) sürümünü kurabilirsiniz.
### Docker Windows Eski Versiyonları / Hyper-V olmadan
Docker'ın eski Windows versiyonlarında ve Hyper-V'siz makinelerde çalışabilmesi için VirtualBox  ile, çok küçük bir Linux işletim sistemi çalıştırması gerekiyor. Kurulumun neredeyse tamamen otomatik. [Bu url'yi](https://docs.docker.com/toolbox/toolbox_install_windows/) kullanarak Docker Toolbox'ı indirebilirsiniz. Sizin için gerekli olan herşeyi yapacak ve Docker'ın kurulumu tamamlanmış olacak.
### Docker Linux
Linux Distro'nuza göre, Docker kurulum talimatları değişiyor. Ama kurulum ve kullanımın basitliği hepsinde aynı. [Bu url'yi](https://docs.docker.com/engine/installation/linux/) kullanarak Docker'ın sitesine gittikten sonra, Distronuzu seçerek, kuruluma başlayabilirsiniz.

## Kaynaklar
- [Docker hakkında genel bilgi](https://kodedu.com/2015/06/docker-nedir-neden-kullanilir/) [Türkçe][Giriş]
- [Docker hakkında detaylı bilgi ve kullanım örnekleri](http://www.gokhansengun.com/docker-nedir-nasil-calisir-nerede-kullanilir/) [Türkçe][Giriş]
- [Information about Docker and Usage Examples](https://larry-price.com/blog/2015/01/11/an-example-use-case-for-docker) [English][Giriş]

## Karar Detayları
Bu kararın verilmesine sebep olan issue'ya [buradan](https://github.com/Yengas/KYCUBYO/issues/7) erişebilirsiniz.
### Deneyimli Kişiler
- [Yiğitcan](https://github.com/Yengas)