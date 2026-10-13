---
title: Cora Max ana ekranı
description: Cora Max'te üst çubuğun, durum etiketinin, uyarı etiketlerinin, akvaryum menüsünün ve panonun ne anlama geldiği; akvaryumlar arasında geçiş ve Prizler ve Besleme'yi açma.
section: Cora Max
reviewed: 2026-10-13
order: 2
group: Getting started
twin: mobile-tour
---

Bu sayfa Cora Max'te gördüklerinizi açıklar. Cora Max aynı anda tek bir akvaryum gösterir ve ekranı odanın öbür ucundan okuyabileceğiniz canlı ölçümlerle doldurur.

![Üst çubuğun altında bir akvaryumun göstergeleri, değerleri, grafikleri ve cihaz kutucuklarıyla Cora Max ana ekranı](img/max-home.webp "Bir akvaryumun panosu ekranı doldurur, üstünde üst çubuk durur.")

## Üst çubuk {#the-top-bar}

![Cora Max üst çubuğu](img/max-topbar.webp "Üst çubuk, aşağıdaki listeyle eşleşecek şekilde soldan sağa numaralandırılmış.")

Soldan sağa:

1. **Izgara simgesi**, bu ekranın gösterdiği tüm akvaryumların genel görünümü olan [Reef Room](/help/max-reef-room)'u açar.
2. Küçük bir okla birlikte **akvaryum adı**. Baktığınız akvaryumun tüm ekranlarını içeren **akvaryum menüsünü** açmak için dokunun. Tam liste aşağıda.
3. **Uyarı etiketleri** şu anda dikkat gerektiren şeyleri gösterir: aralık dışındaki ölçümler, cihaz arızaları, kaçırılan dozlar ya da azalan sarf malzemeleri. O uyarıyı yeniden ekranın ortasına getirmek için bir etikete dokunun. Sığandan fazlası varsa **+2** (ya da kaç tane varsa) görürsünüz. Tüm etkin alarmları görmek için ona dokunun.
4. **Saat**. Onu **Ayarlar → Cora Max Ayarları** içindeki **Saati göster** ile gizleyebilirsiniz.
5. **Durum etiketi**, bu ekranın şu anda ne yaptığını gösterir. Yeşil her şeyin yolunda, mavi meşgul, turuncu bakılması gereken bir şey, kırmızı bir arıza olduğu anlamına gelir. Tüm durumlar aşağıda listelenir.
6. **Pil ve Wi-Fi**.
7. **Cihazlar simgesi**, bu akvaryuma göre süzülmüş **Cihazlar**'ı açar. Cihazı olmayan bir akvaryumda görünmez.
8. **Reef Buddy simgesi** bugünün özetini açar. Nokta, onu henüz okumadığınız anlamına gelir.
9. **Cora Assistant simgesi** sesli bir konuşma başlatır.
10. **Dişli** ayarları açar.

:::warning Cora Assistant hemen dinlemeye başlar
Cora Assistant simgesine dokunmak canlı bir sesli oturum başlatır. Ayarları istediyseniz en sağdaki dişliye dokunun.
:::

### Durum etiketinin anlamı {#what-the-status-pill-means}

| Etiket | Anlamı |
|---|---|
| **Çevrimiçi** | Bu ekran ölçümlerinizi topluyor ve ölçümler güncel |
| **Bulut** | Bu akvaryumun ölçümlerini başka bir Cora topluyor ve bu ekran onları gösteriyor. **Çevrimiçi**'deki kadar günceller. Birden fazla Cora'nız varsa toplamayı yapmayan bunu gösterir |
| **Apex yoklanıyor**, **Ses etkin** | Şu anda bir işle meşgul (mavi) |
| **Yoklama kapalı** | Bu akvaryum için toplama kapalı. Cora Mobile'da yeniden açabilirsiniz |
| **Güncelleniyor** | Bir güncelleme yüklenirken toplama duraklatıldı |
| **Eski** | Ölçümler gelmeyi bıraktı. Ekran aldığı son ölçümleri gösterir |
| **Apex tekrar deneme 12 s** | Apex'iniz yanıt vermedi. Geri sayım bitince Cora Max yeniden dener |
| **Bulut eşitleme başarısız** | Apex'iniz yanıt verdi ama ölçümleri Cora Cloud'a kaydedilemedi, bu yüzden pano geride kalıyor. Cora Max denemeye devam eder |
| **Bulut kaydı reddedildi** | Cora Cloud bu ekranın bazı verilerini kaydetmeyi reddediyor. Akvaryumunuzda ya da Cora Max'te bir sorun yok ve bu ekranda değiştirilmesi gereken bir şey yok. Çözüm bir Cora Cloud güncellemesidir. **Ayarlar → Cora Max Ayarları**'nı açın ve **Durum** bölümüne kaydırın, orada **Bulut kaydı** satırı hangi verilerin etkilendiğini söyler. Sonra [destekle iletişime geçin](/support.html) |
| **Çevrimdışı** | Bağlantı yok. Ekran aldığı son veriyi gösterir |
| **Çevrimdışı, 45 s içinde tekrar denenecek** | Ağınız çalışıyor ama Cora Cloud'a 30 saniyeden uzun süredir ulaşılamıyor. Cora Max kendiliğinden yeniden bağlanır ve geri sayım bir sonraki denemenin ne zaman olacağını gösterir |
| **Ana Cora çevrimdışı** | Bu ekran bu akvaryum için ikinci bir Cora Max ve **Birincil Cora Max** (bu akvaryumun ekipmanını okumak için sabitlenen) çevrimdışı oldu. Bu ekran, birincil geri gelene ya da siz başka bir Birincil Cora Max seçene kadar elindeki son veriyi göstermeye devam eder. Ayrıntılar [Birden fazla Cora cihazı](/help/mobile-multi-device) sayfasında |
| **Apex parolası** | Apex'iniz kayıtlı parolayı reddetti. [Sorun giderme](/help/troubleshooting) sayfasına göz atın |

