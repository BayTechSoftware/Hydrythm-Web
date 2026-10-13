---
title: Cora Max panosunu düzenleme
description: Izgara seçin, widget ekleyin ve Cora Max ekranı için düzenlerinizi kaydedin.
section: Cora Max
reviewed: 2026-10-13
order: 4
group: Your dashboard
---

Cora Max panosu **sabit bir ızgara** kullanır. Tüm kutucuklar tek ekrana sığmalıdır, çünkü ekran kaymaz. Telefondaki panodan en büyük farkı budur.

Düzenleyiciyi **akvaryum menüsünden** açın. Üst çubukta akvaryum adına, sonra **Pano düzeni**'ne dokunun. Aynı ekran **Ayarlar → Akvaryum ayarları → [akvaryumunuz] → Pano düzeni** altında da var.

![Cora Max'te pano düzenleyicisi](img/max-dashboard-editor.webp "Üstte ızgara boyutları, altında kutucuklar. Kutucuklarda ölçüm değil, tür ve kaynak yazar, çünkü bu bir düzen ekranıdır. Kaydet'e basana kadar hiçbir şey kaydedilmez.")

:::tip Telefonunuzdan da düzenleyebilirsiniz
**Cihazlar → Cora Max'iniz → Panoyu Düzenle** ile aynı düzeni Cora Mobile'dan kurarsınız. Kutucukları duvardaki ekranda tek tek yerleştirmekten daha hızlıdır. Sonuç ekranda hemen görünür.
:::

## Izgara seçme

Önce yoğunluğu seçin. Izgarayı sonradan değiştirirseniz tüm kutucuklar yeniden yerleşir.

| Izgara | Kutucuk | Nasıl görünür |
|---|---|---|
| 2×2, 3×2, 3×3 | 4-9 | Büyük. Odanın öbür ucundan okunur. |
| 4×4, 5×3, 6×4 | 16-24 | Eksiksiz bir sistem için en çok seçilen. |
| 6×5, 8×4, 8×5 | 30-40 | Yoğun. Tüm reef odası tek ekranda. |
| 9×5, 10×5 | 45-50 | Çok yoğun. En büyük ekranlara uygun. |
| **Otomatik** | 32'ye kadar | Cora, eklediğiniz kutucuk sayısına uygun bir şekil seçer. |

Sabit ızgaraya hücre sayısı kadar kutucuk sığar. 10×5'te bu 50'dir. Kendi sınırı olan tek seçenek **Otomatik**'tir. 32 kutucukta durur, çünkü daha fazlasında yazılar uzaktan okunamayacak kadar küçülür.

:::note Emin değilseniz Otomatik ile başlayın
İstediğiniz kutucukları ekleyin ve ızgarayı **Otomatik**'te bırakın. Cora onlara uyan bir şekil seçer. Sonucu beğenirseniz ızgarayı o sabit şekle ayarlayın.
:::

:::warning Izgarayı değiştirince kutucuklar yalnızca yer kalmazsa silinir
Kutucuklar yeni şekle yeniden yerleştirilir, konumlarına göre atılmaz. Hâlâ geçerli bir hücrede olan kutucuk yerinde kalır, geri kalanlar sırayla yeniden dizilir. Kutucuk yalnızca yeni ızgarada **kutucuklarınızdan daha az hücre** varsa kaybolur. Cora kaç tanesinin silindiğini size söyler. 10×5'ten (50 hücre) 3×3'e (9 hücre) geçerseniz çoğu gider.
:::

## Ekleme ve yerleştirme

Düzenleyicinin üstünde üç hareket yazar: **düzenlemek için kutucuğa dokunun**, **taşımak için uzun basın**, **kaldırmak için ✕**. Kutucuklar bir ya da iki hücre genişliğinde, bir ya da iki hücre yüksekliğinde olabilir.

**Prizler ve Besleme**, kontrol edebildiğiniz prizleri ve besleme döngülerini tek tek değil, tek adımda ekler. **Tümünü temizle** ızgarayı boşaltır, baştan başlayabilirsiniz.

On altı kutucuk türü var: Değer, Gösterge, Grafik, Durum, Priz, Sahne, ReefBeat, Apex modülü, Jecod, Maxspect *(Beta)*, GHL *(Beta)*, HYDROS *(Beta)*, Radion *(Beta)*, VorTech *(Beta)*, Versa *(Beta)* ve Kamera *(Beta)*. Hepsi **[Widget rehberi](/help/mobile-widgets)** sayfasında anlatılıyor.

Beta kutucuklar, yalnızca Beta kullanıcılarının ekleyebildiği Beta entegrasyonlara aittir ve bir kutucuğu ancak cihaza sahip olduğunuzda görürsünüz. Ayrıntılar [Beta özellikleri](/help/mobile-beta) sayfasında.

## Şablonlar

**Şablonlar**, düzenleyicinin üstünde **Yapay zeka ile tasarla**'nın yanında bulunur. Her planda açıktır ve hiç yapay zeka kullanmaz, bu yüzden yapay zeka veri paylaşımı kapalıyken de çalışır.

**Pano şablonları**'nı açar. Bunlar, bu akvaryumun bildirdiği ve bağladığı şeylerden oluşturulan birkaç hazır düzendir:

- **Genel bakış**: az sayıda büyük kutucuk. Temel parametreler gösterge olarak, yanlarında ana cihazlarınız
- **Ekipman**: önce her cihaz için bir kutucuk, ardından prizler ve temel parametreler
- **Parametreler**: önce grafikler ve ölçümler, cihazlar ve prizler en sonda
- **Kamera**: sol üstte büyük bir canlı görüntü, yanında temel parametreler. Yalnızca akvaryumda kamera varsa görünür. Kameralar Beta aşamasındadır ve yalnızca Beta kullanıcılarına açıktır.

Her şablon bir önizleme ve hangi ızgarada kaç kutucuğu olduğunu gösterir. **Bunu kullan**'a dokunun. Cora önce **Panonuz değiştirilsin mi?** diye sorar. Mevcut düzeninizi saklamak istiyorsanız **Önce mevcut olanı ön ayar olarak kaydet**'e, istemiyorsanız **Değiştir**'e dokunun. **Kaydet**'e basana kadar hiçbir şey kaydedilmez.

## Yapay zeka ile tasarla

Ücretli bir planda düzenleyicide **Yapay zeka ile tasarla** düğmesi bulunur. Cora, bu akvaryumun bildirdiği ve bağladığı şeylere bakarak komple bir düzen önerir ve kaç kutucuğu olduğunu, hangi ızgarada olduğunu gösterir. Düzenleyiciye almak için **Bunu kullan**'a, başka bir öneri için **Tekrar deneyin**'e dokunun. Her akvaryum için günde 5 tasarım yapabilirsiniz.

Yapay zeka tasarımı bu panodaki mevcut düzenin yerine geçer. **Kaydet**'e basana kadar hiçbir şey kaydedilmez ve mevcut düzeninizi önce panolarınızdan biri olarak kaydederek saklayabilirsiniz. Ücretsiz plandaysanız **Yapay zeka ile tasarla** sizi planlara yönlendirir. Ayrıca Cora uygulamasında yapay zeka veri paylaşımının açık olması gerekir.

## Uzaktan okunacak şekilde tasarlayın

Duvardaki ekranı telefondan daha uzaktan okursunuz. Genellikle de dikkatle değil, bir göz atarak.

- **Öne çıkan parametrelere 2×2 yer verin.** Alkalinite, sıcaklık, pH gibi yanına gitmeden görmek istediğiniz değerler.
- **Kontrolleri kenarlara koyun.** En çok dokunduğunuz kutucuklar priz kutucuklarıdır. Kenardayken onlara daha kolay dokunursunuz.
- **Türe göre değil, konuya göre gruplayın.** Dozajla ilgili her şey bir yerde, akışla ilgili her şey başka bir yerde olsun. Duvardaki ekrana bölge bölge bakarsınız.
- **Eser elementleri küçük tutun.** Eser elementler ve yavaş değişen diğer değerler anlık izlemek için değil, arada bakmak içindir. 1×1 bir değer kutucuğu yeter.

## Düzenleri kaydetme

Düzenleyicide yaptığınız değişiklikler ancak **Kaydet**'e basınca geçerli olur. Kaydetmeden çıkarsanız değişiklikler silinir.

Tekrar kullanmak istediğiniz düzenleri **Panolarım**'da saklarsınız. Böylece her seferinde baştan kurmak yerine aralarında geçiş yaparsınız. Örneğin günlük kullanım için yoğun bir düzen, akvaryumda çalışırken büyük kutucuklu bir düzen kullanabilirsiniz. Aralarında geçmek tek dokunuş.

## Birden çok akvaryum

Her akvaryumun kendi düzeni vardır. Her birini kendi ayarlarından, tek tek düzenleyin.
