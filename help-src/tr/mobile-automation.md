---
title: Otomasyonlar ve sahneler
description: Cora'nın bir ölçüm, uyarı, saat ya da çevrimdışı kalan cihaz karşısında kendi başına harekete geçmesini sağlayın ve eylemleri tek dokunuşluk sahnelerde toplayın.
section: Cora Mobile
reviewed: 2026-10-24
order: 25
group: Alerts and automation
twin: max-automation
---

Otomasyon, Cora'nın sizin için çalıştırdığı bir kuraldır: *bu olduğunda şunu kontrol et, sonra bunu yap.* Sahne ise birkaç eylemi, istediğinizde çalıştırdığınız tek bir şeyde toplar.

**Ayarlar → Otomasyonlar** yoluna gidin.

![Cora Mobile'da Otomasyonlar ve Sahneler sekmeleriyle Otomasyon ekranı](img/mobile-automation.webp "Otomasyonlar ve Sahneler ayrı sekmelerdir. Her kuralın kendi anahtarı vardır.")

Ekranın iki sekmesi vardır, **Otomasyonlar** ve **Sahneler**, ve bir **Yeni otomasyon** ya da **Yeni sahne** düğmesi bulunur. Her kural tek satırlık bir özet, bir etkinleştirme anahtarı ve onu **Düzenle**mek ya da **Sil**mek için bir menü gösterir. Henüz çalışmamış bir kural bunu söyler.

:::warning Kurallar gerçek ekipman üzerinde çalışır
Bir kural bir pompayı açıp kapatıyorsa, siz izlemiyorken de pompa açılıp kapanır. Her seferinde bir kural oluşturun ve bir sonrakini eklemeden önce beklediğiniz şeyi yaptığını kontrol edin.
:::

## Bir kuralın yapısı {#shape}

Her otomasyonun üç parçası vardır.

- Tetikleyici onu uyandırır.
- Koşulların da doğru olması gerekir.
- Eylemler, ardından sırayla yaptığı şeylerdir.

![Cora Mobile'da boş bir Yeni otomasyon formu](img/mobile-rule-builder.webp "Yeni bir otomasyon: tetikleyiciler, Eğer koşulları, Sonra eylemleri, Aksi halde eğer ve Aksi halde, ardından bekleme süresi ve zaman aralığı.")

## Bir kuralı ne uyandırabilir {#triggers}

**Ne zaman: herhangi bir tetikleyici** altına bir ya da daha fazla tetikleyici ekleyin. Herhangi biri kuralı başlatır.

| Tetikleyici | Ne zaman çalışır |
|---|---|
| **Bir parametre değiştiğinde** | Bir parametre belirlediğiniz bir değeri geçtiğinde. **Yön**'ü seçin: **Yükseliyor**, **Düşüyor** ya da **Herhangi bir değişiklik** |
| **Bir uyarı tetiklendiğinde** | Bir uyarı **Tetiklendiğinde**, **Temizlendiğinde** ya da ikisinde de. Bunu **Eşik** ya da **Değişim hızı** uyarılarıyla sınırlayabilirsiniz. |
| **Günün belirli bir saatinde** | Kendi saat diliminizde günün bir saatinde |
| **Bir cihaz çevrimdışı olduğunda** | Cora Max'iniz **Çevrimdışı** olduğunda, yeniden **Çevrimiçi** olduğunda ya da her iki durumda |

:::tip Cora Max'iniz düştüğünde haberiniz olsun
**Bir cihaz çevrimdışı olduğunda** ve **Beni Bilgilendir** içeren bir kural, ekipmanınızı okuyan Cora Max'in elektriği ya da Wi-Fi'ı kesildiğinde size haber verir.
:::

## Koşullar {#conditions}

Koşullar eylemlerin çalışıp çalışmayacağına karar verir. **Koşul ekle**'ye dokunun ve seçin:

- **Parametre karşılaştırma**: bir değerin üstünde, altında ya da ona eşit bir ölçüm
- **Parametre bir aralığın içinde / dışında**
- **Uyarı etkin**
- **Priz açık / kapalı**: bir Apex prizi için
- **Günün saati**: 22:00 ile 06:00 gibi bir zaman aralığı
- **Önceki bir adımın sonucuna göre**: önceki bir adımın **TAMAM** mı geçtiğini yoksa **Atlandı** mı olduğunu kontrol eder. "Bunu dene, işe yaramadıysa onun yerine şunu yap" için kullanın

Birden fazla koşul varsa **Eşleşme**'yi **Hepsi (VE)** ya da **Herhangi biri (VEYA)** olarak ayarlayın.

## Dallar ve adım başına kontroller {#branches}

Bir otomasyon farklı durumlarda farklı şeyler yapabilir. İlk bloğu **Eğer**'dir. Başka bir durum eklemek için **Aksi halde eğer**'e dokunun ya da geri kalan her şey için bir **Aksi halde** bloğu ekleyin. Cora koşulları sağlanan ilk bloğu çalıştırır.

Tek bir eylemi de bir koşula bağlayabilirsiniz. O adımda **Yalnızca şu durumda…**'ya dokunun ve ona kendi koşulunu verin. Koşul yoksa adım her zaman çalışır.

## Ne zaman çalışabilir {#when-it-may-run}

- **Çalıştırmalar arası bekleme süresi**, bir kuralın çok erken yeniden çalışmasını önler. 10 dk ile başlar.
- **Yalnızca şu saatler arasında çalıştır**, kuralı bir zaman aralığıyla sınırlar, örneğin yalnızca gündüz.
- **Canlı değerlere karşı test et**, hiçbir şey yapmadan kuralı akvaryumunuzun şu anki ölçümlerine göre kontrol eder. Neyin *çalışacağını* ya da neden hiçbir şeyin çalışmayacağını söyler.

## Bir kural neler yapabilir {#actions}

Ekipman gerektiren bir eylem yalnızca o ekipmanı olan bir akvaryumda görünür.

| Eylem | Ne yapar |
|---|---|
| **Apex Ekipmanını Kontrol Et** | Bir prizi açar ya da kapatır |
| **Apex Besleme Döngüsünü Çalıştır** | Bir besleme başlatır. Apex onu kendi zamanlayıcısıyla bitirir |
| **Bir Trident Testi Çalıştır** | Bir test başlatır. Her çalışma reaktif kullanır |
| **Bir DŌS Kafasından Dozaj Ver** | Bir DŌS kafasında ölçülü bir doz çalıştırır |
| **Bir Red Sea Ekipmanını Kontrol Et** | Bir ReefBeat ünitesini yönetir |
| **Bir Dalga Pompasını Kontrol Et** | Bir Jecod pompasının akışını, dalga modunu ya da gücünü ayarlar ya da **Besleme için duraklat**. Besleme bittiğinde akvaryumdaki Cora Max pompayı eski haline getirir |
| **Beni Bilgilendir** | Kendi **Başlık** ve **Mesaj**'ınızla kendinize bir bildirim gönderir |
| **Sonraki Adımdan Önce Bekle** | Devam etmeden önce duraklar |
| **Bir Sahne Çalıştır** | Bu kuralın içinden bir sahne çalıştırır |
| **Bir Otomasyonu Yönet** | Başka bir kuralı açar ya da kapatır |
| **Bakım görevi oluştur** | Akvaryumun [bakım](/help/mobile-maintenance) listesine bir iş koyar, örneğin pH bir değerin altına düştüğünde CO2 yıkayıcı medyasını değiştirmek |


:::warning Bir doz geri alınamaz ve sınırlıdır
Bir dozu akvaryumdan geri çıkaramazsınız. Bir kural yalnızca bir Cora Max'te **Dozajlamak için ölç** ile ölçülmüş bir kafadan dozaj yapabilir. Doz akvaryumdaki bir Cora Max'te çalışır. Kurallardan dozaj, kural nasıl yazılmış olursa olsun **kafa başına günde 10 mL** ile sınırlıdır.
:::

:::note Bakım görevi oluştur ne yapar
Akvaryumu seçin, sonra **Mevcut görev** (var olan bir görevin zamanı şimdiye çekilir) ya da **Yeni görev** (ona bir **Görev adı** verin). Yeni bir görev tek seferliktir, zamanı hemen gelir ve kural, görev açık kaldığı sürece onu yeniden oluşturmaz. Tek bir bildirim alırsınız ve tek seferlik görev, onu tamamladığınızda listeden çıkar.
:::

:::note Bekleme kısadır
**Sonraki Adımdan Önce Bekle** en fazla 60 saniye duraklar ve bir dal toplamda 60 saniye bekleyebilir. Duraklamadan sonra bir sonraki adım taze ölçümleri görür. Su değişimi sırasında ana pompanın 30 dakika kapalı kalması gibi daha uzun bir bekleme için **Şu süre boyunca çalıştır** ayarlı bir sahne kullanın (aşağıda).
:::

## Sahneler {#scenes}

Sahne, "Su değişimi", "Fotoğraf modu" ya da "Gece" gibi adı olan bir eylem grubudur. **Yeni otomasyon**'a ya da **Yeni sahne**'ye dokunun ve en üstte **Sahne**'yi seçin. Bir sahnenin tetikleyicisi yoktur. Onu listedeki **Şimdi çalıştır** ile, bir kuralın içinden **Bir Sahne Çalıştır** ile ya da **Günün belirli bir saatinde** içeren bir kural aracılığıyla bir zaman çizelgesine göre çalıştırırsınız.

**Şu süre boyunca çalıştır**, bir sahnenin ne kadar süreceğini ayarlar: birkaç dakika ya da saat ya da **Ben değiştirene kadar**. Süre dolduğunda Cora sahnenin prizlerini eski hallerine getirir. Diğer ekipman sahnenin bıraktığı gibi kalır. Süreli bir sahne çalışırken liste bir geri sayım ve onu erken bitiren bir **Durdur** düğmesi gösterir.

Bir sahne ısıtıcı, soğutucu, ana pompa ya da su tamamlama gibi önemli bir prizi değiştiriyorsa Cora onu çalıştırmadan önce sorar ve o adımları listeler. Bunu sahnedeki **Çalıştırmadan önce sor** ile kapatabilirsiniz.

Bir sahne başka bir sahneyi 3 seviye derinliğe kadar çağırabilir. Cora kendini çağıran bir sahneyi çalıştırmaz, çünkü döngüye girip akvaryum üzerinde işlem yapmaya devam edebilir.

Bir sahne çalıştıktan sonra, başarısız olan ya da çalışmayan her şey dahil, adım adım ne olduğunu görürsünüz.

## Cora Max'te yapılan sahneler {#scenes-on-cora-max}

Sahneleri bir Cora Max'te de oluşturup düzenleyebilirsiniz. Hesapta paylaşılan aynı sahne setidir. Eski bir Cora Max telefonda yapılmış bir sahneyi yine de çalıştırabilir. Ancak cihazda düzenleme daha yenidir, bu yüzden eski bir Cora Max bir sahneyi değiştirmenize izin vermeden gösterebilir. Onun yerine telefondan düzenleyin.

## Bir kuralı kapatma {#turning-a-rule-off}

Her kuralın bir etkinleştirme anahtarı vardır. Bir kuralı kapatmak ayarlarını saklar, bu da onu gelecek mevsim geri istediğinizde işe yarar.

## Bir kuralın ne yaptığını görme {#seeing-what-a-rule-did}

Bir kuralın yaptığı her eylem, nedeni olarak **Otomasyon kuralı** ile kaydedilir. Onu [Etkinlik](/help/mobile-activity) içinde bulursunuz.

Başarısız olan ya da bekleyecek olan bir adım beklemede kalmaz. Hemen süresi dolar, çalıştırma başarısız olarak kaydedilir ve otomasyonun adını, adımı ve nedenini söyleyen bir bildirim alırsınız. Örneğin cihazı çevrimdışıysa, onu yürütecek bir Cora Max yoksa, cihaz reddederse ya da yanıt vermezse veya bir ısıtıcı ya da soğutucu az önce açılıp kapatıldıysa adım başarısız olur. Kaldırılmış bir akvaryumdaki bir adım için bildirim gelmez.
