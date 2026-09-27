---
title: Otomasyonlar ve sahneler
description: Kendi başına çalışan kurallar (tetikleyiciler, koşullar, eylemler) oluşturun ve bunları sahnelere gruplayın.
section: Cora Mobile
reviewed: 2026-09-27
order: 17
group: Alerts and automation
---

Bir otomasyon, Cora'nın sizin için çalıştırdığı bir kuraldır: *bu olduğunda, şunu kontrol et, ardından bunu yap.* Sahneler, çalıştırabileceğiniz veya zamanlayabileceğiniz tek bir şeye birkaç eylemi gruplar.

**Ayarlar → Otomasyon.**

![Otomasyon listesi](img/mobile-automation.webp "Otomasyonlar ve Sahneler ayrı sekmelerdir. Her kuralın bir etkinleştirme anahtarı vardır.")

Ekranda iki sekme (**Otomasyonlar** ve **Sahneler**) ve bir **Yeni otomasyon** düğmesi bulunur. Her kural, ne yaptığının tek satırlık bir özetini, bir etkinleştirme anahtarını ve düzenleme veya silme için bir menüyü gösterir. Henüz çalışmamış bir kural bu şekilde işaretlenir.

:::warning Bunlar gerçek ekipman üzerinde etkilidir
Bir pompayı açıp kapatan bir kural, izliyor olsanız da olmasanız da onu açıp kapatır. Bir kerede bir kural oluşturun ve bir sonrakini eklemeden önce her birinin beklediğinizi yaptığını kontrol edin.
:::

## Bir kuralın şekli

Her kural aynı üç parçadır:

**Tetikleyici**: onu neyin uyandırdığı
**Koşullar**: ayrıca doğru olması gereken şey
**Eylemler**: ardından sırayla ne yaptığı

## Bir kuralı ne uyandırabilir

Dört şey:

| Tetikleyici | Şu durumda tetiklenir |
|---|---|
| **Bir parametre değiştiğinde** | Bir parametre, seçtiğiniz bir yönde belirlediğiniz bir değeri geçtiğinde |
| **Bir uyarı tetiklendiğinde** | Bir uyarı yükseltildiğinde, kapandığında, veya ikisinde de |
| **Günün belirli bir saatinde** | Kendi saat diliminizde bir günün saati |
| **Bir cihaz çevrimdışı olduğunda** | Bir cihaz çevrimdışı olduğunda veya geri geldiğinde |

## Koşullar

Koşullar, eylemlerin gerçekten çalışıp çalışmayacağına karar verir. Olağan karşılaştırmaları alırsınız (eşittir, eşit değildir, büyüktür, küçüktür, vb.) ve bunları **ve**, **veya** ve **değil** ile birleştirebilirsiniz.

Ayrıca *önceki* adımın nasıl sonuçlandığını kontrol eden bir **adım** koşulu da vardır. "Bunu dene; işe yaramazsa, bunun yerine şunu yap" yazmanızı sağlayan budur.

## Bir kural ne yapabilir

Ekipman gerektiren bir eylem, yalnızca o ekipmana sahip bir akvaryumda sunulur:

| Eylem | Ne yaptığı |
|---|---|
| **Apex Ekipmanını Kontrol Et** | Bir prizi açıp kapatın |
| **Bir Red Sea Ekipmanını Kontrol Et** | Bir ReefBeat birimini çalıştırın |
| **Bir Dalga Pompasını Kontrol Et** | Bir Jecod pompasının akışını, dalga modunu veya gücünü ayarlayın, veya **Besleme için duraklat**: akvaryumdaki Cora Max, besleme bittiğinde pompayı geri koyar |
| **Bir Cora Ekipmanını Kontrol Et** | Akıllı bir fişi açıp kapatın |
| **IR Cihazını Kontrol Et** | Bir kızılötesi komut gönderin |
| **Apex Besleme Döngüsünü Çalıştır** | Bir besleme başlatın |
| **Bir Trident Testi Çalıştır** | Bir testi tetikleyin |
| **Beni Bilgilendir** | Kendinize bir push gönderin |
| **Sonraki Adımdan Önce Bekle** | Devam etmeden önce duraklayın |
| **Bir Sahne Çalıştır** | Bu kuralın içinden başka bir sahne çalıştırın |
| **Bir Otomasyonu Yönet** | Başka bir kuralı açıp kapatın |
| **Bir DŌS Kafasından Dozaj Ver** | Bir DŌS kafasında ölçülmüş bir dozaj çalıştırın |

:::warning Bir kuraldan dozajlamak geri alınamaz ve sınırlıdır
Bir dozaj akvaryumdan geri alınamaz. Bir kural ondan dozaj verebilmeden önce kafanın **kalibre edilmiş** olması gerekir ve gözetimsiz dozajlama **kafa başına günde 10 mL** ile sınırlıdır; bir kural nasıl yazılmış olursa olsun bunu aşamaz. Dozaj eylemleri, kafalarınız dozaj kafası olarak tanındıktan sonra görünür.
:::

:::note Bekle'yi bir kural içindeki adımları sıralamak için kullanın
Bir duraklama, tek bir kuralın (örneğin bir prizi kapatma, bekleme, ardından yeniden açma gibi) ikinci bir kural ve bir zamanlama olmadan sıralı bir işlem gerçekleştirmesine izin verir.
:::

## Sahneler

Bir sahne, talep üzerine, bir zamanlamadan, veya başka bir kuralın içinden çalıştırabileceğiniz adlandırılmış bir eylem grubudur: "Su değişimi", "Fotoğraf modu", "Gece".

Bir sahne başka bir sahneyi çağırabilir. Cora, derinlik sınırını aşan iç içe bir sahneyi çalıştırmayı ve kendini çağıracak bir sahneyi reddeder; bu, akvaryum üzerinde süresiz devam edecek bir döngüyü önler.

Bir sahne çalıştığında size adım adım ne olduğu, başarısız olan her şey dahil, söylenir.

Bir sahneyi elle çalıştırmak önce onaylamanızı ister, çünkü bir sahne aynı anda birden fazla ekipman parçasını açıp kapatabilir.

## Cora Max'te yapılan sahneler

Sahneler, sadece telefonda değil, doğrudan bir Cora Max tabletinde de oluşturulup düzenlenebilir: her iki durumda da aynı sahne setidir, hesap boyunca paylaşılır. Bir hanede daha eski bir Cora Max varsa, telefonda yapılmış bir sahneyi hâlâ çalıştırabilir; yalnızca cihaz üzerinde düzenleme daha yeni bir yetenektir, bu yüzden eski bir tablet bir sahneyi gösterebilir ama orada değiştirmenize izin vermeyebilir. Bunun yerine telefondan düzenleyin.

## Bir kuralı kapatma

Her kuralın bir etkinleştirme anahtarı vardır. Birini kapatmak tanımını korur; bir kuralı yeniden oluşturmak yerine bir sonraki sezon geri istediğinizde kullanışlıdır.

## Bir kuralın ne yaptığını görme

Bir kuralın gerçekleştirdiği her eylem, nedeni olarak kuralla birlikte kaydedilir. Bkz. **[Etkinlik](/help/mobile-activity)**.
