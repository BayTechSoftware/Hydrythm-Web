---
title: Ekipmanınızı bağlama
description: Bir Neptune Apex, Red Sea ReefBeat, Jecod ya da AquaWiz ünitesini Cora'ya nasıl bağlayacağınız.
section: Cora Mobile
reviewed: 2026-10-17
order: 12
group: Equipment
---

Bu sayfa her ekipman markasını Cora'ya nasıl bağlayacağınızı ve her bağlantının neye ihtiyaç duyduğunu gösterir. Hepsi aynı şekilde başlar: **Cihazlar → Cihaz Ekle**, ardından markayı seçin.

![Cihaz Ekle'deki marka listesi](img/mobile-add-device-brands.webp "Marka listesi.")


| Marka | Ne açılır | Cora Max olmadan |
|---|---|---|
| Cora | Wi-Fi ya da Bluetooth üzerinden yeni bir Cora Max araması | |
| Neptune Apex | Bir ağ taraması ya da IP adresi, ardından hangi akvaryumlara hizmet ettiği | Yalnızca yerel |
| Red Sea | Ağınızda bir tarama, ardından her ünitenin hangi akvaryuma ait olduğu | Yalnızca yerel |
| Jecod / Jebao | Ağınızda bir tarama ya da Bluetooth | Yalnızca yerel |
| AquaWiz | AquaWiz girişiniz | Çalışır |

## Cora Max olmadan: yalnızca yerel {#local-only}

Neptune Apex, Red Sea ve Jecod ekipmanı ev ağınızdadır (ya da Bluetooth'ta). Cora Max'iniz yoksa (ya da eklediğiniz akvaryumda yoksa) bu markaların ekleme ekranında *Bu entegrasyon, Cora Max olmadan yalnızca Mobile uygulamasında yerel olarak çalışır.* yazar. Bunun anlamı şudur:

- Telefonunuz, Cora Mobile aynı ağda açıkken ya da Bluetooth menzilindeyken ekipmanı okur ve kontrol eder.
- Evden uzaktayken telefonunuzun kaydettiği son ölçümleri görürsünüz ve onu kontrol edemezsiniz.

Akvaryumdaki bir Cora Max bu ekipmanı gece gündüz okur ve siz uzaktayken komutlarınızı iletir. AquaWiz'e üreticinin kendi hizmeti üzerinden ulaşılır, bu yüzden Cora Max olmadan her yerden çalışır. Ayrıntılar [Birden fazla Cora cihazı](/help/mobile-multi-device) sayfasında.

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

Cora, yerel ağınızdaki ReefBeat ekipmanıyla konuşur. **ReefDose**, **ReefATO+**, **ReefMat** ve **ReefRun**'ı destekler.

1. Üniteyi önce Red Sea'nin ReefBeat uygulamasında kurun ve telefonunuzla aynı ağda olduğunu kontrol edin.
2. **Cihazlar → Cihaz Ekle → Red Sea** yoluna gidin. Cora ağınızı tarar.
3. Her ünitenin hangi akvaryuma ait olduğunu seçin.

Bir Red Sea ünitesi tek bir akvaryuma hizmet eder. Farklı birini seçmek onu oraya taşır.

Her ünite kendi cihaz sayfasını alır ve ölçümleri kaynak olur. ReefDose kafalarını ve kaplarını, ReefATO+ deposunu ve dolumlarını, ReefMat kalan günlerini, ReefRun da pompa durumunu bildirir. Her sayfanın neler yapmanızı sağladığı [Ekipmanınızı kontrol etme](/help/mobile-device-control#red-sea) sayfasında.

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

İki bağlantıyla da canlı durum, mod ve yoğunluk, besleme duraklatması ve günlük zamanlama elde edersiniz. Telefonunuzdan başlatılan bir besleme duraklatması bazı pompalarda pompanın sayfasının açık tutulmasını gerektirir. Ayrıntılar [Ekipmanınızı kontrol etme](/help/mobile-device-control#jecod) sayfasında, günlük zamanlama da [Ekipman zamanlamaları](/help/mobile-schedules) sayfasında anlatılır.

## AquaWiz KH Controller {#aquawiz-kh-controller}

Cora bir AquaWiz KH kontrolöründen alkaliniteyi AquaWiz hesabınız üzerinden okur, bu yüzden evden uzaktayken çalışır ve Cora Max gerektirmez.

1. **Cihazlar → Cihaz Ekle → AquaWiz** yoluna gidin.
2. AquaWiz kullanıcı adınızı ve şifrenizi girin ve **Bağlan**'a dokunun.
3. Akvaryumu seçin, **pH'ını da oku**'yu kontrol edin (pH bildiren bir ünitede başta açıktır) ve **Cora'ya Bağla**'ya dokunun.

**Otomatik olarak bağlı kal** açıkken Cora AquaWiz şifrenizi saklar ve bağlantıyı kendisi yeniler. Kapalıyken Cora yalnızca AquaWiz'in yaklaşık 30 günde bir sona erdirdiği bir giriş belirteci saklar ve yeniden giriş yapma zamanı geldiğinde size bir bildirim gönderir.

Kaynak olarak alkaliniteyi alırsınız. Üniteniz bildiriyorsa ve **pH'ını da oku** açıksa pH da gelir. İlk ölçümünüz bağlar bağlamaz gelir. Sonrasında AquaWiz, Cora'nın bulutunu otomatik olarak yalnızca 12 saatte bir okumasına izin verir; yani oradan gelen bir ölçüm yarım güne kadar eski olabilir. Akvaryumdaki bir Cora Max, ulaşabildiğinde kontrolörü her saat kendisi de okuyabilir. Her ölçümün ne zaman yapıldığını ve nereden geldiğini görmek için cihazın sayfasını açın, yenisi için **Şimdi oku**'ya dokunun (en fazla 15 dakikada bir). AquaWiz kartının ne gösterdiği ve uyarıları [Ekipmanınızı kontrol etme](/help/mobile-device-control#aquawiz) sayfasında.

:::warning Cora AquaWiz girişinizi paylaşır
AquaWiz her hesaba tek bir giriş verir, bu yüzden Cora AquaWiz uygulamasıyla aynı girişi kullanır. AquaWiz şifrenizi değiştirirseniz Cora'nın bağlantısı kesilir. Sonrasında cihaz satırından yeniden bağlayın. Cora'nın erişimini tamamen kaldırmak için cihazı Cora'dan kaldırın ve AquaWiz şifrenizi değiştirin.
:::


## Elle kaydetme {#logging-by-hand}

Bazı parametreler ekipmandan değil, bir test kitinden gelir. Bir sonuç girmek için panonun en altına kaydırın ve **Parametreleri Kaydet**'e dokunun.

Elle kaydettiğiniz ölçümler diğerleri kadar sayılır. Widget'larda kendi kaynakları ve yaşlarıyla görünürler ve Reef Buddy'yi beslerler. Cora, iki kaynağın uyuşmadığını size söylerken problarınızı da onlara göre kontrol eder.

## Bir bağlantı çalışmayı bırakırsa {#if-a-connection-stops-working}

Cihaz satırı ne tür bir sorun olduğunu söyler. Ona [Cihaz ekleme, düzenleme ve kaldırma](/help/mobile-devices#health) sayfasındaki tablodan bakın. Orada olmayan her şey için [Sorun giderme](/help/troubleshooting) sayfasına bakın.
