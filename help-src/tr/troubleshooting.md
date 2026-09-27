---
title: Sorun giderme
description: Okumalar durdu, bir cihaz çevrimdışı oldu, uyarılar kapanmıyor, veya bir şey yanlış görünüyor. Buradan başlayın.
section: Help
reviewed: 2026-09-27
order: 1
---

Belirtiden başlayın.

## Bir widget değer göstermiyor

Bu listeyi sırayla kontrol edin:

1. **Yakındaki widget'larda yaşı kontrol edin.** Her şey eskiyse, sorun bağlantıdır, parametre değil.
2. **Cihazlar sekmesini açın.** Ulaşılamayan bir cihaz bunu kendi satırında söyler.
3. **Akvaryum atamasını kontrol edin.** Yanlış akvaryuma bildiren bir cihaz, hiç bildirmeyen bir cihazla tıpatıp aynı görünür. Cihazı açın ve akvaryumunu doğrulayın.
4. **Kaynağın var olduğunu kontrol edin.** Onu ölçen bir ekipmanınız olmadıkça veya elle kaydetmedikçe hiçbir şey fosfat bildirmez.

## Bir okuma eski

Yaş rozeti size gerçeği söylüyor: yeni bir şey gelmedi.

- **Elle kaydedilen parametreler**, hiçbir okuma girilmediğinde eskir. Bir tane kaydedin.
- **Ekipman okumalarının** eskimesi, cihazın bildirmeyi durdurduğu anlamına gelir; **Cihazlar**'da satırını kontrol edin.
- **Bazı ekipman yavaş olmak üzere tasarlanmıştır.** Saatlik ölçüm yapan bir titratör normal olarak `1s` okur. Bu bir arıza değildir.

## Bir cihaza ulaşılamıyor

Genellikle ağdır.

1. Ekipman açık ve kendi uygulamasında çalışıyor mu?
2. Eklendiği ağda mı?
3. Yönlendiriciniz değişti mi (yeni donanım, yeni ağ adı, misafir ağ izolasyonu)?

Yerel ağınız üzerinden bağlanan ekipmanın o ağda erişilebilir olması gerekir. Bir üretici hesabı üzerinden bağlanan ekipmanın buna gereksinimi yoktur, ama o hesabın hâlâ geçerli olması gerekir.

## Bir cihaz oturum açmanın reddedildiğini söylüyor

Üretici kayıtlı oturum açmayı reddetti. Bu neredeyse her zaman parolanızı onların tarafında değiştirdiğiniz içindir.

Cihaz satırını açın ve yeniden oturum açın.

## Bir Cora Max'i eşleştirme başarısız oluyor

Bir Cora Max ekleme ortasında dururuyorsa, Cora Mobile hangi adımın ve neden başarısız olduğunu, altında **İptal** ve **Tekrar dene** ile söyler.

- *"Telefonunuz Wi-Fi'nizdeki Cora Max'e ulaşamadı."* Telefonunuzu ve Cora Max'i aynı Wi-Fi ağına koyun. iPhone'da, Cora'nın Yerel Ağ erişimi olduğunu da kontrol edin: **Ayarlar → Cihaz erişimi** sizi oraya götürür (bkz. [Ayarlar](/help/mobile-settings)). Ardından **Tekrar dene**'ye dokunun.
- *"Cora Max bu eşleştirme oturumunu kabul etmedi."* Yeniden denemek yardımcı olmayacaktır. Ekranı kapatın ve **Cihazlar → Cihaz Ekle**'den yeniden başlayın.

Başka herhangi bir mesaj için, **Tekrar dene**'ye dokunun.

## Cora Max eski veri gösteriyor

Üst çubuktaki durum hapını kontrol edin. **Çevrimiçi** ve **Bulut** ikisi de sağlıklıdır: birden fazla Cora'yla, toplamayı yapmayan ekran **Bulut** gösterir ve okumaları tam olarak aynı derecede günceldir. **Eski** veya **Çevrimdışı**, ekranın kaynağını kaybettiği ve aldığı son veriyi gösterdiği anlamına gelir (doğru davranış, ama güncel değil).

