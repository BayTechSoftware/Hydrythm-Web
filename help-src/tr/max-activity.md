---
title: Cora Max'te etkinlik
description: Bir komutun ekipmanınıza gerçekten ulaşıp ulaşmadığını, onu kimin ya da neyin istediğini ve neden reddedildiğini Cora Max'te kontrol edin.
section: Cora Max
reviewed: 2026-10-13
order: 11
group: Records
twin: mobile-activity
---

Etkinlik, ekipmanınızda bir şeyi değiştirmeye yönelik her denemenin ve sonucunun kaydıdır. Telefonunuzun gösterdiği kayıtla aynıdır. İstediğiniz bir şey olmamış gibi görünüyorsa ilk buraya bakın.

**Akvaryum menüsünden** (üst çubukta akvaryum adına dokunun) ya da **Ayarlar → [akvaryumunuz] → Etkinlik** yolundan açın.

![Cora Max'te etkinlik günlüğü](img/max-activity.webp "Üstteki açıklama her sonucun anlamını anlatır.")

## Her kayıt size ne söyler

Her satırda ekipman ve istenen şey (örneğin *Ana pompa: Kapatıldı*) ile saat yazar. Ayrıca iki bilgi daha verir.


**İsteği ne verdi.** Örneğin **Bu Cora'da dokunuldu**, **Bu Cora'da sesle**, **Cora uygulaması**, **Cora uygulamasında sesle**, **Otomasyon kuralı** ya da **Buluttan gönderildi**.

**Komut hangi yoldan gitti.** **LAN**, komutun kendi ağınız üzerinden gittiği anlamına gelir. **BULUT ÜZERİNDEN**, Cora Cloud üzerinden gittiği anlamına gelir. Birden fazla Cora Max'iniz varsa kayıt, komutu hangisinin uyguladığını da söyler.

## Dört sonuç

Ekranın üstündeki açıklama bunları tekrarlar.

| Sonuç | Anlamı |
|---|---|
| **Onaylandı** | Ekipman işi yaptığını bildirdi |
| **Onaylanmadı** | Komut gönderildi ama yanıt gelmedi. Çalışıp çalışmadığını bilmiyoruz |
| **Reddedildi** | Çalışmadı. Bir güvenlik kuralı, bir kilit ya da ekipmanın kendisi reddetti |
| **Değişiklik yok** | Ekipman zaten istediğiniz durumdaydı |

**Reddedildi** ya da **Onaylanmadı** kaydının altındaki satır nedenini ve tekrar denemeden önce neyi kontrol etmeniz gerektiğini söyler. Örneğin: *Hiçbir cihaz zamanında yanıt vermedi, yani komut yine de çalışmış OLABİLİR. Tekrarlamadan önce ekipmanı kontrol edin.*

## Bir şey olmadığında

Dokunmatik ekranda, gönderilmiş ama hiç onaylanmamış bir komut ile çalışmış bir komut aynı görünür. Farkı bu ekranda görürsünüz.

1. İstediğiniz şeyin kaydını bulun.
2. **Reddedildi** ise altındaki nedeni okuyun. Hiçbir şey çalışmadı.
3. **Onaylanmadı** ise aynı şeyi iki kez yapmamak için tekrar denemeden önce ekipmanın kendisini kontrol edin.

Hâlâ anlam veremiyorsanız [Bir şeyin neden değiştiğini bulma](/help/troubleshooting#establishing-why-something-changed) bölümüne bakın.

## Günlükle birlikte okuyun

Etkinlik, sistemin yaptıklarını gösterir. [Günlük](/help/max-records#journal) ise sizin elle yaptıklarınızı. İkisi birlikte çoğu sürprizi açıklar.
