---
title: Panonuzu okuma
description: Cora panosu nasıl okunur: widget'lar, ölçüm yaşı ve kaynaklardan renklerin anlamına ve gelip giden kartlara kadar.
section: Cora Mobile
reviewed: 2026-10-13
order: 6
group: Your dashboard
---

Pano, bir akvaryum için **widget'lardan** oluşan bir ızgaradır. Her widget tek bir şeyi gösterir. Neyin yer alacağına [Panonuzu düzenleme](/help/mobile-dashboard-editing) sayfasında anlatıldığı gibi siz karar verirsiniz.

![Bir Cora Mobile panosu](img/mobile-dashboard.webp "Akvaryum başlığı ve Reef Buddy kartı, ardından göstergeler, değerler, grafikler ve cihaz kutucukları.")

## Akvaryum başlığı {#the-tank-header}

Her pano şunlarla başlar:

- Yanında küçük bir simgeyle akvaryumun adı. Akvaryumun adını değiştirmek için ada dokunun. Yaptığı tek şey budur.
- **Besle**, yalnızca Neptune Apex'i olan bir akvaryumda. Apex'inizin **Besleme A**'dan **Besleme D**'ye kadar döngüleriyle **Besleme modu**'nu açar. Neyin duracağına ve ne zaman geri döneceğine, orada nasıl ayarladıysanız öyle Apex'iniz karar verir. Bir döngü çalışırken düğme hangisi olduğunu gösterir, örneğin **Besleme A**. Erken bitirmek için ona dokunun ve **Beslemeyi iptal et**'i seçin. Evden uzaktayken akvaryumdaki bir Cora Max komutu sizin için gönderir.
- En son **Reef Buddy** özetini açan gazete simgesi.
- Akvaryumun anlık görüntüsünü hazırlayan paylaş simgesi. [Akvaryumunuzu paylaşın](/help/mobile-sharing) sayfasına bakın.
- Bu akvaryum için **Birimler**'i açan cetvel. [Akvaryum profiliniz](/help/mobile-tank-profile#units) sayfasına bakın.
- [Akvaryum profilini](/help/mobile-tank-profile) açan sağdaki kalem.

:::note Birbirine benzeyen üç kontrol
Akvaryum adı akvaryumun adını değiştirir. Sağdaki kalem akvaryum **profilini** açar. Panonun kendisini düzenlemek için widget'ların hemen altındaki **Panoyu düzenle**'ye dokunun.
:::

Birden fazla akvaryumunuz varsa aralarında geçmek için yana kaydırın. [Akvaryumlarınızı yönetme](/help/mobile-tanks) sayfasına bakın.

## Reef Buddy kartı {#the-reef-buddy-card}

Widget'ların üstündeki bir kart en son özeti özetler. Başlığı, Cora'nın yeterli verisi olduğunda 100 üzerinden bir puanı, hangi tarihe ait olduğunu ve kaç içgörü ve kayan ölçüm olduğunu gösterir. Tam özeti açmak için ona dokunun ya da **×** ile kapatın. Bir sonraki özetle yeni bir kart görünür. Ayrıntılar [Reef Buddy](/help/mobile-reef-buddy) sayfasında.

## Parametre widget'ı nasıl okunur {#how-to-read-a-parameter-widget}

**Ölçülen bir parametreyi** gösteren widget her zaman aynı üç şeyi aynı yerlerde gösterir. Priz, dozaj ünitesi ya da pompa gibi cihaz ve kontrol kutucukları ise kendi durumlarını gösterir, çünkü arkalarında tek bir ölçüm yoktur.

Değer, ölçümün kendisidir, büyük ve ortadadır.

