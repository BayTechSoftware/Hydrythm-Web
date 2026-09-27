---
title: Cihaz ekleme, düzenleme ve kaldırma
description: Cora'ya ekipman ekleyin, akvaryuma atayın, adını değiştirin ve sorunsuz şekilde kaldırın.
section: Cora Mobile
reviewed: 2026-09-27
order: 9
group: Equipment
---

**Cihazlar** sekmesinde bağladığınız her şey markaya göre gruplanmış olarak durur. Her grubu daraltabilirsiniz. Böylece ekipmanla dolu bir reef odası bile derli toplu görünür.

![Cihazlar sekmesi](img/mobile-devices.webp "Ekipman markaya göre gruplanır. Her grup daraltılabilir.")

## Ekipman ekleme

Listenin altında üç düğme var. Her biri farklı bir iş yapar:

| Düğme | Ne ekler |
|---|---|
| **Cihaz Ekle** | Cora Max ekler. Wi-Fi ağınızdaki üniteleri ya da Bluetooth ile yakındakileri bulur. Arama cihazı bulamazsa aynı ekranda **IP Adresini Elle Girin** seçeneği var. |
| **Ağınızda bir pompa bulun** | Yerel ağda kendini gösteren Jecod pompaları |
| **AquaWiz Ekle** | AquaWiz hesabınız üzerinden AquaWiz kontrol ünitesi |

![Cora Max ekleme](img/mobile-add-device.webp "Cihaz Ekle, Cora Max'i Wi-Fi ve Bluetooth üzerinden arar.")

Neptune Apex ve Red Sea ReefBeat gibi diğer ekipmanları bu listeden değil, akvaryumun kendisinden bağlarsınız. Ayrıntılar [Ekipmanınızı bağlama](/help/mobile-connections) sayfasında.

Isıtıcı, pompa ya da skimmer gibi bir ekipman eklerken marka ve model alanı **otomatik tamamlama** yapar. Yazmaya başlayın, Cora kaynağı doğrulanmış geniş bir marka listesinden öneriler getirir. Sizin markanız listede yoksa yine de yazın. Cora ne yazarsanız onu kaydeder.

:::note Cora ve telefonunuz aynı ağda olmalı
Yerel ağda bulunan ekipmanı eklerken telefonunuz da aynı ağda olmalıdır. **Kurulumdan sonra da ekipmana yalnızca o ağ üzerinden** (Bluetooth kullanan ünitelerde Bluetooth üzerinden) ulaşılır. Tek istisna, ekipmana sizin yerinize ulaşabilen ve akvaryumun yanında duran bir Cora cihazıdır.

Bu yüzden evde doğru ölçüm gösteren ekipman, siz dışarıdayken daha eski değerler gösterebilir. Akvaryumun yanında onu yoklayan bir Cora Max varsa bu olmaz. Bu bir arıza değildir. Ekipmana nereden ulaşılabildiğiyle ilgilidir.
:::

## Cihazı akvaryuma atama

Çoğu ekipman tek bir akvaryuma aittir. Ölçümlerin o akvaryumun panosunda görünmesini sağlayan da bu atamadır.

**Cora Max bu kuralın istisnasıdır.** En fazla dört akvaryuma atanabilir ve ekranda bunlar arasında geçiş yapar. Ayrıntılar [Birden fazla Cora cihazı](/help/mobile-multi-device) sayfasında.

Cihazı açın ve **Akvaryum**'u seçin. Birden fazla sisteminiz varsa en önemli ayar budur. Yanlış akvaryuma atanan bir ısıtıcı sorunsuz çalışır, ama ölçümlerini yanlış yere gönderir.

:::warning Ölçümlere güvenmeden önce akvaryumu atayın
Akvaryuma atanmamış bir cihaz ölçüm göndermeye devam eder, ama bu sayıların gideceği bir yer yoktur. Yeni eklediğiniz cihaz panoda görünmüyorsa önce bunu kontrol edin.
:::

## Adını değiştirme

Cihazı açın ve adını düzenleyin. Günlük hayatta kullandığınız adı verin: "Ana pompa", "Sol gyre", "Sump ısıtıcısı". Bu ad widget'larda, uyarılarda ve Cora'ya sorduğunuz her soruda geçer. Sizin için anlamlı bir ad seçerseniz her şey daha kolay anlaşılır.

Yeni ad yalnızca Cora'da geçerlidir. Üreticinin kendi uygulamasındaki adı değiştirmez.

## Cihazın sağlıklı çalışıp çalışmadığını kontrol etme

Her satırda cihazın şu anki durumu görünür. Görmek istediğiniz şey yakın zamanlı bir güncelleme saati ve hiçbir uyarı olmamasıdır.

| Gördüğünüz | Anlamı |
|---|---|
| Yakın zamanlı bir güncelleme saati | Normal çalışıyor |
| Yalnızca birkaç saatte bir veri gönderen bir cihazda "3 sa önce güncellendi" | Sorun yok |
| "… ulaşılamadı" | Ağ sorunu var ya da cihaz kapalı |
| "… girişi reddetti" | Üretici hesabının yeniden bağlanması gerekiyor. Cihazı açıp yeniden giriş yapın |
| Hiçbir şey | Cihaz hiç veri göndermemiş. Akvaryum atamasını ve bağlantıyı kontrol edin |

## Cihazı kaldırma

Cihazı açın ve **Kaldır**'ı seçin. Cora sizden onay ister ve tam olarak neyin kaldırılacağını söyler.

**Ölçümleriniz silinmez.** Cihazı kaldırdığınızda Cora ondan yeni veri toplamayı bırakır. Önceden toplanan geçmiş akvaryumda kalır. O cihaza bağlı widget'lar da geçmiş ölçümleri göstermeye devam eder.

Kaybettiğiniz şey canlı bağlantıdır. Cihaz bir üretici hesabıyla bağlandıysa kayıtlı giriş bilgisi de silinir. Cihazı yeniden eklerseniz tekrar giriş yapmanız gerekir.

:::tip Çok uyarı veren cihazı kaldırmadan sessize alın
Cihaz doğru çalışıyor ama çok sık uyarı veriyorsa eşiklerini ya da bildirim ayarlarını değiştirin. Ayrıntılar **[Uyarılar ve eşikler](/help/mobile-alerts)** sayfasında. Böylece hem bağlantı hem veriler korunur, gereksiz uyarılar da kesilir.
:::
