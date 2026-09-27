---
title: Sorun giderme
description: Ölçümler durdu, bir cihaz çevrimdışı, uyarı kapanmıyor ya da bir şey ters gidiyor. Buradan başlayın.
section: Help
reviewed: 2026-09-27
order: 1
---

Gördüğünüz belirtiyi aşağıda bulun.

## Widget değer göstermiyor

Şunları sırayla kontrol edin:

1. **Yakındaki widget'larda ölçümlerin yaşına bakın.** Hepsi eskiyse sorun parametrede değil, bağlantıdadır.
2. **Cihazlar sekmesini açın.** Ulaşılamayan cihazın satırında bu yazar.
3. **Cihazın hangi akvaryuma atandığına bakın.** Yanlış akvaryuma veri gönderen bir cihaz, hiç veri göndermeyen bir cihazla tıpatıp aynı görünür. Cihazı açın ve akvaryumunu kontrol edin.
4. **Bu değeri ölçen bir kaynak var mı, bakın.** Fosfatı ölçen bir ekipmanınız yoksa ya da fosfatı elle girmiyorsanız hiçbir yerden fosfat değeri gelmez.

## Ölçüm eski

Yaş etiketi doğruyu söylüyor, yeni bir ölçüm gelmemiş.

- **Elle girilen parametreler** yeni ölçüm girilmezse eskir. Yeni bir ölçüm girin.
- **Ekipmandan gelen ölçümler** eskiyorsa cihaz veri göndermeyi bırakmıştır. **Cihazlar**'da cihazın satırına bakın.
- **Bazı ekipmanlar zaten yavaştır.** Saatte bir ölçüm yapan bir titratörde normalde `1 sa` yazar. Bu bir arıza değildir.

## Cihaza ulaşılamıyor

Sorun genellikle ağdadır.

1. Ekipman açık mı ve kendi uygulamasında çalışıyor mu?
2. Eklendiği ağa bağlı mı?
3. Modeminiz değişti mi? Yeni cihaz, yeni ağ adı ya da misafir ağı yalıtımı olabilir.

Yerel ağınız üzerinden bağlanan ekipmana o ağdan ulaşılabilmesi gerekir. Üretici hesabı üzerinden bağlanan ekipman için bu gerekmez, ama o hesabın hâlâ geçerli olması gerekir.

## Cihazda oturum açma reddedildi yazıyor

Üretici kayıtlı giriş bilgilerini kabul etmedi. Bunun sebebi neredeyse her zaman üreticinin hesabındaki şifrenizi değiştirmiş olmanızdır.

Cihazın satırını açın ve yeniden giriş yapın.

## Cora Max eşleştirmesi başarısız oluyor

Cora Max eklerken işlem yarıda kalırsa Cora Mobile hangi adımın neden başarısız olduğunu söyler. Altında **İptal** ve **Tekrar dene** düğmeleri olur.

- *"Telefonunuz Wi-Fi'nizdeki Cora Max'e ulaşamadı."* Telefonunuzu ve Cora Max'i aynı Wi-Fi ağına bağlayın. iPhone'da Cora'nın Yerel Ağ izni olduğunu da kontrol edin. **Ayarlar → Cihaz erişimi** sizi bu izne götürür ([Ayarlar](/help/mobile-settings) sayfasında anlatılıyor). Sonra **Tekrar dene**'ye dokunun.
- *"Cora Max bu eşleştirme oturumunu kabul etmedi."* Yeniden denemek işe yaramaz. Ekranı kapatın ve **Cihazlar → Cihaz Ekle**'den baştan başlayın.

Başka bir mesaj görürseniz **Tekrar dene**'ye dokunun.

## Cora Max eski veri gösteriyor

Üst çubuktaki durum etiketine bakın. **Çevrimiçi** de **Bulut** da her şeyin yolunda olduğunu gösterir. Birden çok Cora varsa, ölçüm toplamayan ekranda **Bulut** yazar ve ölçümleri aynı ölçüde günceldir. **Eski** ya da **Çevrimdışı** ise ekranın veri kaynağıyla bağlantısını kaybettiğini ve aldığı son veriyi gösterdiğini anlatır. Ekran doğru davranıyor, ama veriler güncel değil.

- Wi-Fi bağlantısını **Ayarlar → Cora Max Ayarları → Wi-Fi** altından kontrol edin
- Ağın kendisinin çalıştığından emin olun
- Etikette **Çevrimiçi** ya da **Bulut** yazıyor ama veri hâlâ eskiyse sorun ekranda değil, Cora Max'ten önceki bir yerdedir. Aynı akvaryuma telefonunuzdan bakın

