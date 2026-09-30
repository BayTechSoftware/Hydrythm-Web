---
title: Ekipmanınızı kontrol etme
description: Cihazın sayfasını açın, canlı durumunu görün ve kontrol edin. Prizler, pompalar, dozaj kafaları ve test cihazları.
section: Cora Mobile
reviewed: 2026-09-30
order: 11
group: Equipment
---

Bağlı her ekipmanın Cora'da kendi sayfası var. Sayfa cihazın canlı durumunu ve cihazın desteklediği bütün kontrolleri gösterir. Sayfayı **Cihazlar** sekmesinden açın.

![Cihaz sayfası](img/mobile-device-detail.webp "Üstte canlı ölçümler, altında cihazın desteklediği kontroller.")

Bütün cihaz sayfaları aynı düzendedir: en üstte cihazın kimliği, altında canlı ölçümler satırı, cihazın bildirdiği durumlar ve en altta kontroller. Başlık çubuğundaki zil simgesiyle o cihazın uyarı eşiklerini ayarlarsınız. Ayrıntılar [Sarf malzemeleri](/help/mobile-consumables) sayfasında.

:::warning Bu kontroller çalışan ekipmanı etkiler
Önizleme ya da geri alma yoktur. Bazı kontroller önce onay ister.
:::

## Komut gönderdiğinizde ne olur

Komutlar her zaman başarılı olmaz. Cora varsayım yapmaz, dört sonuçtan hangisinin gerçekleştiğini söyler:

| Sonuç | Anlamı |
|---|---|
| **Onaylandı** | Ekipman değişikliği kabul etti ve yeni durumunu bildirdi |
| **Onaylanmadı** | Komut gönderildi ama geri bildirim gelmedi. **Bu "çalıştı" değil, "bilmiyoruz" demektir.** Cihazın kendi durumuna bakın |
| **Reddedildi** | Bir güvenlik kuralı, kilit ya da ekipmanın kendisi komutu reddetti. Ya da hiçbir Cora cihazı komutu zamanında almadı ve komut iptal edildi. Hiçbir şey çalışmadı |
| **Değişiklik yok** | Ekipman zaten istediğiniz durumdaydı |

Her sonuç, kaynağıyla birlikte [Etkinlik](/help/mobile-activity) ekranına kaydedilir.

## Neptune Apex

Apex sayfasında problarınız ve prizleriniz listelenir.

- **Problar** Cora'ya kaynak olarak veri gönderir. Onları panoya ekleyebilirsiniz.
- **Prizler** **Otomatik**, **Kapalı** ve **Açık** arasında geçiş yapar. Otomatik, kontrolü Apex'teki programınıza geri verir.
- **Takılı modüllerin** (Trident, DŌS ve diğerleri) her birinin kendi sayfası var.

## Trident

Trident sayfası o anki test durumunu, kalan reaktif ve atık su seviyelerini gösterir. Buradan test başlatabilirsiniz.

Bu sayfadan kalan test sayısı için uyarı eşiği de koyabilirsiniz. Böylece Cora reaktif bitmeden sizi uyarır. Ayrıntılar [Sarf malzemeleri](/help/mobile-consumables) sayfasında.

## DŌS

DŌS QD tıpkı DŌS gibi çalışır. Burada anlatılan her şey ikisi için de geçerlidir. Apex'inizi bir Cora Max okuyorsa dozaj kafaları priz listesinde değil, her zaman DŌS sayfasında görünür.

Her dozaj kafasında şunlar görünür: neyi dozladığı, programı, bugün ne kadar dozladığı, kapta ne kadar kaldığı ve **kalan süresi**, yani şu anki hızla kaç gün yeteceği.

Her kafa için şunları yapabilirsiniz:

- Programı **Duraklat** ve **Sürdür**
- **Doldur**: Cora'ya kabın yeniden dolduğunu söyleyin ya da içindeki miktarı girin
- **Şimdi dozajla**: ölçülü dozu elle verin

:::note Programlar burada değil, Apex Fusion'da düzenlenir
Cora programı gösterir ve verilen dozları takip eder, ama programı değiştirmez. Programı, doz hızını ya da doz sayısını Apex Fusion uygulamasından düzenlersiniz. Duraklatma, doldurma ve elle dozajı buradan yapabilirsiniz.
:::

