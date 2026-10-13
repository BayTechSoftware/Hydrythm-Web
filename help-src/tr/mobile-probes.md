---
title: Parametre Eşlemesi ve problar
description: Her ölçümü hangi probun sağlayacağını seçin, her probun neyi ölçtüğünü Cora'ya söyleyin, prob kalibrasyonunu ve temizliğini kaydedin.
section: Cora Mobile
reviewed: 2026-10-13
order: 15
group: Equipment
---

Her probun neyi ölçtüğünü ve iki prob aynı şeyi bildirdiğinde hangisine güveneceğini Cora'ya söylemek için **Parametre Eşlemesi**'ni kullanın. **Ayarlar**'a gidin, akvaryumu açın ve **Parametre Eşlemesi**'ne dokunun.

**Akvaryumu düzenle** ile **Uyarı eşikleri** arasında yer alır. Panonun üstündeki kalem **Akvaryumu düzenle**'yi açar ve orada bu seçenek yoktur. Ona Neptune Apex ve GHL (Beta) cihaz sayfalarından da ulaşabilirsiniz. GHL yalnızca Beta kullanıcılarına açıktır. [Beta özellikleri](/help/mobile-beta) sayfasına bakın.

Ekranda bir arama alanı (**Parametre ara**) ve iki sekme var: **Eşleme** ve **Kaynaklar**. Arama parametre adlarına, prob adlarına, cihazlara ve markalara bakar. Aynı arama alanı her parametre seçicisinde bulunur.

## Problar: her birinin ne olduğunu Cora'ya söyleme {#mapping}

![Eşleme sekmesi](img/mobile-probe-mapping.webp "Her prob, onu bildiren cihaza göre gruplanmış ve eşlendiği parametreyle.")

İlk **Eşleme** sekmesi açılır. Cora'nın bildiği her probu, onu bildiren cihaza göre gruplanmış ve güncel ölçümüyle birlikte listeler. Cora standart prob adlarını kendisi tanır ve her satır neyle eşleştirdiğini gösterir. Genellikle yalnızca yerleştiremediği birkaçını düzeltmeniz gerekir.

Her satırda üç seçenek var.

- **Bir Cora parametresi**, o probun ölçtüğü metriktir.
- **Özel…**, Cora'da standart bir parametresi olmayan problar içindir. **Özel metrik (BÜYÜK HARF token)** alanına kısa, büyük harfli bir ad yazın, Cora da onu bu adla izler.
- **Yok say**, hiç kaydedilmesini istemediğiniz problar içindir.

Yok sayılan ya da eşlenmemiş bir prob panoda görünmez ve uyarı tetiklemez.

Bir eşleme, bir sonraki ölçümler geldiğinde çalışmaya başlar. Burada yaptığınız bir düzeltme geçmişi yeniden yazmaz, yalnızca o andan sonra kaydedilenleri değiştirir. Değişikliklerinizi uygulamak için **Kaydet**'e dokunun.

:::warning Cora eşlenmemiş bir probu göremez
Prob çalıştığı halde bir parametrede hiç ölçüm görünmüyorsa önce eşlemesini kontrol edin.
:::

## Her ölçüm nereden geliyor {#sources}

![Kaynaklar sekmesi](img/mobile-probes.webp "Her ölçüm, onu sağlayan prob ve Otomatik mi yoksa sizin seçiminiz mi olduğu.")

**Kaynaklar** sekmesi, Cora'nın bu akvaryum için izlediği pH ya da sıcaklık gibi her metriği listeler ve şu anda onu hangi probun sağladığını gösterir.

Bağladığınız tüm kontrolcülerde onu bildiren her probu görmek için bir ölçüme dokunun. Her biri markasını, prob için kullandığı kendi adını ve canlı değerini gösterir. Sabitlemek için birini seçin ya da Cora'nın en son bildiren probu kullanması için **Otomatik (en yeni ölçüm kazanır)**'ı seçin. Diğerleri geçmişte kalır.

Her ölçümün yanındaki etiket hangisinin geçerli olduğunu gösterir: **Otomatik** ya da bir probu sabitlediğinizde **Sizin seçiminiz**. Seçiminiz tek bir widget için değil, o ölçüm için tüm akvaryumda geçerlidir.

Sabitlenmiş bir prob bildirmeyi bırakırsa Cora ondan en son ne zaman haber alındığını gösterir ve **Otomatik'e Dön**'ü önerir. Böylece ölü bir prob bir ölçümü takılı bırakamaz.

Bir ölçüme kendi görünen adını vermek için **Yeniden adlandır**'a dokunun. Bu, probun kendisine verdiğiniz addan ayrıdır. Panonuzda, uyarılarda ve Reef Buddy'de görünen budur.

Akvaryum profilinde de bir **Parametre Kaynakları** bölümü vardır (yeni bir akvaryum oluştururken gizlidir). Aynı şeyi daha kısa bir biçimde ayarlar. Her kontrolcüdeki her probu tek yerde görmek istediğinizde Parametre Eşlemesi'ni kullanın.

:::note Sızıntı sensörü burada yeniden atanamaz
Bir sızıntı sensörünün alarmı kendi adına bağlıdır, bu yüzden bu seçicinin dışında tutulur. Her zamanki gibi çalışır.
:::

## Bir parametre için birden fazla prob {#multiple-probes}

İki sıcaklık probunuz varsa, ister aynı kontrolcüde ister iki farklı kontrolcüde olsun, ikisini de eşleyin. Cora onları ayrı kaynaklar olarak tutar. Ölçümü hangisinin sağlayacağını **Kaynaklar** sekmesinde seçersiniz ya da Otomatik'te bırakırsınız. İkisini [parametre görünümünde](/help/mobile-metric-detail) karşılaştırabilirsiniz.

İki kaynak aynı parametreyi bildirdiğinde en yeni ölçüm kazanır. Ekrandaki bir değerin yerini, hangi cihazdan gelirse gelsin, yalnızca daha geç bir ölçüm zamanı olan bir ölçüm alır. Daha eski bir ölçüm ya da eski bir ölçümü yeniden gönderen bir cihaz geçmişe gider ve güncel değerin üzerine yazmaz. **Kaynaklar** sekmesinde bir kaynağı sabitlediyseniz Cora onun yerine o kaynağı izler.

## Prob bakımını kaydetme {#recording-probe-care}

Problar zamanla kayar. Bir probu kalibre ettiğinizde, temizlediğinizde ya da değiştirdiğinizde Cora'ya söyleyin, böylece ölçümdeki sıçramayı akvaryumda gerçek bir değişiklik sanmaz.

1. Panoda parametrenin widget'ına dokunun, örneğin pH, sıcaklık, tuzluluk ya da ORP.
2. Üst çubuktaki **Prob bakımını kaydet**'e (sensör simgesi) dokunun.
3. Ne yaptığınızı seçin: **Kalibre Edildi**, **Temizlendi**, **Değiştirildi**, **Yeniden Konumlandırıldı** ya da **Referansla Karşılaştırıldı**. Bir **Referans ölçüm** ve not ekleyebilirsiniz.
4. **Prob bakımını kaydet**'e dokunun.

Parametre görünümü bundan sonra o probun ne zaman kalibre edildiğini gösterir. Prob bakımı tekrarlanan bir [bakım görevi](/help/mobile-maintenance) olarak da iyi işler.

:::note Kalibrasyon tarihleri uyuşmazlıkları açıklar
Bir prob ile bir test kiti farklı sonuç verdiğinde probu en son ne zaman kalibre ettiğinize bakın. Yanıt genellikle budur.
:::
