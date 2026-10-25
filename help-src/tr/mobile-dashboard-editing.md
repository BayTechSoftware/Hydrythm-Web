---
title: Panonuzu düzenleme
description: Telefon panonuzda widget ekleyin, taşıyın, boyutlandırın ve kaldırın, sütun sayısını ayarlayın ve bir Cora Max panosunu telefonunuzdan düzenleyin.
section: Cora Mobile
reviewed: 2026-10-18
order: 8
group: Your dashboard
twin: max-dashboard-editing
---

Pano düzenleyici, bir akvaryumun panosunda hangi widget'ların görüneceğini ve nasıl yerleşeceğini belirler. Her akvaryumun kendi düzeni vardır ve bu düzen, giriş yaptığınız her telefona hesabınızla birlikte gelir.

## Düzenleyiciyi açma {#opening-the-editor}

Panoda aşağı kaydırın ve widget'ların hemen altındaki **Panoyu düzenle**'ye dokunun. Düzenleyici **Panoyu Düzenle** başlığıyla ve **Taşımak için bir kutucuğa uzun basın. Yapılandırmak için dokunun.** ipucuyla açılır.

:::note Akvaryum başlığındaki kalem başka bir şeyi açar
Kalem, hacim, canlılar, dozaj, aydınlatma ve akış bilgilerinin olduğu akvaryum profili **Akvaryumu düzenle**'yi açar. Bu, [Akvaryum profiliniz](/help/mobile-tank-profile) sayfasında anlatılır.
:::