:::note Elle dozajdan önce kafayı ölçün
Bir kafa ölçülmeden Cora o kafadan elle dozaj yapmaz. **Dozajlamak için ölç** ve **Yeniden ölç**, akvaryumun dozajını yapan Cora Max'te bulunur. Cora kafayı yirmi saniye çalıştırır, siz çıkan sıvıyı ölçersiniz, Cora da kafanın gerçek hızını hesaplar. Tek ölçüm bütün Cora Max'ler ve Cora Mobile için geçerlidir. Her kafayı bir kez ölçün. Hortumunu değiştirdikten sonra yeniden ölçün.
:::

:::warning DŌS, kap boşalsa da dozaja devam eder
Ünitede seviye sensörü yoktur ve kendi kendine durmaz. Kap kurumadan Cora'nın sizi uyarması için kafanın sayfasından dolum uyarısı kurun.
:::

### Her kafa ne için kullanılıyor

Her kafaya **kullanım türü** atanır. Böylece Cora kafanın ne iş yaptığını bilir ve onun hakkında doğru konuşur. Türler: **Takviye**, **Su değişimi: yeni tuzlu su girişi**, **Su değişimi: eski su çıkışı**, **Kalkwasser**, **Kalsiyum reaktörü**, **Yem**, **Su tamamlama** ya da **Diğer**. Türü kafanın ayarlarında **Kullanım amacı** altından seçin.

İki su değişimi türü **eşleştirilmek** için vardır. Bir kafanın **Eşleştirilmiş kafa** ayarını, suyu ters yönde taşıyan diğer kafaya ayarlayın. Cora bu iki kafayı birbirinden bağımsız iki kafa olarak değil, tek bir su değişimi çifti olarak görür.

Her kafanın ayrıca **Elle verilecek en büyük dozaj** sınırı var. Bu sınır, yanlış yazılan elle dozun istenenden çok daha büyük olmasını önler. Büyük elle dozlar, ancak kafanın hızı akvaryumda gerçek testle ölçüldükten sonra açılır.

## Red Sea ReefBeat

Her ünitenin kendine uygun sayfası var:

| Ünite | Sayfada neler var | Neler yapabilirsiniz |
|---|---|---|
| **ReefDose** | Her kafa, kabı ve verdiği dozlar | Her kafa için: **Günlük dozaj**, **Şişede kalan**, **Şimdi dozajla** ve **Zaman planını etkinleştir**. Her kafa için ayrı dolum uyarısı kurun |
| **ReefATO+** | Rezervuar seviyesi ve su tamamlama hareketleri | Rezervuar uyarısı kurun |
| **ReefMat** | Kalan rulo, gün ve metre olarak | Ruloyu ilerletin, dolum uyarısı kurun |
| **ReefRun** | Ana pompa ve skimmer pompasının hızı ve durumu | Hızı değiştirin, pompayı açıp kapatın, skimmer ayarlarını değiştirin |

**ReefRun ana pompa ve skimmer pompası kontrol ünitesidir**, dalga pompası değildir.

Bir ünite kendini durdurabilir. Örneğin skimmer kabı dolunca ReefRun pompası durur. Bu durumda ünitenin sayfası nedenini yazar ve çözümü gösterir:

| Ünite | Sayfada yazan | Dokunun |
|---|---|---|
| ReefRun | Hangi pompanın neden durduğu. Örneğin *Kap dolu. Boşaltın, ardından devam edin.* | **Sürdür** |
| ReefRun ya da ReefMat | **Acil durdurma** | **Acil durumu temizle** |
| ReefMat | **Mat sıkıştı**, **Kurulum hatası** ya da **Ayar hatası** | **Sürdür** |
| ReefMat | *Yeni bir rulo yükleyin, sonra Red Sea uygulamasında onaylayın.* | **Zaten yeni bir rulo yükledim** |
| ReefMat | **Sensörün temizlenmesi gerekiyor** | **Sensör temizlendi** |
| ReefDose | **Kafa arızası** ve kafanın adı | **Sıfırla** |
| ReefATO+ | **Arızayı Temizle** | **Sürdür** |

