---
title: Ekipmanınızı kontrol etme
description: Canlı durumunu görmek ve prizleri, pompaları, dozaj kafalarını ve test cihazlarını marka marka değiştirmek için bir cihazın sayfasını açın.
section: Cora Mobile
reviewed: 2026-10-24
order: 13
group: Equipment
twin: max-device-control
---

Canlı durumunu görmek ve yaptığı şeyi değiştirmek için bir cihazın kendi sayfasını kullanın. Onu **Cihazlar** sekmesinde cihaza dokunarak ya da panodaki kutucuğuna dokunarak açın.

![Cora Mobile'da bir ReefATO+ sayfası](img/mobile-device-detail.webp "Durum, bugünün ölçümleri ve su seviyesi, ardından sızıntı, dolumlar ve prob kalibrasyonu.")

Her cihaz sayfası aynı şekilde düzenlenmiştir. Ad ve ayrıntılar en üstte, ardından bir sıra canlı ölçüm, cihazın bildirdiği her durum ve kontrolleri gelir. Başlık çubuğundaki zil, [Sarf malzemeleri](/help/mobile-consumables) sayfasında anlatıldığı gibi o cihaz için uyarı eşiklerini ayarlar. Bir cihazı ilk başta nasıl ekleyeceğiniz [Ekipmanınızı bağlama](/help/mobile-connections) sayfasında.

Ekipmanınıza atlayın: [Neptune Apex](#neptune-apex) · [Trident](#trident) · [DŌS](#dos) · [Red Sea](#red-sea) · [ReefDose](#reefdose) · [ReefRun](#reefrun) · [ReefMat](#reefmat) · [ReefATO+](#reefato) · [Dozaj pompası uyarıları](#doser-alerts) · [Jecod](#jecod) · [AquaWiz](#aquawiz)

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

Apex sayfası kontrolörün durumunu, ardından **Modüller**, **Parametre Eşlemesi** ve **Akvaryumlar**'ı gösterir.

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

Her dozaj kafası neyi dozladığını, zamanlamasını, bugün ne dozladığını ve kapta ne kadar kaldığını gösterir. Ayrıca bunun mevcut hızla kaç gün yeteceğini gösteren **Kalan süre**'yi de gösterir.

DŌS, AquaBus'ta yanıt vermeyi bırakırsa sayfası **Veri yolunda değil** ve bir **Dikkat gerekiyor** kartı gösterir. Bu durumda sayfadaki değerler şu anda yaptığı şey değil, bildirdiği son değerlerdir. Modülün AquaBus kablosunu ve Apex'i kontrol edin.

Her kafa için şunları yapabilirsiniz:

- Zamanlamasını **Duraklat** ve **Sürdür**
- **Doldur**: Cora'ya kabın yeniden dolu olduğunu söylemek ya da içinde ne kadar olduğunu ayarlamak için (**Toplam Hacim** kabın boyutu, **Kalan Hacim** şu anda içinde olan miktardır, **Dolu** birini diğerine eşitler)
- **Şimdi dozajla**: elle ölçülü bir doz için

:::note Zamanlamaları Apex Fusion'da düzenleyin
Cora zamanlamayı gösterir ve neyin dozlandığını izler, ama zamanlamayı değiştirmez. Zamanlamayı, dozaj hızını ve doz sayısını Apex Fusion uygulamasında düzenlersiniz. Duraklatma, doldurma ve elle dozaj burada çalışır.
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

Her kafanın ayrıca bir **Elle verilecek en büyük dozaj** sınırı vardır, böylece bir yazım hatası elle bir dozu kastettiğinizden çok daha büyük bir şeye çeviremez. Büyük elle dozlar yalnızca kafanın hızı akvaryumun başında gerçek bir teste göre ölçüldükten ve siz kafanın ayarlarında **Büyük dozlar**'ı açtıktan sonra kullanılabilir. Varsayılan olarak kapalıdır. Bunu yalnızca ilk büyük dozun çalışmasını akvaryumun başında izledikten sonra açın.

## Red Sea ReefBeat {#red-sea}

Her Red Sea ünitesinin yaptığı işe uyan bir sayfası vardır:

| Ünite | Sayfada | Yapabilecekleriniz |
|---|---|---|
| [ReefDose](#reefdose) | Her kafa, kabı ve ne dozladığı | Dozaj yapma, günlük dozu değiştirme, **Dozaj planı**'nı düzenleme |
| [ReefRun](#reefrun) | Ana pompa ve skimmer pompası hızı ve durumu | Hızı değiştirme, bir pompayı açıp kapatma |
| [ReefMat](#reefmat) | Gün ve metre olarak kalan rulo | Matı ilerletme, **ReefMat ayarları**'nı ayarlama, yeni bir rulo kaydetme |
| [ReefATO+](#reefato) | Depo seviyesi ve su tamamlama etkinliği | Bir depo uyarısı kurma |



Ünitenin ağından uzaktayken Cora Mobile Red Sea komutlarını akvaryumdaki bir Cora Max üzerinden gönderir. Bunu hiçbir Cora Max yapamıyorsa sayfa bunu söyler ve hiçbir şey gönderilmez.

## ReefDose {#reefdose}

![Cora Mobile'da bir ReefDose 4 sayfası](img/mobile-reefdose.webp "Durum, kafalar ve bugünün toplamı, tüketim için dozaj pompasını kullan, ardından her dozaj kafası.")

Her kafa için **Günlük dozaj** ve **Şişede kalan** değerlerini ayarlayabilir, **Şimdi dozajla**'yı çalıştırabilir ve **Zamanlamayı etkinleştir** diyebilirsiniz. Dolum uyarıları, [Dozaj pompası uyarıları](#doser-alerts) bölümünde anlatıldığı gibi zil ile kafa başına kurulur.

**Dozaj** bölümü **Yaklaşan dozlar**'ı, her kafanın bugün ne dozladığını (**Bugün şimdiye kadar dozlanan**) ve **Son 7 gün** ya da **Toplam** için **Kafa başına dozlanan**'ı gösterir. Cora bunu bir Cora Max ya da telefonunuz ev ağınızdayken okur.

### Bir dozaj planını düzenleme {#reefdose-plan}

**Dozaj planı**'nı açmak için bir ReefDose sayfasındaki takvim simgesine dokunun.

Bir plan, en fazla dört zaman aralığına bölünmüş günlük bir toplamdır. Her aralığın bir başlangıç ve bitiş saati, kaç doz vermesi gerektiği ve bir hızı vardır: **Fısıltı**, **Normal** ya da **Hızlı**. Aralık ekleyip kaldırın, sonra kaydedin. Cora, kafanın tüm planının yerine geçmeden önce göndermek üzere olduğunuz şeyi gösterir ve onaylamanızı ister.

Düzenleyici önce ünitede zaten olan planı okur, böylece boş bir formu değil gerçek planı düzenlersiniz.

## ReefRun {#reefrun}

ReefRun ana pompaları ve skimmer pompalarını kontrol eder. Bir dalga pompası değildir. Bir pompanın hızını değiştirebilir, onu açıp kapatabilir ve skimmer ayarlarını düzenleyebilirsiniz.


## ReefMat {#reefmat}

ReefMat sayfası gün ve metre olarak ne kadar rulo kaldığını gösterir. Matı elle ilerletmek için **Şimdi ilerlet**'e dokunun. Cora önce **Mat şimdi ilerletilsin mi?** diye sorar. Rulo için bir dolum uyarısı da kurabilirsiniz.

**ReefMat ayarları** için dişliye dokunun:

- **Zamanlanmış ilerletme**, sayfada zaten bulunan otomatik ilerletme sensöründen ayrı, sabit zamanlı bir ilerletmeyi açar. Açın ve ne sıklıkla ve her ilerletmenin matı ne kadar taşıyacağını ayarlayın.
- **ReefMat modeli** ve **Motor konumu** (**Sol** ya da **Sağ**), Cora'ya hangi üniteye ve yöne sahip olduğunuzu söyler.

Yeni bir rulo taktıktan sonra bunu **Yeni rulo** ile Cora'ya bildirin: kalınlığı ve biliyorsanız dış çapı. **Şimdi ilerlet** yalnızca zaten takılı olan matı ilerletir.

## ReefATO+ {#reefato}

ReefATO+ sayfası depo seviyesini ve son su tamamlamaları gösterir. Zil ile bir depo uyarısı kurun. Cora deponun kaç gün yeteceğini son su tamamlama kullanımından tahmin eder ve bunu asistana da sorabilirsiniz.

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
- **Kaçırılan dozaj uyarıları**: kafa zamanlanmış bir dozu kaçırdığında size haber veren bir anahtar

Her eşiğin kendi anahtarı vardır, böylece birini kapatıp değerini saklayabilirsiniz. Bitirdiğinizde **Kaydet**'e dokunun.

Bir ReefDose sayfasında başlık çubuğundaki zile dokunun. Her kafanın kendi kalan gün eşiği ve anahtarı vardır.

Varsayılanlar ve diğer sarf malzemeleri [Sarf malzemeleri](/help/mobile-consumables) sayfasında.

## Jecod / Jebao pompaları {#jecod}

Pompa sayfası mevcut dalga desenini (mod) ve yoğunluğu gösterir ve ikisini de değiştirebilirsiniz. Durumu başlık satırında, pompanın adının yanındadır. **Tüm gün aynı** ve **Zamanlama** seçenekli bir anahtar çalışanı *· çalışıyor* ile işaretler ve sayfa onda açılır. Günlük zamanlama hazırlamak ve onu kopyalamak, kaydetmek ya da paylaşmak [Ekipman zamanlamaları](/help/mobile-schedules) sayfasında.

Pompa bir grubun parçasıysa sayfa onun rolünü gösterir, örneğin **Grubu yönetir**, **Takip eder: eş zamanlı** ya da **Takip eder: dönüşümlü**.

### Besleme duraklatması {#jecod-feeding}

Pompanın sayfasında **Besleme** bölümünden bir besleme duraklatması başlatın: **5**, **10**, **15** ya da **30** dk'ya dokunun. Bazı pompalar duraklatmayı kendileri bitirir ve sayfada *Pompa bunu kendiliğinden bitirir.* yazar.

:::warning Besleme duraklatması sırasında pompanın sayfasını açık tutun
Bazı pompalar bir beslemeyi kendileri bitirmez ve sayfa bunu söyler. Bunlar için ve zamanlamada olan her pompa için Cora Mobile dalga desenini ve zamanlamayı yalnızca pompanın sayfası açık kaldığı sürece geri getirir. Sayfadan çıkarsanız pompa, siz onu yeniden değiştirene ya da **Zamanlama**'ya dokunana kadar besleme modunda durmuş ya da zamanlamasının dışında kalır.
:::

Eviniz bir Cora Max içeriyorsa, süre dolduğunda besleme molasını o bitirir ve pompayı programına döndürür; Cora Mobile kapalı olsa bile. Yukarıdaki uyarı bu durumda yalnızca Cora Max yoksa geçerlidir.

Bir besleme başlatmak için Bluetooth bir pompanın telefonunuzun menzilinde, bir ağ pompasının da ağınızda olması gerekir.

### Arıza kontrolleri {#jecod-fault-checks}

**Arıza kontrolleri**, sıkışmış ya da kuru çalışan bir pompa gibi bir arıza konusunda sizi uyarabilmek için Cora'nın pompayı ne sıklıkla yeniden okuyacağını ayarlar. Kapalıya ayarlarsanız o pompa için bu uyarılar durur. Arıza kontrolleri akvaryumda bir Cora Max gerektirir. Seçiminiz kaydedilir ve bir Cora Max eklendiğinde kontroller başlar. **Bunu bu akvaryumdaki her pompa için kullan**, ayarı hepsine kopyalar.

## AquaWiz {#aquawiz}

AquaWiz kartı alkalinite ölçümlerinizi ve üniteniz bildiriyorsa pH'ı gösterir. Cora bir AquaWiz'i kontrol edemez, bu yüzden ayarlarını AquaWiz uygulamasında değiştirin.

Cihaz sayfasındaki **Denetleyici** bölümünde Cora, kontrolörün bildirdiklerini gösterir; her satır yalnızca kontrolör bildiriyorsa görünür:

- hedef KH;
- ne kadar alkalinite takviyesi kaldığı ve kontrolörde belirlediğiniz uyarı seviyesi (örneğin *100 mL altında düşük*);
- 1 dKH için kaç mL gerektiği (örneğin *dKH başına 48 mL doz*);
- ölçüm başına en yüksek doz (*Ölçüm başına en fazla 20 mL*);
- yazılım sürümü.

Ölçümlerin altında kart, sonuncusunun ne zaman ölçüldüğünü (örneğin *Ölçüm: 14:00*) ve nereden geldiğini söyler: **Cora Max cihazınızdan saatlik** ya da **AquaWiz bulutundan, 12 saatte bir**. Ayrıca **pH değişimi**ni de gösterir. Sayfayı açmak yeni bir ölçüm ister, **Şimdi oku** da yeniden ister; en fazla 15 dakikada bir. Bir ölçüm değişmediyse bu normaldir: ünite ölçümü yalnızca ara sıra yapar.

Kart ayrıca pompayı ve pH probunu gösterir. Pompa arıza bildirdiğinde, pH probu bozulduğunda ya da ömrünün sonuna yaklaştığında Cora sizi uyarır. Bu, Cora Max olsun olmasın her AquaWiz için geçerlidir. Bir Cora Max üniteyi her saat okuyorsa kart su kutusu seviyesini de gösterir ve seviye bir saatten uzun süre düşük ya da yüksek kalırsa Cora sizi uyarır.

Üniteniz kabını izliyorsa Cora takviye azaldığında, kontrolörde belirlediğiniz uyarı seviyesinde sizi uyarır. Bunu yine [Uyarı Merkezi](/help/mobile-alerts)'ndeki kuralından değiştirebilirsiniz ve değişikliğiniz korunur.


## Bir şeyi değiştirdikten sonra ne olur {#what-happens-after-you-change-something}

Her değişiklik, geldiği yüzeyle birlikte [Etkinlik](/help/mobile-activity) içine kaydedilir. Bir cihaz bir değişikliği kabul etmezse bu da orada kaydedilir.