Yaş, onun altında ya da yanında `şimdi`, `1 sa` ya da `2 g` olarak durur. Ekranın en son ne zaman yenilendiği değil, kaynağın o değeri en son ne kadar önce doğruladığıdır. Bir prob için bu, cihazının en son ne zaman bağlandığıdır, bu yüzden çalışan bir probdan gelen sabit bir ölçüm, sayı değişmese bile taze kalır. Bir test kiti ya da ICP sonucu için testi yaptığınız zamandır. Bir probda sürekli büyüyen bir yaş, cihazının bildirmeyi bıraktığı anlamına gelir.

Kaynak rozeti, yaşın yanındaki küçük işarettir. Sayının nereden geldiğini gösterir: bir prob, bir kontrolcü, bir laboratuvar sonucu ya da test kitiyle siz. Kaynağın açık adını ve yakın geçmişini görmek için widget'a dokunun.

:::note Yaş neden önemli
Dört gün önceki kusursuz bir alkalinite ölçümü bugünkü alkaliniteniz değildir. Farkı hızlıca görebilmeniz için her değer yaşını gösterir.
:::

## Renkler {#colours}

Cora rengi az kullanır ve her renk her zaman aynı anlama gelir:

| Renk | Anlamı |
|---|---|
| Yeşil | Bu parametrenin aralığının rahatça içinde |
| Turuncu | Bir sınıra yakın. **Genellikle hâlâ aralığın içinde**, son onda birlik kısmında |
| Kırmızı | Sınırı geçti ve harekete geçmeye değer |
| Gri | Değerlendirme yok. Yakın tarihli bir ölçüm ya da onu değerlendirecek kullanılabilir bir aralık yok |

:::note Turuncu genellikle "şimdilik iyi ama kayıyor" demektir
Turuncu bir paydır. Aralığının içinde ama son %10'unda olan bir ölçüm turuncuya döner, böylece harekete geçmek için hâlâ vakit varken kaymayı görürsünüz.

İki ayrıntı vardır.

**Kendi belirlediğiniz bir aralık kesin bir çizgidir.** Onu geçerseniz widget turuncu payı olmadan doğrudan kırmızıya döner. **Cora'nın sağladığı** bir aralık daha yumuşaktır. Onu geçmek, sınırın ötesindeki ilk %10'da turuncu, daha ötesinde kırmızı gösterir.

**Tek yönlü bir sınır**, örneğin bir kirletici için üst sınır ya da bir besin için alt sınır, yalnızca üst kenarına göre değerlendirilir. Bu yüzden sıfırdaki bakır yeşil görünür ve ölçeğin altında durduğu için turuncuya dönmez.
:::

Turuncu ya da kırmızı çerçeveli bir widget ilgi ister. Çerçeve widget'ın tamamını çevreler, böylece kaydırırken onu fark edersiniz.

Bir aralığı değiştirmek için widget'a uzun basın. Ayrıntılar [Uyarılar ve eşikler](/help/mobile-alerts) sayfasında.

## Gelip giden kartlar {#cards-that-come-and-go}

Bazı kartlar yalnızca söylenecek bir şey olduğunda görünür. Çoğu başlık ile widget'lar arasında durur.