![Cora Mobile'da Panoyu Düzenle ekranı](img/mobile-edit.webp "Üstte sütunlar, ardından adı ve türüyle her kutucuk. Kaldırmak için kırmızı çarpıya dokunun.")

## Sütun sayısını ayarlama {#setting-the-column-count}

Düzenleyicinin üstünde **SÜTUNLAR**'ın yanından **2**, **3** ya da **4**'ü seçin. Widget ekledikçe ızgara aşağı doğru uzar ve pano kaydırılır.

| Sütun | Ne zaman kullanılır |
|---|---|
| 2 | Az sayıda parametre izliyorsanız ve büyük kutucuklar istiyorsanız |
| 3 | Varsayılan. Çoğu akvaryum için uygun |
| 4 | Sık bir görünüm istiyorsanız ya da telefonunuz büyükse |

## Widget ekleme {#adding-a-widget}

1. Izgaranın altındaki **Kutucuk ekle**'ye ya da boş bir hücreye dokunun.
2. **Bir kutucuk ekle** içinde türünü seçin. **Metrik**, bir parametre için değer, gösterge, grafik ya da durum gösterir. **Priz** bir Apex prizini kontrol eder. Diğer satırlar **ReefBeat**, **Trident**, **DŌS** ya da **Jecod** gibi ekipmanlar içindir. Bunların çoğu yalnızca akvaryumda o ekipman varsa görünür. **Işık**, **Dalga pompası** ve **Pompa**, markası ne olursa olsun akvaryumdaki tüm ışıkları, dalga pompalarını ve pompaları listeler; her biri yalnızca akvaryumda böyle bir cihaz varsa görünür. **ReefBeat** ve **Jecod**, ReefDose ya da bir Jecod dozaj pompası gibi diğer cihazlarını korur.
3. Parametreyi, prizi ya da cihazı seçin.
4. Bir metrik için türü seçin. [Widget rehberi](/help/mobile-widgets) her birini anlatır.

Yalnızca akvaryumda bulunan parametreleri görürsünüz. Kaynağı olmayan bir parametre, onu bildiren ekipmanı bağladığınızda ya da elle bir ölçüm girdiğinizde görünür.

Izgara en fazla 20 satır alır. Dolduğunda Cora **Pano dolu: önce bir kutucuk kaldırın.** der. Bir grafik yan yana iki boş hücre ister.


Bir cihazı akvaryumdan çıkardığınızda kutucukları panodan kendiliğinden kalkar, telefonunuzda ve o akvaryumdaki her Cora Max'te. Cihazı gitmiş bir kutucuk **Bu cihaz artık bu akvaryumda değil** yazar ve hiçbir şey açmaz.

## Widget'ları yerleştirme {#arranging-widgets}

- Bir widget'ı taşımak için basılı tutun ve sürükleyin. Diğerleri onun çevresinde yer değiştirir.
- Bir widget'ı kaldırmak için köşesindeki kırmızı çarpıya ya da widget'a, ardından **Kaldır**'a dokunun.
- Bir widget'ın ayarlarını değiştirmek için ona dokunun.

## Widget ayarları {#widget-settings}

Ayarlarını açmak için düzenleyicide bir widget'a dokunun. Widget'a göre şunları ayarlayabilirsiniz:

| Ayar | Nerede geçerli |
|---|---|
| **Tür** | Metrik widget'ları: Değer, Gösterge, Grafik ya da Durum |
| **Parametre** | Metrik widget'ları: hangi parametreyi gösterdiği |
| Priz ya da cihaz | Priz ve ekipman kutucukları: hangisini gösterdiği |
| **Kalanı şu şekilde göster** | Dozaj pompası kutucukları: **Gün** ya da **Mililitre (mL)** |
| **Genişlik** | Her widget: **1×** ya da **2×**. Grafik her zaman en az 2 genişliktedir |
| **Yükseklik** | Her widget: **1×** ya da **2×** |
| **Zaman aralığı** | Grafik: 1 sa, 6 sa, 24 sa, 7 g, 30 g ya da 1 y |

Ayarları saklamak için **Bitti**'ye, widget'ı çıkarmak için **Kaldır**'a dokunun.

Bir widget'ın kendine ait etiketi, kaynağı ya da aralığı yoktur. Uyarı aralığı akvaryumun uyarı eşiklerinden gelir: panoda widget'a uzun basın ya da [Uyarılar ve eşikler](/help/mobile-alerts) sayfasına bakın. Bir parametrenin hangi kaynağı izleyeceği her akvaryum için [Parametre Eşlemesi](/help/mobile-probes) içinde ayarlanır.

## Kaydetme {#saving}

Düzeni saklamak için **Kaydet**'e dokunun. Değişikliklerinizden vazgeçmek için kapatma simgesine dokunun. Bir şeyi değiştirdiyseniz Cora **Değişiklikler atılsın mı?** diye sorar. **At**'a ya da geri dönmek için **Düzenlemeye devam et**'e dokunun.

Telefon düzenleyicisinde geri alma ve kayıtlı tasarım yoktur. Ölçümler, geçmiş ve günlük kayıtları düzenden ayrı saklanır, bu yüzden bir panoyu düzenlemek onları asla kaybettirmez.

## Cora Max panosunu düzenleme {#editing-the-cora-max-dashboard}

Cora Max panosunu ayrı olarak, akvaryumun kartındaki **Cihazlar →** Cora Max'iniz **→ Pano düzeni** yolundan düzenlersiniz. Kaymayan sabit bir ızgara kullanır ve siz **Kaydet ve Yayınla**'ya dokunana kadar Cora Max'e hiçbir şey ulaşmaz.

Bu düzenleyicide telefon panosunda olmayan üç ek özellik vardır:

- **Panolarım**, hesabınızda en fazla 30 kayıtlı tasarım tutar. Hesaptaki her Cora Max bunlardan birini yükleyebilir. Hedefin dolduramayacağı kutucuklar, yüklemeden önce **Geride kalanlar:** altında listelenir.
- **Şablonlar**, **Pano şablonları**'nı açar: **Genel bakış**, **Ekipman** ve **Parametreler**. Her planda açıktır ve yapay zeka kullanmaz.
- **Yapay zeka ile tasarla**, ücretli bir planda ya da deneme süresinde, akvaryumun bildirdiği ve bağladığı şeylerden komple bir düzen önerir. Her akvaryum için günde 5 tasarım yapabilirsiniz.

Her birinin nasıl çalıştığı [Cora Max panosunu düzenleme](/help/max-dashboard-editing) sayfasında.
