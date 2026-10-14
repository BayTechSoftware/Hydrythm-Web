---
title: Widget rehberi
description: Cora Mobile panosundaki her widget türü, değer, gösterge, grafik, durum ve prizden cihaz kutucuklarına kadar, ve her birini ne zaman kullanacağınız.
section: Cora Mobile
reviewed: 2026-10-13
order: 9
group: Your dashboard
---

Widget, panonuzdaki bir kutucuktur ve tek bir şeyi gösterir. Bu sayfa her türü ve onda neleri ayarlayabileceğinizi anlatır.

Widget'ları [pano düzenleyicisinde](/help/mobile-dashboard-editing) ekler ve yerleştirirsiniz. Ayarlarını açmak için orada bir widget'a dokunun: bir metrik için **Tür** ve **Parametre**, diğerleri için priz ya da cihaz, ardından **Genişlik** ve **Yükseklik**, bir grafik için de **Zaman aralığı**.

![Cora Mobile'da bir widget'ın ayarlar sayfası](img/mobile-widget-config.webp "Bir widget'ın ayarlarının alt yarısı: parametre, genişlik, yükseklik ve zaman aralığı, ardından Kaldır ve Bitti.")

## On beş tür {#the-fifteen-types}

| Tür | Ne gösterir |
|---|---|
| **Değer** | Güncel ölçüm, birimi, yaşı ve kaynağı |
| **Gösterge** | Üzerinde aralığınızın işaretli olduğu bir yay ve değerde duran bir düğme |
| **Grafik** | Seçtiğiniz zaman aralığındaki eğilim |
| **Durum** | Renkli bir noktayla birlikte düz yazı olarak ölçüm |
| **Priz** | Üç konumlu bir kontrol: Otomatik, Kapalı, Açık |
| **ReefBeat** | Kendi özetiyle tek bir Red Sea ünitesi |
| **Apex modülü** | Trident ya da DŌS gibi takılı tek bir Apex modülü |
| **Jecod** | Modu ve yoğunluğuyla tek bir Jecod pompası |

Priz'den sonraki her şey bir **cihaz** kutucuğudur. Her biri bir parametreye değil bir ekipmana aittir ve o ünite ne bildiriyorsa onu gösterir. Cora Max'te ayrıca Cora Max'te eklediğiniz bir **Sahne** kutucuğu vardır. [Cora Max panosunu düzenleme](/help/max-dashboard-editing) sayfasına bakın.


## Boyut {#sizing}

**Genişlik** ve **Yükseklik** her biri **1×** ya da **2×** olabilir, yani bir widget bir ya da iki hücre genişliğinde ve bir ya da iki hücre yüksekliğindedir. Grafik hiçbir zaman tek hücre genişliğinde olmaz. Üç sütunlu bir panoda iki hücre genişliğindeki bir gösterge satırın üçte ikisini kaplar. Bu genellikle en önemli parametreniz için iyi bir biçimdir.

## Parametre widget'ı neler gösterir {#what-a-parameter-widget-shows}

Değer, Gösterge, Grafik ve Durum widget'larının hepsi ölçülen bir parametreyi gösterir ve her zaman üç şey gösterirler. Priz ve cihaz kutucukları kendi durumlarını gösterir, çünkü arkalarında tek bir ölçüm yoktur.

- Büyük yazıyla **değer**
- **Yaş** (`şimdi`, `1 sa`, `2 g`): kaynağın değeri en son ne kadar önce doğruladığı. Bir prob için bu, cihazının en son ne zaman bağlandığıdır, bu yüzden sabit bir ölçüm taze kalır. Bir test kiti ya da ICP sonucu için testi yaptığınız zamandır. Ayrıntılar [Panonuzu okuma](/help/mobile-dashboard#how-to-read-a-parameter-widget) sayfasında.
- **Kaynak**: sayının nereden geldiğini söyleyen küçük bir rozet

Bir parametre widget'ının kendine ait aralık ya da kaynak ayarı yoktur. Aralık akvaryumun uyarı eşiklerinden (panoda widget'a uzun basın), kaynak da [Parametre Eşlemesi](/help/mobile-probes)'nden gelir. Tüm geçmişini, onu bildiren her kaynağı ve uyarı bandınızı görmek için panoda widget'a dokunun.

## Değer {#value}

Düz sayıdır. Güncel ölçümü, birimini, ne kadar eski olduğunu ve nereden geldiğini gösterir.

Eğiliminden çok sayısına baktığınız parametreler için kullanın, kalsiyum, magnezyum ya da nitrat gibi.