:::note Yeniden deneme geri sayımı nasıl çalışır
Cora Max düzenli bir tempoyla yeniden bağlanmayı dener. İlk kopuştan sonra yaklaşık 15 saniye, sonra yine 15 saniye, sonra iki kez 30 saniye, ardından bağlanana kadar dakikada bir bekler. Hiçbir zaman pes etmez. **Çevrimdışı, 45 s içinde tekrar denenecek** normaldir.
:::

## Pano {#the-dashboard}

Ekranın geri kalanı panodur: her widget'ı görünür tutan sabit bir ızgara. Kaymaz.

Widget'lar telefonunuzdakilerle aynı şekilde çalışır, yalnızca birkaç adım geriden okunacak kadar büyüktür. Her biçimin ne gösterdiği [Widget rehberi](/help/mobile-widgets) sayfasında. Panoda neler olduğunu değiştirmek için [Cora Max panosunu düzenleme](/help/max-dashboard-editing) sayfasına bakın.

Ölçülen bir parametreyi gösteren her widget, tıpkı telefonunuzdaki gibi **yaşını** ve **kaynağını** gösterir. Yanında `2 g` yazan bir sayı iki günlüktür. Cihaz ve kontrol kutucukları ise kendi durumlarını gösterir.

### Ekran karardığında {#when-the-screen-is-dimmed}

**Şu kadar süre sonra karart** süresi boyunca dokunulmazsa ekran kararır. İlk dokunuşunuz yalnızca ekranı uyandırır, böylece yanlışlıkla bir kontrole basamaz. Ekranı kullanmak için yeniden dokunun.

## Akvaryum menüsü {#the-tank-menu}

![Pano üzerinde açık akvaryum menüsü: Parametreleri kaydet, Günlük, Reef Buddy ve akvaryumun diğer ekranları](img/max-menu.webp "Üst çubuktaki akvaryum adından açılan akvaryum menüsü.")

Ekrandaki akvaryumun menüsünü açmak için akvaryum adına dokunun.

| Öğe | Ne açılır |
|---|---|
| **Parametreleri kaydet** | Test kiti ölçümlerini ekran klavyesiyle girin |
| **Günlük** | Bu akvaryumun [günlüğü](/help/max-records) |
| **Reef Buddy** | En son [özet](/help/max-intelligence) |
| **Sağlık Raporları** | Sağlık değerlendirmeleri |
| **Bakım** | [Görev listesi](/help/max-records) |
| **ICP Raporları** | Yüklenen [laboratuvar sonuçları](/help/max-intelligence) |
| **Parametre geçmişi** | Verisi olan herhangi bir parametreyi seçin ve [grafiğini](/help/max-intelligence) açın |
| **Uyarı eşikleri** | Bu akvaryumdaki her metrik için [sağlıklı aralık](/help/max-alerts) |
| **Canlılar** | Bu akvaryumun envanteri, bu ekranda yalnızca görüntüleme |
| **Etkinlik** | [Her priz, besleme ve doz](/help/max-activity) ve ne olduğu |
| **Pano düzeni** | [Bu ekrandaki widget'ları düzenleyin](/help/max-dashboard-editing) |
| **Birimler** | Bu akvaryumun ölçümleri için görüntüleme birimleri |
| **Akvaryum ayarları** | Bu akvaryumun tam ayarlar ekranı |

## Akvaryumlar arasında geçiş {#switching-tanks}

[Reef Room](/help/max-reef-room)'a gitmek için üst çubuğun en solundaki **ızgara simgesine** dokunun, sonra istediğiniz akvaryumu açın. Panoda yana da kaydırabilirsiniz. Her akvaryumun kendi pano düzeni vardır, bu yüzden geçiş yaptıkça tüm ekran değişir.

## Prizler ve Besleme çekmecesi {#the-outlets-feed-drawer}

Neptune Apex'i olan bir akvaryumda panonun altında küçük bir **Prizler ve Besleme** etiketi durur. **Kontroller**'i açmak için ona dokunun ya da panonun herhangi bir yerinde yukarı kaydırın.

- **BESLEME**, Apex besleme döngülerinizden birini **A**, **B**, **C** ya da **D** ile başlatır. **İptal** onu erken bitirir.
- **PRİZLER**'in her biri Otomatik, Kapalı ve Açık arasında değiştirilebilir.

Çekmece bu pano için seçtiğiniz prizleri ve besleme döngülerini, hiç seçmediyseniz hepsini listeler. Ayrıntılar [Prizler ve kontroller](/help/max-controls) sayfasında.

:::warning Bu çekmece gerçek ekipmanı kontrol eder
Dokunduğunuz anda bir komut gider, ama göndermek yapıldığı anlamına gelmez. Sonuç Onaylandı, Onaylanmadı, Reddedildi ya da Değişiklik yok olarak döner ve hangisi olduğunu [Etkinlik](/help/max-activity) içinde görebilirsiniz. Besleme modu, yem verirken akışı durdurmanın güvenli yoludur, çünkü her şeyi kendisi eski haline getirir. Elle yapılan Kapalı, siz geri değiştirene kadar kapalı kalır.
:::

## Bir şey yerinde görünmüyorsa {#if-something-looks-out-of-place}

Ölçümler eski görünüyorsa ya da durum etiketi turuncu veya kırmızıysa [Sorun giderme](/help/troubleshooting) ile başlayın.