Bunların bazıları önce onay ister. Ünitenin ağında değilseniz Cora Mobile bu komutları akvaryumdaki bir Cora Max üzerinden gönderir. Bunu yapabilecek bir Cora Max yoksa sayfada bu yazar ve hiçbir şey gönderilmez.

## Jecod pompaları

Pompa sayfası pompanın şu anki modunu ve yoğunluğunu gösterir. İkisini de buradan değiştirebilirsiniz.

Ayrıca şunları yapabilirsiniz:

- **Programı şuraya kopyala…**: bu pompanın programını başka bir pompaya aktarın
- **Programı farklı kaydet…** ve **Kayıtlı programlar…**: programı saklayın ve sonra yeniden uygulayın
- **Bu zamanlamayı paylaş** ve **Bir zamanlama kodu yapıştır…**: programı kısa kodla başka sisteme taşıyın

## Maxspect

:::note Maxspect desteği beta aşamasında
Maxspect gyre desteğinin testleri ve geliştirmesi sürüyor. Bazı kontroller sınırlı olabilir ve burada gördükleriniz güncellemelerle değişebilir. Bir şey anlatıldığı gibi çalışmıyorsa [Yardım alma](/help/mobile-support) sayfasındaki yoldan bize bildirin.
:::

Gyre sayfası gyre'nin çalışıp çalışmadığını, **Gyre A** ve **Gyre B**'nin dalga desenini ve hızını ve bu bilgilerin en son ne zaman okunduğunu gösterir. Bu sayfada şunları yapabilirsiniz:

- Durumun yanındaki anahtarla gyre'yi açıp kapatın. Cora önce onay ister. Kapatınca iki gyre de durur, program olduğu gibi kalır.
- **Ayarları değiştir**'e dokunarak her gyre'nin dalga desenini ve pompa hızını (süresi olan desenlerde süreyi de) ve iki gyre'nin bağlı çalışıp çalışmayacağını ayarlayın. Cora neyin değişeceğini listeler ve uygulamadan önce onay ister. Dönüşümlü mod Maxspect uygulamasından ayarlanır. Bu modda çalışan bir gyre kendi hızlanma ve bekleme sürelerini korur.
- Gyre'de kayıtlı program okunamıyorsa bunun yerine **Programı ayarla**'ya dokunun. Bu seçenek iki gyre'yi de ayarlar ve gyre yeniden çalışabilir.
- Gyre'nin günlük programını **Program** kartında görün. Program yalnızca görüntülenir. Programı Maxspect uygulamasından ayarlayın.
- **Pompa sağlığı** bilgisine bakın: pompanın bir sonraki temizliğe ne kadar kaldığı (pompa bunu kendisi geri sayar), A kafasının çektiği akım, hangi kafaların takılı olduğu ve yazılım sürümü. Bilgileri almak için **Oku**'ya dokunun.

:::note Cora Mobile gyre'ye nasıl ulaşır
Akvaryuma bağlı bir Cora Max varsa Cora Mobile, evden uzaktayken de o Cora Max üzerinden çalışır. **Ayarları değiştir** de o Cora Max'in son okumasından başlar. Cora Max yoksa telefonunuz gyre'yle doğrudan bağlantı kurar ve gyre'yle aynı ağda olması gerekir. Bu durumda sayfayı açınca gyre okunur. Sayfa daha eski, kayıtlı okumayı gösteriyorsa yenile simgesine dokunana kadar **Ayarları değiştir** görünmez.
:::

## GHL ProfiLux ve Mitras

:::note GHL desteği beta aşamasında
GHL desteğinin testleri ve geliştirmesi sürüyor. Bazı ölçümler ya da kontroller henüz çalışmayabilir, burada gördükleriniz güncellemelerle değişebilir. Bir şey anlatıldığı gibi çalışmıyorsa [Yardım alma](/help/mobile-support) sayfasındaki yoldan bize bildirin.
:::

Kontrol cihazının sayfası probları, prizleri, dozaj ünitelerini ve seviye sensörlerini, Director modellerinde de KH ile iyon test sonuçlarını gösterir.