- **Ayarlar → Cora Max → Ağ** altında Wi-Fi'yi kontrol edin
- Ağın kendisinin çalıştığını kontrol edin
- Hap **Çevrimiçi** veya **Bulut** okuyorsa ve veri hâlâ eskiyse, sorun ondan önceki bir yerdedir: aynı akvaryumu telefonunuzda kontrol edin

## Bir uyarı kapanmıyor

Okuma aralığına döndüğünde bir uyarı kapanır. Kapanmıyorsa:

- **Okuma gerçekten aralık dışında.** Widget'ın geçmişine bakın.
- **Eşik akvaryumunuz için yanlış.** Bkz. [Uyarılar ve eşikler](/help/mobile-alerts).
- **Kaynak yanlış.** Kalibrasyon gerektiren bir prob, gerçekten aralık dışında bir sayı bildirir. Eşiği değil probu düzeltin.

## İki kaynak anlaşmıyor

Bu, Cora'nın çalışması, başarısız olması değil. Probunuz ve test kitiniz anlaşmadığında, bu sisteminiz hakkında gerçek bir gerçektir.

Bir ICP sonucu burada kullanışlı bir üçüncü görüştür, ama tartışmayı çözmez: laboratuvarlar birbirinden farklıdır ve bir örneğin taşınması ve nakliyesi sonucu hareket ettirir. Anlaşan iki test, birinden çok daha değerlidir.

Genellikle prob kalibrasyon gerektirir; bazen test kiti eskidir. Probu kalibre edin, testi taze reaktifle yeniden çalıştırın ve ikisini aynı koşullar altında karşılaştırın. Bir [ICP sonucu](/help/mobile-icp-health), bu karşılaştırmaya üçüncü bir veri noktası ekler.

## Bildirim almıyorum

1. **Ayarlar → Bildirimler**: o kategorinin push göndermeye izinli olduğunu kontrol edin
2. Telefonunuzun Cora için kendi bildirim izinlerini kontrol edin
3. Günlük briefinginin, hiçbir şey değişmediği günlerde bilerek sessiz kaldığını unutmayın

## Bir şeyin neden değiştiğini belirleme

**Ayarlar → Etkinlik**, her priz değişikliğini, beslemeyi, dozajı ve fiş değişikliğini, onu kimin istediğiyle birlikte listeler: Cora Mobile, bir Cora ekranı, ses, Assistant, bir otomasyon kuralı, akıllı bir düğme veya hesabınız.

## Panom düzenledikten sonra yanlış görünüyor

Kaydedilmiş bir tasarım yükleyin: **Panolarım**, ardından bir tanesini seçin.

Bir tane kaydetmediyseniz, düzeni yeniden oluşturun ve ardından bir tasarım olarak kaydedin. O noktadan sonra, ona geri dönmek tek bir dokunuştur.

Her iki durumda da, okumalar, geçmiş ve günlük kayıtları düzenden ayrı saklanır, bu yüzden panonun arkasındaki hiçbir şey kaybolmaz.

## "Red Sea okumaları güncellenmeyi durdurdu"

**Ne anlama gelir:** Bu akvaryumun ağındaki hiçbir cihaz şu anda Red Sea ekipmanınızı yoklamıyor, bu yüzden ekrandaki okumalar yenilenmemiş.

