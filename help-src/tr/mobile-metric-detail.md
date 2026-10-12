---
title: Parametre ayrıntıları
description: Bir widget'a dokunun. Tüm geçmişi, değeri bildiren her kaynağı ve aralığı nereden değiştireceğinizi görün.
section: Cora Mobile
reviewed: 2026-10-12
order: 8
group: Your dashboard
---

Widget size bir sayı gösterir. Widget'a dokunduğunuzda o sayının arkasındaki hikâyeyi görürsünüz.

Ekrana iki yoldan girersiniz. Panodaki bir widget'a dokunun ya da widget'ların altındaki düğme satırında **Parametre geçmişi**'ne dokunup bir parametre seçin. **Parametre geçmişi**, panoda widget'ı olmasa bile verisi olan her parametreyi listeler.

## Bu ekranda neler var

![Parametre ayrıntıları](img/mobile-metric-detail.webp "Üstte açılır listeler, altında uyarı aralığı gölgeli grafik.")

**Geçmiş grafiği.** Üstündeki üç açılır liste neyi göstereceğini belirler. **Parametre**, verisi olan başka bir parametreye geçer ve zaman aralığınızı korur. **Zaman aralığı** 1h'den 6h, 12h, 24h, 3d, 7d, 15d, 30d, 90d, 180d ve 360d üzerinden Tümü'ne kadar gider. **Kaynak** **Tüm kaynaklar** ile başlar ve bu akvaryumda bu parametreyi bildiren kaynakları listeler, örneğin *Apex*, *Cora*, *Red Sea* ya da *Manuel*. Yalnızca o kaynağın ölçümlerini görmek için birini seçin. Probu test kitiyle doğrudan böyle karşılaştırırsınız: aynı grafikte ikisi arasında geçiş yapın.

Ekran her zaman 24h ve **Tüm kaynaklar** ile açılır. Son seferki seçiminizi hatırlamaz.

**Dozaj hesaplayıcı bağlantısı** (dozladığınız parametrelerde). Hesaplayıcı akvaryum hacmini [akvaryum profilinizden](/help/mobile-tank-profile), ürün güçlerini [Dozaj](/help/mobile-dosing) ayarlarından alır.

**Karşılaştırma katmanı.** **Karşılaştır** ile aynı grafiğe ikinci bir parametre eklersiniz. Örneğin alkaliniteyle kalsiyumu ya da pH ile sıcaklığı üst üste koyabilirsiniz. Liste, akvaryumun sahip olduğu her parametreyi içerir. Aklınızdaki bir ilişkiyi hatırlamaya çalışmadan grafikte görürsünüz. İkinci çizgiyi kaldırmak için çipe yeniden dokunun.

**Özet istatistikler**: ekrandaki zaman aralığı için **En son**, **Min**, **Ort** ve **Maks** değerleri olan bir satır.

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

Bir parametreyi birden fazla kaynak bildiriyorsa Cora bunların ortalamasını almaz, ayrı tutar. **Kaynak** açılır listesiyle her birine sırayla bakın.

Panoda hangisinin görüneceğini en yeni ölçüm belirler. Canlı bir değerin yerini, hangi kaynaktan olursa olsun yalnızca daha geç bir ölçüm zamanına sahip bir ölçüm alır. Daha eski bir ölçüm geçmişe girer ve widget'taki değerin üzerine yazmaz. Widget için bir kaynağı sabitlediyseniz Cora onun yerine o kaynağı izler.

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

Test kitinizin sonucunu girin. Liste gruplanmıştır ve **İz Elementler** grubu iyot, demir ve bakırı µg/L cinsinden, potasyumu mg/L cinsinden kapsar. Elle girilen ölçümler diğerlerinden aşağı sayılmaz. Kendi kaynakları ve zamanları olur, grafikte görünürler ve Reef Buddy'ye veri sağlarlar. Cora ekipmanınızı da bu ölçümlerle karşılaştırır.

:::note Cora mantıksız görünen değerleri sorar
Girdiğiniz değer akvaryumun alışılmış değerlerinden çok farklıysa Cora kaydetmeden önce onay ister. Böylece yanlış yere konmuş bir virgül ya da yanlış parametreye girilmiş bir değer yakalanır. Onaylarsanız ölçüm normal şekilde kaydedilir.
:::
