---
title: Kameralar ve Skimmer Gözcüsü
description: Cora'ya bir Wyze, Tapo, Sonoff ya da başka bir RTSP kamera ekleyin, akvaryumunuzu bir kutucukta ya da tam ekran izleyin ve skimmer kabı taşmadan önce Skimmer Gözcüsü'nün sizi uyarmasını sağlayın.
section: Cora Mobile
reviewed: 2026-10-13
order: 17
group: Equipment
---

:::note Beta
**Beta.** Kameralar Beta aşamasındadır ve yalnızca Beta kullanıcılarına açıktır. Beta kullanıcısı değilseniz bunları **Cihaz Ekle** içinde görmezsiniz. Beta erişimi istemek için [destek](/support.html) ile iletişime geçin. Ayrıntılar [Beta özellikleri](/help/mobile-beta) sayfasında.
:::

Akvaryumunuzu Cora'dan, telefonunuzda ve Cora Max'te görmek ve Skimmer Gözcüsü'nün skimmer kabını izlemesini sağlamak için bir kamera ekleyin. **Cihazlar → Cihaz Ekle → Kamera** ile başlayın. Bir kamera akvaryumda bir Cora Max gerektirir, bu yüzden akvaryumda bir tane olana kadar **Kamera** satırında **Cora Max Gerektirir** yazar.

## Kamera ekleme {#adding-a-camera}

1. **Cihazlar → Cihaz Ekle → Kamera**'ya, ardından **Kamera ekle**'ye gidin.
2. Türü seçin: Wyze, Tapo, Sonoff ya da **Diğer kamera (RTSP)**.
3. Cora'nın o tür için gösterdiği adımları izleyin. Önce kameranın kendi uygulamasında neyi açmanız gerektiğini söylerler.
4. Adı, akış adresini, kullanıcı adını, şifreyi ve akvaryumu doldurun, sonra **Bağlantıyı test et**'e dokunun. Kamera yanıt verdiğinde **Kamera ekle**'ye dokunun.

Eklerken telefonunuz kamerayla aynı Wi-Fi'da olmalıdır. Adres ev ağınızda olmalıdır ve kullanıcı adını ve şifreyi adrese değil kendi alanlarına girersiniz.

Wyze, Tapo ve Sonoff kameralar test edildi (Wyze Cam v4, Tapo C120 ve Sonoff Cam S3W). RTSP sunan diğer kameralar da çalışabilir.

| Kamera | Önce bunu açın |
|---|---|
| Wyze | Wyze uygulamasında kamerayı açın, sonra Ayarlar, Gelişmiş Ayarlar, RTSP. RTSP'yi açın, bir kullanıcı adı ve şifre seçin, sonra kamerayı yeniden başlatın. Kameranın 4.52.17 ya da daha yeni bir yazılımı olmalıdır. |
| Tapo | Tapo uygulamasında Ayarlar, Gelişmiş Ayarlar, Kamera Hesabı'nı açın ve bir kullanıcı adı ve şifre oluşturun. Bu sizin TP-Link hesabınız değildir. Bir Tapo kamera Tapo Care, SD kart kaydı ve diğer uygulamalara yayından aynı anda yalnızca ikisini çalıştırabilir. |
| Sonoff | eWeLink'te kamera için RTSP'yi açın ve hesabını ayarlayın. Cora sizin için bir **Sonoff adresi** hazır ayarı doldurur. |
| Diğer kamera (RTSP) | Kameranın uygulamasında RTSP ya da ONVIF'i açın, bir kamera girişi ayarlayın ve kılavuzundaki akış adresini girin. Kameranızın girişi yoksa giriş bilgilerini boş bırakın. |

## Bir kamerayı değiştirme {#changing-a-camera}

Kamerayı açın ve menüsünü kullanın: **Yeniden adlandır**, **Adresleri düzenle**, **Parolayı değiştir** ya da **Kamerayı kaldır**. Kaldırmak, kayıtlı parolasını da siler.

## İzleme {#watching-it}

![Bir kamera sayfası](img/mobile-camera.webp "Kamera sayfası, üstte görüntü ve altında Skimmer Gözcüsü kartı.")

Bir kamera panonuzda en fazla 3×2 boyutunda bir kutucuk olabilir. [Panonuzu düzenleme](/help/mobile-dashboard-editing) sayfasına bakın. **Tam ekran** ve **Döndür** için onu açın.

Evde, telefonunuz kameranın Wi-Fi'ındayken Cora **Canlı video**'yu doğrudan kameradan oynatır. Evden uzaktayken ya da **Anlık görüntüler**'i seçtiğinizde Cora Max'iniz kameradan durağan görüntüler alır ve Cora onları birkaç saniyede bir güncellenen, canlıya yakın görüntü olarak gösterir. Cora Max görüntü göndermiyorsa kutucuk bunu söyler.

## Skimmer Gözcüsü {#skimmer-watch}

:::note Beta
**Beta.** Skimmer Gözcüsü Beta aşamasındadır ve yalnızca Beta kullanıcılarına açıktır. Ayrıca ücretli bir plan gerektirir. Plan yoksa kartta **Skimmer Gözcüsü ücretli planlara dahildir.** yazar ve **Planları gör** önerilir. Beta erişimi istemek için [destek](/support.html) ile iletişime geçin.
:::

Skimmer Gözcüsü, skimmer toplama kabını bir kamera aracılığıyla izler ve taşmadan önce sizi uyarır. Kameranın sayfasında, **Skimmer Gözcüsü** kartında yer alır.

![Kabı işaretleme](img/mobile-camera-mark-cup.webp "Çerçeveyi kabın üstüne sürükleyin: alt kenar kabın dibine, üst kenar ağzın hemen altına.")

