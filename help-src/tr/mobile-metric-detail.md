---
title: Parametre ayrıntıları
description: Bir widget'a dokunun. Tüm geçmişi, değeri bildiren her kaynağı ve aralığı nereden değiştireceğinizi görün.
section: Cora Mobile
reviewed: 2026-09-09
order: 8
group: Your dashboard
---

Widget size bir sayı gösterir. Widget'a dokunduğunuzda o sayının arkasındaki hikâyeyi görürsünüz.

## Bu ekranda neler var

![Parametre ayrıntıları](img/mobile-metric-detail.webp "Üstte zaman aralıkları, altında bu parametreyi bildiren kaynaklar, en altta uyarı aralığı gölgeli grafik.")

**Geçmiş grafiği** ve kendi zaman aralığı seçicisi: **1h · 6h · 12h · 24h · 3d · 7d** ve daha uzunları.

**Kaynak filtresi.** Zaman aralıklarının altında çipler var: **Tümü** ve bu parametreyi bildiren her kaynak için bir çip. Örneğin *Apex*, *Cora*, *Red Sea* ya da *Manuel*. Yalnızca o kaynağın ölçümlerini görmek için bir çip seçin. Probu test kitiyle doğrudan böyle karşılaştırırsınız: aynı grafikte ikisi arasında geçiş yapın.

**Dozaj hesaplayıcı bağlantısı** (dozladığınız parametrelerde). Hesaplayıcı akvaryum hacmini [akvaryum profilinizden](/help/mobile-tank-profile), ürün güçlerini [Dozaj](/help/mobile-dosing) ayarlarından alır.

**Karşılaştırma katmanı.** *Şununla karşılaştır* ile aynı grafiğe ikinci bir parametre eklersiniz. Örneğin alkaliniteyle kalsiyumu ya da pH ile sıcaklığı üst üste koyabilirsiniz. Aklınızdaki bir ilişkiyi hatırlamaya çalışmadan grafikte görürsünüz.

**Özet istatistikler**: ekrandaki zaman aralığı için **MİN**, **ORT** ve **MAKS**. Güncel değerin altında bir satır olarak görünür.

**Grafikte dozaj işaretleri.** Bir değişimi gerçekte verdiğiniz dozlarla yan yana görürsünüz.

**Ham ölçüm listesi**: çizginin arkasındaki her ölçüm, kaynağı ve zamanıyla.

**Uyarı aralığınız** grafikte gölgeli olarak görünür. Böylece her ölçümü tek başına değil, aralığıyla birlikte okursunuz. Aralığı değiştirmek için panodaki widget'a uzun basın. Ayrıntılar [Uyarılar ve eşikler](/help/mobile-alerts) sayfasında.

**Ölçüm girme**: test sonuçlarını elle girebilirsiniz.

## Zaman aralığı seçme

Doğru aralık, parametrenin ne kadar hızlı değiştiğine bağlıdır:

| Parametre | İşe yarayan aralık |
|---|---|
| pH | 24 saat. pH gün içinde iner çıkar |
| Sıcaklık | 24 saat ya da 7 gün |
| Alkalinite | 7 ya da 30 gün |
| Eser elementler | 30 gün ya da 1 yıl |

:::note Düz çizgide ölçümün ne kadar eski olduğuna bakın
Hiç kıpırdamayan bir çizgi parametrenin sabit olduğunu gösterebilir. Ama veri göndermeyi bırakmış bir kaynak da aynı görüntüyü verir. Değerin yanındaki ölçüm yaşı hangisi olduğunu söyler.
:::

## Kaynakları karşılaştırma

Bir parametreyi birden fazla kaynak bildiriyorsa Cora bunların ortalamasını almaz, ayrı tutar. Kaynak çipleriyle her birine sırayla bakın.

Probla elle girilen test arasında sürekli bir fark varsa genellikle probun kalibre edilmesi gerekiyordur.

[ICP sonucu](/help/mobile-icp-health) işe yarar bir üçüncü görüştür, ama son sözü söylemez. Laboratuvarlar birbirinden farklı sonuç verebilir. Numunenin nasıl alındığı, saklandığı ve taşındığı da sonucu değiştirir. Tek ICP'yi kesin değer olarak değil, kanıt olarak görün. Birbiriyle uyuşan iki test, tek testten çok daha değerlidir.

## Widget'ın hangi kaynağı izleyeceğini seçme

Widget'ın belli bir kaynağı izlemesini istiyorsanız bunu widget'ın ayarlarından seçin. Ayrıntılar **[Panoyu düzenleme](/help/mobile-dashboard-editing)** sayfasında.

## Hatalı ölçümü hariç tutma

Probun bir anlık sıçraması, yanlış okunmuş bir test, su değişimi sırasında alınmış bir numune. Tek bir hatalı ölçüm grafiği, ortalamaları ve bunlara dayanan her şeyi bozar.

![Ham ölçüm listesi](img/mobile-readings.webp "Çizginin arkasındaki her ölçüm, kaynağı ve zamanıyla.")

Üst çubuktaki simgeden ölçüm listesini açın. Hariç tutmak istediğiniz ölçüme dokunun. Ekranda bu açıkça yazar: *Ortalamalardan ve içgörülerden hariç tutmak için bir ölçüme dokunun. Günlüğünüzde kalır.* Hiçbir şey silinmez, ölçümü istediğiniz zaman geri getirebilirsiniz.

:::warning Hoşunuza gitmeyen ölçümü değil, hatalı ölçümü hariç tutun
Hariç tutma, geçersiz olduğunu bildiğiniz ölçümler içindir. Beğenmediğiniz ama hatasını bulamadığınız bir ölçüm de veridir. Onu çıkarırsanız sonraki bütün karşılaştırmalar yanıltıcı olur.
:::

## Prob bakımını kaydetme

Kalibrasyonu ya da temizliği buradan kaydederseniz tarih o kaynağa işlenir. İleride bir uyuşmazlık çıktığında probun en son ne zaman bakım gördüğüne bakabilirsiniz. Ayrıntılar [Problar](/help/mobile-probes) sayfasında.

## Elle ölçüm girme

Test kitinizin sonucunu girin. Elle girilen ölçümler diğerlerinden aşağı sayılmaz. Kendi kaynakları ve zamanları olur, grafikte görünürler ve Reef Buddy'ye veri sağlarlar. Cora ekipmanınızı da bu ölçümlerle karşılaştırır.

:::note Cora mantıksız görünen değerleri sorar
Girdiğiniz değer akvaryumun alışılmış değerlerinden çok farklıysa Cora kaydetmeden önce onay ister. Böylece yanlış yere konmuş bir virgül ya da yanlış parametreye girilmiş bir değer yakalanır. Onaylarsanız ölçüm normal şekilde kaydedilir.
:::