Cihazın sayfasında **Cora'dan kontrole izin ver (Beta)**'yı açana kadar kontroller kapalıdır. Varsayılan olarak kapalıdır. Açtığınızda Cora'nın o kontrol cihazına besleme molası, bakım, su değişimi, fırtına, aydınlatma, ayar noktası ve priz komutları göndermesine izin vermiş olursunuz.

Açıldıktan sonra:

- Bir priz **Her zaman açık**, **Her zaman kapalı** ya da kontrolü kontrol cihazının kendi programına geri veren **Otomatiğe dön** olarak ayarlanabilir.
- Sıcaklık ya da pH gibi bir ayar noktası izin verilen aralığını gösterir ve aralık dışındaki bir değeri reddeder.

:::warning Priz ya da ayar noktası değişikliği kontrol cihazının kendisine kaydedilir
Bu yalnızca Cora'da saklanmaz. Bir prizi Her zaman açık ya da Her zaman kapalı yapmak, siz Otomatiğe dön'ü seçene kadar kontrol cihazının o priz için kendi programını geçersiz kılar.
:::

Bir priz ya da ayar noktası bir ısıtıcıya ya da geri dönüş pompasına ait gibi görünüyorsa Cora, göndermeden önce sizden iki kez onay ister.

Kontrol cihazı değişikliği kabul etmiyorsa GHL API'sinin tam erişimle açık olduğunu kontrol edin. GHL bunu her yazılım güncellemesinden sonra kapatır. Adımlar için [Sorun giderme](/help/troubleshooting) sayfasına bakın.

## HYDROS

:::note HYDROS desteği beta aşamasında
HYDROS desteğinin testleri ve geliştirmesi sürüyor. Bazı ölçümler ya da kontroller henüz çalışmayabilir, burada gördükleriniz güncellemelerle değişebilir. Bir şey anlatıldığı gibi çalışmıyorsa [Yardım alma](/help/mobile-support) sayfasındaki yoldan bize bildirin.
:::

Burada gördükleriniz bağladığınız anahtara bağlıdır. Bir **Read** anahtarı yalnızca girişlerini verir. Bir **Write** anahtarı çıkışları, modları, dozaj ve test cihazı komutlarını da ekler, ayrıca hangi anahtar türünde olduğunuzu hatırlatan bir sayfa şeridi gösterir.

Write anahtarıyla da kontroller, cihazın sayfasında **Cora'dan kontrole izin ver (Beta)**'yı açana kadar kapalı kalır. Varsayılan olarak kapalıdır.

Açıldıktan sonra sayfa şunları gösterebilir:

- **Çıkışlar**: açık/kapalı bir çıkış için anahtar, pompa ya da ışık gibi bir seviye için kaydırıcı, ya da bir bayrak için düğme. Geçersiz kılınmış bir çıkış, kendi programına geri vermek için bir **Programa geri dön** düğmesiyle birlikte **Geçersiz kılındı** yazısını gösterir.
- **Modlar**: Besleme ya da Su Değişimi gibi, bir seçim satırı olarak. Birine dokunmak onay ister.
- **Dozaj kafaları**: her birinde bir **Dozla** düğmesi ve kendi sınırlarını, yani en büyük elle dozu ve günlük üst sınırı ayarladığınız bir **Başlık ayarları** girişi. Bir kafanın sınırından fazlasını, ya da o gün için kalan günlük üst sınırından fazlasını istemek, mesajdaki sayılarla birlikte reddedilir.
- **Test cihazı komutları**: bağlı bir iV ya da Maven için, bir düğmeden çalıştırılır ve önce onay ister.

Kontrol cihazı bir süredir haber vermiyorsa sayfa bunu söyler ve ölçümler güncel olmayabilir. Çevrimdışı görünürken gönderilen bir komut hiç gönderilmez, sayfa bunu da söyler.

## Bir şeyi değiştirdikten sonra

Her değişiklik, onu isteyen yüzeyle birlikte [Etkinlik](/help/mobile-activity) ekranına kaydedilir. Cihaz değişikliği kabul etmezse bu hata da orada kaydedilir.
