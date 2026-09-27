---
title: Cora Max ana ekranı
description: Cora Max ekranındaki her şeyin ne anlama geldiği: üst çubuk, pano ızgarası ve prizler çekmecesi.
section: Cora Max
reviewed: 2026-09-27
order: 2
group: Getting started
---

Cora Max, bir kerede bir akvaryumu gösterir; ekranı odanın karşısından okuyabileceğiniz canlı okumalarla doldurur.

![Cora Max ana ekranı](img/max-home.webp "Bir akvaryum, ekranı dolduruyor.")

## Üst çubuk

Soldan sağa:

- **Izgara simgesi**, bu ekranın gösterdiği her akvaryumun genel görünümü olan Reef Room'u açar
- Bir şevronla birlikte **akvaryum adı**. Buna dokunmak, test sonucu kaydetmekten panoyu düzenlemeye kadar akvaryum için her ekranı içeren **akvaryum menüsünü** açar. Tam liste aşağıdadır.
- **Uyarı hapları**: şu anda aralık dışında olan her şey, sığandan fazlası olduğunda bir **+n** ile. Tümünü görmek için dokunun.
- **Saat**
- **Durum hapı**: bu ekranın şu anda ne yaptığı. Yeşil sağlıklı, amber ilgi gerektiriyor, kırmızı bir arıza. Tam sözlük aşağıdadır.
- **Pil ve Wi-Fi**
- **Cihazlar simgesi**: bağlı olan her şey ve nasıl gittiği
- **Reef Buddy simgesi**: günün briefingini açar. Bir nokta, briefingin henüz okunmadığı anlamına gelir
- **Cora Assistant simgesi**: sesli bir konuşma başlatır
- **Dişli**: ayarlar

### Durum hapı ne anlama gelir

| Hap | Anlamı |
|---|---|
| **Çevrimiçi** | Bu ekran okumalarınızı topluyor ve bunlar güncel |
| **Bulut** | Başka bir Cora bu akvaryumun okumalarını topluyor ve bu ekran onları gösteriyor. **Çevrimiçi** ile tam olarak aynı derecede güncel; birden fazla Cora varsa, toplamayı yapmayan ekran bunu gösterir |
| **Apex yoklanıyor**, **Ses etkin** | Şu anda bir şey üzerinde çalışıyor |
| **Yoklama kapalı** | Bu akvaryum için toplama kapatılmış. Cora Mobile'dan yeniden açabilirsiniz |
| **Güncelleniyor** | Bir güncelleme kurulurken toplama duraklatılmış |
| **Eski** | Okumalar gelmeyi durdurdu. Ekran aldığı son veriyi gösterir |
| **Apex tekrar deneme 12s** | Apex'iniz yanıt vermedi. Geri sayım bittiğinde Cora Max yeniden dener |
| **Bulut eşitleme başarısız** | Apex'iniz yanıt verdi ama okumaları Cora Cloud'a kaydedilemedi, bu yüzden pano geride kalıyor. Cora Max yeniden denemeye devam ediyor |
| **Çevrimdışı** | Bağlantı yok. Ekran aldığı son veriyi gösterir |
| **Çevrimdışı, 45s içinde tekrar deniyor** | Ağınız çalışıyor, ama Cora Cloud'a 30 saniyeden fazla süredir ulaşılamıyor. Cora Max kendini yeniden bağlar; geri sayım bir sonraki denemesine kalan süredir |
| **Ana Cora çevrimdışı** | Bu ekran bu akvaryum için ikinci bir Cora Max'tir ve **birincil Cora Max** (bu akvaryumun ekipmanını yoklamak üzere sabitlenmiş olan) çevrimdışı olmuş. Bu ekran, birincil geri gelene kadar veya siz farklı bir birincil Cora Max seçene kadar elindeki son veriyi göstermeyi sürdürür. Bkz. [Birden fazla Cora cihazı](/help/mobile-multi-device) |
| **Apex parolası** | Apex'iniz kayıtlı parolayı reddetti. Bkz. [Sorun giderme](/help/troubleshooting) |

