---
title: Bir parametreyi inceleme
description: Bir parametrenin tüm geçmişini görmek, kaynakları ve parametreleri karşılaştırmak, hatalı bir ölçümü hariç tutmak ve prob bakımını kaydetmek için bir widget'a dokunun.
section: Cora Mobile
reviewed: 2026-10-13
order: 7
group: Your dashboard
---

Widget size bir sayı gösterir. O sayının arkasındaki hikayeyi görmek için ona dokunun.

İki yoldan girebilirsiniz. Panoda bir widget'a dokunun ya da widget'ların altındaki düğme satırında **Parametre geçmişi**'ne dokunup bir parametre seçin. **Parametre geçmişi**, panoda widget'ı olmasa bile verisi olan her parametreyi listeler.

## Neler görürsünüz {#what-you-get}

![Bir parametreyi inceleme](img/mobile-metric-detail.webp "Üstte açılır listeler, ardından uyarı bandınız gölgelenmiş grafik.")

- Bir geçmiş grafiği. Üstündeki satır neyi göstereceğini belirler. **Parametre**, verisi olan başka herhangi bir parametreye geçer ve zaman aralığınızı korur. **Zaman aralığı** 1 sa'ten başlayıp 6 sa, 12 sa, 24 sa, 3 g, 7 g, 15 g, 30 g, 90 g, 180 g ve 360 g üzerinden Tümü'ne kadar gider. **Kaynak**, **Tüm kaynaklar** ile başlar ve bu akvaryumda bu parametreyi bildiren *Apex*, *Cora*, *Red Sea* ya da *Manuel* gibi kaynakları listeler. Yalnızca onun ölçümlerini görmek için birini seçin.
- Aynı satırın sonundaki **Karşılaştır**, grafiğe ikinci bir parametre çizer, örneğin alkaliniteyle kalsiyumu ya da pH ile sıcaklığı. Düğme bu durumda diğer parametrenin adını ve **ile** yazısını gösterir (örneğin *Kalsiyum ile*). İkinci çizgiyi kaldırmak için ona yeniden dokunun.
- Ekrandaki zaman aralığı için **En son**, **Min**, **Ort** ve **Maks** değerlerini içeren bir satır.
- Üst çubukta simgeler: **Ölçümler** ham ölçüm listesini açar, **Prob bakımını kaydet** bir kalibrasyonu ya da temizliği kaydeder. Alkalinite, kalsiyum ve magnezyum için ayrıca [akvaryum profilinizdeki](/help/mobile-tank-profile) akvaryum hacmini ve [Dozaj](/help/mobile-dosing) sayfasındaki yoğunlukları kullanan dozaj hesaplayıcısı vardır.

Ekran her zaman 24 sa ve **Tüm kaynaklar** ile açılır. Son seferki seçiminizi hatırlamaz.

## Grafiği okuma {#reading-the-chart}

- Yeşil bant uyarı aralığınızdır, böylece her ölçümü ona göre görürsünüz. Aralığı değiştirmek için panoda widget'a uzun basın. Ayrıntılar [Uyarılar ve eşikler](/help/mobile-alerts) sayfasında.
- Kesikli bir çizgi kaydedilen bir dozu işaretler, böylece bir değişimi dozladığınız şeyle yan yana getirebilirsiniz.
- **30g yüksek** ve **30g düşük**, son 30 günün uç değerlerini gösteren kesikli çizgilerdir.
- İçi boş bir nokta, hariç tuttuğunuz bir ölçümdür.
- **Karşılaştır** açıkken ikinci parametre sağ taraftaki ekseni kullanır.

## Zaman aralığı seçme {#choosing-a-range}

Parametrenin nasıl değiştiğine uyan zaman aralığını seçin.

| Parametre | İşe yarayan aralık |
|---|---|
| pH | 24 saat, çünkü günlük bir döngüyle iner çıkar |
| Sıcaklık | 24 saat ya da 7 gün |
| Alkalinite | 7 ya da 30 gün |
| Eser elementler | 30 gün ya da bir yıl |

:::note Düz çizgi mi? Ölçümün ne kadar eski olduğuna bakın
Hiç kıpırdamayan bir çizgi parametrenin kararlı olduğu anlamına gelebilir. Kaynağın bildirmeyi bıraktığı anlamına da gelebilir. Widget'ta değerin yanındaki yaş hangisi olduğunu söyler.
:::

## Kaynakları karşılaştırma {#comparing-sources}

Bir parametreyi birden fazla kaynak bildirdiğinde Cora onları ayrı tutar ve ortalamalarını almaz. Her birine bakmak için **Kaynak** açılır listesini kullanın. Bir probu bir test kitiyle karşılaştırmanın en hızlı yolu budur.