## Uyarı kapanmıyor

Ölçüm aralığa dönünce uyarı kapanır. Kapanmıyorsa şu üç durumdan biri geçerlidir:

- **Ölçüm gerçekten aralık dışında.** Widget'ın geçmişine bakın.
- **Eşik akvaryumunuza uymuyor.** Eşikleri [Uyarılar ve eşikler](/help/mobile-alerts) sayfasından düzenleyin.
- **Kaynak yanlış ölçüyor.** Kalibrasyonu gereken bir prob gerçekten aralık dışında bir değer bildirir. Eşiği değil, probu düzeltin.

## İki kaynak farklı sonuç veriyor

Bu Cora'nın hatası değil, tam da yapması gereken şey. Probunuzla test kitiniz farklı sonuç veriyorsa bu, sisteminizle ilgili gerçek bir bilgidir.

Böyle bir durumda ICP sonucu işe yarayan üçüncü bir görüştür. Ama tartışmayı tek başına bitirmez. Laboratuvarlar birbirinden farklı sonuç verebilir, numunenin nasıl alındığı ve taşındığı da sonucu etkiler. Birbirini tutan iki test, tek bir testten çok daha değerlidir.

Çoğu zaman probun kalibrasyonu gerekir. Bazen de test kiti eskimiştir. Probu kalibre edin, testi taze reaktifle tekrarlayın ve ikisini aynı koşullarda karşılaştırın. Bir [ICP sonucu](/help/mobile-icp-health) bu karşılaştırmaya üçüncü bir veri ekler.

## Bildirim gelmiyor

1. **Ayarlar → Bildirimler**'de o kategori için anlık bildirimin açık olduğunu kontrol edin
2. Telefonunuzun kendi ayarlarında Cora'nın bildirim izinlerine bakın
3. Günlük özetin, hiçbir şeyin değişmediği günlerde zaten sessiz kaldığını unutmayın

## Bir şeyin neden değiştiğini bulmak

**Ayarlar → Etkinlik**'te tüm priz değişiklikleri, beslemeler, dozajlar ve fiş değişiklikleri listelenir. Her kayıtta isteği kimin verdiği de yazar: Cora Mobile, bir Cora ekranı, sesli komut, Assistant, bir otomasyon kuralı, akıllı düğme ya da hesabınız.

## Düzenlemeden sonra pano bozuk görünüyor

Kayıtlı bir tasarımı yükleyin. **Panolarım**'ı açın ve birini seçin.

Hiç tasarım kaydetmediyseniz düzeni yeniden kurun ve tasarım olarak kaydedin. Bundan sonra o düzene tek dokunuşla dönersiniz.

Her iki durumda da ölçümler, geçmiş ve günlük kayıtları düzenden ayrı saklanır. Panonun arkasındaki hiçbir veri kaybolmaz.

## "Red Sea değerleri güncellenmiyor"

Bu akvaryumun ağındaki hiçbir cihaz şu anda Red Sea ekipmanınızı yoklamıyor. Bu yüzden ekrandaki ölçümler yenilenmedi.

Şunları deneyin:
1. **Ayarlar → Birincil Cora Max**'ı açın ve bir Cora Max'in seçili olduğunu (ya da **Aktif olan herhangi biri (otomatik)** seçeneğinin açık olduğunu) kontrol edin.
2. Akvaryumu, Red Sea ekipmanıyla aynı Wi-Fi'ye bağlı bir cihazda açın.
3. Red Sea ekipmanının açık ve kendi uygulamasında çevrimiçi olduğunu kontrol edin.

Sorun sürerse akvaryumun ve cihazın adını yazarak **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## "Bu pompaya ulaşılamadı: hiçbir şey gönderilmedi"

Jecod ya da Jebao pompasına verilen komut uygulamadan hiç çıkmadı. Genellikle pompa kapalıdır ya da ağına bağlı değildir.

Şunları deneyin:
1. Pompanın açık olduğunu kontrol edin.
2. Eklendiği ağa bağlı olduğunu kontrol edin.
3. **Tekrar dene**'ye dokunun.

Sorun sürerse akvaryumun ve cihazın adını yazarak **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## "Bu pompaya Bluetooth üzerinden ulaşılamadı. Yakınına gidip tekrar deneyin."