1. Kamerayı kaba doğrultun ve **Kabı izle**'yi açın.
2. **Kabı işaretle**'ye dokunun. Çerçeveyi kabın üstüne sürükleyin ve köşelerinden çekerek oturtun: alt kenar kabın dibine, üst kenar kabın dolu olduğu yere, ağzın hemen altına. Daha sonra düğmede **Kabın çerçevesini taşı** yazar.
3. Kabı boşaltın ve **Kap şu an boş**'a dokunun. Cora karşılaştırmak için boş kabın bir görüntüsünü alır. Yaklaşık 10 saniye sürer. Kamerayı ya da çerçeveyi oynatırsanız bunu yeniden yapın.
4. **%… dolulukta uyar** kaydırıcısını sizi uyarması gereken doluluk seviyesine sürükleyin. Biraz pay bırakın, çünkü Cora 15 dakikada bir kontrol eder.

![Bir kamera sayfasında Skimmer Gözcüsü kartı](img/mobile-skimmer-watch.webp "Kap şu an boş, son ölçüm, son 24 saat, Şimdi kontrol et ve kamera ipuçları.")

Cora Max kabı 15 dakikada bir kontrol eder. Kart son ölçümü ve ne kadar önce alındığını gösterir, panonuzdaki kamera kutucuğu da kabın seviyesini gösterir. **Şimdi kontrol et** kabı hemen kontrol eder, bu yaklaşık 10 saniye sürer. **Son 24 saat**, kabın gün boyunca nasıl dolduğunu gösterir.

Kap **%… dolulukta uyar** seviyenize ulaştığında tek bir bildirim alırsınız. **Ekipman Arızaları** altında gönderilir, bu yüzden [Bildirimler](/help/mobile-notifications) içinde o kategoriyi açık tutun. Kabı boşalttıktan sonra uyarı yeniden tetiklenmeye hazırdır.

### Ölçüm yanlış görünüyorsa {#skimmer-watch-problems}

| Kartta yazan | Ne yapmalı |
|---|---|
| **Kabın arkasındaki ışık çok parlak** | Kabın arkasındaki ışığı kapatın ya da yerini değiştirin. Aşağıdaki kamera ipuçlarına bakın |
| **Emin değil (düşük güven)** | Görüntü zor okundu. Kamera ipuçlarını kontrol edin, sonra **Şimdi kontrol et**'e dokunun |
| **Önce kabı işaretleyin** | **Kabı işaretle**'ye dokunun ve çerçeveyi çizin |
| **Kalibre edilmedi: kabı boşaltın ve Kap şu an boş düğmesine dokunun** | Kabı boşaltın, sonra **Kap şu an boş**'a dokunun |
| **Çerçeve taşındı: yeniden kalibre edin** | Çerçeveyi taşıdınız. Kabı boşaltın ve yeniden **Kap şu an boş**'a dokunun |
| **Cora Max kameradan görüntü alamadı.** | Kameranın açık olduğunu ve akvaryumun Cora Max'inin çevrimiçi olduğunu kontrol edin |
| **Son kontrol başarısız oldu.** | **Şimdi kontrol et**'e dokunun. Başarısız olmaya devam ederse [Sorun giderme](/help/troubleshooting) sayfasına bakın |
| **Henüz ölçüm yok. Cora Max 15 dakikada bir kontrol eder.** | İlk kontrolü bekleyin ya da **Şimdi kontrol et**'e dokunun |

### Kamera ipuçları {#camera-tips}

Karttaki **Kamera ipuçları** size buradakiyle aynı tavsiyeleri verir.

- Kameranın gece görüşünü Otomatik değil Açık (her zaman kızılötesi) yapın, böylece her görüntü gece de gündüz de aynı görünür.
- Kameranın spot ışığını Manuel'e ayarlayın ve kapalı bırakın. Sump'taki kabarcıklar ve su hareket sayılır ve ışığı sürekli yakar.
- Güçlü ışıkların kabın arkasından doğrudan kameraya parlamasını önleyin.

### Cora Max'te {#skimmer-watch-on-cora-max}

![Cora Max'te kamera kutucukları, biri skimmer kabının seviyesini gösteriyor](img/max-skimmer-watch.webp "Cora Max'te kamera kutucuğu kabın seviyesini ve ne kadar eski olduğunu gösterir.")

Cora Max'te kamera kutucuğu ve tam ekran kamera, doluluk seviyesi ve ölçümün ne kadar eski olduğuyla birlikte **Kap** gösterir. Çip, kap uyarı seviyenize 10 puan kaldığında turuncuya, ona ulaştığında kırmızıya döner. Tam ekran kamerada **%… olunca uyar** düğmesi, seviyeyi orada da değiştirebileceğiniz **Köpük kabı uyarısı**'nı açar. Bir kontrol çalışırken canlı görüntü birkaç saniye duraklayabilir. Ayrıntılar [Cora Max'ten ekipman kontrolü](/help/max-device-control) sayfasında.

## Görüntülere ne olur {#pictures}

Evde video doğrudan kameradan oynar ve kaydedilmez. Evden uzaktayken kamera başına yalnızca bir durağan görüntü saklanır ve her yenisi bir öncekinin yerine geçer. Skimmer Gözcüsü, işaretlenen kabın en son görüntüsünü, son 24 saatin doluluk ölçümlerini (yalnızca sayılar) ve boş kabın küçük bir görüntüsünü saklar. Bunlar kamerayı kaldırdığınızda ya da hesabınızı sildiğinizde silinir. Tüm ayrıntılar [gizlilik politikasında](/privacy-policy.html).
