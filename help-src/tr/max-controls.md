---
title: Prizler ve kontroller
description: Cora Max'ten Apex prizlerini açıp kapatın, besleme modunu başlatın ya da iptal edin ve Otomatik, Kapalı ve Açık'ın ne anlama geldiğini öğrenin.
section: Cora Max
reviewed: 2026-10-13
order: 5
group: Equipment
---

Bu sayfa Cora Max'ten prizleri açıp kapatmayı ve besleme modunu başlatmayı anlatır. Bunu panodaki priz kutucuklarından, **Prizler ve Besleme** çekmecesinden ya da sesle yapabilirsiniz.

:::warning Bu kontroller akvaryumunuzu doğrudan etkiler
Geri alma yoktur. Asma kilitli prizler önce onay ister. Diğerleri dokunduğunuz anda değişir. Bir komutun sonucu **Onaylandı**, **Onaylanmadı** (gönderildi ama yanıt gelmedi), **Reddedildi** ya da **Değişiklik yok** olabilir. Ayrıntılar [Ekipmanınızı kontrol etme](/help/mobile-device-control) sayfasında.
:::

## Üç durum {#the-three-states}

Her priz üç durumdan birindedir.

**Otomatik**, prizi Apex programına geri verir. Bir priz çoğu zaman bu durumda olmalıdır.

**Kapalı** ve **Açık** elle yapılan geçersiz kılmalardır. Hemen devreye girer ve **siz geri değiştirene kadar öyle kalırlar**. Süreleri dolmaz ve hiçbir şey onları sizin yerinize sıfırlamaz.

:::warning Elle yapılan geçersiz kılmanın süresi dolmaz
İşiniz bitince prizi **Otomatik**'e geri alın, çünkü bunu başka hiçbir şey yapmaz. Yine de manuel ayar bir kilit değildir. Siz, sesiniz ya da bir otomasyon onu daha sonra değiştirebilir.
:::

## Panodan açıp kapatma {#switching-from-the-dashboard}

Priz kutucukları üç durumu gösterir, geçerli olan vurgulanır. İstediğinize dokunun.

Bazı prizlerde bir **asma kilit** vardır. Bu, prizin değişmeden önce onay istediği anlamına gelir. Böylece yanlışlıkla yapılan bir dokunuş önemli bir şeyi açıp kapatamaz. Dokunduğunuzda bir pencere prizi, şu anki durumunu, ayarlamak üzere olduğunuz manuel ayarı ve bunun akvaryuma ne yapabileceğini gösterir. Başka bir yerden kapatılacak bir kilit yoktur.

Varsayılan olarak asma kilit ısıtıcılarda, soğutucularda, ana pompalarda, otomatik su tamamlamada (ATO), otomatik yemliklerde ve Cora'nın sınıflandıramadığı her prizde bulunur. Işıklar, skimmer'lar, dalga pompaları, dozaj pompaları, reaktörler, UV ve fanlar tek dokunuşla değişir.

## Prizler ve Besleme çekmecesi {#the-controls-drawer}

Bunu yalnızca Neptune Apex'i olan bir akvaryumda görürsünüz. Panonun altındaki küçük **Prizler ve Besleme** etiketine dokunun ya da panonun herhangi bir yerinde yukarı kaydırın. **Kontroller** açılır: üstte **BESLEME**, altında **PRİZLER**.

![Kontroller çekmecesi](img/max-controls.webp "Üstte besleme döngüleri, altında bu pano için seçilen prizler.")

Çekmece, [pano düzenleyicisinde](/help/max-dashboard-editing#outlets-feed) **Prizler ve Besleme** altında seçtiğiniz prizleri ve besleme döngülerini gösterir. Hiç seçmediyseniz hepsini gösterir. Asma kilitli prizler burada da onay ister. Diğer kontrolörlerdeki prizler kendi cihaz sayfalarından açılıp kapatılır, [Cora Max'ten ekipman kontrolü](/help/max-device-control) sayfasına bakın.

Bir prize dokunduğunuzda *Apex yanıt vermedi: uygulanmış olabilir* mesajı gelirse tekrar denemeden önce prizi kontrol edin.

## Besleme modu {#feed-mode}

Besleme modu, yem verirken akışı durdurmanın güvenli yoludur. Apex'iniz durması gereken ekipmanı durdurur, gerisine dokunmaz ve süre dolunca **her şeyi kendisi eski haline getirir**.

Pompaları elle kapatmak yerine bunu kullanın. Siz unutsanız bile sistemi eski haline getirir.

Dört besleme döngüsü vardır: Besleme A, Besleme B, Besleme C ve Besleme D. **BESLEME** altında **A**, **B**, **C** ve **D** olarak gösterilir. Bunlar Apex'inizde programlanmış döngülerdir ve her biri farklı bir ekipman grubunu durdurabilir. Yaptığınız işe uygun olanı seçin. **İptal**, çalışan bir döngüyü erken bitirir ve her şeyi hemen eski haline getirir.

Döngüyü çekmeceden başlatın ya da *"besleme modunu başlat"* deyin.

Cora Max, Apex'in yanıt vermediğini söylerse besleme zaten çalışıyor olabilir. Tekrar başlatmadan önce ana pompayı kontrol edin.

## Sesle {#by-voice}

Prizleri sesle de açıp kapatabilirsiniz, örneğin *"skimmer'ı kapat"* ya da *"fanı yeniden otomatiğe al"*.

Ekipmanınıza bir şey ulaşmadan önce Cora **önce size danışır**. Ne yapmak üzere olduğunu söyler ve onayınızı bekler. Ne istediğinizden emin değilse hiçbir şey yapmaz.

Ayrıntılar [Cora ile konuşma](/help/max-voice) sayfasında.

## Ne olduğunu görme {#seeing-what-happened}

Her istek, onu neyin istediği ve nasıl sonuçlandığıyla birlikte kaydedilir. Cora Mobile'dan, bir Cora Max'ten, sesle, asistandan ya da bir otomasyondan gelmesi fark etmez. Cora Max'te üst çubukta akvaryum adına dokunun ve **Etkinlik**'i seçin. Telefonunuzda **Ayarlar → Etkinlik** altındadır. Ayrıntılar [Cora Max'te etkinlik](/help/max-activity) sayfasında.

Bir şey değiştiyse ve nedenini bilmiyorsanız ilk oraya bakın.