Yalnızca Bluetooth ile çalışan Jecod cihazı telefonunuzun menzili dışında.

Şunları deneyin:
1. Pompaya yaklaşın.
2. **Tekrar dene**'ye dokunun.

Sorun sürerse akvaryumun ve cihazın adını yazarak **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## "Bu Gyre'ye ulaşılamadı. Besleme başlatılmadı."

Cora besleme modunu başlatmaya çalıştığında Maxspect gyre (beta entegrasyon) cevap vermedi.

Şunları deneyin:
1. Gyre'nin açık ve ağına bağlı olduğunu kontrol edin.
2. **Tekrar dene**'ye dokunun.

Sorun sürerse akvaryumun ve cihazın adını yazarak **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## "Bu Gyre'ye ulaşılamadı. Programı değiştirilmedi."

Maxspect gyre'ye (beta entegrasyon) gönderilen zamanlama ona ulaşmadı.

Şunları deneyin:
1. Telefonunuzun ya da Cora Max'inizin gyre ile aynı ağda olduğunu kontrol edin.
2. Zamanlama ekranından **Tekrar dene**'ye dokunun.

Sorun sürerse akvaryumun ve cihazın adını yazarak **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## "Apex'e ulaşılamadı: hiçbir şey değişmedi" / "hiçbir şey dozajlanmadı"

Neptune Apex, Trident ya da DŌS kafası komuta veya dozaj isteğine cevap vermedi.

Şunları deneyin:
1. Apex'in kendi uygulamasını açın ve çevrimiçi olduğunu kontrol edin.
2. Kullandığınız cihazın ağ bağlantısını kontrol edin.
3. **Tekrar dene**'ye dokunun.

Sorun sürerse akvaryumun ve cihazın adını yazarak **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## "Bu gönderilemedi: bu akvaryumda bunu gönderebilecek cihaz yok"

Bu akvaryumdaki hiçbir Cora cihazında komutu uygulamak için gereken Apex bağlantı bilgileri yok. Ya da bu bilgilere sahip cihaz çevrimdışı.

Şunlardan birini yapın:
1. Şu anda çevrimiçi olan bir cihazda **Ayarlar**'dan Apex bilgilerini ekleyin.
2. Bu akvaryum için çalışan başka bir Cora Max'i **Birincil Cora Max** olarak seçin.

Sorun sürerse akvaryumun ve cihazın adını yazarak **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## İkincil Cora Max'te "Ana Cora çevrimdışı" yazıyor

Bu akvaryumun birincil tableti çevrimdışı oldu. Bu yüzden ikincil ekran canlı veri yerine aldığı son veriyi gösteriyor.

Şunları deneyin:
1. Birincil tabletin gücünü ve Wi-Fi bağlantısını kontrol edin.
2. Yeniden bağlanmasını bekleyin ya da **Birincil Cora Max** olarak şu anda çevrimiçi olan bir cihazı seçin.

Sorun sürerse akvaryumun ve cihazın adını yazarak **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## "Cihaz çevrimdışı. Son bilinen durum gösteriliyor."

Bu, cihaz çevrimdışı olduğunda olması gereken davranıştır. Cihaz veri göndermeyi bıraktı. Cora da elindeki son değerleri gösteriyor, onları güncelmiş gibi sunmuyor.

Şunları deneyin:
1. Cihazın kendi ağ bağlantısını kontrol edin.
2. Satırda çevrimdışı yazısı kaybolana kadar gösterilen değerlerin canlı olmadığını unutmayın.

Sorun sürerse akvaryumun ve cihazın adını yazarak **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Bazı ReefBeat ayarları gri ya da hiç görünmüyor

Bu bir arıza değil, böyle tasarlandı. Cihaza özel ayarlar yalnızca telefonunuz cihazla aynı ağdayken açılır. Ağın dışındayken yalnızca ölçümler görünür.

Şunları bilin:
1. Bu ayarları değiştirmek için telefonunuzu akvaryumun Wi-Fi'sine bağlayın.
2. Akvaryumdan uzaktayken de ölçümler ve geçmiş normal şekilde çalışır.

Sorun sürerse **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## "Cora'ya ulaşılamadı. Wi-Fi veya mobil verinizi kontrol edip tekrar deneyin."

Giriş yaparken telefonunuz Cora Cloud'a bağlanamıyor. Sorun akvaryum ekipmanınızda değil, telefonunuzun kendi bağlantısında.

