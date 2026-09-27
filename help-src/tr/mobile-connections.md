---
title: Ekipmanınızı bağlama
description: Neptune Apex, Red Sea ReefBeat, Jecod ve AquaWiz ekipmanını Cora'ya nasıl bağlanır.
section: Cora Mobile
reviewed: 2026-09-17
order: 10
group: Equipment
---

Cora, zaten sahip olduğunuz ekipmanla çalışır. Bu sayfa nelerin desteklendiğini ve her bağlantının neye ihtiyacı olduğunu kapsar.

Her marka kendisine en uygun şekilde bağlanır, bu yüzden ekipmanınız için giriş noktasından başlayın:

| Marka | Başlanacak yer |
|---|---|
| Neptune Apex | Akvaryum; profili Apex bağlantısını tutar |
| Red Sea ReefBeat | Akvaryum |
| Jecod / Jebao | **Cihazlar → Ağınızda bir pompa bulun**, veya Bluetooth |
| AquaWiz | **Cihazlar → AquaWiz Ekle** |
| Maxspect *(beta)* | **Cihazlar → Ağınızda bir pompa bulun** |
| Cora Max | **Cihazlar → Cihaz Ekle** |

## Neptune Apex

Cora, Apex'inizi yerel ağınız üzerinden okur: problar, prizler ve taktığınız herhangi bir genişletme modülü.

**İhtiyacınız olacak:** Apex'inizin ağınızdaki adresi ve oturum açma bilgisi.

**Ne alırsınız:** Apex'inizin bildirdiği her prob, panoya koyabileceğiniz bir kaynak olarak görünür. Prizler kontrol olarak görünür. Takılı genişletme modülleri kendi cihaz kutularını alır.

:::note Apex'iniz kendi programlamasını sürdürür
Cora, Apex'inizi okur, onu diğer her şeyin yanında gösterir ve istediğinizde prizleri açıp kapatabilir. Kendi programlamanız yapılandırdığınız şekilde çalışmayı sürdürür.
:::

## Red Sea ReefBeat

Cora, yerel ağınızdaki ReefBeat ekipmanıyla konuşur. Desteklenen birimler **ReefDose**, **ReefATO+**, **ReefMat** ve **ReefRun**'dır.

**İhtiyacınız olacak:** ekipman zaten ReefBeat'te kurulmuş ve eklediğinizde telefonunuzla aynı ağda olmalı.

**Ne alırsınız:** birim başına bir cihaz sayfası, artı her birimin okumaları kaynak olarak. ReefDose kafalarını ve kaplarını bildirir; ReefATO+ rezervuarını ve doldurmalarını bildirir; ReefMat kalan günleri bildirir; ReefRun pompa durumunu bildirir.

## Jecod / Jebao

Cora, Jecod pompalarına bağlanır ve onları okuyup kontrol edebilir. Jecod birimleri Cora'ya iki şekilden biriyle ulaşır ve sizinkinin hangisini kullandığı ne mümkün olduğuna karar verir.

![Bir pompa bulma](img/mobile-connections.webp "Tarama neye ihtiyacı olduğunu ve bir pompanın ilk taramada neden görünmeyebileceğini açıklar.")

**Ağınız üzerinden.** **Ağınızda bir pompa bulun**'u kullanın; kendini duyuran birimleri bulur, bu yüzden bir adres girilmesi gerekmez. Bir ağ pompası, açık **ve erişilebilir** olduğunda okunabilir ve çalıştırılabilir: ya telefonunuz aynı ağdadır, ya da o ağdaki bir Cora Max sizin için aktarır. Sahada bir Cora Max olmadan evden uzaktayken, yalnızca ağ üzerinden erişilen bir pompa görünür ama kontrol edilemez.

:::note Bir pompa sık sık ilk taramayı kaçırır
Pompalar bir taramayı yanıtlar ve bir sonrakini kaçırır. Sizinki listede değilse, ulaşılamaz olduğunu varsaymak yerine yeniden tarayın.
:::

Bir arama hiçbir şey bulmazsa, sonuç Wi-Fi üzerinden baktığı adresleri gösterir. Pompanızın Jebao uygulamasında farklı bir adresi varsa, telefonunuz başka bir ağdadır. Bir misafir veya IoT ağı, veya yalnızca 5 GHz bandı, bu pompaları görmez. iPhone'da, Cora'nın Wi-Fi'nizdeki pompaları görmesi için Yerel Ağ erişimine de ihtiyacı vardır. Kapalıysa, liste boş kalır ve hiçbir hata görünmez, bu yüzden sonuç bunu açıklar ve tekrar açmak için **Ayarları Aç**'ı sunar. **Ayarlar → Cihaz erişimi** her zaman aynı yeri açar; bkz. [Ayarlar](/help/mobile-settings).

