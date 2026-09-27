---
title: Panoyu okuma
description: Cora panosu nasıl okunur. Widget'lar, ölçümlerin yaşı, kaynaklar ve renklerin anlamı.
section: Cora Mobile
reviewed: 2026-09-09
order: 5
group: Your dashboard
---

Pano, **widget'lardan** oluşan bir ızgaradır. Her widget bir akvaryumla ilgili tek bir şeyi gösterir. Panoda ne olacağına tamamen siz karar verirsiniz. Ayrıntılar **[Panoyu düzenleme](/help/mobile-dashboard-editing)** sayfasında.

![Cora Mobile panosu](img/mobile-dashboard.webp "Göstergeler, sayılar, eğilimler ve kontroller tek ekranda.")

## Akvaryum başlığı

Her panonun üstünde şunlar var:

- **Akvaryumun adı** ve yanında küçük bir simge. Bu simge yalnızca **adı hızlıca değiştirmek** içindir
- **Besle**: besleme için akışı ve skimmer'ı durdurur, sonra her şeyi eski hâline getirir
- **Reef Buddy**: bu sabahki özeti açar
- **Paylaş**: panonun anlık görüntüsünü gönderir
- **Sağdaki kalem**: [akvaryum profilini](/help/mobile-tank-profile) açar

:::note Birbirine benzeyen üç düğme, üç farklı ekran
Adın yanındaki simge akvaryumun adını değiştirir. Sağdaki kalem akvaryum **profilini** açar. Panonun kendisini düzenlemek için ikisi de değil, widget'ların *altında*, panonun *en altındaki* **Gösterge panelini düzenle** düğmesi kullanılır.
:::

Birden fazla akvaryumunuz varsa aralarında geçmek için yana kaydırın.

## Reef Buddy kartı

Başlığın altındaki kart en son özeti kısaca gösterir: bir başlık, **Kararlılık** ve **Veri** puanları ve bulgu sayısı. Özetin tamamını açmak için karta dokunun. Kapatmak için **×**'e dokunun. Bir sonraki özetle yeni kart gelir.

## Parametre widget'ı nasıl okunur

**Ölçülen bir parametreyi** gösteren her widget'ta aynı üç bilgi hep aynı yerde durur. Priz, dozaj ünitesi ya da pompa gibi cihaz ve kontrol kutucuklarında ise tek bir ölçüm olmadığı için cihazın durumu görünür.

**Değer**, ölçümün kendisidir. Büyük harflerle ortada durur.

**Yaş**, değerin altında ya da yanında yazar: `şimdi`, `1 sa`, `2 g`. Bu, ekranın ne zaman yenilendiğini değil, ölçümün ne kadar önce alındığını gösterir. İki gündür değişmeyen bir sayının yanında `2 g` yazar. Bu da bir bilgidir.

**Kaynak rozeti**, yaşın yanındaki küçük işarettir. Sayının nereden geldiğini gösterir: prob, kontrol ünitesi, laboratuvar sonucu ya da test kitiyle sizin girdiğiniz ölçüm. Kaynağın açık adını ve yakın geçmişi görmek için widget'a dokunun.

:::note Yaş neden bu kadar önemli
Dört gün önce ölçülmüş kusursuz bir alkalinite değeri, bugünün alkalinite değeri değildir. Farkı bir bakışta görebilmeniz için her değerin yanında yaşı yazar.
:::

## Renkler

Cora rengi az kullanır ve her renk hep aynı anlama gelir:

| Renk | Anlamı |
|---|---|
| Yeşil | Değer bu parametrenin aralığının rahatça içinde |
| Turuncu | Sınıra yakın: **genellikle hâlâ aralığın içinde**, aralığın son onda birlik kısmında |
| Kırmızı | Sınır aşıldı, harekete geçmek gerekiyor |
| Gri | Değerlendirme yok: yakın zamanda ölçüm yok ya da karşılaştırılacak bir aralık yok |

:::note Turuncu genellikle "şimdilik iyi ama bir yöne gidiyor" demektir
Turuncu bir *uyarı payıdır*, sınırın aşıldığı anlamına gelmez. Aralığın içinde ama son %10'luk kısmında kalan bir ölçüm bilerek turuncu gösterilir. Böylece kayma sorun olduğu anda değil, harekete geçmek için hâlâ vakit varken görünür.

Bundan iki ayrıntı çıkar.

**Kendi belirlediğiniz aralık kesin bir sınır sayılır.** Değer bu sınırı geçerse widget doğrudan kırmızıya döner. Turuncu pay yoktur, çünkü o çizgiyi bilerek siz çektiniz. **Cora'nın önerdiği** aralık ise daha esnek bir referanstır. Sınırı geçen değer, sınırın ötesindeki ilk %10'da turuncu görünür, daha ötesinde kırmızıya döner.

**Tek yönlü sınırlar** (kirleticiler için üst sınır ya da besinler için alt sınır) yalnızca sınır tarafında değerlendirilir. Bu yüzden sıfırdaki bakır, ölçeğin en altında durduğu için turuncu olmaz, yeşil görünür.
:::

Turuncu ya da kırmızı çerçeveli widget ilgilenmeniz gereken widget'tır. Çerçeve yalnızca sayının değil, widget'ın tamamının etrafındadır. Böylece ekranı kaydırırken de gözünüze çarpar.

## Widget'ların altında

![Panonun alt kısmı](img/mobile-dashboard-foot.webp "Gösterge panelini düzenle, Parametreleri Kaydet ve dört kayıt alanının kısayolları.")

Panonun en altında şunlar var:

- **Gösterge panelini düzenle**: [pano düzenleyiciyi](/help/mobile-dashboard-editing) açar
- **Parametreleri Kaydet**: test kiti sonuçlarını elle girersiniz
- **Günlük · Uyarılar · Bakım · Canlılar**: bu akvaryumun ilgili bölümlerine kısayollar

Bunların üstündeki satır panonun en son ne zaman güncellendiğini ve hangi kaynaklardan veri aldığını gösterir.

## Ayrıntılara geçme

Ayrıntıları açmak için bir widget'a dokunun. Tüm geçmişi grafik olarak, değeri bildiren bütün kaynakları ve şu an geçerli olan eşikleri görürsünüz. Buradan elle yeni ölçüm girebilir, aralığı değiştirebilir ya da daha eskiye bakabilirsiniz.

## Widget'ta değer yoksa

Widget, değer gelir gelmez onu gösterir. Widget boşsa nedeni genellikle şunlardan biridir:

- Cihaz çevrimdışı. **Cihazlar** sekmesine bakın
- Parametrenin henüz bir kaynağı yok. Değeri elle girin ya da bu değeri ölçen ekipmanı bağlayın
- Parametre için henüz hiç ölçüm gelmemiş ya da girilmemiş

Eski bir ölçüm, grafiğin zaman aralığından daha eski diye widget'tan kaybolmaz. Yaşıyla birlikte widget'ta kalır. Böylece eski bir değer eksik değil, eski olarak görünür.

Bunların dışındaki durumlar için **[Sorun giderme](/help/troubleshooting)** sayfasına bakın.