Şunları deneyin:
1. Telefonunuzun Wi-Fi ya da mobil veri bağlantısının çalıştığını kontrol edin.
2. Başka bir ağ varsa onu deneyin.
3. **Tekrar dene**'ye dokunun.

Sorun sürerse **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Her şey birden başka bir dilde görünüyor

Hesap dili bir cihazdan değiştirilmiş. Dil cihaz başına değil, tüm hesap için tek bir ayardır.

Şunları deneyin:
1. Uygulamalardan birinde **Ayarlar → Dil**'i açın.
2. Dil yanlışlıkla değiştirildiyse geri alın. Değişiklik her yerde aynı anda geçerli olur.

Sorun sürerse **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Dil değiştikten sonra eski bir uyarı ya da rapor hâlâ eski dilde

Bu bir hata değil, beklenen bir durum. Cora önceden oluşturulmuş içeriği yeniden çevirmez. Yalnızca yeni uyarılar, raporlar ve özetler yeni dilde gelir.

Yapmanız gereken bir şey yok. Yeni içerik güncel dilde gelecek.

Sorun sürerse **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Uyarıyı gördüm ama bildirim gelmeye devam ediyor

Cora Max'teki **Ertele** ve **Kapat** yalnızca o Cora Max'i susturur. Ölçüm aralık dışında kaldığı sürece telefonunuza bildirim gelmeye devam eder.

Şunları yapın:
1. Telefonunuzda daha seyrek haber almak için Cora Mobile'da uyarı kuralını açın ve daha uzun bir **Uyarılar arası bekleme süresi** seçin (en fazla 1 hafta).
2. Eşik akvaryumunuza uymuyorsa eşiğin kendisini değiştirin.

Sorun sürerse [Uyarılar ve eşikler](/help/mobile-alerts) sayfasına bakın ya da **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Dozaj yarıda kaldı ve "geri yükleme" uyarısı geldi

DŌS kafasının bağlantısı dozajın ortasında koptu. Cora dozajın tamamının verildiğini varsaymıyor, bunu size bilerek söylüyor.

Şunları yapın:
1. Uyarıyı açın ve dozaj durmadan önce gerçekte ne kadar verildiğine bakın.
2. Dozajı başta planlanan miktara göre değil, verilen bu miktara göre sürdürün ya da ayarlayın.

Sorun sürerse akvaryumun ve cihazın adını yazarak **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Telefonda oluşturulan sahne Cora Max'te düzenlenemiyor

Sahneleri doğrudan tablette düzenlemek, Cora Max'e yeni gelen bir özellik. Eski bir yazılım, telefonda oluşturulan sahneleri çalıştırır ama düzenleyemez.

Şunlardan birini yapın:
1. Cora Max'i güncelleyin.
2. Sahneyi telefondan düzenlemeye devam edin. Sahne her iki durumda da tablette çalışır.

Sorun sürerse [Güncellemeler ve kurtarma](/help/max-updates) sayfasına bakın ya da **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Cora Assistant yanlış akvaryumdan bahsediyor

Soruyu sormadan önce akvaryum seçilmemiş ya da şu anda yanlış akvaryum seçili.

Şunları yapın:
1. Önce kastettiğiniz akvaryumu seçin.
2. Soruyu yeniden sorun.

Sorun sürerse [Assistant](/help/mobile-assistant) sayfasına bakın ya da **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Cora Assistant cevap vermiyor ya da onay ekranı yeniden çıkıyor

"Cora Assistant'ın kayıtlı akvaryum verilerini kullanmasına izin ver" ayarı kapatılmış. Bu yüzden Assistant'ın cevap verirken kullanacağı veri yok.

Ayarı yeniden açmak için onay ekranında **Kabul Et ve Devam Et**'e dokunun.

Sorun sürerse [Assistant](/help/mobile-assistant) sayfasına bakın ya da **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Laboratuvardan ya da e-postayla gelen ICP sonucu hiç görünmedi

Bir sonucun Cora'ya eklenebilmesi için önce bir akvaryum seçilmesi gerekir. Bazen gönderenin de tanınması gerekir.

Şunları kontrol edin:
1. Cora'ya ilk kez sonuç gönderdiğinizde çıkan ipucunu okuyun.
2. Sorulduğunda sonucun hangi akvaryuma ekleneceğini onaylayın.
3. Daha önce de sonuç gönderdiyseniz e-postayı yine aynı adresten gönderdiğinizden emin olun.

