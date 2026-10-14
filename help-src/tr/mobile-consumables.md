---
title: Sarf malzemeleri ve dolum uyarıları
description: Reaktif, dozaj kapları, su tamamlama depoları ve filtre ruloları için dolum uyarıları kurun ve doldurduğunuzda Cora'ya bildirin.
section: Cora Mobile
reviewed: 2026-10-13
order: 16
group: Equipment
---

Reaktif, dozaj sıvısı, su tamamlama suyu ya da filtre rulosu bitmeden Cora'nın sizi uyarması için dolum uyarılarını kullanın. Cihazı **Cihazlar** sekmesinden açın (ya da panodaki kutucuğuna dokunun), sonra üst çubuktaki **zile** dokunun.

## Dolum uyarısı kurma {#setting-a-refill-alert}

![Bir ReefDose 4 için Uyarılar sayfası, her kafa için kalan gün eşiği ve anahtarıyla](img/mobile-consumables.webp "Her kafa için bir eşik, her birinin kendi anahtarı var.")

Sayfanın adı **Uyarılar:** ve ardından cihazın adıdır. Ekipmanda birden fazla kap varsa her birinin kendi eşiği ve kendi anahtarı olur. Böylece yakından izlediğiniz bir kafayla nadiren dokunduğunuz bir kafayı farklı ayarlayabilirsiniz. Bir anahtarı kapatmak değeri sonrası için saklar.

Nereden ayarlanır:

- **Çoğu cihaz**: cihaz sayfasının üst çubuğundaki zil.
- **DŌS**: DŌS sayfasındaki **Uyarılar** kartı ya da zil. [Dozaj pompası uyarıları](/help/mobile-device-control#doser-alerts) bölümüne bakın.
- **AquaWiz**: [Uyarı Merkezi](/help/mobile-alerts)'nin **Kurallar** sekmesindeki kuralları.

Eşiklerin çoğu hacim olarak değil gün olarak girilir. Cora, kalan miktarın sizin kullanım hızınızla ne kadar yeteceğini hesaplar. "Dört günlük kalsiyum kaldı" bilgisiyle bir şey yapabilirsiniz. "180 mL kaldı" bilgisiyle yapamazsınız.

## Neler için uyarı alabilirsiniz {#thresholds}

| Cihaz | Eşik | Başlangıç değeri |
|---|---|---|
| Trident | **Kalan testler** (en az kalan reaktif) | 10 test |
| Trident | **Atık şişesi** (dolu şişe bir sonraki testi başarısız yapar) | %85 dolu |
| DŌS kafası | *[kafa] · kalan gün* | 7 gün |
| DŌS kafası | *[kafa] · kalan*, mL olarak | 100 mL |
| Eski suyu dışarı alan DŌS kafası | **Atık kabında kalan alan** | |
| DŌS kafası | **Kaçırılan dozaj uyarıları** (bir anahtar) | |
| ReefDose kafası | Takviyenin kaç gün yeteceği | 7 gün |
| ReefATO+ | Son su tamamlama kullanımından tahmin edilen **Depo süresi** | 2 gün |
| ReefMat | Rulonun ilerleme hızından tahmin edilen **Kalan rulo** | 3 gün |
| AquaWiz | Kalan alkalinite takviyesi | 100 mL |


Sarf malzemesi uyarısı diğer uyarılar gibi çalışır. [Uyarı Merkezi](/help/mobile-alerts)'nde görünür ve telefonunuza bildirim gönderebilir. Bir seviye aşıldığında **tek** bildirim alırsınız. Seviye yeniden eşiğin üstüne çıkınca uyarı kapanır.

## Eşik seçme {#choosing-a-threshold}

Eşiği, harekete geçmeye vaktiniz kalacak kadar erken ayarlayın. Bir şeyin bittiği gün gelen uyarı hiç uyarı sayılmaz.

:::warning Bazı ekipmanlar boşken de çalışmaya devam eder
Kabı boş bir DŌS kafası zamanlamasını çalıştırmaya devam eder ve hiç vermediği dozları vermiş gibi bildirir. Kendine ait bir düşük seviye uyarısı yoktur. Bunu yakalamanın yolu dolum uyarısıdır, bu yüzden dozaj yaptığınız her kafa için bir tane kurun.
:::

## Doldurduktan sonra {#after-refilling}

Uyarının kapanması ve bir sonraki uyarının doğru seviyeden hesaplanması için bunu cihaz sayfasında Cora'ya bildirin.

| Cihaz | Dokunun |
|---|---|
| DŌS kafası | **Doldur**, ardından **Dolu**, ya da **Kalan Hacim**'i ayarlayın |
| DŌS atık kabı | Boşalttıktan sonra boş alanını tam olarak sıfırlayın |
| ReefDose kafası | **Şişede kalan** |
| ReefMat | Yeni rulo taktıktan sonra **Yeni rulo** |

Trident, ReefATO+ ve AquaWiz kendi seviyelerini bildirir, bu yüzden Cora'da sıfırlanacak bir şey yoktur.
