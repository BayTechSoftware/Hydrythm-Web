---
title: EcoTech ışıkları, pompaları ve dozaj pompaları
description: EcoTech Radion ışıklarını, VorTech pompalarını ve Versa dozaj pompalarını Bluetooth üzerinden Cora'ya bağlayın ve onlarla neler yapabileceğinizi öğrenin.
section: Cora Mobile
reviewed: 2026-10-13
order: 18
group: Equipment
---

:::note Beta
**Beta.** EcoTech Beta aşamasındadır ve yalnızca Beta kullanıcılarına açıktır. Beta kullanıcısı değilseniz onu **Cihaz Ekle** içinde görmezsiniz. Beta erişimi istemek için [destek](/support.html) ile iletişime geçin.
:::

EcoTech Radion ışıklarını, VorTech pompalarını ve Versa dozaj pompalarını Cora'ya bağlamak ve kontrol etmek için bu sayfayı kullanın. **Cihazlar → Cihaz Ekle → EcoTech** ile başlayın. Aynı satır, aynı Bluetooth ağında bulunan AquaIllumination, NYOS Quantum, Nero ve Orbit cihazlarını da bulur.

## Nelere ihtiyacınız var {#what-you-need}

- Akvaryumda bir Cora Max. Okumayı yapar ve komutlarınızı ekipmana Bluetooth üzerinden gönderir. Yoksa **EcoTech** satırında **Cora Max Gerektirir** yazar ve satır soluk kalır.
- Telefonunuzda açık Bluetooth ve Cora için Bluetooth izni. Cora bunu tarama yaparken ister.
- Açık ve Cora Max'in menzilinde olan ekipman.

## Bağlama {#linking-it}

1. **Cihazlar → Cihaz Ekle → EcoTech** yoluna gidin.
2. Cora yakındaki ışıkları, pompaları ve dozaj pompalarını tarar. EcoTech'in kendi Mobius uygulamasına zaten bağlı olan ışıklar görünmeyebilir.
3. Aynı Bluetooth ağındaki ekipman tek bir **Mobius akvaryumu** olarak gruplanır. **Bağlan…**'a dokunun ve ait olduğu Cora akvaryumunu seçin.
4. Cora sorduğunda gruba bir ad verin, bağlantı tamamdır.

**Salt okunur** işaretli bir cihaz ölçümlerini gösterir ama Cora onu henüz kontrol edemez. O modelin kontrolü, test edildikten sonra gelir.

Aynı Bluetooth ağında başka bir akvaryumun ışıkları da varsa ve iki akvaryumu farklı Cora Max'ler okuyorsa Cora **Tek Cora Max okur** der. Bu durumda tek bir Cora Max iki akvaryum için de tüm ağı okur.

Hiçbir şey bulunmazsa Bluetooth'un açık ve ekipmanın çalışır durumda olduğunu kontrol edin, sonra **Tekrar tara**'ya dokunun.

## Radion ışıkları {#radion}

![Cora Mobile'da bir Radion sayfası](img/mobile-radion.webp "Durum, bu ağdaki ışıklar (hepsi ya da biri), ardından yoğunluk ve her renk kanalı.")

Işığın sayfasında bir program düzenleyici ve hızlı sahneler (**Takvim**, **Fırtına**, **Bulutlar**, **Renkler**, **Besleme**, **Kapalı**) bulunur. Alıştırmayı, fanı, ay döngüsünü ve saati de ayarlayabilirsiniz.

Program düzenleyicide **Günü önizle** günü hızlandırılmış oynatır, böylece beklemeden görebilirsiniz. **Önizlemeyi durdur** ışıkları eski haline getirir. **Geri al** ve **Yinele** düzenlemeleriniz arasında gezinir. **Başlangıç noktası…** ise yeni bir programa mevcut bir programın kopyasından başlar.

Cora ışıkları belli aralıklarla okur. **Radion ayarları** içinde **Okuma** altındaki **Işıkları şu aralıkla oku** bunun ne sıklıkta olacağını belirler. Daha seyrek okumak ışıklara daha az yük bindirir. Sayfayı açmak ve her komut yine de ışıkları hemen okur.

**Radion ayarları** içinde ayrıca şunlar var:

- **Saati ayarla**: ışığın saatini ayarlar.
- **Alıştırma**: yeni mercanlar için. Tüm program, belirlediğiniz gün sayısı boyunca kademeli olarak yükselir. Açmak alıştırmayı daha düşük seviyeden yeniden başlatır.
- **Uyarılar**: **Işık yanıt vermeyi durdurursa**, **Arıza: ısı, fan veya LED**, **Saatte 5 dk sapma var** ve **LED sıcaklığı**. İstediklerinizi açın.

## VorTech pompaları {#vortech}

Bir VorTech kutucuğu pompanın modunu ve hızını gösterir. Modu ve **Hız**'ı değiştirebilir, programını düzenleyebilir ve birkaç dakikalığına **Besleme** başlatabilirsiniz. Besleme akvaryumdaki her VorTech'i yavaşlatır, bittiğinde hepsi programlarına döner. Her modun yanında kısa bir açıklama vardır: sabit akıştan resif kenarı dalgalanmalarına, gelgit kabarmalarına ve darbelere kadar. Bir pompa yalnızca desteklediği modları sunar.

## Versa dozaj pompaları {#versa}

Bir Versa sayfası kabını, dozlarını ve sınırlarını gösterir. Kap boyutunu ayarlayabilir, **Dolduruldu olarak işaretle**'ye dokunabilir, **Şimdi dozla**'yı çalıştırabilir, dozajı gece yarısına kadar **Duraklat**abilir ve programı düzenleyebilirsiniz. Cora her kafa için bir doz geçmişi tutar. Zil, [Sarf malzemeleri](/help/mobile-consumables) sayfasında anlatıldığı gibi kalan gün ya da kabın doluluğuna göre dolum uyarıları kurar.

:::warning Henüz donanımda kanıtlanmadı
VorTech pompalarına ve Versa dozaj pompalarına giden komutlar henüz gerçek donanımda kanıtlanmadı. Okuma çalışır. Bir şeyi değiştirdiğiniz ilk birkaç seferde ekipmanın kendisine bakın ve ne gördüğünüzü [Sorun bildirme](/help/mobile-support) sayfasından bize söyleyin.
:::

## Uyarılar {#alerts}

Cora bir EcoTech cihazını, kendi okuma aralığına göre üç ölçüm kaçırdıktan sonra sessiz sayar. Yalnızca ışık içeren bir ağ varsayılan olarak her 30 dakikada bir okunur, yani bu en az 90 dakika sürer. [Uyarılar ve eşikler](/help/mobile-alerts) sayfasına bakın. Radion ışıklarının ayrıca yukarıda anlatılan **Radion ayarları** içinde kendi uyarıları vardır.

## Cora Max'te {#on-cora-max}

Aynı ekipmanın duvardaki ekranda kendi sayfaları vardır. Ayrıntılar [Cora Max'ten ekipman kontrolü](/help/max-device-control) sayfasında.
