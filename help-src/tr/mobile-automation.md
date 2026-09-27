---
title: Otomasyonlar ve sahneler
description: Kendi kendine çalışan kurallar (tetikleyiciler, koşullar, eylemler) oluşturun ve bunları sahnelerde toplayın.
section: Cora Mobile
reviewed: 2026-09-27
order: 17
group: Alerts and automation
---

Otomasyon, Cora'nın sizin yerinize çalıştırdığı bir kuraldır: *şu olunca şunu kontrol et, sonra şunu yap.* Sahneler ise birkaç eylemi tek seferde çalıştırabileceğiniz ya da zamanlayabileceğiniz tek grupta toplar.

**Ayarlar → Otomasyon.**

![Otomasyon listesi](img/mobile-automation.webp "Otomasyonlar ve Sahneler ayrı sekmelerdir. Her kuralın açma kapama anahtarı var.")

Ekranda iki sekme (**Otomasyonlar** ve **Sahneler**) ve bir **Yeni otomasyon** düğmesi var. Her kuralda ne yaptığını anlatan tek satırlık özet, açma kapama anahtarı ve düzenleme ya da silme menüsü bulunur. Henüz hiç çalışmamış kurallarda bu da belirtilir.

:::warning Kurallar gerçek ekipmanı çalıştırır
Pompayı açıp kapatan bir kural, siz başında olsanız da olmasanız da pompayı açıp kapatır. Kuralları tek tek oluşturun. Yenisini eklemeden önce her birinin beklediğiniz gibi çalıştığını kontrol edin.
:::

## Kuralın yapısı

Her kural aynı üç bölümden oluşur:

**Tetikleyici**: kuralı neyin başlattığı
**Koşullar**: ayrıca neyin doğru olması gerektiği
**Eylemler**: kuralın sırasıyla ne yaptığı

## Kuralı ne başlatabilir

Dört şey:

| Tetikleyici | Ne zaman çalışır |
|---|---|
| **Bir parametre değiştiğinde** | Bir parametre, belirlediğiniz değeri seçtiğiniz yönde geçtiğinde |
| **Bir uyarı tetiklendiğinde** | Bir uyarı verildiğinde, kapandığında ya da ikisinde de |
| **Günün belirli bir saatinde** | Kendi saat diliminize göre günün belli bir saatinde |
| **Bir cihaz çevrimdışı olduğunda** | Bir cihaz çevrimdışı olduğunda ya da yeniden bağlandığında |

## Koşullar

Eylemlerin gerçekten çalışıp çalışmayacağına koşullar karar verir. Bilinen karşılaştırmaları kullanabilirsiniz (eşittir, eşit değildir, büyüktür, küçüktür ve diğerleri). Bunları **ve**, **veya** ve **değil** ile birleştirebilirsiniz.

Bir de *önceki* adımın sonucuna bakan **adım** koşulu var. "Bunu dene, olmazsa şunu yap" gibi kurallar bu koşulla yazılır.

## Kural neler yapabilir

Ekipman gerektiren eylemler yalnızca o ekipmanın olduğu akvaryumlarda çıkar:

| Eylem | Ne yapar |
|---|---|
| **Apex Ekipmanını Kontrol Et** | Prizi açıp kapatır |
| **Bir Red Sea Ekipmanını Kontrol Et** | Bir ReefBeat ünitesini çalıştırır |
| **Bir Dalga Pompasını Kontrol Et** | Jecod pompasının akışını, dalga modunu ya da gücünü ayarlar. **Besleme için duraklat** seçeneği de var. Besleme bitince akvaryumdaki Cora Max pompayı eski ayarına döndürür |
| **Bir Cora Ekipmanını Kontrol Et** | Akıllı fişi açıp kapatır |
| **IR Cihazını Kontrol Et** | Kızılötesi komut gönderir |
| **Apex Besleme Döngüsünü Çalıştır** | Beslemeyi başlatır |
| **Bir Trident Testi Çalıştır** | Test başlatır |
| **Beni Bilgilendir** | Size bildirim gönderir |
| **Sonraki Adımdan Önce Bekle** | Devam etmeden önce bekler |
| **Bir Sahne Çalıştır** | Bu kuralın içinden başka bir sahneyi çalıştırır |
| **Bir Otomasyonu Yönet** | Başka bir kuralı açar ya da kapatır |
| **Bir DŌS Kafasından Dozaj Ver** | DŌS kafasından ölçülü doz verir |

:::warning Kuralla yapılan dozaj geri alınamaz ve sınırlıdır
Verilen dozu akvaryumdan geri alamazsınız. Kuralın bir kafadan dozaj yapabilmesi için kafanın **kalibre edilmiş** olması gerekir. Siz başında değilken yapılan dozaj **kafa başına günde 10 mL** ile sınırlıdır. Kural nasıl yazılırsa yazılsın bu sınırı aşamaz. Dozaj eylemleri, kafalarınız dozaj kafası olarak tanındıktan sonra listede çıkar.
:::

:::note Adımları sıralamak için Bekle'yi kullanın
Bekleme adımıyla tek kural sırayla birkaç iş yapabilir. Örneğin prizi kapatır, bekler, sonra yeniden açar. Bunun için ikinci kurala ve programa gerek kalmaz.
:::

## Sahneler

Sahne, adı olan eylem grubudur: "Su değişimi", "Fotoğraf modu", "Gece" gibi. Sahneyi istediğiniz an, bir programla ya da başka bir kuralın içinden çalıştırabilirsiniz.

Bir sahne başka bir sahneyi çağırabilir. Ama Cora, iç içe geçme sınırını aşan sahneleri ve kendi kendini çağıran sahneleri çalıştırmaz. Böylece akvaryumda sonsuza kadar dönen döngü oluşmaz.

Sahne çalıştıktan sonra Cora adım adım neler olduğunu, başarısız olan adımlarla birlikte size bildirir.

Bir sahneyi elle çalıştırmak istediğinizde Cora önce onay ister. Çünkü sahne aynı anda birkaç ekipmanı açıp kapatabilir.

## Cora Max'te hazırlanan sahneler

Sahneleri yalnızca telefondan değil, doğrudan Cora Max tabletten de oluşturup düzenleyebilirsiniz. İki yerde de aynı sahneler görünür, çünkü sahneler hesapta ortaktır. Evinizde eski bir Cora Max varsa telefonda hazırlanan sahneyi yine çalıştırır. Yalnızca cihaz üzerinde düzenleme yeni bir özelliktir. Bu yüzden eski tablet sahneyi gösterip değiştirmenize izin vermeyebilir. Bu durumda sahneyi telefondan düzenleyin.

## Kuralı kapatma

Her kuralın açma kapama anahtarı var. Kuralı kapattığınızda tanımı silinmez. Kuralı gelecek mevsim yeniden kullanmak istiyorsanız baştan kurmak yerine kapatıp bekletin.

## Kuralın neler yaptığını görme

Kuralın yaptığı her işlem, kaynağı olarak o kuralla birlikte kaydedilir. Ayrıntılar **[Etkinlik](/help/mobile-activity)** sayfasında.
