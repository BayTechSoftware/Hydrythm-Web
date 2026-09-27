---
title: Ekipmanınızı bağlama
description: Neptune Apex, Red Sea ReefBeat, Jecod ve AquaWiz ekipmanlarını Cora'ya bağlayın.
section: Cora Mobile
reviewed: 2026-09-17
order: 10
group: Equipment
---

Cora, zaten sahip olduğunuz ekipmanla çalışır. Bu sayfada hangi ekipmanların desteklendiğini ve her bağlantı için nelerin gerektiğini bulabilirsiniz.

Her marka kendine en uygun yoldan bağlanır. Ekipmanınız için aşağıdaki başlangıç noktasını kullanın:

| Marka | Nereden başlanır |
|---|---|
| Neptune Apex | Akvaryumdan. Apex bağlantısı akvaryumun profilinde durur |
| Red Sea ReefBeat | Akvaryumdan |
| Jecod / Jebao | **Cihazlar → Ağınızda bir pompa bulun** ya da Bluetooth |
| AquaWiz | **Cihazlar → AquaWiz Ekle** |
| Maxspect *(beta)* | **Cihazlar → Ağınızda bir pompa bulun** |
| Cora Max | **Cihazlar → Cihaz Ekle** |

## Neptune Apex

Cora, Apex'inizi yerel ağınız üzerinden okur: problar, prizler ve taktığınız genişletme modülleri.

Bağlamak için Apex'inizin ağdaki adresi ve giriş bilgileri gerekir.

Apex'inizin bildirdiği her prob, panoya ekleyebileceğiniz bir kaynak olarak görünür. Prizler kontrol düğmesi olarak gelir. Takılı genişletme modüllerinin her biri kendi cihaz kutucuğunu alır.

:::note Apex'iniz kendi programıyla çalışmaya devam eder
Cora Apex'inizi okur, diğer ekipmanlarla birlikte gösterir ve siz isteyince prizleri açıp kapatır. Sizin Apex'te yaptığınız programlama da ayarladığınız gibi çalışmaya devam eder.
:::

## Red Sea ReefBeat

Cora, yerel ağınızdaki ReefBeat ekipmanlarıyla bağlantı kurar. Desteklenen üniteler **ReefDose**, **ReefATO+**, **ReefMat** ve **ReefRun**'dır.

Ekipmanın ReefBeat'te önceden kurulmuş olması gerekir. Eklerken ekipman ve telefonunuz aynı ağda olmalıdır.

Her ünite için bir cihaz sayfası açılır. Her ünitenin ölçümleri de kaynak olarak görünür. ReefDose kafalarını ve kaplarını, ReefATO+ rezervuarını ve dolumlarını, ReefMat kalan gün sayısını, ReefRun da pompa durumunu bildirir.

## Jecod / Jebao

Cora, Jecod pompalarına bağlanır. Pompaları okuyabilir ve kontrol edebilir. Jecod üniteleri Cora'ya iki yoldan biriyle ulaşır. Neler yapabileceğiniz de pompanızın hangi yolu kullandığına bağlıdır.

![Pompa bulma](img/mobile-connections.webp "Tarama ekranı neye ihtiyaç duyduğunu ve pompanın ilk taramada neden görünmeyebileceğini açıklar.")

**Ağınız üzerinden.** **Ağınızda bir pompa bulun**'a dokunun. Bu seçenek kendini ağda gösteren pompaları bulur, adres girmeniz gerekmez. Ağ pompası açık **ve erişilebilir** olduğu sürece okunabilir ve kontrol edilebilir. Bunun için ya telefonunuz aynı ağda olmalı ya da o ağdaki bir Cora Max komutları sizin yerinize iletmelidir. Evden uzaktaysanız ve akvaryumun yanında Cora Max yoksa, yalnızca ağ üzerinden bağlanan bir pompayı görürsünüz ama kontrol edemezsiniz.

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

Cora, AquaWiz KH denetleyicisinin alkalinite ölçümlerini AquaWiz hesabınız üzerinden okur.

Bağlamak için AquaWiz kullanıcı adınız ve şifreniz gerekir. Cora sizin adınıza giriş yapar ve ölçümleri okumaya devam edebilmek için oturumu açık tutar.

Alkalinite, denetleyicinizin titrasyon sıklığında güncellenen bir kaynak olarak görünür. Üniteniz pH da bildiriyorsa onu da seçebilirsiniz.

:::warning Tek giriş, ortak kullanım
AquaWiz her hesap için tek bir oturum verir. Cora'nın kullandığı oturum, AquaWiz'in kendi uygulamasının kullandığıyla aynıdır. AquaWiz şifrenizi değiştirirseniz Cora'nın bağlantısı kopar. Sonrasında cihaz satırından yeniden bağlayın. Cora'nın erişimini tamamen kaldırmak için cihazı Cora'dan silin ve AquaWiz şifrenizi değiştirin.
:::

## Maxspect

:::note Maxspect desteği beta aşamasında
Maxspect gyre desteğinin testleri ve geliştirmesi sürüyor. Bazı kontroller sınırlı olabilir ve burada gördükleriniz güncellemelerle değişebilir. Bir şey anlatıldığı gibi çalışmıyorsa [Yardım alma](/help/mobile-support) sayfasındaki yoldan bize bildirin.
:::

Cora, Maxspect Gyre pompalarına bağlanır. Pompaları okuyabilir ve çalıştırabilir.

Eklerken gyre ile telefonunuz aynı ağda olmalıdır. **Cihazlar → Ağınızda bir pompa bulun**'a dokunun.

Bağlandıktan sonra **Gyre A** ve **Gyre B** için dalga desenini ve hızı, gyre'nin programını (yalnızca görüntüleme, programı Maxspect uygulamasından ayarlayın), **Pompa sağlığı** bilgisini ve pompanın çalışıp çalışmadığını görürsünüz. Son okuma zamanı da gösterilir. Ayrıntılar [Ekipmanınızı kontrol etme](/help/mobile-device-control) sayfasında.

:::note Cora Mobile gyre'ye nasıl ulaşır
Akvaryuma bağlı bir Cora Max varsa Cora Mobile, evden uzaktayken de o Cora Max üzerinden çalışır. **Ayarları değiştir** de o Cora Max'in son okumasından başlar. Cora Max yoksa telefonunuz gyre'yle doğrudan bağlantı kurar ve gyre'yle aynı ağda olması gerekir. Bu durumda gyre'nin sayfasını açınca gyre okunur. Sayfa daha eski, kayıtlı bir okumayı gösteriyorsa yenile simgesine dokunana kadar **Ayarları değiştir** görünmez.
:::

## Elle girme

Bazı parametreler ekipmandan değil, test kitinden gelir. Sonucu girmek için panonun en altına inin ve **Parametreleri Kaydet**'e dokunun.

Elle girilen ölçümler diğerlerinden aşağı sayılmaz. Widget'larda görünür, kendi kaynakları ve yaşlarıyla gelir ve Reef Buddy'ye veri sağlarlar. İki kaynağın farklı sonuç verdiğini söylerken Cora problarınızı da bu ölçümlerle karşılaştırır.

## Bağlantı çalışmayı bırakırsa

Cihaz satırı sorunun türünü gösterir. **[Cihaz ekleme, düzenleme ve kaldırma](/help/mobile-devices)** sayfasındaki tabloya bakın. Orada olmayan durumlar için **[Sorun giderme](/help/troubleshooting)** sayfasına bakın.
