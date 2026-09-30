---
title: Widget rehberi
description: Cora'daki bütün widget türleri (değer, gösterge, grafik, durum, priz ve cihaz kutucukları) ve hangisini ne zaman kullanacağınız.
section: Cora Mobile
reviewed: 2026-09-30
order: 7
group: Your dashboard
---

Widget, panonuzda tek bir şeyi gösteren kutucuktur. Bu sayfada bütün widget türlerini ve her birinde neleri ayarlayabileceğinizi bulabilirsiniz.

Widget'ları **[pano düzenleyicide](/help/mobile-dashboard-editing)** ekleyip yerleştirirsiniz. Bir widget'ın ayarlarını açmak için düzenleyicide üzerine dokunun.

![Widget ayarları](img/mobile-widget-config.webp "Tür, parametre, ardından genişlik ve yükseklik.")

## On bir tür

| Tür | Ne gösterir |
|---|---|
| **Değer** | Güncel ölçüm, birimi, yaşı ve kaynağı |
| **Gösterge** | Aralığınızın işaretli olduğu yay ve değeri gösteren düğme |
| **Grafik** | Seçtiğiniz zaman aralığındaki eğilim |
| **Durum** | Yazıyla durum: çalışıyor, boşta, kapalı |
| **Priz** | Üç konumlu anahtar: Otomatik, Kapalı, Açık |
| **ReefBeat** | Tek bir Red Sea ünitesi ve kendi özeti |
| **Apex modülü** | Trident ya da DŌS gibi takılı tek bir Apex modülü |
| **Jecod** | Tek bir Jecod pompası, modu ve yoğunluğuyla |
| **Maxspect** *(beta)* | Tek bir gyre, iki motoruyla birlikte |
| **GHL** *(beta)* | Tek bir ProfiLux ya da Mitras kontrol cihazı, kendi özetiyle |
| **HYDROS** *(beta)* | Tek bir HYDROS kontrol cihazı, kendi özetiyle |

Son altısı **cihaz** kutucuklarıdır. Parametreye değil, ekipmana bağlıdırlar. Her biri o ünitenin bildirdiği bilgileri gösterir.

## Boyut

**Genişlik** ve **Yükseklik** için **1×** ya da **2×** seçebilirsiniz. Yani widget'lar bir ya da iki hücre genişliğinde, bir ya da iki hücre yüksekliğindedir. Grafik hiçbir zaman tek hücre genişliğinde olmaz. Üç sütunlu panoda iki hücrelik gösterge satırın üçte ikisini kaplar. En önemli parametreniz için genellikle en uygun boyut budur.

## Değer

Yalnızca sayı. Güncel ölçüm, birimi, ne kadar eski olduğu ve nereden geldiği.

Eğilimine değil, sayısına baktığınız parametreler için kullanın: kalsiyum, magnezyum, nitrat.

Ayarlarda etiketi, kaynağı ve boyutu seçersiniz.

## Gösterge

Hedef aralığınızın işaretli olduğu yay ve güncel değerde duran düğme. Düğmenin rengi durumu gösterir: aralığın içinde, sınıra kayıyor ya da aralığın dışında.

Sürekli yönettiğiniz parametreler için kullanın: alkalinite, pH, tuzluluk, sıcaklık.

Ayarlarda etiketi, kaynağı, aralığı ve boyutu seçersiniz. Aralığı burada değiştirmezseniz akvaryumun hedefleri kullanılır.

:::note Göstergeyi en az iki sütun genişliğinde kullanın
Tek sütunda yay bir bakışta okunamayacak kadar küçük kalır. Yeriniz darsa **Değer** widget'ını kullanın.
:::

## Grafik

Seçtiğiniz zaman aralığı boyunca küçük çizgi grafik. En yüksek ve en düşük değer işaretlenir, güncel değer ayrıca yazılır.

Test ettiğiniz parametrelerde (Trident ya da test kitiyle) çizgi gerçek testlerinizi birleştirir. Aralıkta yalnızca bir test varsa çizgi bir önceki testten gelir ve en yüksek ya da en düşük değer işaretlenmez. Aralıkta hiç test yoksa ya da tek testi bağlayacak daha eski bir test yoksa kutucukta çizgi yerine **Toplanıyor…** yazar.

Değişen her şey için kullanın: gün içinde pH, sıcak havalarda sıcaklık, dozlar arasında alkalinite.

Ayarlarda etiketi, kaynağı, **zaman aralığını** (1 saat, 6 saat, 24 saat, 7 gün, 30 gün, 1 yıl) ve boyutu seçersiniz.

Eğilim widget'ı her zaman **en az iki hücre genişliğindedir**. Tek hücreye sıkışan çizgi grafik hiçbir şey anlatmaz. Bu yüzden düzenleyici buna izin vermez.

:::note Zaman aralığını parametrenin ritmine göre seçin
pH gün içinde iner çıkar. 24 saat bu dalgayı gösterir. Alkalinite günler içinde değişir. 7 ya da 30 günlük aralık, 24 saatin gösteremeyeceğini gösterir.
:::

## Durum

Sayı yerine yazı. Durumu olan şeyler için: çalışıyor, boşta, açık, kapalı, besleniyor.

Ayarlarda etiketi, kaynağı ve boyutu seçersiniz.

## Priz

Priz için üç konumlu anahtar: **Otomatik**, **Kapalı**, **Açık**.

- **Otomatik**, prizin kontrolünü normalde onu yöneten şeye geri verir: bir program, bir kural ya da prizin bağlı olduğu kontrol ünitesi.
- **Kapalı** ve **Açık**, elle yapılan ayarlardır. Siz değiştirene kadar öyle kalırlar.

Ayarlarda etiketi, prizi ve boyutu seçersiniz.

:::warning Elle yapılan ayarın süresi dolmaz
Kapalı, siz Otomatik'e geri alana kadar kapalı demektir. Akvaryumda çalışmak için ana pompayı kapattıysanız işiniz bitince Otomatik'e geri alın. Cora bunu sizin yerinize yapmaz.
:::

## ReefBeat

Bütün ekipman için tek kutucuk. Tek parametre yerine cihazın kendi özetini gösterir: ATO'nun durumu ve rezervuarı, dozaj ünitesinin kafaları, mat rulosunun kalan günleri.

Hangi cihazların kutucuğu olduğu, neleri bağladığınıza bağlıdır. Ayrıntılar **[Ekipmanınızı bağlama](/help/mobile-connections)** sayfasında.

Ayarlarda etiketi, cihazı ve boyutu seçersiniz.

## Parametre widget'ında neler görünür

Ölçülen bir parametreyi gösteren widget'larda (Değer, Gösterge, Grafik ve Durum) şu üç bilgi hep bulunur. Priz ve cihaz kutucuklarının arkasında tek bir ölçüm olmadığı için bunlar kendi durumlarını gösterir:

- **Değer**, büyük yazıyla
- **Yaş** (`şimdi`, `1 sa`, `2 g`): ekranın ne zaman yenilendiği değil, ölçümün ne kadar eski olduğu
- **Kaynak**: sayının nereden geldiğini gösteren küçük rozet

Tüm geçmişi, değeri bildiren bütün kaynakları ve geçerli eşikleri görmek için bir widget'a dokunun.
