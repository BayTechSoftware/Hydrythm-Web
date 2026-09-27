---
title: Bildirimler
description: Telefonunuza neyin ulaşacağını, ne zaman gelebileceğini ve kaçırdığınızı nerede okuyacağınızı seçin.
section: Cora Mobile
reviewed: 2026-09-27
order: 16
group: Alerts and automation
---

**Ayarlar → Bildirimler**, Cora'nın size gönderebileceği her şeyi kontrol eder.

![Bildirim ayarları](img/mobile-notifications.webp "Her kategori bağımsız olarak push gönderebilir.")

## Neyin push gönderebileceği

Her kategori bağımsız olarak açılıp kapatılır:

| Kategori | Kapsadığı |
|---|---|
| **Parametre Uyarıları** | Belirlediğiniz bir aralığın dışındaki su kimyası |
| **Bakım Hatırlatıcıları** | Su değişimleri gibi zamanladığınız görevler |
| **Ekipman Arızaları** | Bir sorun bildiren bir cihaz: örneğin test etmeyi durdurmuş bir Trident |
| **Sarf Malzemesi Azalıyor** | Reaktif, tamamlama suyu, dozaj kapları ve dolu bir atık şişesi |
| **ICP Raporu Hazır** | ICP sonuçlarınız analiz edildi ve okumaya hazır |

Bir kategoriyi kapatmak push'u durdurur. Olay hâlâ kaydedilir ve hâlâ zilde görünür.

:::warning "Parametre Uyarıları" kimya anlamına gelir ve sadece kimya
O anahtarın akvaryumun size söyleyebileceği her şeyi kapsadığını düşünmek doğaldır. Kapsamaz. Test etmeyi durdurmuş bir Trident bir **Ekipman Arızasıdır** ve reaktif bitmesi **Sarf Malzemesi Azalıyor**dur; her birinin kendi anahtarı vardır. Parametre Uyarılarını uzun süredir açık tutup diğer ikisini kapsadığını varsaydıysanız, diğer ikisini kontrol edin.
:::

**Sarf Malzemesi Azalıyor, azalmak yerine dolan atık şişesini de içerir.** Bu kategoride olmasının nedeni, gerektirdiği eylemin aynı olmasıdır: testleri durdurmadan önce boşaltılacak veya değiştirilecek bir şey.

## Zil

Her ekranın sağ üstünde. Push gönderilmiş olsun olmasın, Cora'nın yükselttiği her şeyi en yeniden en eskiye tutar. Sayı, okumadığınız kadarıdır.

Telefonunuzdan bir gün uzak kaldıktan sonra, veya kapattığınız bir kategori bir şey yükselttikten sonra kontrol edilecek doğru yer burasıdır.

## Hiçbir şey gelmiyorsa

Bu listeyi sırayla kontrol edin:

1. **Ayarlar → Bildirimler**: o kategori push göndermeye izinli mi?
2. Telefonunuzun kendi ayarları: Cora'nın hiç bildirim göndermesine izin var mı? Kurulum sırasında reddedilen bir izin, buradaki her şeyi geçersiz kılar.
3. Gerçekten gönderilecek bir şey var mı? Hiçbir şey değişmediği günlerde Reef Buddy sessiz kalır.

## Çok fazla şey geliyorsa

Bildirimleri kapatmadan önce eşiklerinizi gözden geçirin. Aşırı uyarılar genellikle akvaryumun çalıştığından daha sıkı belirlenmiş bir aralığı veya kalibrasyon gerektiren bir kaynağı gösterir. Bkz. [Uyarılar ve eşikler](/help/mobile-alerts).

Bir kategoriyi kapatmak o kategori için hep ya da hiç'tir. Bunun yerine belirli bir uyarı çok sık push gönderiyorsa, tüm kategoriyi kapatmak yerine kuralın kendisinde 15 dakikadan 1 haftaya kadar **Uyarılar arası bekleme süresini** değiştirin. Bekleme süresi seçenekleri ve Cora Max'te "erteleme"nin ne anlama geldiği için bkz. [Uyarılar ve eşikler](/help/mobile-alerts).
