---
title: Ekipmanınızı kontrol etme
description: Canlı durumunu görmek ve prizleri, pompaları, dozaj kafalarını ve test cihazlarını marka marka değiştirmek için bir cihazın sayfasını açın.
section: Cora Mobile
reviewed: 2026-10-13
order: 13
group: Equipment
twin: max-device-control
---

Canlı durumunu görmek ve yaptığı şeyi değiştirmek için bir cihazın kendi sayfasını kullanın. Onu **Cihazlar** sekmesinde cihaza dokunarak ya da panodaki kutucuğuna dokunarak açın.

![Cora Mobile'da bir ReefATO+ sayfası](img/mobile-device-detail.webp "Durum, bugünün ölçümleri ve su seviyesi, ardından sızıntı, dolumlar ve prob kalibrasyonu.")

Her cihaz sayfası aynı şekilde düzenlenmiştir. Ad ve ayrıntılar en üstte, ardından bir sıra canlı ölçüm, cihazın bildirdiği her durum ve kontrolleri gelir. Başlık çubuğundaki zil, [Sarf malzemeleri](/help/mobile-consumables) sayfasında anlatıldığı gibi o cihaz için uyarı eşiklerini ayarlar. Bir cihazı ilk başta nasıl ekleyeceğiniz [Ekipmanınızı bağlama](/help/mobile-connections) sayfasında.

Ekipmanınıza atlayın: [Neptune Apex](#neptune-apex) · [Trident](#trident) · [DŌS](#dos) · [Red Sea](#red-sea) · [ReefDose](#reefdose) · [ReefRun](#reefrun) · [ReefMat](#reefmat) · [ReefATO+](#reefato) · [Dozaj pompası uyarıları](#doser-alerts) · [Jecod](#jecod) · [AquaWiz](#aquawiz) · [Maxspect](#maxspect) · [GHL](#ghl) · [HYDROS](#hydros) · [Focustronic](#focustronic) · [EcoTech, Inkbird ve kameralar](#ecotech-inkbird-cameras)

:::warning Bu kontroller canlı ekipman üzerinde çalışır
Önizleme ve geri alma yoktur. Bazı kontroller önce onay ister.
:::

## Bir komut gönderdiğinizde ne olur {#what-happens-when-you-send-a-command}

Bir komut her zaman ulaşmaz. Cora size dört şeyden hangisinin olduğunu söyler:

| Sonuç | Anlamı |
|---|---|
| **Onaylandı** | Ekipman değişikliği kabul etti ve yeni durumunu bildirdi |
| **Onaylanmadı** | Komut gitti ama yanıt gelmedi. **Bu "bilmiyoruz" demektir. Çalıştığı anlamına gelmez.** Cihazın kendi durumunu kontrol edin |
| **Reddedildi** | Bir şey onu geri çevirdi (bir güvenlik kuralı, bir kilit ya da ekipmanın kendisi) ya da hiçbir Cora cihazı onu zamanında almadı. İptal edildi ve hiçbir şey çalışmadı |
| **Değişiklik yok** | Ekipman zaten istediğiniz şekilde ayarlıydı |

Her sonuç, ona neyin neden olduğuyla birlikte [Etkinlik](/help/mobile-activity) içine kaydedilir.

Akvaryumda Cora Max yokken Neptune Apex, Red Sea ve Jecod ekipmanı yalnızca yerel çalışır: bir komut göndermek için telefonunuzun aynı ağda (ya da Bluetooth menzilinde) olması gerekir. Akvaryumda bir Cora Max varken Cora Mobile, siz evden uzaktayken bile komutu o Cora Max üzerinden gönderir.

## Neptune Apex {#neptune-apex}

![Cora Mobile'da durumunu, Trident ve DŌS modüllerini, Parametre Eşlemesi'ni ve hizmet ettiği akvaryumu gösteren bir Apex sayfası](img/mobile-apex.webp "Apex sayfası: Durum, Modüller, Parametre Eşlemesi ve Akvaryumlar.")

Apex sayfası kontrolcünün durumunu, ardından **Modüller**, **Parametre Eşlemesi** ve **Akvaryumlar**'ı gösterir.

- **Modüller**, takılı her Trident ve DŌS'u listeler. Kendi sayfasını açmak için birine dokunun.
- **Parametre Eşlemesi**, her probun neyi besleyeceğini seçtiğiniz yerdir. Problar Cora'ya kaynak olarak bildirir ve onları bir panoya koyabilirsiniz. [Parametre Eşlemesi ve problar](/help/mobile-probes) sayfasına bakın.
- **Akvaryumlar**, Apex'in hangi akvaryumlara hizmet ettiğini gösterir. Düzenlemek için **Değiştir**'e dokunun.
- **Prizler**, panodaki bir **Priz** widget'ından **Otomatik**, **Kapalı** ve **Açık** arasında geçer. Otomatik, kontrolü Apex programınıza geri verir. [Widget rehberi](/help/mobile-widgets#outlet) sayfasına bakın.

Apex'iniz kendi programını çalıştırmaya devam eder. Cora bir prizi yalnızca siz istediğinizde değiştirir.

## Trident {#trident}

Trident sayfası mevcut test durumunu ve reaktif ve atık su seviyelerini gösterir. Buradan bir test başlatabilirsiniz.

Ayrıca kalan testler ve atık şişesi için bir uyarı kurabilirsiniz, böylece Cora reaktif bitmeden ya da şişe dolmadan önce sizi uyarır. [Sarf malzemeleri](/help/mobile-consumables) sayfasına bakın.

## DŌS {#dos}

![AquaBus'ta yanıt vermeyen bir DŌS'u, son kalan süresi, bugünkü dozu ve günlük planıyla, ardından Uyarılar satırıyla gösteren bir DŌS sayfası](img/mobile-dos.webp "AquaBus'tan düşmüş bir DŌS: sayfa son bilinen değerlerini, bir Dikkat gerekiyor kartını ve Uyarılar satırını gösterir.")

Bir DŌS QD tam olarak bir DŌS gibi çalışır ve buradaki her şey ikisi için de geçerlidir. Bir Cora Max Apex'inizi okuduğunda dozaj kafaları DŌS sayfasında görünür. Priz listesinde hiçbir zaman görünmezler.

Her dozaj kafası neyi dozladığını, programını, bugün ne dozladığını ve kapta ne kadar kaldığını gösterir. Ayrıca bunun mevcut hızla kaç gün yeteceğini gösteren **Kalan süre**'yi de gösterir.

DŌS, AquaBus'ta yanıt vermeyi bırakırsa sayfası **Veri yolunda değil** ve bir **Dikkat gerekiyor** kartı gösterir. Bu durumda sayfadaki değerler şu anda yaptığı şey değil, bildirdiği son değerlerdir. Modülün AquaBus kablosunu ve Apex'i kontrol edin.

Her kafa için şunları yapabilirsiniz:

- Programını **Duraklat** ve **Sürdür**
- **Doldur**: Cora'ya kabın yeniden dolu olduğunu söylemek ya da içinde ne kadar olduğunu ayarlamak için (**Toplam Hacim** kabın boyutu, **Kalan Hacim** şu anda içinde olan miktardır, **Dolu** birini diğerine eşitler)
- **Şimdi dozajla**: elle ölçülü bir doz için

:::note Programları Apex Fusion'da düzenleyin
Cora programı gösterir ve neyin dozlandığını izler, ama programı değiştirmez. Programı, dozaj hızını ve doz sayısını Apex Fusion uygulamasında düzenlersiniz. Duraklatma, doldurma ve elle dozaj burada çalışır.
:::

:::note Elle dozaj yapmadan önce bir kafayı ölçün
Cora, kafa ölçülene kadar elle dozaj yapmaz. **Dozajlamak için ölç** ve **Yeniden ölç**, akvaryum için dozaj yapan Cora Max'tedir. Cora kafayı yirmi saniye çalıştırır, siz çıkan miktarı ölçersiniz, Cora da kafanın gerçek hızını hesaplar. Tek bir ölçüm her Cora Max ve Cora Mobile için geçerlidir. Her kafayı bir kez ve hortumunu değiştirdikten sonra yeniden ölçün.
:::

:::warning Bir DŌS kabı boşken de dozaj yapmaya devam eder
Ünitenin seviye sensörü yoktur ve kendi kendine durmaz. Cora'nın kap boşalmadan önce sizi uyarması için DŌS sayfasında **Uyarılar** altında her kafa için bir dolum uyarısı kurun. [Dozaj pompası uyarıları](#doser-alerts) bölümüne bakın.
:::

### Her kafanın ne için kullanıldığı {#dos-head-use}

Cora'nın ne yaptığını bilmesi ve ondan doğru söz etmesi için her kafaya bir **kullanım amacı** verin. Seçenekler **Takviye**, **Su değişimi: yeni tuzlu su girişi**, **Su değişimi: eski su çıkışı**, **Kalkwasser**, **Kalsiyum reaktörü**, **Yem**, **Su tamamlama** ve **Diğer**'dir. Bunu kafanın ayarlarında **Kullanım amacı** altında ayarlayın.

İki su değişimi kullanım amacı **çiftler** halinde gelir. Bir kafanın **Eşleştirilmiş kafa**'sını suyu diğer yöne taşıyan kafaya ayarlayın, Cora da ikisini tek bir su değişimi çifti olarak ele alır.

Her kullanım amacı için bir kap 1.000 L'ye kadar olabilir. Apex'in kendisi yalnızca 150 L'ye kadar sayar, bu yüzden bunun üstünde Cora kabı kafanın dozladığından kendisi izler. Kurarken **Toplam Hacim**'i girin. Cora ayrıca Apex'in kendi sayacını zaman zaman sıfırlar ve Etkinlik bunu *Apex'in kendi sayacı 150 L'ye sıfırlandı* olarak gösterir.

Her kafanın ayrıca bir **Elle verilecek en büyük dozaj** sınırı vardır, böylece bir yazım hatası elle bir dozu kastettiğinizden çok daha büyük bir şeye çeviremez. Büyük elle dozlar yalnızca kafanın hızı akvaryumun başında gerçek bir teste göre ölçüldükten ve siz kafanın ayarlarında **Büyük dozlar (Beta)**'yı açtıktan sonra kullanılabilir. Varsayılan olarak kapalıdır. Bunu yalnızca ilk büyük dozun çalışmasını akvaryumun başında izledikten sonra açın.

## Red Sea ReefBeat {#red-sea}

Her Red Sea ünitesinin yaptığı işe uyan bir sayfası vardır:

| Ünite | Sayfada | Yapabilecekleriniz |
|---|---|---|
| [ReefDose](#reefdose) | Her kafa, kabı ve ne dozladığı | Dozaj yapma, günlük dozu değiştirme, **Dozaj planı (Beta)**'nı düzenleme |
| [ReefRun](#reefrun) | Ana pompa ve skimmer pompası hızı ve durumu | Hızı değiştirme, bir pompayı açıp kapatma, **Pompa programı (Beta)**'nı düzenleme |
| [ReefMat](#reefmat) | Gün ve metre olarak kalan rulo | Matı ilerletme, **ReefMat ayarları (Beta)**'nı ayarlama, yeni bir rulo kaydetme |
| [ReefATO+](#reefato) | Hazne seviyesi ve su tamamlama etkinliği | Bir hazne uyarısı kurma |
| **ReefControl** *(Beta)* | Sıcaklık, pH, tuzluluk ve ORP probları | Ölçümlerini görüntüleme |
| **ReefWave**, **ReefLED** *(Beta)* | Mevcut modu | Şimdilik yalnızca görüntüleme |

ReefControl, ReefControl Power, ReefWave ve ReefLED'in adında *(Beta)* geçer ama herkese açıktır. [Beta özellikleri](/help/mobile-beta) sayfasına bakın.

**ReefControl Power** *(Beta)* prizleri, bir Apex prizi ile aynı priz kontrolünden yalnızca açık ya da kapalı olarak değiştirilen prizler şeklinde görünür. Bunlar için henüz otomatik mod yoktur.

Ünitenin ağından uzaktayken Cora Mobile Red Sea komutlarını akvaryumdaki bir Cora Max üzerinden gönderir. Bunu hiçbir Cora Max yapamıyorsa sayfa bunu söyler ve hiçbir şey gönderilmez.

## ReefDose {#reefdose}

![Cora Mobile'da bir ReefDose 4 sayfası](img/mobile-reefdose.webp "Durum, kafalar ve bugünün toplamı, tüketim için dozaj pompasını kullan, ardından her dozaj kafası.")

Her kafa için **Günlük dozaj** ve **Şişede kalan** değerlerini ayarlayabilir, **Şimdi dozajla**'yı çalıştırabilir ve **Zaman planını etkinleştir** diyebilirsiniz. Dolum uyarıları, [Dozaj pompası uyarıları](#doser-alerts) bölümünde anlatıldığı gibi zil ile kafa başına kurulur.

**Dozaj** bölümü **Yaklaşan dozlar**'ı, her kafanın bugün ne dozladığını (**Bugün şimdiye kadar dozlanan**) ve **Son 7 gün** ya da **Toplam** için **Kafa başına dozlanan**'ı gösterir. Cora bunu bir Cora Max ya da telefonunuz ev ağınızdayken okur.

### Bir dozaj planını düzenleme *(Beta)* {#reefdose-plan}

**Dozaj planı (Beta)**'nı açmak için bir ReefDose sayfasındaki takvim simgesine dokunun.

Bir plan, en fazla dört zaman aralığına bölünmüş günlük bir toplamdır. Her aralığın bir başlangıç ve bitiş saati, kaç doz vermesi gerektiği ve bir hızı vardır: **Fısıltı**, **Normal** ya da **Hızlı**. Aralık ekleyip kaldırın, sonra kaydedin. Cora, kafanın tüm planının yerine geçmeden önce göndermek üzere olduğunuz şeyi gösterir ve onaylamanızı ister.

Düzenleyici önce ünitede zaten olan planı okur, böylece boş bir formu değil gerçek planı düzenlersiniz.

## ReefRun {#reefrun}

ReefRun ana pompaları ve skimmer pompalarını kontrol eder. Bir dalga pompası değildir. Bir pompanın hızını değiştirebilir, onu açıp kapatabilir ve skimmer ayarlarını düzenleyebilirsiniz.

**Pompa programı (Beta)**'nı açmak için takvim simgesine dokunun. Bir program, tek bir pompa portunda en fazla altı bölümden oluşur. Her bölümün bir başlangıç saati ve bir hızı vardır ve kısa bir darbe ekleyebilir. Hız ya 0'dır ya da %5'ten yukarıdır. ReefDose planında olduğu gibi önce ünitedeki programı okur ve **Kaydet**, pompanın tüm programının yerine geçmeden önce onaylamanızı ister.

## ReefMat {#reefmat}

ReefMat sayfası gün ve metre olarak ne kadar rulo kaldığını gösterir. Matı elle ilerletmek için **Şimdi ilerlet**'e dokunun. Cora önce **Mat şimdi ilerletilsin mi?** diye sorar. Rulo için bir dolum uyarısı da kurabilirsiniz.

**ReefMat ayarları (Beta)** için dişliye dokunun:

- **Zamanlanmış ilerletme**, sayfada zaten bulunan otomatik ilerletme sensöründen ayrı, sabit zamanlı bir ilerletmeyi açar. Açın ve ne sıklıkla ve her ilerletmenin matı ne kadar taşıyacağını ayarlayın.
- **ReefMat modeli** ve **Motor konumu** (**Sol** ya da **Sağ**), Cora'ya hangi üniteye ve yöne sahip olduğunuzu söyler.

Yeni bir rulo taktıktan sonra bunu **Yeni rulo (Beta)** ile Cora'ya bildirin: kalınlığı ve biliyorsanız dış çapı. **Şimdi ilerlet** yalnızca zaten takılı olan matı ilerletir.

## ReefATO+ {#reefato}

ReefATO+ sayfası hazne seviyesini ve son su tamamlamaları gösterir. Zil ile bir hazne uyarısı kurun. Cora haznenin kaç gün yeteceğini son su tamamlama kullanımından tahmin eder ve bunu asistana da sorabilirsiniz.

## Bir Red Sea ünitesi kendini durdurduğunda {#red-sea-stops}

Bir ünite kendini durdurabilir. Örneğin bir ReefRun pompası skimmer kabı dolduğunda bunu yapar. Bu olduğunda sayfa nedenini söyler ve çözümü önerir:

| Ünite | Sayfada yazan | Dokunun |
|---|---|---|
| ReefRun | Hangi pompanın neden durduğu, örneğin *Kap dolu. Boşaltın, ardından devam edin.* | **Sürdür** |
| ReefRun ya da ReefMat | **Acil durdurma** | **Acil durumu temizle** |
| ReefMat | **Mat sıkıştı**, **Kurulum hatası** ya da **Ayar hatası** | **Sürdür** |
| ReefMat | *Yeni bir rulo yükleyin, sonra Red Sea uygulamasında onaylayın.* | **Zaten yeni bir rulo yükledim** |
| ReefMat | **Sensörün temizlenmesi gerekiyor** | **Sensör temizlendi** |
| ReefDose | Kafanın adıyla birlikte **Kafa arızası** | **Sıfırla** |
| ReefATO+ | **Arızayı Temizle** | **Sürdür** |

Bunlardan bazıları önce onay ister. Ünitenin ağından uzaktayken [Red Sea ReefBeat](#red-sea) bölümünde anlatıldığı gibi akvaryumdaki bir Cora Max üzerinden giderler.

## Dozaj pompası uyarıları {#doser-alerts}

Bir DŌS ve bir ReefDose uyarılarını kendi sayfalarında tutar. [Uyarı Merkezi](/help/mobile-alerts)'nin **Kurallar** sekmesinde her dozaj pompası için onu açan bir satır vardır ve bir dozaj pompası uyarısının **Dozaj pompasını aç** düğmesi de sizi buraya getirir.

Bir DŌS sayfasında **Uyarılar** kartına (ya da başlık çubuğundaki zile) dokunun. Sayfa her kafayı listeler ve her biri için şunları ayarlayabilirsiniz:

- *[kafa] · kalan gün*, örneğin *İyot · kalan gün*: bu kadar günlük stokun altına düşünce uyarı alırsınız
- *[kafa] · kalan*: kapta bu kadarın altında kalınca uyarı alırsınız
- **Atık kabında kalan alan**: eski suyu dışarı alan bir kafa için, atık kabı dolmaya başladığında uyarı alırsınız
- **Kaçırılan dozaj uyarıları**: kafa programlanmış bir dozu kaçırdığında size haber veren bir anahtar

Her eşiğin kendi anahtarı vardır, böylece birini kapatıp değerini saklayabilirsiniz. Bitirdiğinizde **Kaydet**'e dokunun.

Bir ReefDose sayfasında başlık çubuğundaki zile dokunun. Her kafanın kendi kalan gün eşiği ve anahtarı vardır.

Varsayılanlar ve diğer sarf malzemeleri [Sarf malzemeleri](/help/mobile-consumables) sayfasında.

## Jecod / Jebao pompaları {#jecod}

Pompa sayfası mevcut dalga desenini (mod) ve yoğunluğu gösterir ve ikisini de değiştirebilirsiniz. En üstten **Tüm gün aynı** ya da **Program**'ı seçin. Günlük program hazırlamak ve onu kopyalamak, kaydetmek ya da paylaşmak [Ekipman programları](/help/mobile-schedules) sayfasında.

Pompa bir grubun parçasıysa sayfa onun rolünü gösterir, örneğin **Grubu yönetir**, **Takip eder: eş zamanlı** ya da **Takip eder: değişimli**.

### Besleme duraklatması {#jecod-feeding}

Pompanın sayfasındaki **Besleme** bölümünden bir besleme duraklatması başlatın. Bazı pompalar duraklatmayı kendileri bitirir ve sayfada *Pompa bunu kendiliğinden bitirir.* yazar.

:::warning Besleme duraklatması sırasında pompanın sayfasını açık tutun
Bazı pompalar bir beslemeyi kendileri bitirmez ve sayfa bunu söyler. Bunlar için ve programda olan her pompa için Cora Mobile dalga desenini ve programı yalnızca pompanın sayfası açık kaldığı sürece geri getirir. Sayfadan çıkarsanız pompa, siz onu yeniden değiştirene ya da **Program**'a dokunana kadar besleme modunda durmuş ya da programının dışında kalır.
:::

Bir besleme başlatmak için Bluetooth bir pompanın telefonunuzun menzilinde, bir ağ pompasının da ağınızda olması gerekir.

### Arıza kontrolleri {#jecod-fault-checks}

**Arıza kontrolleri**, sıkışmış ya da kuru çalışan bir pompa gibi bir arıza konusunda sizi uyarabilmek için Cora'nın pompayı ne sıklıkla yeniden okuyacağını ayarlar. Kapalıya ayarlarsanız o pompa için bu uyarılar durur. Arıza kontrolleri akvaryumda bir Cora Max gerektirir. Seçiminiz kaydedilir ve bir Cora Max eklendiğinde kontroller başlar. **Bunu bu akvaryumdaki her pompa için kullan**, ayarı hepsine kopyalar.

## AquaWiz {#aquawiz}

AquaWiz kartı alkalinite ölçümlerinizi ve üniteniz bildiriyorsa pH'ı gösterir. Ayrıca hedef KH'nizi, dozaj yoğunluğunuzu ve dozaj kurulu bir ünite için saatlik en yüksek dozunu ve kapta ne kadar alkalinite takviyesi kaldığını gösterir. Bunlar doğrudan AquaWiz ayarlarınızdan gelir, bu yüzden onları AquaWiz uygulamasında değiştirin. Cora bir AquaWiz'i kontrol edemez.

Üniteniz kabını izliyorsa Cora takviye azaldığında, varsayılan olarak 100 mL'de, sizi uyarır. Bunu [Uyarı Merkezi](/help/mobile-alerts)'ndeki kuralından değiştirin.

## Maxspect {#maxspect}

:::note Beta
**Beta.** Maxspect Beta aşamasındadır ve yalnızca Beta kullanıcılarına açıktır. Beta kullanıcısı değilseniz onu **Cihaz Ekle** içinde görmezsiniz. Beta erişimi istemek için [destekle iletişime geçin](/support.html). Bazı kontroller sınırlı olabilir ve burada gördükleriniz güncellemeler arasında değişebilir. Bir şey anlatıldığı gibi çalışmıyorsa [Sorun bildirme](/help/mobile-support) sayfasından bize bildirin. Ayrıntılar [Beta özellikleri](/help/mobile-beta) sayfasında.
:::

Gyre sayfası gyre'nin çalışıp çalışmadığını, **Gyre A** ve **Gyre B**'nin dalga desenini ve hızını ve en son ne zaman okunduklarını gösterir. Buradan şunları yapabilirsiniz:

- Durumunun yanındaki anahtarla gyre'yi açıp kapatın. Cora önce onaylamanızı ister. Kapatmak iki gyre'yi de durdurur ve programa dokunmaz.
- Her gyre'nin dalga desenini ve pompa hızını, süresi olan desenler için süreyi ve iki gyre'nin bağlı olup olmadığını ayarlamak için **Ayarları değiştir**'e dokunun. Cora neyin değişeceğini listeler ve onaylamanızı ister. Değişimli mod Maxspect uygulamasında ayarlanır ve onu çalıştıran bir gyre rampalarını ve bekleme sürelerini korur.
- Gyre'de kayıtlı program okunamıyorsa **Programı ayarla**'ya dokunun. Gyre'nin yeniden başlayabilmesi için iki gyre'yi de ayarlar.
- Gyre'nin günlük programını **Program** kartında görün. Onu burada yalnızca görüntüleyebilirsiniz. Programı Maxspect uygulamasında ayarlayın.
- **Pompa sağlığı**'nı kontrol edin. Pompanın bir sonraki temizliğe ne zaman ihtiyaç duyacağını (pompa bunu kendisi geri sayar), A kafasının çektiği akımı, hangi kafaların takılı olduğunu ve yazılımı gösterir. Getirmek için **Oku**'ya dokunun.

:::note Cora Mobile bir gyre'ye nasıl ulaşır
Akvaryuma bir Cora Max hizmet ediyorsa Cora Mobile, siz evden uzaktayken bile o Cora Max üzerinden gider. **Ayarları değiştir** bu durumda o Cora Max'in son okumasından başlar. Aksi halde telefonunuz gyre ile doğrudan konuşur ve gyre'nin ağında olması gerekir. Sayfayı açmak gyre'yi okur. Sayfa daha eski kayıtlı bir okuma gösteriyorsa **Ayarları değiştir**, siz yenile'ye dokunana kadar gizli kalır.
:::

## GHL ProfiLux ve Mitras {#ghl}

:::note Beta
**Beta.** GHL Beta aşamasındadır ve yalnızca Beta kullanıcılarına açıktır. Beta kullanıcısı değilseniz onu **Cihaz Ekle** içinde görmezsiniz. Beta erişimi istemek için [destekle iletişime geçin](/support.html). Bazı ölçümler ya da kontroller henüz çalışmayabilir ve burada gördükleriniz güncellemeler arasında değişebilir. Bir şey anlatıldığı gibi çalışmıyorsa [Sorun bildirme](/help/mobile-support) sayfasından bize bildirin. Ayrıntılar [Beta özellikleri](/help/mobile-beta) sayfasında.
:::

Kontrolcünün sayfası problarını, prizlerini, dozaj pompalarını ve seviye sensörlerini ve Director modellerinde KH ve iyon test sonuçlarını gösterir.

Kontroller, cihazın sayfasında **Cora'dan kontrole izin ver (Beta)**'yı açana kadar kapalı kalır. Varsayılan olarak kapalıdır ve onu açmak Cora'nın o kontrolcüye besleme duraklatması, bakım, su değişimi, fırtına, aydınlatma, ayar noktası ve priz komutları göndermesini sağlar. Cihazı ekleyebildiğiniz sürece bu anahtar ek erişim gerektirmez.

Açıldığında:

- Bir priz **Her zaman açık**, **Her zaman kapalı** ya da onu kontrolcünün kendi programına geri vermek için **Otomatiğe dön** olarak ayarlanabilir.
- Sıcaklık ya da pH gibi bir ayar noktası izin verilen aralığını gösterir ve dışındaki bir değeri reddeder.

:::warning Bir priz ya da ayar noktası değişikliği kontrolcünün kendisine kaydedilir
Yalnızca Cora'da saklanmaz. Bir prizi Her zaman açık ya da Her zaman kapalı yapmak, siz Otomatiğe dön'ü seçene kadar o priz için kontrolcünün kendi programını geçersiz kılar.
:::

Bir priz ya da ayar noktası bir ısıtıcıya ya da ana pompaya ait gibi görünüyorsa Cora göndermeden önce iki kez onaylamanızı ister.

Bir dozaj pompasının kabı azalıyorsa Cora sizi diğer sarf malzemelerinde olduğu gibi uyarır. Varsayılan %20 doluluktur ve bunu [Uyarı Merkezi](/help/mobile-alerts)'ndeki dozaj pompası kuralından değiştirebilirsiniz.

:::note ProfiLux mini
Bir mini yalnızca prizlerini açıp kapatabilir. Ayar noktaları ve besleme duraklatması gibi buradaki diğer her şey bir ProfiLux 3, 4 ya da Mitras gerektirir.
:::

Kontrolcü değişikliği reddederse GHL API'sinin tam erişimle açık olduğunu kontrol edin. GHL bunu her yazılım güncellemesinden sonra kapatır. Adımlar [Sorun giderme](/help/troubleshooting) sayfasında.

## HYDROS {#hydros}

:::note Beta
**Beta.** HYDROS Beta aşamasındadır ve yalnızca Beta kullanıcılarına açıktır. Beta kullanıcısı değilseniz onu **Cihaz Ekle** içinde görmezsiniz. Beta erişimi istemek için [destekle iletişime geçin](/support.html). Bazı ölçümler ya da kontroller henüz çalışmayabilir ve burada gördükleriniz güncellemeler arasında değişebilir. Bir şey anlatıldığı gibi çalışmıyorsa [Sorun bildirme](/help/mobile-support) sayfasından bize bildirin. Ayrıntılar [Beta özellikleri](/help/mobile-beta) sayfasında.
:::

Burada gördükleriniz bağladığınız anahtara bağlıdır. Bir **Read** (okuma) anahtarı yalnızca girişlerini verir. Bir **Write** (yazma) anahtarı çıkışları, modları, dozajı ve test cihazı komutlarını ve hangi tür anahtarda olduğunuzu hatırlatan bir sayfa şeridini ekler.

Bir yazma anahtarıyla da kontroller, cihazın sayfasında **Cora'dan kontrole izin ver (Beta)**'yı açana kadar kapalı kalır. Varsayılan olarak kapalıdır.

Açıldığında sayfa şunları gösterebilir:

- **ÇIKIŞLAR**: açık/kapalı bir çıkış için bir anahtar, pompa ya da ışık gibi bir seviye için bir kaydırıcı ya da bir bayrak için bir düğme. Geçersiz kılınmış bir çıkış, onu kendi programına geri vermek için bir **Programa geri dön** düğmesiyle **Geçersiz kılındı** gösterir.
- **MOD**: Besleme ya da Su Değişimi gibi modlar, bir sıra seçenek olarak. Birine dokunmak onay ister.
- **DOZAJ BAŞLIKLARI**: her biri bir **Dozla** düğmesiyle ve kendi sınırlarını (elle en büyük doz ve günlük üst sınır) ayarladığınız bir **Başlık ayarları** girişiyle. Bir kafanın sınırından ya da kendi günlük üst sınırından o gün kalandan fazlasını istemek, mesajdaki sayılarla birlikte reddedilir.
- **TEST KOMUTLARI**: bağlı bir iV ya da Maven için, bir düğmeden çalıştırılır ve önce onaylanır.

Kontrolcü bir süredir bildirmediyse sayfa bunu söyler ve ölçümler güncel olmayabilir. Çevrimdışı görünürken gönderilen bir komut hiç gönderilmez ve sayfa bunu da size söyler.

## Focustronic {#focustronic}

:::note Beta
**Beta.** Focustronic Beta aşamasındadır ve yalnızca Beta kullanıcılarına açıktır. Beta kullanıcısı değilseniz onu **Cihaz Ekle** içinde görmezsiniz. Beta erişimi istemek için [destekle iletişime geçin](/support.html). Ayrıntılar [Beta özellikleri](/help/mobile-beta) sayfasında.
:::

Her cihaz durumunu, yazılımını, son testini ve bir Alkatronic için ölçtüğü alkalinite ve pH'ı gösterir. Ayrıca her birinde ne kadar kaldığıyla pompaları, parametreleri, şişeleri ve reaktif ya da tampon uyarılarını görürsünüz. Cora her 30 dakikada bir Focustronic'ten yeni ölçümler ister.

**Kontroller** altında **Şimdi ölç**, bir pompadan **Şimdi dozla** (bir seferde en fazla 500 mL) ve bir Mastertronic'te **Şimdi test et** yapabilirsiniz. Her biri önce onay ister. Cora bir dozu asla yeniden denemez, bu yüzden sonuç bilinmiyor diyorsa cihazı kontrol edin. Komutlar Cora'nın kontrol etmediği Focustronic sunucularından geçer ve yalnızca cihaz çevrimiçiyken kullanılabilir.

## EcoTech, Inkbird ve kameralar {#ecotech-inkbird-cameras}

:::note Beta
**Beta.** EcoTech, Inkbird ve kameralar Beta aşamasındadır ve yalnızca Beta kullanıcılarına açıktır. Beta kullanıcısı değilseniz bunları **Cihaz Ekle** içinde görmezsiniz. Beta erişimi istemek için [destekle iletişime geçin](/support.html).
:::

Bunların kendi sayfaları vardır:

- EcoTech Radion ışıkları, VorTech pompaları ve Versa dozaj pompaları: [EcoTech ışıkları, pompaları ve dozaj pompaları](/help/mobile-ecotech)
- Inkbird oda havası monitörleri yalnızca ölçüm bildirir, bu yüzden kontrol edilecek bir şey yoktur: [Ekipmanınızı bağlama](/help/mobile-connections#inkbird-room-air-monitor)
- Kameralar ve Skimmer Gözcüsü: [Kameralar ve Skimmer Gözcüsü](/help/mobile-cameras)

## Bir şeyi değiştirdikten sonra ne olur {#what-happens-after-you-change-something}

Her değişiklik, geldiği yüzeyle birlikte [Etkinlik](/help/mobile-activity) içine kaydedilir. Bir cihaz bir değişikliği kabul etmezse bu da orada kaydedilir.
