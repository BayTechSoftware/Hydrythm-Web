---
title: Kameralar ve Skimmer Gözcüsü
description: Cora'ya bir Wyze, Tapo, Sonoff ya da başka bir RTSP kamera ekleyin, bir kutucukta ya da tam ekran izleyin ve Skimmer Gözcüsü'nün skimmer kabı taşmadan önce sizi uyarmasını sağlayın.
section: Cora Mobile
reviewed: 2026-10-12
order: 35
group: Equipment
---

:::note Beta
**Beta.** Kameralar Beta aşamasındadır ve yalnızca Beta kullanıcılarına açıktır. Beta kullanıcısı değilseniz bunları **Cihaz Ekle** içinde görmezsiniz. Beta erişimi istemek için [destek](/support.html) ile iletişime geçin.
:::

Akvaryumunuzu Cora'dan, telefonunuzda ve Cora Max'te görmek için bir kamera ekleyin. Kamera için akvaryumda bir Cora Max gerekir, bu yüzden akvaryumda Cora Max olana kadar **Kamera** satırında **Cora Max Gerektirir** yazar.

## Kamera ekleme

1. **Cihazlar → Cihaz Ekle → Kamera**'ya, sonra **Kamera ekle**'ye gidin.
2. Türü seçin: Wyze, Tapo, Sonoff ya da **Diğer kamera (RTSP)**.
3. Cora'nın o tür için gösterdiği adımları izleyin. Önce kameranın kendi uygulamasında nelerin açılması gerektiğini anlatırlar.
4. Adı, akış adresini, kullanıcı adını, şifreyi ve akvaryumu doldurun, sonra **Bağlantıyı test et**'e dokunun. Kamera cevap verince **Kamera ekle**'ye dokunun.

Eklerken telefonunuz kamerayla aynı Wi-Fi'de olmalıdır. Adres ev ağınızda olmalı ve kullanıcı adıyla şifreyi adrese değil, kendi alanlarına yazmalısınız.

Wyze, Tapo ve Sonoff kameralar denendi (Wyze Cam v4, Tapo C120 ve Sonoff Cam S3W). RTSP sunan diğer kameralar da çalışabilir.

| Kamera | Önce şunu açın |
|---|---|
| Wyze | Wyze uygulamasında kamerayı açın, sonra Ayarlar, Gelişmiş Ayarlar, RTSP'ye gidin. RTSP'yi açın, bir kullanıcı adı ve şifre seçin, sonra kamerayı yeniden başlatın. Kameranın yazılımı 4.52.17 ya da daha yeni olmalıdır. |
| Tapo | Tapo uygulamasında Ayarlar, Gelişmiş Ayarlar, Kamera Hesabı'nı açıp bir kullanıcı adı ve şifre oluşturun. Bu, TP-Link hesabınız değildir. Bir Tapo kamera Tapo Care, SD kart kaydı ve diğer uygulamalara yayın özelliklerinden aynı anda yalnızca ikisini çalıştırabilir. |
| Sonoff | eWeLink'te kamera için RTSP'yi açın ve hesabını ayarlayın. Cora sizin için bir **Sonoff adresi** hazır ayarı doldurur. |
| Diğer kamera (RTSP) | Kameranın uygulamasında RTSP ya da ONVIF'i açın, bir kamera girişi ayarlayın ve kılavuzundaki akış adresini girin. Kameranızda giriş yoksa giriş alanlarını boş bırakın. |

## Kamerayı değiştirme

Kamerayı açın ve menüsünü kullanın: **Yeniden adlandır**, **Adresleri düzenle**, **Parolayı değiştir** ya da **Kamerayı kaldır**. Kamerayı kaldırmak, kayıtlı parolasını da siler.

## İzleme

Bir kamera panonuzda en fazla 3×2 boyutunda bir kutucuk olabilir ve onu **Tam ekran** açabilir, **Döndür**'ü kullanabilirsiniz.

Evdeyken, telefonunuz kameranın Wi-Fi'sindeyse Cora **Canlı video**'yu doğrudan kameradan oynatır. Evden uzaktayken ya da **Anlık görüntüler**'i seçtiğinizde Cora Max'iniz kameradan durağan görüntüler alır ve Cora bunları birkaç saniyede bir güncellenen, canlıya yakın görüntü olarak gösterir. Cora Max görüntü göndermiyorsa kutucuk bunu söyler.

## Skimmer Gözcüsü

:::note Beta
**Beta.** Skimmer Gözcüsü Beta aşamasındadır ve yalnızca Beta kullanıcılarına açıktır. Ayrıca ücretli bir plan gerekir: **Skimmer Gözcüsü ücretli planlara dahildir.** Beta erişimi istemek için [destek](/support.html) ile iletişime geçin.
:::

Skimmer Gözcüsü, skimmer toplama kabını bir kamerayla izler ve taşmadan önce sizi uyarır. Kameranın sayfasındaki **Skimmer Gözcüsü** kartında yer alır.

1. Kamerayı kaba doğrultun ve **Kabı izle**'yi açın.
2. **Kabı işaretle**'ye dokunun. Kutuyu kabın üstüne sürükleyin ve köşelerinden çekerek ona oturtun: alt kenar kabın dibine, üst kenar kabın dolu olduğu yere, yani kenarın hemen altına gelsin.
3. Kabı boşaltın ve **Kap şu an boş**'a dokunun. Cora, karşılaştırmak için boş kabın bir görüntüsünü alır. Bu yaklaşık 10 saniye sürer. Kamerayı ya da kutuyu oynatırsanız bunu yeniden yapın.
4. Sizi uyaracak doluluk seviyesini **%… dolulukta uyar** ayarından belirleyin. Kart bunu yüzde olarak gösterir.

Cora Max kabı birkaç dakikada bir kontrol eder. Kart son ölçümü ve ne kadar önce alındığını gösterir. **Şimdi kontrol et** hemen bir kontrol ister ve yaklaşık 10 saniye sürer. **Son 24 saat**, kabın gün içinde nasıl dolduğunu gösterir.

Görüntü okunması zorsa kart bunu söyler, örneğin **Kabın arkasındaki ışık çok parlak**.

### Kamera ipuçları

Kartın üzerindeki **Kamera ipuçları**, burada yazanların aynısını verir.

- Kameranın gece görüşünü Otomatik değil, Açık (hep kızılötesi) yapın. Böylece her görüntü gece de gündüz de aynı görünür.
- Kameranın spot ışığını Manuel yapın ve kapalı bırakın. Sump'taki kabarcıklar ve su hareket sayılır ve ışığı sürekli yakar.
- Kabın arkasından kameraya doğru güçlü ışık gelmesin.

## Görüntülere ne olur

Evdeyken video doğrudan kameradan oynar ve kaydedilmez. Evden uzaktayken kamera başına yalnızca bir durağan görüntü saklanır ve her yenisi bir öncekinin yerine geçer. Skimmer Gözcüsü, işaretlenen kabın son görüntüsünü, son 24 saatin doluluk ölçümlerini (yalnızca sayılar) ve boş kabın küçük bir görüntüsünü saklar. Kamerayı, akvaryumu ya da hesabınızı kaldırdığınızda silinirler. Ayrıntılar [gizlilik politikasında](/privacy-policy.html).