| Kart | Ne zaman görünür | Neye dokunulur |
|---|---|---|
| **Yeni bir akvaryum mu kuruyorsunuz?** | Hiç ölçümü olmayan bir akvaryumda. Başladıktan sonra **Döngüye devam et** olur | Rehberli döngüyü başlatmak için karta. [Rehberli yolculuklar](/help/mobile-journeys) sayfasına bakın |
| *Henüz ölçüm yok* ile **Akvaryum parametreleri** | Akvaryumun henüz ölçümü yok | **Akvaryumu yapılandır** |
| *Ölçümlerinize ulaşılamadı: önbellekteki gösteriliyor.* | Cora en son ölçümleri yükleyemiyor, çoğu zaman bağlantı olmadığında | **Tekrar dene** |
| **{lab} laboratuvarından bir sonuç sizi bekliyor.** | Bir laboratuvar bir sonuç gönderdi ve Cora'nın hangi akvaryum için olduğunu bilmesi gerekiyor | **Akvaryum seç**. [ICP ve sağlık raporları](/help/mobile-icp-health) sayfasına bakın |
| Profil hatırlatması (**Daha akıllı öngörülerin kilidini açın**) | Akvaryum profili %80'in altında tamamlanmış | Profile devam etmek için karta |
| **Cora Pro deneme: 9 gün kaldı** | Denemenizin son günleri | Karta ya da **Pro'yu koru**'ya. [Planlar ve abonelikler](/help/mobile-plans) sayfasına bakın |
| **Reef Buddy** | Bir özet hazır | Karta |
| **Normalde nasıl besliyorsun?** | Bir besleme rutini ayarlamadınız | **Rutini ayarla** |
| *Red Sea değerleri güncellenmiyor.* | Bu akvaryumun Red Sea cihazlarını hiçbir şey okumuyor | [Uyarılar ve eşikler](/help/mobile-alerts) sayfasına bakın |
| **Kameralar** (Beta) | Akvaryumda bir kamera var, widget'ların altında. Kameralar yalnızca Beta kullanıcılarına açıktır | **Canlı izle** |
| **İlk su testini kaydet** | Ölçüm ve bağlı ekipman yok, widget'ların altında | Karta. [Cora Mobile'ı kurma](/help/mobile-setup#the-first-test-card) sayfasına bakın |

## Widget'ların altında {#below-the-widgets}

![Cora Mobile'da panonun alt kısmı](img/mobile-dashboard-foot.webp "Panoyu düzenle, Parametreleri Kaydet, Parametre geçmişi ve Besleme düğmeleri ve dört kayıt alanına kısayollar.")

Yukarıdan aşağıya şunları bulursunuz:

- Panonun en son ne zaman güncellendiğini ve hangi kaynakları kullandığını söyleyen bir satır, yanında **Panoyu düzenle**. Bu, [pano düzenleyicisini](/help/mobile-dashboard-editing) açar.
- Ölçümü ve bağlı ekipmanı olmayan bir akvaryumda **İlk su testini kaydet** kartı.
- Test kiti ölçümlerini elle girmek için **Parametreleri Kaydet**.
- Widget'ı olmasa bile verisi olan herhangi bir parametrenin geçmişini açmak için **Parametre geçmişi**. [Bir parametreyi inceleme](/help/mobile-metric-detail) sayfasına bakın.
- Rutininizden farklı bir beslemeyi kaydetmek için **Besleme**. [Günlük](/help/mobile-journal) sayfasına bakın.
- **Günlük · Uyarılar · Bakım · Canlılar**: bu akvaryum için o alanlara kısayollar.

## Dokunma ve uzun basma {#tapping-through}

Ayrıntısını açmak için herhangi bir parametre widget'ına dokunun. Tüm geçmişi grafik olarak, onu bildirmiş her kaynağı ve uyarı bandınızı görürsünüz. Oradan kaynakları karşılaştırabilir, hatalı bir ölçümü hariç tutabilir ya da prob bakımını kaydedebilirsiniz. [Bir parametreyi inceleme](/help/mobile-metric-detail) sayfasına bakın.

Uyarı aralığını doğrudan panodan ayarlamak için bir parametre widget'ına **uzun basın**.

## Bir widget'ta değer yoksa {#if-a-widget-has-no-value}

Bir widget değer aldığında onu gösterir. Boşsa genellikle şunlardan biridir:

- Cihaz çevrimdışı. **Cihazlar** sekmesini kontrol edin.
- Parametrenin henüz bir kaynağı yok. Onu elle kaydedin ya da onu bildiren ekipmanı bağlayın.
- Parametre için hiçbir zaman bir şey bildirilmedi ya da kaydedilmedi.

Eski bir ölçüm, grafik aralığından eski diye kaybolmaz. Yaşıyla birlikte widget'ta kalır, böylece eski bir değer eksik değil, eski görünür.

Diğer her şey için [Sorun giderme](/help/troubleshooting#a-widget-shows-no-value) sayfasına bakın.
