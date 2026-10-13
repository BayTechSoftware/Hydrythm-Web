---
title: Ekipmanınızı bağlama
description: Bir Neptune Apex, Red Sea ReefBeat, Jecod ya da AquaWiz ünitesini ve Beta'da Maxspect, GHL, HYDROS, Focustronic ve Inkbird ekipmanını Cora'ya nasıl bağlayacağınız.
section: Cora Mobile
reviewed: 2026-10-13
order: 12
group: Equipment
---

Bu sayfa her ekipman markasını Cora'ya nasıl bağlayacağınızı ve her bağlantının neye ihtiyaç duyduğunu gösterir. Hepsi aynı şekilde başlar: **Cihazlar → Cihaz Ekle**, ardından markayı seçin.

![Bir Beta kullanıcısı için Cihaz Ekle listesi](img/mobile-add-device-beta.webp "Marka listesi. Beta markalarında bir Beta çipi bulunur.")

*(Beta)* işaretli markalar yalnızca Beta kullanıcılarına açıktır. [Beta özellikleri](/help/mobile-beta) sayfasına bakın.

| Marka | Ne açılır | Cora Max olmadan |
|---|---|---|
| Cora | Wi-Fi ya da Bluetooth üzerinden yeni bir Cora Max araması | |
| Neptune Apex | Bir ağ taraması ya da IP adresi, ardından hangi akvaryumlara hizmet ettiği | Yalnızca yerel |
| Red Sea | Ağınızda bir tarama, ardından her ünitenin hangi akvaryuma ait olduğu | Yalnızca yerel |
| Jecod / Jebao | Ağınızda bir tarama ya da Bluetooth | Yalnızca yerel |
| AquaWiz | AquaWiz girişiniz | Çalışır |
| Maxspect *(Beta)* | Jecod ile aynı tarama | **Cora Max Gerektirir** |
| GHL *(Beta)* | Adresi, arayüzü ve mini için giriş bilgisi | **Cora Max Gerektirir** |
| HYDROS *(Beta)* | HYDROS uygulamasından bir cihaz anahtarı | Çalışır |
| Focustronic *(Beta)* | Focustronic girişiniz, ardından her cihazın hangi akvaryuma ait olduğu | Çalışır |
| EcoTech *(Beta)* | Radion ışıkları, VorTech pompaları ve Versa dozaj pompaları için bir Bluetooth taraması. [EcoTech ışıkları, pompaları ve dozaj pompaları](/help/mobile-ecotech) sayfasına bakın | **Cora Max Gerektirir** |
| Inkbird *(Beta)* | Oda havası monitörünüz için bir Bluetooth taraması | **Cora Max Gerektirir** |
| Kamera *(Beta)* | Wyze, Tapo, Sonoff ya da başka bir RTSP kamera. [Kameralar ve Skimmer Gözcüsü](/help/mobile-cameras) sayfasına bakın | **Cora Max Gerektirir** |

## Cora Max olmadan: yalnızca yerel {#local-only}

