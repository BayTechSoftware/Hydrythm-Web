---
title: Ekipmanınızı bağlama
description: Neptune Apex, Red Sea ReefBeat, Jecod, AquaWiz, GHL ve HYDROS ekipmanlarını Cora'ya bağlayın.
section: Cora Mobile
reviewed: 2026-09-30
order: 10
group: Equipment
---

Cora, zaten sahip olduğunuz ekipmanla çalışır. Bu sayfada hangi ekipmanların desteklendiğini ve her bağlantı için nelerin gerektiğini bulabilirsiniz.

Hepsi aynı şekilde başlar: **Cihazlar → Cihaz Ekle**, ardından markayı seçin. Her biri ekipmanınızı bulmak için tam olarak gerekeni açar.

| Marka | Ne açılır |
|---|---|
| Cora | Yeni bir Cora Max için Wi-Fi ya da Bluetooth üzerinden tarama |
| Neptune Apex | Ağdaki adresi, giriş bilgisi, ardından hangi akvaryuma ait olduğu |
| Red Sea | Ağınızda tarama, ardından her ünitenin hangi akvaryuma ait olduğu |
| Jecod / Jebao | Ağınızda tarama ya da Bluetooth |
| Maxspect *(beta)* | Jecod ile aynı tarama |
| GHL *(beta)* | Adresi, arayüzü ve mini için giriş bilgisi |
| HYDROS *(beta)* | HYDROS uygulamasından bir cihaz anahtarı |
| AquaWiz | AquaWiz giriş bilgileriniz |

## Neptune Apex

Cora, Apex'inizi yerel ağınız üzerinden okur: problar, prizler ve taktığınız genişletme modülleri.

**Cihazlar → Cihaz Ekle → Neptune Apex**'ten ekleyin. Apex'inizin ağdaki adresi ve giriş bilgileri gerekir, ardından hangi akvaryuma ait olduğunu seçersiniz. Bir Apex birden fazla akvaryuma hizmet edebilir.

Apex'inizin bildirdiği her prob, panoya ekleyebileceğiniz bir kaynak olarak görünür. Prizler kontrol düğmesi olarak gelir. Takılı genişletme modüllerinin her biri kendi cihaz kutucuğunu alır.

:::note Apex'iniz kendi programıyla çalışmaya devam eder
Cora Apex'inizi okur, diğer ekipmanlarla birlikte gösterir ve siz isteyince prizleri açıp kapatır. Sizin Apex'te yaptığınız programlama da ayarladığınız gibi çalışmaya devam eder.
:::

## Red Sea ReefBeat

Cora, yerel ağınızdaki ReefBeat ekipmanlarıyla bağlantı kurar. Desteklenen üniteler **ReefDose**, **ReefATO+**, **ReefMat**, **ReefRun** ve beta aşamasında **ReefControl**, **ReefControl Power**, **ReefWave** ile **ReefLED**'dir.

Ekipmanın ReefBeat'te önceden kurulmuş olması gerekir. Eklerken ekipman ve telefonunuz aynı ağda olmalıdır. **Cihazlar → Cihaz Ekle → Red Sea**'den ekleyin; bu seçenek ağınızı tarar ve her ünitenin hangi akvaryuma ait olduğunu sorar. Bir Red Sea ünitesi tek bir akvaryuma hizmet eder: farklı bir akvaryum seçmek üniteyi oraya taşır.

Her ünite için bir cihaz sayfası açılır. Her ünitenin ölçümleri de kaynak olarak görünür. ReefDose kafalarını ve kaplarını, ReefATO+ rezervuarını ve dolumlarını, ReefMat kalan gün sayısını, ReefRun da pompa durumunu bildirir. ReefControl da problarını aynı şekilde bildirir. ReefWave ve ReefLED *(beta)* şimdilik yalnızca modunu gösterir, yalnızca görüntüleme.

## Jecod / Jebao

Cora, Jecod pompalarına bağlanır. Pompaları okuyabilir ve kontrol edebilir. **Cihazlar → Cihaz Ekle → Jecod**'dan bir tane ekleyin. Jecod üniteleri Cora'ya iki yoldan biriyle ulaşır. Neler yapabileceğiniz de pompanızın hangi yolu kullandığına bağlıdır.

![Pompa bulma](img/mobile-connections.webp "Tarama ekranı neye ihtiyaç duyduğunu ve pompanın ilk taramada neden görünmeyebileceğini açıklar.")

**Ağınız üzerinden.** Tarama, kendini ağda gösteren pompaları bulur, adres girmeniz gerekmez. Ağ pompası açık **ve erişilebilir** olduğu sürece okunabilir ve kontrol edilebilir. Bunun için ya telefonunuz aynı ağda olmalı ya da o ağdaki bir Cora Max komutları sizin yerinize iletmelidir. Evden uzaktaysanız ve akvaryumun yanında Cora Max yoksa, yalnızca ağ üzerinden bağlanan bir pompayı görürsünüz ama kontrol edemezsiniz.