**Bluetooth üzerinden.** Bazı pompalara yalnızca yanlarında duran bir telefondan ulaşılabilir. Pompanın sayfası bunu söyler ve okumayı başardığı son ayarları, ne kadar eski olduklarıyla birlikte gösterir.

Cora bunun için Bluetooth izni gerektirir. Bir Bluetooth pompası eklemeden önce bunu verin: izin olmadan pompa hiç keşfedilemez, sadece görünmesi daha uzun sürmez.

**Ne alırsınız:** canlı durum, mod ve yoğunluk, besleme duraklaması ve bir gün programı. Bkz. [Ekipman zamanlama](/help/mobile-schedules).

:::warning Bir Bluetooth pompasına yalnızca yanındayken ulaşılabilir
Sayfası, Cora'nın okuduğu son ayarları ve ne kadar önce olduğunu gösterir. Bir besleme duraklaması başlatmak dahil, herhangi bir şeyi değiştirmek pompanın menzilde olmasını gerektirir. Yanına gidin ve sayfayı yeniden açın.
:::

## AquaWiz KH Denetleyicisi

Cora, AquaWiz hesabınız üzerinden bir AquaWiz KH denetleyicisinden alkalinite okur.

**İhtiyacınız olacak:** AquaWiz kullanıcı adınız ve parolanız. Cora sizin adınıza oturum açar ve okumayı sürdürebilmek için oturumu tutar.

**Ne alırsınız:** denetleyiciniz titrasyon yaptığı sıklıkta güncellenen bir kaynak olarak alkalinite. Biriminiz bildiriyorsa pH bir seçenek olarak sunulur.

:::warning Bir oturum açma, paylaşılan
AquaWiz, hesap başına tek bir oturum açma verir, bu yüzden Cora'nın tuttuğu, kendi uygulamalarının kullandığıyla aynıdır. AquaWiz parolanızı değiştirmek Cora'nın bağlantısını kesecektir; sonrasında onu cihaz satırından yeniden bağlayın. Cora'nın erişimini tamamen iptal etmek için, cihazı Cora'dan kaldırın ve AquaWiz parolanızı değiştirin.
:::

## Maxspect

:::note Maxspect desteği beta aşamasında
Maxspect gyre desteği hâlâ test edilip geliştiriliyor, bu yüzden bazı kontroller sınırlı olabilir ve burada gördükleriniz güncellemeler arasında değişebilir. Bir şey açıklandığı gibi çalışmıyorsa, bize [Yardım alma](/help/mobile-support)'dan bildirin.
:::

Cora, Maxspect Gyre pompalarına bağlanır ve onları okuyup çalıştırabilir.

**İhtiyacınız olacak:** eklerken, gyre ve telefonunuz aynı ağda. **Cihazlar → Ağınızda bir pompa bulun**'u kullanın.

**Ne alırsınız:** **Gyre A** ve **Gyre B** için dalga deseni ve hız, görüntülemek için gyre'nin zamanlaması (Maxspect uygulamasında ayarlayın), **Pompa sağlığı** ve çalışıp çalışmadığı, son ne zaman okunduğuyla birlikte. Bkz. [Ekipmanınızı kontrol etme](/help/mobile-device-control).

:::note Cora Mobile bir gyre'ye nasıl ulaşır
Bir Cora Max akvaryuma hizmet ettiğinde, Cora Mobile, evden uzaktayken dahil, o Cora Max üzerinden çalışır ve **Ayarları değiştir**, o Cora Max'in son okumasından başlar. Aksi halde telefonunuz doğrudan gyre'yle konuşur ve gyre'nin ağında olmalıdır. Gyre'nin sayfasını açmak sonra onu okur; sayfa bunun yerine daha eski kaydedilmiş bir okuma gösteriyorsa, yenilemeye dokunana kadar **Ayarları değiştir** gizli kalır.
:::

## Elle kaydetme

Bazı parametreler ekipmandan değil bir test kitinden gelir. Bir sonuç girmek için, panonun altına kaydırın ve **Parametreleri Kaydet**'e dokunun.

Elle kaydedilen okumalar birinci sınıftır: widget'larda görünürler, kendi kaynaklarını ve yaşlarını taşırlar, Reef Buddy'yi beslerler ve Cora'nın probunuzu neyle karşılaştırdığı, iki kaynağın anlaşmadığını size söylediğinde budur.

## Bir bağlantı çalışmayı durdurursa

Cihaz satırı ne tür bir sorun olduğunu size söyler. **[Cihaz ekleme, düzenleme ve kaldırma](/help/mobile-devices)**'daki tabloya, ve kapsamadığı her şey için **[Sorun giderme](/help/troubleshooting)**'ye bakın.