Neptune Apex, Red Sea ve Jecod ekipmanı ev ağınızdadır (ya da Bluetooth'ta). Cora Max'iniz yoksa (ya da eklediğiniz akvaryumda yoksa) bu markaların ekleme ekranında *Bu entegrasyon, Cora Max olmadan yalnızca Mobile uygulamasında yerel olarak çalışır.* yazar. Bunun anlamı şudur:

- Telefonunuz, Cora Mobile aynı ağda açıkken ya da Bluetooth menzilindeyken ekipmanı okur ve kontrol eder.
- Evden uzaktayken telefonunuzun kaydettiği son ölçümleri görürsünüz ve onu kontrol edemezsiniz.

Akvaryumdaki bir Cora Max bu ekipmanı gece gündüz okur ve siz uzaktayken komutlarınızı iletir. AquaWiz, HYDROS ve Focustronic'e üreticinin kendi hizmeti üzerinden ulaşılır, bu yüzden Cora Max olmadan her yerden çalışırlar. **Cora Max Gerektirir** işaretli satırlar, akvaryumda bir Cora Max olana kadar soluk görünür. Ayrıntılar [Birden fazla Cora cihazı](/help/mobile-multi-device) sayfasında.

## Neptune Apex {#neptune-apex}

Cora, Apex'inizi problar, prizler ve taktığınız tüm genişletme modülleri dahil yerel ağınız üzerinden okur.

1. **Cihazlar → Cihaz Ekle → Neptune Apex** yoluna gidin.
2. **APEX için Ağı Tara**'ya dokunun ve Apex'inizi seçin ya da adresini **Veya IP'yi elle girin:** altına yazın.
3. **Apex girişi (yalnızca Apex'te bir tane ayarladıysanız):** alanını doldurun. Bir şifre ayarlamadıysanız şifreyi boş bırakın.
4. **APEX'ten parametreleri yükle**'ye dokunun ve **Takip edilecek parametreler** altında istediklerinizi işaretleyin.
5. **Sorgulama Sıklığı**'nı ayarlayın. Onu kapalı bırakmayın: sorgulama kapalıyken Apex'i hiçbir şey okumaz ve ölçümleri eskir.
6. **Devam et**'e dokunun, **Bu Apex hangi akvaryumlara hizmet veriyor?** altında her akvaryumu işaretleyin, sonra **Kaydet**'e dokunun. Bir Apex birden fazla akvaryuma hizmet edebilir.

Tarama hiçbir şey bulamazsa telefonunuzun Apex ile aynı Wi-Fi'da olduğunu kontrol edin ya da IP adresini kendiniz girin.

Bağlandıktan sonra Apex'inizin bildirdiği her prob panoya koyabileceğiniz bir kaynak olur. Prizler kontrol olarak görünür ve takılı her genişletme modülü kendi cihaz kutucuğunu alır. Kendi Apex programınız tam olarak ayarladığınız gibi çalışmaya devam eder. Neleri kontrol edebileceğiniz [Ekipmanınızı kontrol etme](/help/mobile-device-control#neptune-apex) sayfasında.

## Red Sea ReefBeat {#red-sea-reefbeat}

Cora, yerel ağınızdaki ReefBeat ekipmanıyla konuşur. **ReefDose**, **ReefATO+**, **ReefMat** ve **ReefRun**'ı ve ayrıca adlarında *(Beta)* geçen ama herkese açık olan **ReefControl**, **ReefControl Power**, **ReefWave** ve **ReefLED**'i destekler.

1. Üniteyi önce Red Sea'nin ReefBeat uygulamasında kurun ve telefonunuzla aynı ağda olduğunu kontrol edin.
2. **Cihazlar → Cihaz Ekle → Red Sea** yoluna gidin. Cora ağınızı tarar.
3. Her ünitenin hangi akvaryuma ait olduğunu seçin.

Bir Red Sea ünitesi tek bir akvaryuma hizmet eder. Farklı birini seçmek onu oraya taşır.

Her ünite kendi cihaz sayfasını alır ve ölçümleri kaynak olur. ReefDose kafalarını ve kaplarını, ReefATO+ haznesini ve dolumlarını, ReefMat kalan günlerini, ReefRun da pompa durumunu bildirir. ReefControl problarını aynı şekilde bildirir. ReefWave ve ReefLED şimdilik yalnızca modlarını gösterir. Her sayfanın neler yapmanızı sağladığı [Ekipmanınızı kontrol etme](/help/mobile-device-control#red-sea) sayfasında.

## Jecod / Jebao {#jecod}

Cora Jecod pompalarına bağlanır ve onları okuyup kontrol edebilir. Birini **Cihazlar → Cihaz Ekle → Jecod** yolundan ekleyin. Bir Jecod pompası Cora'ya iki yoldan biriyle ulaşır ve onunla ne yapabileceğinizi bu belirler.

![Cora Mobile'da henüz pompa bulunamamış Pompa ekle ekranı](img/mobile-connections.webp "Henüz hiçbiri görülmedi: tarama neye ihtiyaç duyduğunu ve bir pompanın neden bir taramayı kaçırabileceğini açıklar.")

**Ağınız üzerinden.** Tarama kendini duyuran pompaları bulur, bu yüzden adres yazmanız gerekmez. Bir ağ pompasını, gücü açık ve ulaşılabilir olduğu sürece okuyabilir ve yönetebilirsiniz. Bu, telefonunuzun aynı ağda olması ya da o ağdaki bir Cora Max'in komutlarınızı iletmesi demektir. Evden uzaktaysanız ve yerinde Cora Max yoksa bir ağ pompasını görebilirsiniz ama kontrol edemezsiniz.

:::note Bir pompa ilk taramayı sık sık kaçırır
Pompalar bir taramaya yanıt verip bir sonrakini kaçırır. Sizinki listede yoksa ulaşılamayacağına karar vermeden önce yeniden tarayın.
:::

Bir arama hiçbir şey bulamazsa sonuç Wi-Fi üzerinden kontrol ettiği adresleri gösterir. Jebao uygulaması pompanız için farklı bir adres gösteriyorsa telefonunuz başka bir ağdadır. Bir misafir ya da IoT ağı ya da yalnızca 5 GHz bant bu pompaları görmez. iPhone'da Cora'nın Wi-Fi'ınızdaki pompaları görmesi için Yerel Ağ erişimi de gerekir. Bu erişim olmadan liste boş kalır ve hata görünmez, bu yüzden sonuç bunu açıklar ve onu yeniden açmak için **Ayarları Aç**'ı önerir. Oraya istediğiniz zaman [Ayarlar](/help/mobile-settings) sayfasında anlatılan **Ayarlar → Cihaz erişimi** yolundan da ulaşabilirsiniz.

**Bluetooth üzerinden.** Bazı pompalara yalnızca yakınında duran bir telefondan ulaşılabilir. Pompanın sayfası bunu söyler ve okuduğu son ayarları ve ne kadar eski olduklarını gösterir. Cora'nın bunun için Bluetooth iznine ihtiyacı vardır. Bluetooth bir pompa eklemeden önce izni verin, yoksa Cora pompayı hiç bulamaz.

:::warning Bluetooth bir pompanın yakınında olmanız gerekir
Sayfası Cora'nın okuduğu son ayarları ve ne kadar önce okuduğunu gösterir. Herhangi bir şeyi değiştirmek, bir besleme duraklatması başlatmak bile, pompanın menzilde olmasını gerektirir. Yakınında durun ve sayfayı yeniden açın.
:::

İki bağlantıyla da canlı durum, mod ve yoğunluk, besleme duraklatması ve günlük program elde edersiniz. Telefonunuzdan başlatılan bir besleme duraklatması bazı pompalarda pompanın sayfasının açık tutulmasını gerektirir. Ayrıntılar [Ekipmanınızı kontrol etme](/help/mobile-device-control#jecod) sayfasında, günlük program da [Ekipman programları](/help/mobile-schedules) sayfasında anlatılır.

## AquaWiz KH Controller {#aquawiz-kh-controller}

Cora bir AquaWiz KH kontrolcüsünden alkaliniteyi AquaWiz hesabınız üzerinden okur, bu yüzden evden uzaktayken çalışır ve Cora Max gerektirmez.

1. **Cihazlar → Cihaz Ekle → AquaWiz** yoluna gidin.
2. AquaWiz kullanıcı adınızı ve şifrenizi girin ve **Bağlan**'a dokunun.
3. Akvaryumu seçin, isterseniz **pH'ını da oku**'yu açın ve **Cora'ya Bağla**'ya dokunun.

**Otomatik olarak bağlı kal** açıkken Cora AquaWiz şifrenizi saklar ve bağlantıyı kendisi yeniler. Kapalıyken Cora yalnızca AquaWiz'in yaklaşık 30 günde bir sona erdirdiği bir giriş belirteci saklar ve yeniden giriş yapma zamanı geldiğinde size bir bildirim gönderir.

Kaynak olarak, kontrolcünüz ne sıklıkla titrasyon yapıyorsa o sıklıkla güncellenen alkaliniteyi alırsınız. Açtıysanız ve üniteniz bildiriyorsa pH da gelir. AquaWiz kartının ne gösterdiği ve takviye uyarısı [Ekipmanınızı kontrol etme](/help/mobile-device-control#aquawiz) sayfasında.

:::warning Cora AquaWiz girişinizi paylaşır
AquaWiz her hesaba tek bir giriş verir, bu yüzden Cora AquaWiz uygulamasıyla aynı girişi kullanır. AquaWiz şifrenizi değiştirirseniz Cora'nın bağlantısı kesilir. Sonrasında cihaz satırından yeniden bağlayın. Cora'nın erişimini tamamen kaldırmak için cihazı Cora'dan kaldırın ve AquaWiz şifrenizi değiştirin.
:::

## Maxspect {#maxspect}

:::note Beta
**Beta.** Maxspect Beta aşamasındadır ve yalnızca Beta kullanıcılarına açıktır. Beta kullanıcısı değilseniz onu **Cihaz Ekle** içinde görmezsiniz. Beta erişimi istemek için [destek](/support.html) ile iletişime geçin. Bazı kontroller sınırlı olabilir ve burada gördükleriniz güncellemeler arasında değişebilir. Bir şey anlatıldığı gibi çalışmıyorsa [Sorun bildirme](/help/mobile-support) sayfasından bize bildirin.
:::

Cora Maxspect Gyre pompalarına bağlanır ve onları okuyup yönetebilir. Birini Jecod'un kullandığı taramayla aynı olan **Cihazlar → Cihaz Ekle → Maxspect** yolundan ekleyin. Akvaryumda bir Cora Max gerektirir. Yoksa satırda **Cora Max Gerektirir** görünür.

Bir gyre eklerken telefonunuzla aynı ağda olması gerekir. Sonrasında Cora Mobile ona, siz uzaktayken bile, akvaryumun Cora Max'i üzerinden ulaşır. Dalga deseni, hız, program ve **Pompa sağlığı** [Ekipmanınızı kontrol etme](/help/mobile-device-control#maxspect) sayfasında.

## GHL ProfiLux ve Mitras {#ghl-profilux-and-mitras}

:::note Beta
**Beta.** GHL Beta aşamasındadır ve yalnızca Beta kullanıcılarına açıktır. Beta kullanıcısı değilseniz onu **Cihaz Ekle** içinde görmezsiniz. Beta erişimi istemek için [destek](/support.html) ile iletişime geçin. Bazı ölçümler ya da kontroller henüz çalışmayabilir. Bir şey anlatıldığı gibi çalışmıyorsa [Sorun bildirme](/help/mobile-support) sayfasından bize bildirin.
:::

Cora bir GHL ProfiLux ya da Mitras kontrolcüsünü okur: problar, prizler, dozaj pompaları, seviye sensörleri ve Director modellerinde KH ve iyon test sonuçları.

1. **Cihazlar → Cihaz Ekle → GHL** yoluna gidin. Akvaryumda bir Cora Max gerektirir ve yoksa **Cora Max Gerektirir** gösterir.
2. Telefonunuz onu tarayamaz, bu yüzden adresini girin ve arayüzü kendiniz seçin: **Resmi API**, **HTTP** ya da **ProfiLux mini** (giriş bilgisi de gerektirir).
3. Hangi akvaryuma ait olduğunu seçin. Bir GHL kontrolcüsü birden fazla akvaryuma hizmet edebilir.

Bir GHL kontrolcüsü telefonunuzla doğrudan konuşmaz. Ağındaki bir Cora Max onu okuyana kadar **Cora Max bekleniyor** gösterir, sonra ölçümleri ve kontrolleri her yerde görünür.

Cora'nın kontrolcüye ulaşabilmesi için GHL API'nin açık olması gerekir. GHL her yazılım güncellemesinden sonra onu kapatır, bu yüzden hiçbir şey görünmüyorsa önce bunu kontrol edin. Ne yapacağınız [Sorun giderme](/help/troubleshooting) sayfasında anlatılır. Kontroller [Ekipmanınızı kontrol etme](/help/mobile-device-control#ghl) sayfasında.

## HYDROS {#hydros}

:::note Beta
**Beta.** HYDROS Beta aşamasındadır ve yalnızca Beta kullanıcılarına açıktır. Beta kullanıcısı değilseniz onu **Cihaz Ekle** içinde görmezsiniz. Beta erişimi istemek için [destek](/support.html) ile iletişime geçin. Bazı ölçümler ya da kontroller henüz çalışmayabilir. Bir şey anlatıldığı gibi çalışmıyorsa [Sorun bildirme](/help/mobile-support) sayfasından bize bildirin.
:::

HYDROS, telefonunuzun ve kontrolcünüzün aynı ağda olmasını ya da bir Cora Max'i gerektirmez. Cora ona HYDROS'un kendi bulutu üzerinden ulaşır, bu yüzden evden uzaktayken ve hatta Cora Mobile kapalıyken de çalışmaya devam eder.

1. HYDROS uygulamasında **cora-iq** sağlayıcısı için bir **cihaz anahtarı** oluşturun. Yalnızca ölçümlerini istiyorsanız **Read**'i (okuma), onu Cora'dan kontrol etmek de istiyorsanız **Write**'ı (yazma) seçin.
2. Cora Mobile'da **Cihazlar → Cihaz Ekle → HYDROS** yoluna gidin. Ekranın adı **HYDROS Ekle (Beta)**'dır.
3. Anahtarı **HYDROS cihaz anahtarı** alanına yapıştırın, **Anahtarı kontrol et**'e dokunun, akvaryumu seçin ve **Bağla**'ya dokunun.

Bağlandıktan sonra Cora geçmişinin son 33 gününü içe aktarır, sonra oradan ileriye doğru okumaya devam eder. Neleri okuyabileceğiniz ve bir yazma anahtarıyla neleri kontrol edebileceğiniz [Ekipmanınızı kontrol etme](/help/mobile-device-control#hydros) sayfasında.

## Focustronic {#focustronic}

:::note Beta
**Beta.** Focustronic Beta aşamasındadır ve yalnızca Beta kullanıcılarına açıktır. Beta kullanıcısı değilseniz onu **Cihaz Ekle** içinde görmezsiniz. Beta erişimi istemek için [destek](/support.html) ile iletişime geçin.
:::

Cora Focustronic Alkatronic, Dosetronic ve Mastertronic cihazlarını Focustronic hesabınız üzerinden okur, bu yüzden evden uzaktayken çalışır ve Cora Max gerektirmez.

1. **Cihazlar → Cihaz Ekle → Focustronic** yoluna gidin ve Focustronic uygulamasında kullandığınız hesapla giriş yapın.
2. Her cihazın hangi akvaryuma ait olduğunu seçin, sonra **Cora'ya bağla**'ya dokunun.

**Oturumu açık tut**, Cora'nın Focustronic şifrenizi şifreli olarak saklamasını ve kendiliğinden yeniden giriş yapmasını sağlar. Kapatırsanız Cora yalnızca geçici bir giriş saklar ve yeniden giriş yapmanız gerektiğinde size bir bildirim gönderir. Focustronic girişi reddederse **Focustronic ekle**'yi açın ve yeniden giriş yapın.

Her cihazın ne gösterdiği ve **Şimdi ölç**, **Şimdi dozla** ve **Şimdi test et** [Ekipmanınızı kontrol etme](/help/mobile-device-control#focustronic) sayfasında.

## Inkbird oda havası monitörü {#inkbird-room-air-monitor}

:::note Beta
**Beta.** Inkbird Beta aşamasındadır ve yalnızca Beta kullanıcılarına açıktır. Beta kullanıcısı değilseniz onu **Cihaz Ekle** içinde görmezsiniz. Beta erişimi istemek için [destek](/support.html) ile iletişime geçin.
:::

Cora bir Inkbird IAM-T1 ya da IAM-T2 oda havası monitörünü okur. Akvaryumdaki bir Cora Max onu Bluetooth üzerinden okur ve Cora monitöre asla bir şey yazmaz. Akvaryumda bir Cora Max olana kadar satırda **Cora Max Gerektirir** görünür.

1. **Cihazlar → Cihaz Ekle → Inkbird** yoluna gidin. Cora yakındaki monitörleri tarar. Bluetooth açık olmalı ve Cora için izin verilmiş olmalıdır.
2. Sizinkini seçin ve **Tanka bağla**'ya dokunun. Hiçbiri görünmezse yaklaşın ve **Yeniden tara**'ya dokunun.

Monitörün sayfası son ölçümünü gösterir. **Örnekleme aralığı**, bir Cora Max'in onu ne sıklıkla okuyacağını ayarlar. Bir Cora Max onu okuyana kadar sayfada **Cora Max bekleniyor** yazar. Sessizleşirse **Veri göndermiyor** gösterir ve Cora sizi uyarır. Oda ölçümleri [Reef Buddy](/help/mobile-reef-buddy)'yi de besler. Durdurmak için **Bağlantıyı kaldır**'ı kullanın. Cora Max onu okumayı bırakır ve geçmiş kalır.

## Elle kaydetme {#logging-by-hand}

Bazı parametreler ekipmandan değil, bir test kitinden gelir. Bir sonuç girmek için panonun en altına kaydırın ve **Parametreleri Kaydet**'e dokunun.

Elle kaydettiğiniz ölçümler diğerleri kadar sayılır. Widget'larda kendi kaynakları ve yaşlarıyla görünürler ve Reef Buddy'yi beslerler. Cora, iki kaynağın uyuşmadığını size söylerken problarınızı da onlara göre kontrol eder.

## Bir bağlantı çalışmayı bırakırsa {#if-a-connection-stops-working}

Cihaz satırı ne tür bir sorun olduğunu söyler. Ona [Cihaz ekleme, düzenleme ve kaldırma](/help/mobile-devices#health) sayfasındaki tablodan bakın. Orada olmayan her şey için [Sorun giderme](/help/troubleshooting) sayfasına bakın.