Panoda en yenisi görünür. Canlı bir değerin yerini, hangi kaynaktan olursa olsun, yalnızca daha geç bir ölçüm zamanı olan bir ölçüm alır. Daha eski bir ölçüm geçmişe gider ve widget'taki değerin üzerine yazmaz. **Parametre Eşlemesi**'nde bir kaynağı sabitlediyseniz Cora onun yerine o kaynağı izler.

Bir prob ile elle kaydettiğiniz testler hep aynı miktarda farklı kalıyorsa prob genellikle kalibrasyon ister.

Bir [ICP sonucu](/help/mobile-icp-health) işe yarar bir üçüncü görüştür, ama soruyu kesin olarak çözmez. Laboratuvarlar birbirinden farklıdır ve numunenin nasıl alındığı, saklandığı ve gönderildiği sonucu değiştirir. Tek bir ICP'yi kanıt olarak değerlendirin. Birbirini tutan iki test, tek bir testten çok daha değerlidir.

## Bir ölçümün hangi kaynağı izleyeceğini seçme {#choosing-which-source-a-widget-trusts}

Kaynak widget başına değil, akvaryum ve parametre başına ayarlanır. **Ayarlar**'a gidin, akvaryuma, **Parametre Eşlemesi**'ne, ardından **Kaynaklar** sekmesine dokunun. Bir prob ya da **Otomatik (en yeni ölçüm kazanır)** seçin. Seçim, akvaryum için o parametrenin her yerinde geçerli olur. Ayrıntılar [Parametre Eşlemesi](/help/mobile-probes) sayfasında.

## Hatalı bir ölçümü hariç tutma {#excluding-a-bad-reading}

Belki bir prob sıçradı, bir testi yanlış okudunuz ya da numuneyi su değişiminin ortasında aldınız. Tek bir yanlış ölçüm grafiği, ortalamaları ve onlardan hesaplanan her şeyi bozar.

![Cora Mobile'da pH ölçüm listesi](img/mobile-readings.webp "Çizginin arkasındaki her ölçüm, zamanı ve kaynağıyla. Hariç tutmak için birine dokunun.")

Üst çubukta **Ölçümler**'e, ardından bir ölçüme dokunun. Cora **Bu ölçüm hariç tutulsun mu?** diye sorar ve ölçümün kaydınızda kalacağını ama ortalamalara, eğilimlere, içgörülere ve asistana sayılmayacağını açıklar. **Hariç Tut**'a dokunun. Hiçbir şey silinmez ve ölçümü aynı yoldan geri getirebilirsiniz.

90 günden eski ölçümler hariç tutulamaz ya da geri getirilemez.

:::warning Hoşa gitmeyen ölçümleri değil, yanlış ölçümleri hariç tutun
Yalnızca geçersiz olduğunu bildiğiniz bir ölçümü hariç tutun. Bir ölçümü beğenmiyor ama onda yanlış bir şey bulamıyorsanız o gerçek veridir. Onu çıkarmak sonraki her karşılaştırmayı daha az dürüst yapar.
:::

## Prob bakımını kaydetme {#recording-probe-care}

**Prob bakımını kaydet**'e (üst çubuktaki sensör simgesi) dokunun ve ne yaptığınızı seçin: kalibrasyon, temizlik, değişim, taşıma ya da karşılaştırma. Cora tarihi o kaynağa işler, böylece yeni bir kalibrasyon kayma sanılmaz. İleride prob bir şeyle uyuşmazsa en son ne zaman bakım gördüğünü görebilirsiniz. Ayrıntılar [Parametre Eşlemesi](/help/mobile-probes) sayfasında.

## Ölçümü elle kaydetme {#logging-a-reading-by-hand}

Ölçümleri bu ekrandan değil, panodan kaydedersiniz. Widget'ların altındaki **Parametreleri Kaydet**'e dokunun ve test kitinizin gösterdiğini girin. Liste gruplanmıştır ve **İz Elementler** grubu iyot, demir ve bakırı µg/L, potasyumu mg/L cinsinden kapsar. Elle kaydedilen ölçümler diğerleri kadar sayılır. Kendi kaynakları ve zamanları olur, grafikte görünürler ve Reef Buddy'yi beslerler. Cora'nın ekipmanınızı karşılaştırdığı da onlardır.

:::note Cora tuhaf görünen girişleri iki kez kontrol eder
Bir değer akvaryumun olduğu yerden çok uzaksa Cora kaydetmeden önce onaylamanızı ister. Bu, yanlış yere konmuş bir ondalık ayırıcıyı ya da yanlış parametreye girilmiş bir ölçümü yakalar. Onayladığınızda ölçüm her zamanki gibi kaydedilir.
:::
