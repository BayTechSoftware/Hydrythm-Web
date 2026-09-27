---
title: Etkinlik ve zaman çizelgesi
description: Ekipmanınıza olan her şey ve buna neyin sebep olduğu.
section: Cora Mobile
reviewed: 2026-09-09
order: 22
group: Records
---

Etkinlik, her **eyleme geçirme isteğini** (bir şeyi değiştirme girişimini), bunu kimin istediğiyle ve sonucunda ne olduğuyla birlikte kaydeder.

Bir istek bir değişiklikle aynı değildir. Reddedilen istekler çalışmadı, bir istisna dışında: *Hiçbir cihaz zamanında yanıt vermedi* diyen bir kayıt hâlâ çalışmış olabilir, bu yüzden onu tekrarlamadan önce ekipmanı kontrol edin. Değişiklik yok istekleri, ekipmanı zaten istenen durumda buldu ve onaylanmamış bir istek ekipmana hiç ulaşmamış da olabilir. Hepsi kaydedilir.

**Ayarlar → Etkinlik.**

![Etkinlik günlüğü](img/mobile-activity.webp "Onu isteyen yüzeyle birlikte her eylem.")

## Ne kaydedilir

Sadece işe yarayanlar değil, her **istek**: priz açıp kapatmalar, besleme döngüleri, dozajlar, fiş değişiklikleri ve bir sahnenin veya otomasyonun yaptığı her şey.

**Reddedilen**, **değişiklik yok** yapan, veya gidip **onaylanmamış** geri gelen bir istek, tam olarak yürütülmüş bir istek gibi kaydedilir. Amaç budur: sessizce hiçbir şey yapmayan bir komut, burada tam olarak bulmak istediğiniz şeydir.

## Buna neyin sebep olduğu

Her kayıt nedenini adlandırır:

| Neden | Anlamı |
|---|---|
| **Bu uygulama** | Buna burada dokundunuz |
| **Bu uygulamada ses** | Bu telefonda sordunuz |
| **Bir Cora'ya dokunuldu** | Biri bir Cora ekranı kullandı; satır hangisini söyler |
| **Bir Cora Max'te ses** | Biri bir ekranla konuştu |
| **Cora Assistant** | Cora'dan bunu yapmasını istediniz |
| **Otomasyon kuralı** | Bir kural tetiklendi |
| **Akıllı düğme** | Fiziksel bir düğmeye basıldı |
| **Cora Cloud'dan gönderildi** | Önünüzdeki bir cihaz tarafından değil hesabınız tarafından verildi |
| **Bilinmeyen kaynak** | Kaynak tanımlanamadan önce kaydedildi |

## Nasıl ilerledi

Her satır bir rota çipi de taşır, çünkü bir isteğin ekipmanınıza *nasıl* ulaştığı, bir şey yanlış gittiğinde çoğunu açıklar:

| Çip | Anlamı |
|---|---|
| **LAN** | Kendi ağınız üzerinden, doğrudan ekipmana gönderildi |
| **BULUT ÜZERİNDEN** | Doğrudan erişilemeyen ekipman için hesabınız üzerinden gönderildi |
| **ROTA ?** | Rotalar takip edilmeden önce kaydedildi: gerçekten bilinmiyor, varsayılmış değil |

Birden fazla Cora'lı bir sistemde, satır ayrıca hangisinin isteği yerine getirdiğini de adlandırır.

## Akvaryum zaman çizelgesi

Ekipman eylemlerinden ayrı olarak, her akvaryumun bir **zaman çizelgesi** vardır: okumalar, uyarılar, günlük kayıtları, ICP sonuçları ve canlı değişiklikleri sırayla düzenlenmiş.

*"Bir şey ne yaptı?"* diye sorarken etkinliği, *"bu tarih civarında ne oluyordu?"* diye sorarken zaman çizelgesini kullanın.

:::note Zaman çizelgesi ve günlük birbirini tamamlar
Zaman çizelgesi Cora'nın kaydettiğini tutar; [günlük](/help/mobile-journal) ise sizin yaptığınızı tutar. Birlikte okunduklarında belirli bir tarih civarında neden ve sonucu belirlerler.
:::