Sorun sürerse [ICP ve sağlık raporları](/help/mobile-icp-health) sayfasına bakın ya da **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## E-postayla gelen ICP bildiriminde laboratuvarın adı yok

Bu, "akvaryum seç" bildiriminde laboratuvar adının eksik çıktığı, bilinen bir sorundu. Güncel sürümlerde düzeltildi.

Şunları bilin:
1. Cora Mobile'ın en son sürüme güncel olduğundan emin olun.
2. Sonucun kendisi etkilenmez. Yalnızca bildirim metninde bir ad eksikti.

Sorun sürerse **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Widget yanlış birimle gösteriyor

Bu bir veri sorunu değil, akvaryumun görüntüleme birimi ayarıdır. Değerler nasıl gösterilirse gösterilsin aynı şekilde saklanır.

Şunları yapın:
1. O akvaryumun **Ayarlar**'ını açın ve görüntüleme birimlerine bakın.
2. Birimleri orada değiştirin. O akvaryumu gösteren tüm telefonlar ve Cora Max ekranları da buna göre güncellenir.

Sorun sürerse **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Görüntüleme birimini değiştirince gösterge ya da eşik farklı görünüyor

Bu beklenen bir durum. Göstergeler, kutucuklar ve geçmiş seçtiğiniz birimle yeniden çizilir. Arkadaki değerler değişmez.

Yapmanız gereken bir şey yok. Değişen yalnızca görünüm.

Sorun sürerse **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Wi-Fi kesintisinden sonra Cora Max hemen yeniden bağlanmıyor

Bağlantısı koptuktan sonra Cora Max ağı sürekli yoklamaz. Her denemeden önce biraz daha uzun bekler ve bekleme süresi aşağı yukarı bir dakikaya kadar çıkar.

Şunları yapın:
1. Ağınız geri geldikten sonra bir dakika kadar bekleyin.
2. Bu süreden sonra hâlâ bağlanmadıysa Wi-Fi bağlantısını **Ayarlar → Cora Max Ayarları → Wi-Fi** altından kontrol edin.

Sorun sürerse [Cora Max ana ekranı](/help/max-tour) sayfasına bakın ya da **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Cora Max'in adını telefonda değiştirdim ama tablette değişmedi

Telefondan verdiğiniz ad, o cihazın hesaptaki etiketidir. Eşleştirme sırasında tablette görünen ad bundan farklı olabilir.

Şunları yapın:
1. Hangi ada baktığınızı kontrol edin: telefondaki cihaz listesindeki ad mı, tabletin kendi eşleştirme ekranındaki ad mı?
2. Değiştirmek istediğiniz hesap etiketiyse, adı telefondaki cihaz listesinden değiştirin.

Sorun sürerse cihazın adını yazarak **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Cora Max'te uyandırma sözcüğünü nereden kapatacağımı bulamıyorum

Uyandırma sözcüğü ayarı **Ses ve Konuşma** bölümünde. Cora Assistant ayarlarında yer almaz.

Şunları yapın:
1. **Ayarlar → Cora Max Ayarları → Ses ve Konuşma → Uyandırma sözcüğü dinleme**'ye gidin.
2. Ayarı kapatın. Sesli konuşma başlatmak için Cora simgesine dokunmaya devam edebilirsiniz.

Sorun sürerse [Cora Max'te ayarlar](/help/max-settings) sayfasına bakın ya da **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Çocuk kilidi Ayarlar'a girmeye izin vermiyor

Çocuk kilidi olması gerektiği gibi çalışıyor. Ekrana belli bir süre dokunulmazsa, kimse bu ekrandan ne dokunarak ne de sesle ekipmanı açıp kapatamaz. Ölçümler güncellenmeye devam eder ve Cora'ya soru sormaya devam edebilirsiniz.

Kilidi açmak için şunlardan birini yapın:
1. **Ses Açma** ya da **Ses Kısma** tuşuna iki saniye içinde üç kez basın.
2. Ekranın sağ üst köşesine beş parmağınızı koyup on saniye basılı tutun.

Sorun sürerse [Cora Max'te ses](/help/max-voice) sayfasına bakın ya da **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Hâlâ çözemediyseniz

**[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin. Hangi akvaryum, hangi ekran olduğunu ve ne görmeyi beklediğinizi yazın. Böylece size daha hızlı ve işe yarar bir cevap verebiliriz.
