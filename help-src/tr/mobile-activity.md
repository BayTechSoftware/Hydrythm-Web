---
title: Etkinlik ve zaman çizelgesi
description: Ekipmanınızda olup biten her şey ve bunları neyin başlattığı.
section: Cora Mobile
reviewed: 2026-09-09
order: 22
group: Records
---

Etkinlik ekranı, ekipmanda bir şeyi değiştirmeye yönelik her **komut isteğini** kaydeder. İsteği neyin gönderdiği ve sonucun ne olduğu da kayıtta yer alır.

Her istek bir değişiklik anlamına gelmez. Reddedilen istekler çalışmamıştır. Tek istisna *Zamanında yanıt veren cihaz olmadı* yazan kayıtlardır. Bu istek yine de çalışmış olabilir, o yüzden tekrarlamadan önce ekipmanı kontrol edin. "Değişiklik yok" sonucu, ekipmanın zaten istenen durumda olduğunu gösterir. Onaylanmayan bir istek ise cihaza ulaşmış da olabilir, ulaşmamış da. Bunların hepsi kaydedilir.

**Ayarlar → Etkinlik.**

![Etkinlik günlüğü](img/mobile-activity.webp "Her işlem ve onu hangi yüzeyin istediği.")

## Neler kaydedilir

Yalnızca başarılı olanlar değil, bütün **istekler** kaydedilir: priz açıp kapatma, besleme döngüleri, dozajlar, akıllı fiş değişiklikleri ve bir sahnenin ya da otomasyonun yaptığı her şey.

**Reddedilen**, **değişiklik yapmayan** ya da gönderilip **onaylanmadan** dönen istekler de uygulanan istekler gibi kaydedilir. Zaten burada bulmak istediğiniz şey tam da budur: sessizce hiçbir şey yapmamış bir komut.

## İsteği ne başlattı

Her kayıtta isteğin kaynağı yazar:

| Kaynak | Anlamı |
|---|---|
| **Bu uygulama** | Buradan dokundunuz |
| **Bu uygulamada ses** | Bu telefondan sesle istediniz |
| **Bir Cora'ya dokunuldu** | Biri bir Cora ekranını kullandı. Satırda hangisi olduğu yazar |
| **Bir Cora Max'te ses** | Biri bir ekrana sesle komut verdi |
| **Cora Assistant** | Cora'dan bunu yapmasını istediniz |
| **Otomasyon kuralı** | Bir kural devreye girdi |
| **Akıllı düğme** | Fiziksel bir düğmeye basıldı |
| **Cora Cloud'dan gönderildi** | Komutu önünüzdeki bir cihaz değil, hesabınız gönderdi |
| **Bilinmeyen kaynak** | Kaynağı belirlenemeden kaydedildi |

## İstek nasıl ulaştı

Her satırda bir yol etiketi de var. Bir şey ters gittiğinde isteğin ekipmana *nasıl* ulaştığı çoğu şeyi açıklar:

| Etiket | Anlamı |
|---|---|
| **LAN** | Kendi ağınız üzerinden doğrudan ekipmana gönderildi |
| **BULUT ÜZERİNDEN** | Doğrudan erişilemeyen ekipmana hesabınız üzerinden gönderildi |
| **ROTA ?** | Yol takibi başlamadan önce kaydedildi. Yol gerçekten bilinmiyor, tahmin de edilmiyor |

Birden fazla Cora'nın olduğu sistemlerde satırda isteği hangi Cora'nın yerine getirdiği de yazar.

## Akvaryum zaman çizelgesi

Ekipman işlemlerinden ayrı olarak her akvaryumun bir **zaman çizelgesi** var. Ölçümler, uyarılar, günlük kayıtları, ICP sonuçları ve canlılardaki değişiklikler burada sırayla görünür.

*"Bu cihaz ne yaptı?"* diye merak ediyorsanız etkinliğe, *"Bu tarihlerde neler oluyordu?"* diye merak ediyorsanız zaman çizelgesine bakın.

:::note Zaman çizelgesi ve günlük birbirini tamamlar
Zaman çizelgesi Cora'nın kaydettiklerini, [günlük](/help/mobile-journal) ise sizin yaptıklarınızı tutar. İkisini birlikte okuyunca belli bir tarihte neyin neye yol açtığını görürsünüz.
:::