**Ne yapmalı:**
1. **Ayarlar → Birincil Cora Max**'ı açın ve bir Cora Max'in ayarlandığını (veya **Aktif olan herhangi biri (otomatik)**'in seçildiğini) kontrol edin.
2. Akvaryumu, Red Sea ekipmanıyla aynı Wi-Fi'deki bir cihazda açın.
3. Red Sea ekipmanının açık olduğunu ve kendi uygulamasında çevrimiçi olduğunu doğrulayın.

**Hâlâ çalışmıyor mu?** Akvaryum ve cihaz adıyla **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## "Bu pompaya ulaşılamadı: hiçbir şey gönderilmedi"

**Ne anlama gelir:** Bir Jecod veya Jebao pompasına bir komut uygulamadan hiç ayrılmadı, genellikle pompa kapalı veya ağının dışında olduğu için.

**Ne yapmalı:**
1. Pompanın açık olduğunu kontrol edin.
2. Eklendiği ağda olduğunu kontrol edin.
3. **Tekrar dene**'ye dokunun.

**Hâlâ çalışmıyor mu?** Akvaryum ve cihaz adıyla **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## "Bu pompaya Bluetooth üzerinden ulaşılamadı. Yanına gidip yeniden deneyin."

**Ne anlama gelir:** Sadece Bluetooth üzerinden çalışan bir Jecod cihazı telefonunuzun menzilinin dışında.

**Ne yapmalı:**
1. Pompaya daha yakına gidin.
2. **Tekrar dene**'ye dokunun.

**Hâlâ çalışmıyor mu?** Akvaryum ve cihaz adıyla **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## "O gyre'ye ulaşılamadı. Hiçbir besleme başlatılmadı."

**Ne anlama gelir:** Bir Maxspect gyre (beta entegrasyonu), Cora onda besleme modunu başlatmaya çalıştığında yanıt vermedi.

**Ne yapmalı:**
1. Gyre'nin açık ve ağında olduğunu kontrol edin.
2. **Tekrar dene**'ye dokunun.

**Hâlâ çalışmıyor mu?** Akvaryum ve cihaz adıyla **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## "O gyre'ye ulaşılamadı. Programı değiştirilmedi."

**Ne anlama gelir:** Bir Maxspect gyre'ye (beta entegrasyonu) bir zamanlama push'u ona ulaşmayı başaramadı.

**Ne yapmalı:**
1. Telefonunuzun veya Cora Max'inizin gyre'nin ağında olduğunu kontrol edin.
2. Zamanlama ekranından **Tekrar dene**'ye dokunun.

**Hâlâ çalışmıyor mu?** Akvaryum ve cihaz adıyla **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## "Apex'e ulaşılamadı: hiçbir şey değişmedi" / "hiçbir şey dozajlanmadı"

**Ne anlama gelir:** Bir Neptune Apex, Trident veya DŌS kafası bir komuta veya dozaj isteğine yanıt vermedi.

**Ne yapmalı:**
1. Apex'in kendi uygulamasını açın ve çevrimiçi olduğunu doğrulayın.
2. Kullandığınız cihazda ağ bağlantısını kontrol edin.
3. **Tekrar dene**'ye dokunun.

**Hâlâ çalışmıyor mu?** Akvaryum ve cihaz adıyla **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## "Bu gönderilemedi: bu akvaryumda hiçbir cihaz bunu gönderemez"

**Ne anlama gelir:** Bu akvaryumdaki hiçbir Cora cihazı komutu yerine getirmek için gereken Apex bağlantı ayrıntılarına sahip değil, veya sahip olan çevrimdışı.

**Ne yapmalı:**
1. Şu anda çevrimiçi olan bir cihazda **Ayarlar**'da Apex ayrıntılarını ekleyin, veya
2. Bu akvaryum için farklı, çalışan bir Cora Max'i **Birincil Cora Max** olarak ayarlayın.

**Hâlâ çalışmıyor mu?** Akvaryum ve cihaz adıyla **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## İkincil bir Cora Max "Ana Cora çevrimdışı" gösteriyor

**Ne anlama gelir:** Bu akvaryum için birincil tablet çevrimdışı oldu, bu yüzden bu ikincil ekran canlı veri yerine aldığı son veriyi gösteriyor.

**Ne yapmalı:**
1. Birincil tabletin gücünü ve Wi-Fi'sini kontrol edin.
2. Yeniden bağlanmasını bekleyin, veya **Birincil Cora Max**'ı şu anda çevrimiçi olan bir cihaza değiştirin.

**Hâlâ çalışmıyor mu?** Akvaryum ve cihaz adıyla **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## "Cihaz çevrimdışı. Bilinen son durum gösteriliyor."

**Ne anlama gelir:** Normal çevrimdışı işleme: cihaz bildirmeyi durdurdu ve Cora, güncelmiş gibi davranmak yerine sahip olduğu son değerleri gösteriyor.

**Ne yapmalı:**
1. Cihazın kendi ağ bağlantısını kontrol edin.
2. Satır artık çevrimdışı demeyene kadar gösterilen değerleri canlı olmayan olarak ele alın.

**Hâlâ çalışmıyor mu?** Akvaryum ve cihaz adıyla **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Bazı ReefBeat ayarları griye dönmüş veya eksik

**Ne anlama gelir:** Bu bir tasarım kararıdır, bir arıza değil. Cihaza özel ayarlar (okumaların aksine) yalnızca telefonunuz cihazın kendisiyle aynı ağdayken açılır; o ağın dışında, yalnızca okumalar gösterilir.

**Ne yapmalı:**
1. Bu ayarları değiştirmek için akvaryumun kendi Wi-Fi'sini ziyaret edin.
2. Okumalar ve geçmiş, akvaryumdan uzaktayken normal şekilde çalışmayı sürdürür.

**Hâlâ çalışmıyor mu?** **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## "Cora'ya ulaşılamadı. Wi-Fi'nizi veya mobil verinizi kontrol edin, ardından yeniden deneyin."

**Ne anlama gelir:** Telefonunuzun oturum açarken Cora Cloud'a kullanılabilir bir bağlantısı yok. Bu, akvaryum ekipmanınızla değil telefonunuzun kendi bağlantısıyla ilgilidir.

**Ne yapmalı:**
1. Telefonunuzun çalışan bir Wi-Fi veya mobil veri bağlantısı olduğunu kontrol edin.
2. Kullanılabiliyorsa farklı bir ağ deneyin.
3. **Tekrar dene**.

**Hâlâ çalışmıyor mu?** **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Her şey aniden yanlış dilde

**Ne anlama gelir:** Hesap dili herhangi bir cihazdan değiştirildi. Dil, cihaz başına değil tüm hesap için bir ayardır.

**Ne yapmalı:**
1. Her iki uygulamada da **Ayarlar → Dil**'i açın.
2. Yanlışlıkla değiştirildiyse geri ayarlayın; değişiklik her yerde aynı anda uygulanır.

**Hâlâ çalışmıyor mu?** **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Değiştirdikten sonra eski bir uyarı veya rapor hâlâ farklı bir dilde

**Ne anlama gelir:** Bu beklenendir, bir hata değil. Cora zaten oluşturulmuş içeriği yeniden çevirmez; sadece yeni uyarılar, raporlar ve briefingler yeni dili takip eder.

**Ne yapmalı:**
1. Düzeltilecek bir şey yok. Geçerli dili kullanacak yeni içeriği bekleyin.

**Hâlâ çalışmıyor mu?** **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Onayladıktan sonra bile bir uyarı bildirmeyi durdurmuyor

**Ne anlama gelir:** **Kapat** (uyarıyı kalıcı olarak kapatır) ile **Ertele** (onu bir haftaya kadar geçici olarak susturur) arasında bir karışıklık.

**Ne yapmalı:**
1. Durumu anlıyor ve kabul ediyorsanız, **Kapat**'ı kullanın.
2. Sadece bir süreliğine sessizlik istiyorsanız, **Ertele**'yi kullanın ve bir uzunluk seçin.

**Hâlâ çalışmıyor mu?** Bkz. [Uyarılar ve eşikler](/help/mobile-alerts), veya **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Bir dozaj yarı yolda durdu ve bir "geri getirme" uyarısı belirdi

**Ne anlama gelir:** DŌS kafası dozaj ortasında bağlantısını kaybetti, bu yüzden Cora tam dozajın girdiğini varsaymak yerine bilerek size bunu söylüyor.

**Ne yapmalı:**
1. Uyarıyı açın ve durmadan önce gerçekte ne kadarının dozajlandığını kontrol edin.
2. Dozajı, orijinal olarak zamanlanan miktar yerine bu miktara göre sürdürün veya ayarlayın.

**Hâlâ çalışmıyor mu?** Akvaryum ve cihaz adıyla **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Telefonda yapılan bir sahne Cora Max'te düzenlenebilir görünmüyor

**Ne anlama gelir:** Sahneleri doğrudan tablette düzenlemek daha yeni bir Cora Max yeteneğidir. Daha eski bir yazılım telefonda yapılan sahneleri hâlâ çalıştırabilir, sadece onları orada düzenleyemez.

**Ne yapmalı:**
1. Cora Max'i güncelleyin, veya
2. O sahneyi telefondan düzenlemeyi sürdürün; her iki durumda da tablette çalışmayı sürdürecektir.

**Hâlâ çalışmıyor mu?** Bkz. [Güncellemeler ve kurtarma](/help/max-updates), veya **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Cora Assistant yanlış akvaryum hakkında yanıt veriyor

**Ne anlama gelir:** Sormadan önce hiçbir akvaryum seçilmedi, veya şu anda yanlış akvaryum etkin.

**Ne yapmalı:**
1. Önce kastettiğiniz akvaryumu seçin.
2. Yeniden sorun.

**Hâlâ çalışmıyor mu?** Bkz. [Assistant](/help/mobile-assistant), veya **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Cora Assistant yanıt vermeyi reddediyor, veya onay ekranını yeniden gösteriyor

**Ne anlama gelir:** "Cora Assistant'ın kayıtlı akvaryum verilerini kullanmasına izin ver" kapatıldı, bu yüzden yanıt verecek hiçbir şeyi yok.

**Ne yapmalı:**
1. Onu yeniden açmak için onay ekranında **Kabul Et ve Devam Et**'e dokunun.

**Hâlâ çalışmıyor mu?** Bkz. [Assistant](/help/mobile-assistant), veya **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Bir lab veya e-postayla gelen ICP sonucu hiç görünmedi

**Ne anlama gelir:** Bir sonucu Cora'ya almak, herhangi bir yere eklenmeden önce onun için seçilmiş bir akvaryum, ve bazen tanınan bir gönderen gerektirir.

**Ne yapmalı:**
1. Cora'ya bir sonuç gönderdiğiniz ilk seferde gösterilen giriş ipucunu kontrol edin.
2. İstendiğinde sonucun hangi akvaryuma eklenmesi gerektiğini doğrulayın.
3. Daha önce bir tane gönderdiyseniz, e-postanın önce kullandığınız adresten gönderildiğinden emin olun.

**Hâlâ çalışmıyor mu?** Bkz. [ICP ve sağlık raporları](/help/mobile-icp-health), veya **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## E-postayla gelen bir ICP bildirimi hiçbir lab adlandırmıyor

**Ne anlama gelir:** "Akvaryum seç" push bildiriminin lab adını kaçırdığı bilinen bir sorun. Geçerli sürümlerde düzeltildi.

**Ne yapmalı:**
1. Cora Mobile'ın en son sürüme güncellendiğinden emin olun.
2. Sonucun kendisi etkilenmez; yalnızca bildirim metninde bir ad eksikti.

**Hâlâ çalışmıyor mu?** **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Bir widget yanlış birimleri gösteriyor

**Ne anlama gelir:** Bu akvaryumun görüntü birimleri ayarıdır, bir veri sorunu değil. Değerler, nasıl görüntülendiklerinden bağımsız olarak aynı şekilde saklanır.

**Ne yapmalı:**
1. O akvaryum için **Ayarlar**'ı açın ve görüntü birimlerini kontrol edin.
2. Onları orada değiştirin; o akvaryumu gösteren her telefon ve Cora Max eşleşecek şekilde güncellenir.

**Hâlâ çalışmıyor mu?** **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Görüntü birimlerini değiştirdikten sonra bir gösterge veya eşik farklı görünüyor

**Ne anlama gelir:** Beklenen. Göstergeler, kutular ve geçmiş, seçtiğiniz birimde yeniden çizilir; altta yatan değerler değişmedi.

**Ne yapmalı:**
1. Düzeltilecek bir şey yok; bu sadece görsel.

**Hâlâ çalışmıyor mu?** **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Cora Max bir Wi-Fi kesintisinden sonra hemen yeniden bağlanmıyor

**Ne anlama gelir:** Bağlantısını kaybettikten sonra Cora Max, ağı bombalamak yerine her tekrar denemeden önce biraz daha uzun bekler; yeniden denemeden önce kabaca bir dakikaya kadar geriler.

**Ne yapmalı:**
1. Ağınız geri geldikten sonra bir dakika kadar bekleyin.
2. O süreden sonra hâlâ yeniden bağlanmadıysa, **Ayarlar → Ağ** altında Wi-Fi'yi kontrol edin.

**Hâlâ çalışmıyor mu?** Bkz. [Cora Max ana ekranı](/help/max-tour), veya **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Bir Cora Max'i telefonda yeniden adlandırmak tabletin gösterdiğini değiştirmiyor

**Ne anlama gelir:** Telefondan belirlediğiniz ad, o cihaz için hesap düzeyinde bir etikettir. Eşleştirme sırasında tabletin kendisinde gösterilen ad farklı bir şey olabilir.

**Ne yapmalı:**
1. Hangi "ada" baktığınızı kontrol edin: telefondaki cihaz listenizdeki mi, yoksa tabletin kendi eşleştirme ekranındaki mi.
2. Değiştirmek istediğiniz hesap etiketiyse, telefonun cihaz listesinden yeniden adlandırın.

**Hâlâ çalışmıyor mu?** Cihaz adıyla **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Cora Max'te uyandırma sözcüğünü nerede kapatacağımı bulamıyorum

**Ne anlama gelir:** Uyandırma sözcüğü anahtarı, çoğu kişiyi şaşırtan bir şekilde Cora Assistant ayarları grubu altında değil **Ses** altındadır.

**Ne yapmalı:**
1. **Ayarlar → Ses → Uyandırma sözcüğü dinleme**'ye gidin.
2. Onu kapatın; sesli bir oturum başlatmak için hâlâ Cora simgesine dokunabilirsiniz.

**Hâlâ çalışmıyor mu?** Bkz. [Cora Max'te ayarlar](/help/max-settings), veya **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Çocuk kilidi kimseyi Ayarlar'a bırakmıyor

**Ne anlama gelir:** Bu, amaçlandığı gibi çalışıyor. Çocuk kilidi, dokunulmadan belirli bir süre geçtikten sonra dokunmatik ekranı ve ses kontrollerini kilitler; okumalar altında güncellenmeyi sürdürür.

**Ne yapmalı:**
1. **Ses Arttır** veya **Ses Azalt**'a iki saniye içinde üç kez basın, veya
2. Ekranın sağ üst köşesinde beş parmağınızı on saniye basılı tutun.

**Hâlâ çalışmıyor mu?** Bkz. [Cora Max'te ses](/help/max-voice), veya **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Hâlâ takılı kaldıysanız

**[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin. Bize hangi akvaryumu, hangi ekranı ve ne görmeyi beklediğinizi söyleyin; bu size daha hızlı kullanışlı bir yanıt sağlar.
