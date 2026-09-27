---
title: Widget referansı
description: Cora'daki her widget türü (değer, gösterge, grafik, durum, priz ve cihaz kutuları) ve her birini ne zaman kullanmalı.
section: Cora Mobile
reviewed: 2026-09-17
order: 7
group: Your dashboard
---

Bir widget, panonuzda bir şey gösteren bir kutudur. Bu sayfa her türü ve neyi yapılandırabileceğinizi kapsar.

Bunları **[pano düzenleyicisinde](/help/mobile-dashboard-editing)** ekleyin ve düzenleyin; ayarlarını açmak için orada bir widget'a dokunun.

![Bir widget'ı yapılandırma](img/mobile-widget-config.webp "Tür, parametre, ardından genişlik ve yükseklik.")

## Dokuz tür

| Tür | Gösterdiği |
|---|---|
| **Değer** | Geçerli okuma, birimi, yaşı ve kaynağı |
| **Gösterge** | Aralığınızın bantlandığı bir yay ve değerde bir topuz |
| **Grafik** | Seçtiğiniz bir pencere boyunca bir eğilim |
| **Durum** | Metin olarak bir durum: çalışıyor, boşta, kapalı |
| **Priz** | Üç yönlü bir kontrol: Otomatik, Kapalı, Açık |
| **ReefBeat** | Kendi özetiyle bir Red Sea birimi |
| **Apex modülü** | Bir Trident veya DŌS gibi takılı bir Apex modülü |
| **Jecod** | Modu ve yoğunluğuyla bir Jecod pompası |
| **Maxspect** *(beta)* | İki motoruyla bir gyre |

Son dört tür **cihaz** kutularıdır: bir parametreye değil bir ekipman parçasına bağlıdırlar ve her biri o birimin bildirdiği her neyse onu gösterir.

## Boyutlandırma

**Genişlik** ve **Yükseklik**, her biri **1×** veya **2×** olabilir. Bir grafik hiçbir zaman bir hücre genişliğinde olmaz.

## Değer

Düz sayı. Geçerli okuma, birimi, ne kadar eski olduğu ve nereden geldiği.

Eğilimle değil sayısal olarak kontrol ettiğiniz parametreler için kullanın: kalsiyum, magnezyum, nitrat.

**Ayarlar:** etiket, kaynak, boyut.

## Gösterge

Hedef aralığınızın bantlandığı bir yay ve geçerli değerde bir topuz. Topuzun rengi nerede durduğunuzu söyler: bant içinde, kayıyor, veya dışında.

Aktif olarak yönettiğiniz parametreler için kullanın: alkalinite, pH, tuzluluk, sıcaklık.

**Ayarlar:** etiket, kaynak, aralık (burada geçersiz kılmadıkça akvaryum hedeflerinizden miras alınır), boyut.

:::note Göstergeleri iki sütun veya daha fazlasında boyutlandırın
Tek bir sütunda yay bir bakışta okunamayacak kadar küçüktür; alan sınırlıysa bunun yerine bir **değer** widget'ı kullanın.
:::

## Grafik

Seçtiğiniz bir pencere boyunca bir sparkline, yüksek ve alçak işaretlenmiş ve geçerli değer belirtilmiş.

Test ettiğiniz bir parametre için (Trident'la veya bir test kitiyle), çizgi gerçek testlerinizi birleştirir. Pencere yalnızca bir test içeriyorsa, çizgi ondan öncekinden gelir ve yüksek veya alçak işaretlenmez. Pencerede hiç test yoksa, veya tek bir testi birleştirecek daha önceki bir şey yoksa, kutu bir çizgi yerine **Toplanıyor…** gösterir.

Hareket eden her şey için kullanın: gün boyunca pH, bir sıcak dalgası boyunca sıcaklık, dozlar arasında alkalinite.

**Ayarlar:** etiket, kaynak, **zaman penceresi** (1 saat, 6 saat, 24 saat, 7 gün, 30 gün, 1 yıl), boyut.

Bir eğilim her zaman **en az iki hücre genişliğindedir**; bir hücreye sıkıştırılmış bir sparkline size hiçbir şey söylemez, bu yüzden düzenleyici böyle bir şey yapmaz.

:::note Pencereyi ritme uyacak şekilde seçin
pH günlük bir döngüde salınır, bu yüzden 24 saat size şekli gösterir. Alkalinite günler içinde hareket eder, bu yüzden 7 veya 30, 24'ün asla söyleyemeyeceğini söyler.
:::

## Durum

Bir sayı değil metin, bir durum olan şeyler için. Çalışıyor, boşta, açık, kapalı, besleniyor.

**Ayarlar:** etiket, kaynak, boyut.

## Priz

Bir priz için üç yönlü bir anahtar: **Otomatik**, **Kapalı**, **Açık**.

- **Otomatik**, prizi normalde onu çalıştıran şeye geri verir: bir zamanlama, bir kural, veya ait olduğu kontrolcü.
- **Kapalı** ve **Açık**, siz geri değiştirene kadar kalan elle yapılan geçersiz kılmalardır.

**Ayarlar:** etiket, hangi priz, boyut.

:::warning Elle yapılan bir geçersiz kılmanın süresi dolmaz
Kapalı, siz onu Otomatik'e geri ayarlayana kadar kapalı anlamına gelir. Akvaryumda çalışmak için ana pompayı kapatırsanız, bitirdiğinizde onu Otomatik'e geri koyun; Cora bunu sizin için yapmaz.
:::

## ReefBeat

Bütün bir ekipman parçası için tek bir kutu, tek bir parametre yerine kendi özetini gösterir: bir ATO'nun durumu ve rezervuarı, bir dozaj biriminin kafaları, bir mat rulosunun kalan günleri.

Hangi cihazların bir kutu sunduğu, neyi bağladığınıza bağlıdır. Bkz. **[Ekipmanınızı bağlama](/help/mobile-connections)**.

**Ayarlar:** etiket, hangi cihaz, boyut.

## Bir parametre widget'ı ne gösterir

Ölçülen bir parametreyle desteklenen bir widget'ta (Değer, Gösterge, Grafik ve Durum), üç şey her zaman mevcuttur. Priz ve cihaz kutuları bunun yerine kendi durumlarını gösterir, çünkü arkalarında tek bir okuma yoktur:

- **Değer**, büyük
- **Yaş** (`şimdi`, `1s`, `2g`): okumanın ne kadar eski olduğu, ekranın en son ne zaman yenilendiği değil
- **Kaynak**: sayının nereden geldiğini söyleyen küçük bir rozet

Tam geçmişini, onu bildiren her kaynağı ve geçerli eşikleri açmak için herhangi bir widget'a dokunun.

## Boyutlar

Widget'lar bir veya iki hücre genişliğinde ve bir veya iki hücre yüksekliğindedir, her zaman en az iki genişliğinde olan bir **eğilim** hariç. Üç sütunlu bir panoda iki genişliğinde bir gösterge, satırın üçte ikisini kaplar; bu genellikle en önemli parametreniz için doğru şekildir.