:::note Tekrar deneme geri sayımı nasıl çalışır
Cora Max sabit bir hızla yeniden bağlanmayı dener: ilk kesilmeden sonra yaklaşık 15 saniye, ondan sonra yine 15 saniye, ardından iki kez 30 saniyede bir, sonra başarana kadar dakikada bir. Anında tekrar denemez ve vazgeçmez; **Çevrimdışı, 45s içinde tekrar deniyor** gösteren bir ekran tam olarak yapması gerekeni yapıyordur.
:::

:::warning Cora Assistant hemen dinlemeye başlar
Cora Assistant simgesine dokunmak canlı bir sesli oturum başlatır. Ayarları açmak istiyorsanız, o en sağdaki dişlidir.
:::

## Pano

Ekranın kalanı panodur: hepsi bir kerede görünen sabit bir widget ızgarası. Cora Max panosu kaydırılmaz.

Widget'lar telefonunuzdakiyle aynı şekilde çalışır, ama geriden okuyabileceğiniz bir boyutta. Her şeklin ne gösterdiği için bkz. **[Widget referansı](/help/mobile-widgets)**, üzerindekini değiştirmek için bkz. **[Cora Max panosunu düzenleme](/help/max-dashboard-editing)**.

Ölçülen bir parametreyi gösteren her widget, telefonda olduğu gibi kendi **yaşını** ve **kaynağını** taşır. Yanında `2g` olan bir sayı iki günlüktür ve öyle gösterilir. Cihaz ve kontrol kutuları bunun yerine kendi durumlarını gösterir.

## Akvaryum menüsü

![Akvaryum menüsü](img/max-menu.webp "Üst çubuktaki akvaryum adından, geçerli akvaryum için her şey.")

Akvaryum adına dokunmak, ekranda o anda görüntülenen akvaryum için menüyü açar:

| Öğe | Açtığı |
|---|---|
| **Parametreleri kaydet** | Ekrandaki klavyede test kiti okumalarını girin |
| **Günlük** | Bu akvaryum için [günlük](/help/mobile-journal) |
| **Reef Buddy** | Geçerli [briefing](/help/mobile-reef-buddy) |
| **Sağlık Raporları** | Sağlık değerlendirmeleri |
| **Bakım** | [Görev listesi](/help/mobile-maintenance) |
| **ICP Raporları** | Yüklenen [laboratuvar sonuçları](/help/mobile-icp-health) |
| **Uyarılar** | Bu akvaryumdaki her metrik için sağlıklı bant |
| **Canlılar** | Bu akvaryumun [envanteri](/help/mobile-livestock), bu ekranda salt okunur |
| **Etkinlik** | [Her priz, besleme ve dozaj](/help/max-activity) ve bundan ne çıktığı |
| **Pano düzeni** | [Bu ekrandaki widget'ları düzenleyin](/help/max-dashboard-editing) |
| **Akvaryum ayarları** | Bu akvaryum için tam ayarlar ekranı |

## Akvaryumlar arasında geçiş

Üst çubuğun en solundaki **ızgara simgesini** kullanarak [Reef Room](/help/max-reef-room)'a ulaşın, ardından istediğiniz akvaryumu açın. Her akvaryum kendi pano düzenini tutar, bu yüzden aralarında hareket ettikçe tüm ekran değişir.

## Prizler ve Besleme çekmecesi

Ekranın altındaki sekme, sistemdeki her prizi ve besleme kontrollerini içeren bir çekmece açar.

- **Prizler**: her biri Otomatik, Kapalı ve Açık arasında değiştirilebilir
- **Besleme**: bir besleme için doğru ekipmanı duraklatır ve sonrasında her şeyi geri koyar

:::warning Bu çekmece gerçek ekipmanı kontrol eder
İçindeki her şey gerçek ekipman üzerinde etkilidir. Dokunduğunuz anda bir komut gönderilir, ama *gönderildi* demek *yapıldı* demek değildir; Onaylandı, Onaylanmadı, Reddedildi veya Değişiklik yok olarak geri döner ve hangisi olduğunu [Etkinlik](/help/max-activity)'te görürsünüz. Besleme modu, akışı besleme için duraklatmanın güvenli yoludur, çünkü her şeyi kendisi geri getirir; elle yapılan bir Kapalı, siz geri değiştirene kadar kapalı kalır.
:::

## Bir şey yerinde değil görünüyorsa

Okumalar eski görünüyorsa veya durum hapı amber ya da kırmızıysa, **[Sorun giderme](/help/troubleshooting)** ile başlayın.