:::note Pompa ilk taramada çoğu zaman görünmez
Pompalar bir taramaya yanıt verip bir sonrakini kaçırabilir. Pompanız listede yoksa ulaşılamadığını düşünmeden önce tekrar tarayın.
:::

Arama hiçbir şey bulamazsa sonuç ekranında Wi-Fi üzerinden hangi adreslere bakıldığı yazar. Pompanızın Jebao uygulamasındaki adresi farklıysa telefonunuz başka bir ağdadır. Misafir ağları, IoT ağları ya da yalnızca 5 GHz bandı bu pompaları görmez. iPhone'da Cora'nın Wi-Fi'nizdeki pompaları görebilmesi için Yerel Ağ izni de gerekir. İzin kapalıysa liste boş kalır ve hata çıkmaz. Sonuç ekranı bu yüzden durumu açıklar ve izni yeniden açmanız için **Ayarları Aç** düğmesini gösterir. Aynı yere istediğiniz zaman **Ayarlar → Cihaz erişimi** yolundan da ulaşabilirsiniz. Ayrıntılar [Ayarlar](/help/mobile-settings) sayfasında.

**Bluetooth üzerinden.** Bazı pompalara yalnızca yakınında duran bir telefondan ulaşılabilir. Pompanın sayfasında bu yazar. Sayfa, okunabilen son ayarları ve ne kadar eski olduklarını gösterir.

Bunun için Cora'ya Bluetooth izni vermeniz gerekir. Bluetooth pompası eklemeden önce izni verin. İzin yoksa pompa geç görünmekle kalmaz, hiç bulunamaz.

Bağlandıktan sonra canlı durumu, modu ve yoğunluğu görür, beslemede pompayı duraklatabilir ve günlük program kurabilirsiniz. Ayrıntılar [Ekipman programları](/help/mobile-schedules) sayfasında.

:::warning Bluetooth pompasına yalnızca yakınındayken ulaşılır
Pompanın sayfası Cora'nın okuduğu son ayarları ve ne kadar önce okunduğunu gösterir. Besleme duraklatması dahil herhangi bir şeyi değiştirmek için pompanın menzilde olması gerekir. Pompanın yanına gidin ve sayfayı yeniden açın.
:::

## AquaWiz KH Denetleyicisi

Cora, AquaWiz KH denetleyicisinin alkalinite ölçümlerini AquaWiz hesabınız üzerinden okur. **Cihazlar → Cihaz Ekle → AquaWiz**'den ekleyin.

Bağlamak için AquaWiz kullanıcı adınız ve şifreniz gerekir. Cora sizin adınıza giriş yapar ve ölçümleri okumaya devam edebilmek için oturumu açık tutar.

Alkalinite, denetleyicinizin titrasyon sıklığında güncellenen bir kaynak olarak görünür. Üniteniz pH da bildiriyorsa onu da seçebilirsiniz.

Cihazın kendi kartında hedef KH değeriniz, dozaj gücünüz ve dozaj ayarı yapılmış bir ünite için saatlik maksimum dozu ile kapta kalan alkalinite takviyesi miktarı gösterilir. Bunlar doğrudan AquaWiz ayarlarınızdan gelir. Değiştirmek için AquaWiz uygulamasını kullanın. Üniteniz kabını takip ediyorsa takviye azaldığında Cora sizi uyarır, varsayılan eşik 100 mL'dir.

:::warning Tek giriş, ortak kullanım
AquaWiz her hesap için tek bir oturum verir. Cora'nın kullandığı oturum, AquaWiz'in kendi uygulamasının kullandığıyla aynıdır. AquaWiz şifrenizi değiştirirseniz Cora'nın bağlantısı kopar. Sonrasında cihaz satırından yeniden bağlayın. Cora'nın erişimini tamamen kaldırmak için cihazı Cora'dan silin ve AquaWiz şifrenizi değiştirin.
:::

## Maxspect

:::note Maxspect desteği beta aşamasında
Maxspect gyre desteğinin testleri ve geliştirmesi sürüyor. Bazı kontroller sınırlı olabilir ve burada gördükleriniz güncellemelerle değişebilir. Bir şey anlatıldığı gibi çalışmıyorsa [Yardım alma](/help/mobile-support) sayfasındaki yoldan bize bildirin.
:::

Cora, Maxspect Gyre pompalarına bağlanır. Pompaları okuyabilir ve çalıştırabilir. **Cihazlar → Cihaz Ekle → Maxspect**'ten bir tane ekleyin; bu, Jecod'un kullandığı taramanın aynısıdır.

Eklerken gyre ile telefonunuz aynı ağda olmalıdır.

