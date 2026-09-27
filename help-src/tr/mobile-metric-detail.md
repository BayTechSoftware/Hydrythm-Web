---
title: Bir parametreye bakma
description: Tam geçmiş, onu bildiren her kaynak ve aralığını değiştirecek yer için herhangi bir widget'a dokunun.
section: Cora Mobile
reviewed: 2026-09-09
order: 8
group: Your dashboard
---

Bir widget size bir sayı gösterir. Ona dokunmak, sayının arkasındaki öyküyü gösterir.

## Aldığınız şey

![Bir parametreye bakma](img/mobile-metric-detail.webp "Üstte aralıklar, ardından bu parametreyi bildiren kaynaklar, ardından uyarı bandınız gölgeli grafik.")

**Kendi aralık seçicisiyle bir geçmiş grafiği**: **1s · 6s · 12s · 24s · 3g · 7g** ve daha uzunu.

**Bir kaynak filtresi.** Aralıkların altında bir çip satırı vardır: **Tümü**, artı bu parametreyi bildiren her kaynak için bir tane, örneğin *Apex*, *Cora*, *Red Sea* veya *Elle*. Yalnızca onun okumalarını görmek için birini seçin. Bir probu bir test kitine karşı doğrudan karşılaştırmanın yolu budur: aynı grafikte aralarında geçiş yapın.

**Dozajladığınız parametreler için bir dozaj hesaplayıcı bağlantısı.** [Akvaryum profilinizden](/help/mobile-tank-profile) akvaryum hacmini ve [Dozaj](/help/mobile-dosing)'dan güçleri kullanır.

**Bir karşılaştırma katmanı.** *Şununla karşılaştır*, aynı grafikte ikinci bir parametre çizer (kalsiyuma karşı alkalinite, sıcaklığa karşı pH); böylece şüphelendiğiniz bir ilişki hatırlanan bir şey olmaktan çıkıp görünür hale gelir.

**Ekrandaki pencere için özet istatistikler**: geçerli değerin altında bir satır olarak gösterilen **MİN**, **ORT** ve **MAKS**.

**Grafikte dozaj işaretleri**; böylece bir hareket, gerçekte dozajladığınızla karşılaştırılabilir.

**Ham okumalar listesi**: çizginin arkasındaki her tek okuma, kaynağı ve zaman damgasıyla.

**Uyarı bandınız**, grafikte gölgeli; böylece bir okuma yalıtılmış olarak değil aralığına karşı okunur. Aralığın kendisini değiştirmek için, panodaki widget'a uzun basın. Bkz. [Uyarılar ve eşikler](/help/mobile-alerts).

Elle **bir okuma kaydedin**.

## Bir aralık seçme

Doğru aralık, parametrenin ritmine bağlıdır:

| Parametre | Kullanışlı pencere |
|---|---|
| pH | 24 saat; günlük bir döngüde salınır |
| Sıcaklık | 24 saat veya 7 gün |
| Alkalinite | 7 veya 30 gün |
| Eser elementler | 30 gün veya bir yıl |

:::note Düz bir eğilimde okuma yaşını kontrol edin
Hareket etmemiş bir çizgi, kararlı bir parametreyi veya bildirmeyi durdurmuş bir kaynağı gösterebilir. Değerin yanındaki gösterilen yaş ikisini birbirinden ayırır.
:::

## Kaynakları karşılaştırma

Birden fazla kaynak bir parametreyi bildirdiğinde, Cora onları ortalamak yerine ayrı tutar. Her birini sırayla görmek için kaynak çiplerini kullanın.

Bir prob ile elle kaydedilen bir test arasındaki kalıcı bir fark, genellikle probun kalibrasyon gerektirdiğini gösterir.

Bir [ICP sonucu](/help/mobile-icp-health) kullanışlı bir üçüncü görüştür, ama bir hakem değildir. Laboratuvarlar birbirinden farklıdır ve örneğin taşınması, saklanması ve nakliyesi hepsi sonucu hareket ettirir. Tek bir ICP'yi gerçek değer olarak değil kanıt olarak ele alın; anlaşan iki test, birinden çok daha değerlidir.

## Bir widget'ın hangi kaynağa güveneceğini seçme

Bir widget'ın belirli bir kaynağı takip etmesini istiyorsanız, bunu widget'ın ayarlarında belirleyin. Bkz. **[Panonuzu düzenleme](/help/mobile-dashboard-editing)**.

## Kötü bir okumayı hariç tutma

Ani sıçrama yapan bir prob, yanlış okunan bir test, su değişimi ortasında alınan bir örnek: tek bir yanlış okuma, grafiği, ortalamaları ve onlardan çıkarım yapan her şeyi bozar.

![Ham okumalar listesi](img/mobile-readings.webp "Çizginin arkasındaki her okuma, kaynağı ve zamanıyla.")

Okumalar listesini üst çubuktaki simgeden açın, ardından hariç tutmak için bir okumaya dokunun. Ekran bunu açıkça söyler: *ortalamalardan ve içgörülerden hariç tutulur, ama günlüğünüzde kalır.* Hiçbir şey silinmez ve geri yüklenebilir.

:::warning Yanlış bir okumayı hariç tutun, hoşunuza gitmeyen bir okumayı değil
Hariç tutma, geçersiz olduğunu bildiğiniz okumalar içindir. Beğenmediğiniz ama kusur bulamadığınız bir okuma veridir ve onu kaldırmak sonraki her karşılaştırmayı daha az dürüst yapar.
:::

## Prob bakımını kaydetme

Buradan bir kalibrasyon veya temizlik kaydetmek, o kaynağa karşı tarihi damgalar; böylece daha sonraki bir anlaşmazlık, probun son ne zaman bakıldığına karşı okunabilir. Bkz. [Problar](/help/mobile-probes).

## Elle bir okuma kaydetme

Test kitinizin ne dediğini girin. Elle kaydedilen okumalar birinci sınıftır: kendi kaynaklarını ve zaman damgalarını alırlar, grafikte görünürler, Reef Buddy'yi beslerler ve Cora'nın ekipmanınızı neyle karşılaştırdığı budur.

:::note Cora, mantıksız görünen kayıtları kontrol eder
Bir değer, akvaryumun çalıştığı yerden çok farklıysa, kaydedilmeden önce onaylamanız istenir. Bu, yanlış yere konmuş bir ondalık noktasını veya yanlış parametreye karşı girilmiş bir okumayı yakalar. Onaylayın ve okuma normal şekilde saklanır.
:::