## Gösterge {#gauge}

Gösterge, üzerinde uyarı aralığınızın işaretli olduğu bir yay ve güncel değerde duran bir düğmedir. Düğmenin rengi nerede olduğunuzu söyler: aralığın içinde, kayıyor ya da dışında.

Aktif olarak yönettiğiniz parametreler için kullanın, alkalinite, pH, tuzluluk ya da sıcaklık gibi.

:::note Göstergeleri en az iki sütun genişliğinde yapın
Tek sütunda yay hızlıca okunamayacak kadar küçüktür. Yeriniz darsa bir **Değer** widget'ı kullanın.
:::

## Grafik {#graph}

Grafik, seçtiğiniz zaman aralığı boyunca küçük bir çizgi grafiktir: 1 sa, 6 sa, 24 sa, 7 g, 30 g ya da 1 y. En yüksek ve en düşük değeri işaretler ve güncel değeri yazar.

Test ettiğiniz bir parametrede (Trident ya da test kitiyle) çizgi gerçek testlerinizi birleştirir. Aralıkta yalnızca bir test varsa çizgi ondan önceki testten gelir ve en yüksek ya da en düşük değer işaretlenmez. Aralıkta hiç test yoksa ya da tek bir testi bağlayacak daha önce bir şey yoksa kutucukta çizgi yerine **Toplanıyor…** yazar.

Değişen her şey için kullanın, gün içinde pH, sıcak havalarda sıcaklık ya da dozlar arasında alkalinite gibi.

Grafik her zaman **en az iki hücre genişliğindedir**. Tek hücreye sıkıştırılmış bir çizgi grafik size hiçbir şey söylemez, bu yüzden düzenleyici buna izin vermez.

:::note Parametreye uyan zaman aralığını seçin
pH günlük bir döngüyle iner çıkar, bu yüzden 24 saat size deseni gösterir. Alkalinite günler içinde değişir, bu yüzden 7 ya da 30 gün çok daha fazlasını söyler.
:::

## Durum {#status}

Ölçümü aralıkta, kayıyor ya da dışında olduğunu gösteren renkli bir noktayla birlikte düz yazı olarak gösterir. İşe yarar bir gösterge aralığı olmayan bir parametre için kullanın.

## Priz {#outlet}

Bir Apex prizi için üç konumlu bir anahtardır: **Otomatik**, **Kapalı** ve **Açık**. Hangi prizi kontrol edeceğini siz seçersiniz.

- **Otomatik**, prizi normalde onu yöneten şeye geri verir. Bu bir program, bir kural ya da bağlı olduğu kontrolcü olabilir.
- **Kapalı** ve **Açık** elle yapılan geçersiz kılmalardır. Siz geri değiştirene kadar öyle kalırlar.

:::warning Elle yapılan geçersiz kılmaların etkisi geçmez
Kapalı, siz Otomatik'e geri alana kadar kapalı demektir. Akvaryumda çalışmak için ana pompayı kapattıysanız işiniz bitince onu Otomatik'e geri alın. Cora bunu sizin yerinize yapmaz.
:::

## ReefBeat {#reefbeat}

Bütün bir ekipman için tek bir kutucuktur. Tek bir parametre yerine ünitenin kendi özetini gösterir, örneğin bir ATO'nun durumu ve haznesi, bir dozaj pompasının kafaları ya da bir mat rulosunun kaç günü kaldığı. Hangi cihazı göstereceğini siz seçersiniz.

Hangi cihazların kutucuğu olabileceği neleri bağladığınıza bağlıdır. [Ekipmanınızı bağlama](/help/mobile-connections) sayfasına bakın.

## Dozaj pompası kutucukları {#doser-tiles}

Bir dozaj pompasının (Apex DŌS ya da ReefDose) kutucuğu her kafa için bir satır gösterir. Bir kafa adı hiçbir zaman okunabilir boyutun altına küçültülmez. Uzun bir kutucukta satır iki satır kaplar: ilkinde ad, ikincisinde kalan miktar, örneğin *40g* ve *2.8 L*. Kısa bir kutucukta ayrıntı satırı çıkarılır ve ad okunabilir kalır.

Neyin önce geleceğini **Kalanı şu şekilde göster** ile ayarlayın: **Gün** ya da **Mililitre (mL)**. Kendi adı olmayan bir ReefDose kafası, cihaz adı, ardından "kafa" ve numarasıyla gösterilir. Jecod dozaj pompası kutucuğu salt okunurdur ve günlük planı gösterir, çünkü Jecod şişede ne kadar kaldığını bildirmez.