Bağlandıktan sonra **Gyre A** ve **Gyre B** için dalga desenini ve hızı, gyre'nin programını (yalnızca görüntüleme, programı Maxspect uygulamasından ayarlayın), **Pompa sağlığı** bilgisini ve pompanın çalışıp çalışmadığını görürsünüz. Son okuma zamanı da gösterilir. Ayrıntılar [Ekipmanınızı kontrol etme](/help/mobile-device-control) sayfasında.

:::note Cora Mobile gyre'ye nasıl ulaşır
Akvaryuma bağlı bir Cora Max varsa Cora Mobile, evden uzaktayken de o Cora Max üzerinden çalışır. **Ayarları değiştir** de o Cora Max'in son okumasından başlar. Cora Max yoksa telefonunuz gyre'yle doğrudan bağlantı kurar ve gyre'yle aynı ağda olması gerekir. Bu durumda gyre'nin sayfasını açınca gyre okunur. Sayfa daha eski, kayıtlı bir okumayı gösteriyorsa yenile simgesine dokunana kadar **Ayarları değiştir** görünmez.
:::

## GHL ProfiLux ve Mitras

:::note GHL desteği beta aşamasında
GHL desteğinin testleri ve geliştirmesi sürüyor. Bazı ölçümler ya da kontroller henüz çalışmayabilir, burada gördükleriniz güncellemelerle değişebilir. Bir şey anlatıldığı gibi çalışmıyorsa [Yardım alma](/help/mobile-support) sayfasındaki yoldan bize bildirin.
:::

Cora, bir GHL ProfiLux ya da Mitras kontrol cihazını okur: problar, prizler, dozaj üniteleri, seviye sensörleri ve Director modellerinde KH ile iyon test sonuçları.

**Cihazlar → Cihaz Ekle → GHL**'den ekleyin. Telefonunuz bu cihazı tarayamaz, bu yüzden adresini kendiniz girer ve arayüzü kendiniz seçersiniz: **Official API**, **HTTP** ya da (girişi de gereken) **ProfiLux mini**. Ardından hangi akvaryuma ait olduğunu seçersiniz. Bir GHL kontrol cihazı birden fazla akvaryuma hizmet edebilir.

GHL kontrol cihazı telefonunuzla doğrudan konuşmaz. Ağındaki bir Cora Max onu okuyana kadar **Cora Max bekleniyor** yazar, ardından ölçümleri ve kontrolleri her yerde görünür.

Cora'nın kontrol cihazına ulaşabilmesi için GHL API'sinin açık olması gerekir. GHL bunu her yazılım güncellemesinden sonra kapatır, bu yüzden hiçbir şey görünmüyorsa önce bunu kontrol edin. Ne yapacağınızı [Sorun giderme](/help/troubleshooting) sayfasında bulabilirsiniz.

## HYDROS

:::note HYDROS desteği beta aşamasında
HYDROS desteğinin testleri ve geliştirmesi sürüyor. Bazı ölçümler ya da kontroller henüz çalışmayabilir, burada gördükleriniz güncellemelerle değişebilir. Bir şey anlatıldığı gibi çalışmıyorsa [Yardım alma](/help/mobile-support) sayfasındaki yoldan bize bildirin.
:::

HYDROS, Cora'nız ile kontrol cihazınızın aynı ağda olmasını gerektirmeyen tek entegrasyondur. Cora ona HYDROS'un kendi bulutu üzerinden ulaşır, bu yüzden evden uzaktayken, hatta Cora kapalıyken bile çalışmaya devam eder.

Bağlamak için HYDROS uygulamasını açın ve **cora-iq** sağlayıcısı için bir **cihaz anahtarı** oluşturun. Yalnızca ölçümlerini istiyorsanız **Read**'i, Cora'dan da kontrol etmek istiyorsanız **Write**'ı seçin. Sonra **Cihazlar → Cihaz Ekle → HYDROS**'a gidin ve anahtarı yapıştırın.

Bağlandıktan sonra Cora, geçmişinin son 33 gününü içe aktarır, ardından oradan itibaren okumaya devam eder. Neleri okuyabileceğinizi ve yazma anahtarıyla neleri kontrol edebileceğinizi [Ekipmanınızı kontrol etme](/help/mobile-device-control) sayfasında bulabilirsiniz.

## Elle girme

Bazı parametreler ekipmandan değil, test kitinden gelir. Sonucu girmek için panonun en altına inin ve **Parametreleri Kaydet**'e dokunun.

Elle girilen ölçümler diğerlerinden aşağı sayılmaz. Widget'larda görünür, kendi kaynakları ve yaşlarıyla gelir ve Reef Buddy'ye veri sağlarlar. İki kaynağın farklı sonuç verdiğini söylerken Cora problarınızı da bu ölçümlerle karşılaştırır.

## Bağlantı çalışmayı bırakırsa

Cihaz satırı sorunun türünü gösterir. **[Cihaz ekleme, düzenleme ve kaldırma](/help/mobile-devices)** sayfasındaki tabloya bakın. Orada olmayan durumlar için **[Sorun giderme](/help/troubleshooting)** sayfasına bakın.
