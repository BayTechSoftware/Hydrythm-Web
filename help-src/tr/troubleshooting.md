---
title: Sorun giderme
description: Eski bir ölçümü, çevrimdışı olan bir cihazı, ulaşmayan bir komutu, eşleşmeyen bir Cora Max'i ya da kapanmayan bir uyarıyı düzeltin.
section: Help
reviewed: 2026-10-18
order: 1
---

Sorununuzun ait olduğu grubu, ardından gördüğünüz mesajı ya da belirtiyi bulun. Tırnak içindeki başlıklar Cora'nın size gösterdiği sözcüklerin tam kendisidir.

- [Ölçümler ve widget'lar](#readings-and-widgets)
- [Bir cihaz bildirmeyi bıraktı ya da ona ulaşılamıyor](#device-not-reporting)
- [Bir komut ulaşmadı](#command-did-not-go-through)
- [Cora Max](#cora-max)
- [Uyarılar, bildirimler ve günlük özet](#alerts-and-notifications)
- [Cora Assistant ve ses](#cora-assistant-and-voice)
- [Laboratuvar sonuçları ve sağlık raporları](#lab-results-and-health-reports)
- [Dil, birimler ve giriş yapma](#language-units-and-signing-in)


## Ölçümler ve widget'lar {#readings-and-widgets}

### Bir widget değer göstermiyor {#a-widget-shows-no-value}

Bunları sırayla kontrol edin.

1. Yakındaki widget'lardaki yaşa bakın. Hepsi de eskiyse sorun parametrede değil bağlantıdadır.
2. **Cihazlar** sekmesini açın. Bir cihaza ulaşılamıyorsa satırında kırmızı bir nokta vardır ya da bunu söyler.
3. Cihazın hangi akvaryumda olduğunu kontrol edin. Yanlış akvaryuma bildiren bir cihaz, hiç bildirmeyen bir cihazla tıpatıp aynı görünür. Cihazı açın ve akvaryumunu kontrol edin.
4. Onu bir şeyin ölçtüğünü kontrol edin. Fosfatı ölçen bir ekipmanınız yoksa ya da onu elle kaydetmiyorsanız hiçbir şey fosfat bildirmez.

### Bir widget gri {#a-widget-is-grey}

Gri, Cora'nın o ölçümü değerlendirmediği anlamına gelir. Üç olağan neden vardır.

1. Onun uyarısı kapalı. Uyarı Merkezi'nin **Kurallar** sekmesinde yeniden açın.
2. Onu değerlendirecek bir aralığı yok. Widget'a uzun basın ve bir aralık ayarlayın.
3. Ölçüm çok eski. Widget'taki yaşı kontrol edin, sonra yeni bir ölçüm kaydedin ya da cihazı kontrol edin.

Her rengin ne anlama geldiği [Panonuzu okuma](/help/mobile-dashboard#colours) sayfasında.

### Bir ölçüm eski {#a-reading-is-stale}

Widget'taki yaş doğrudur. Yeni bir şey gelmemiştir.

- Elle kaydedilen parametreler kimse ölçüm kaydetmediğinde eskir. Bir tane kaydedin.
- Ekipman ölçümleri cihaz bildirmeyi bıraktığında eskir. **Cihazlar** içindeki satırına bakın.
- Bazı ekipmanlar yalnızca ara sıra bildirir. Saatte bir ölçen bir titratör genellikle `1 sa` gösterir. Bu normaldir.

### İki kaynak birbirini tutmuyor {#two-sources-disagree}

Hiçbir şey bozuk değil. Probunuz ile test kitiniz birbirini tutmadığında bu, sisteminiz hakkında gerçek bir şey söyler.

Genellikle probun kalibrasyona ihtiyacı vardır. Bazen test kiti eskidir. Probu kalibre edin, taze reaktifle yeniden test edin ve ikisini aynı koşullarda karşılaştırın. Bir ölçüm açıkça yanlışsa onu hariç tutabilirsiniz. [Bir parametreyi inceleme](/help/mobile-metric-detail) sayfasına bakın.

Bir [ICP sonucu](/help/mobile-icp-health) size karşılaştırmak için üçüncü bir sayı verir, ama soruyu tek başına çözmez. Laboratuvarlar birbirinden farklıdır ve bir numunenin nasıl işlendiği ve gönderildiği sonucu değiştirir.

### Bir widget yanlış birimleri gösteriyor {#a-widget-shows-the-wrong-units}

Bu, akvaryumun görüntüleme birimleridir. Verileriniz sağlamdır ve değerler nasıl gösterilirse gösterilsin aynı şekilde saklanır.

1. **Ayarlar**'ı açın, o akvaryumu açın ve **Birimler**'i seçin.
2. Onları orada değiştirin. O akvaryumu gösteren her telefon ve Cora Max buna uyacak şekilde güncellenir.

### Birimleri değiştirdikten sonra bir gösterge ya da eşik farklı görünüyor {#a-gauge-or-threshold-looks-different-after-changing-display-}

Bu beklenen bir durumdur. Göstergeler, kutucuklar ve geçmiş seçtiğiniz birimde yeniden çizilir. Alttaki değerler değişmemiştir.

### Düzenledikten sonra panom yanlış görünüyor {#my-dashboard-looks-wrong-after-editing}

Ölçümleriniz, geçmişiniz ve günlüğünüz düzenden ayrı saklanır, bu yüzden hiçbir şey kaybetmediniz.

- **Telefonunuzda** düzenleyicide geri alma ya da kayıtlı tasarım yoktur. **Panoyu düzenle**'yi açın ve widget'ları geri koyun. Ayrıntılar [Panonuzu düzenleme](/help/mobile-dashboard-editing) sayfasında.
- **Cora Max'te** kayıtlı bir tasarım yükleyin: **Pano düzeni**'ni açın, **Panolarım**'a dokunun ve birini seçin. Kaydetmediyseniz düzeni yeniden oluşturun ve **Bu tasarımı kaydet**'e dokunun, böylece bir dahaki sefere tek dokunuş yeter. Ayrıntılar [Cora Max panosunu düzenleme](/help/max-dashboard-editing#saving-layouts) sayfasında.

### Bir şeyin neden değiştiğini bulma {#establishing-why-something-changed}

**Ayarlar → Etkinlik**, her priz değişikliğini, beslemeyi ve dozu ve onu neyin istediğini listeler: Cora Mobile, bir Cora Max, ses, asistan, bir otomasyon ya da hesabınız. Ayrıntılar [Etkinlik ve zaman çizelgesi](/help/mobile-activity) sayfasında.

## Bir cihaz bildirmeyi bıraktı ya da ona ulaşılamıyor {#device-not-reporting}

### "[Cihaz]: bildirim yapmıyor" {#device-stopped-reporting}

Cora bunu bir cihaz sessizleştiğinde gönderir. Cihazın bozuk olduğu anlamına gelmez, yalnızca Cora'nın bir süredir ondan haber almadığı anlamına gelir. Cora'nın her marka için ne kadar beklediği [Uyarılar ve eşikler](/help/mobile-alerts#stopped-reporting) sayfasında.

1. Cihazın gücünü ve Wi-Fi ya da Bluetooth menzilini kontrol edin.
2. Onu okuyan Cora Max'in açık ve çevrimiçi olduğunu kontrol edin. Cora Max olmadan telefonunuz bir Neptune Apex, Red Sea ya da Jecod cihazını yalnızca Cora Mobile aynı Wi-Fi'da açıkken okur.
3. Bir sonraki ölçümü bekleyin. Yeniden bildirmeye başladığında ikinci bir bildirim alırsınız.


### "Cihaz çevrimdışı. Son bilinen durum gösteriliyor." {#device-is-offline-showing-last-known-state}

Cihaz bildirmeyi bıraktı ve Cora elindeki son değerleri gösteriyor. Güncel değiller.

1. Cihazın kendi ağ bağlantısını kontrol edin.
2. Satırda çevrimdışı yazması kalkana kadar değerleri canlı saymayın.

### Bir cihaza ulaşılamıyor {#a-device-cannot-be-reached}

Genellikle sorun ağdadır.

1. Ekipman açık ve kendi uygulamasında çalışıyor mu?
2. Onu eklediğiniz ağda mı?
3. Modeminizle ilgili bir şey değişti mi (yeni donanım, yeni ağ adı, misafir ağı yalıtımı)?

Yerel ağınızdaki ekipmana o ağda ulaşılabilmelidir. Bir üretici hesabı üzerinden bağlanan ekipman için bu gerekmez, ama o hesabın yine de geçerli olması gerekir. Cihazın adresi değiştiyse onu **Cihazlar** sekmesinde açın ve **Bağlantı** altında **Bağlantıyı düzenle**'ye dokunun.

### Bir cihaz girişin reddedildiğini söylüyor {#a-device-says-the-sign-in-was-refused}

Üretici kayıtlı girişi reddetti. Neredeyse her zaman bunun nedeni onlarla olan şifrenizi değiştirmiş olmanızdır. Cihazın satırını açın ve yeniden giriş yapın.

### "Red Sea değerleri güncellenmiyor" {#red-sea-readings-have-stopped-updating}

Bu akvaryumda şu anda hiçbir şey Red Sea ekipmanınızı okumuyor, bu yüzden ekrandaki ölçümler yenilenmiyor.

1. **Ayarlar**'ı, akvaryumu, ardından **Birincil Cora Max**'i açın. Bir Cora Max'in ayarlı olduğunu ya da **Aktif olan herhangi biri (otomatik)**'in seçili olduğunu kontrol edin.
2. Cora Max'iniz yoksa telefonunuz Red Sea ekipmanıyla aynı Wi-Fi'dayken akvaryumu Cora Mobile'da açın.
3. Red Sea ekipmanının kendi uygulamasında açık ve çevrimiçi olduğunu kontrol edin.

### Bazı ReefBeat ayarları soluk görünüyor ya da yok {#some-reefbeat-settings-are-greyed-out-or-missing}

Bu normaldir. Bir Red Sea cihazının kendi ayarları yalnızca telefonunuz cihazla aynı ağdayken açılır. O ağdan uzaktayken yalnızca ölçümleri görürsünüz.

1. O ayarları değiştirmek için akvaryumun Wi-Fi'ına katılın.
2. Siz uzaktayken ölçümler ve geçmiş çalışmaya devam eder.


## Bir komut ulaşmadı {#command-did-not-go-through}

Her komut **Onaylandı**, **Onaylanmadı**, **Reddedildi** ya da **Değişiklik yok** olarak sonuçlanır. Her birinin ne anlama geldiği [Ekipmanınızı kontrol etme](/help/mobile-device-control) sayfasında.

### "Bu pompaya ulaşılamadı: hiçbir şey gönderilmedi" {#could-not-reach-this-pump-nothing-was-sent}

Jecod ya da Jebao pompanıza giden bir komut Cora'dan hiç çıkmadı. Telefonunuzda mesaj *"Bu pompaya ulaşılamadı. Telefonunuzla aynı Wi-Fi'de olması gerekir."* şeklindedir. Genellikle pompa kapalıdır ya da ağında değildir.

1. Pompanın açık olduğunu kontrol edin.
2. Onu eklediğiniz ağda olduğunu ve telefonunuzun ya da Cora Max'in de o ağda olduğunu kontrol edin.
3. **Tekrar dene**'ye dokunun.

### "Bu pompaya Bluetooth üzerinden ulaşılamadı. Yakınına gidip tekrar deneyin." {#could-not-reach-this-pump-over-bluetooth-stand-near-it-and-t}

Telefonunuz yalnızca Bluetooth kullanan bir Jecod pompasının menzili dışında. Pompaya yaklaşın ve **Tekrar dene**'ye dokunun.


### "Apex'e ulaşılamadı: hiçbir şey değişmedi" / "hiçbir şey dozajlanmadı" {#could-not-reach-the-apex-nothing-changed-nothing-was-dosed}

Bir Neptune Apex, Trident ya da DŌS kafası bir komuta ya da doz isteğine yanıt vermedi.

1. Apex'in kendi uygulamasını açın ve çevrimiçi olduğunu kontrol edin.
2. Kullandığınız telefonun ya da Cora Max'in ağ bağlantısını kontrol edin. Bir DŌS kafasını telefonunuzdan değiştirmek, telefonun Apex ile aynı ağda olmasını gerektirir.
3. **Tekrar dene**'ye dokunun.

### "… gönderilemedi: Bu Cora Max'te Apex bilgileri yok" {#this-could-not-be-sent-no-device-on-this-tank-can-send-it}

Cora Max bunu Apex'inize ulaşmanın hiçbir yolu olmadığında ve akvaryumdaki başka hiçbir cihaz komutu onun yerine gönderemediğinde gösterir. Mesaj Apex bilgilerini Ayarlar'dan eklemenizi söyler, ama bunlar artık telefonunuzda ayarlanır.

1. Telefonunuzda **Cihazlar**'ı, ardından Apex'inizi açın ve **Bağlantı** altında adresini ve giriş bilgisini kontrol edin. Onları **Bağlantıyı düzenle** ile düzeltin.
2. Ya da çalışan bir Cora Max'i bu akvaryumun **Birincil Cora Max**'i yapın: **Ayarlar**, akvaryumu açın, sonra **Birincil Cora Max**.

### Besleme telefondan başlamıyor {#feed-does-not-start}

Telefonunuzda **Besle** yalnızca Neptune Apex'i olan bir akvaryumda görünür ve Apex'te programlanmış besleme döngülerinden birini başlatır.

- *"Bu akvaryumdaki hiçbir Cora Apex'e ulaşamıyor ve siz onun ağında değilsiniz."* Apex'in Wi-Fi'ına katılın ya da akvaryuma bir Cora Max eşleştirin.
- *"Apex yanıt vermedi ama zaten besleme yapıyor olabilir."* Tekrar denemeden önce kontrolörü kontrol edin.

### Bir doz yarıda durdu ve bir "geri yükleme" uyarısı çıktı {#a-dose-stopped-partway-through-and-a-restore-alert-appeared}

DŌS kafası doz sırasında bağlantıyı kaybetti. Cora, dozun tamamının gittiğini varsaymak zorunda kalmamak için size bunu söyler.

1. Uyarıyı açın ve durmadan önce ne kadar dozlandığını kontrol edin.
2. Dozu sürdürmeye mi yoksa ayarlamaya mı karar vermek için o miktarı kullanın.

## Cora Max {#cora-max}

### Cora Max'im çevrimdışı {#my-cora-max-is-offline}

Telefonunuzda **Cihazlar** sekmesindeki satırında kırmızı bir nokta vardır. Çevrimdışıyken okuduğu ekipman güncellenmeyi bırakır, o ekipman için "bildirim yapmıyor" uyarıları alabilirsiniz ve uzaktan gönderilen komutlar *"Hiçbir şey gönderilmedi"* olarak dönebilir.

1. Cora Max'in elektriği olduğunu ve ekranın açık olduğunu kontrol edin.
2. Cora Max'te **Ayarlar → Cora Max Ayarları → Wi-Fi**'ı ve modeminizin çalıştığını kontrol edin.
3. Akvaryumda başka bir Cora Max varsa devralabilmesi için **Birincil Cora Max**'i **Aktif olan herhangi biri (otomatik)** olarak ayarlayın. [Birden fazla Cora cihazı](/help/mobile-multi-device#primary-cora-max) sayfasına bakın.
4. Düzgün açılmıyorsa [Güncellemeler ve kurtarma](/help/max-updates) sayfasına bakın.

:::tip Bir dahaki sefere haberiniz olsun
Cora Mobile'da **Ayarlar → Otomasyonlar**'ı açın ve **Bir cihaz çevrimdışı olduğunda** tetikleyicisiyle bir kural oluşturun, Cora Max'inizi seçin ve **Beni Bilgilendir** eylemini ekleyin. Ayrıntılar [Otomasyonlar ve sahneler](/help/mobile-automation) sayfasında.
:::

### Cora Max eşleştirme başarısız oluyor {#pairing-a-cora-max-fails}

Cora Mobile yeni bir Cora Max'i Bluetooth üzerinden bulur, sonra ona Wi-Fi'ınızı verir. Başlamadan önce Cora Mobile'da en az bir akvaryumunuz olsun, Bluetooth açık olsun ve telefonunuz ekranın yakınında olsun. Eşleştirme yarıda durursa Cora Mobile size nedenini, altında **İptal** ve **Tekrar dene** ile söyler.

- *"Bluetooth kapalı. Açın, ardından tekrar Tara'ya dokunun."* Bluetooth'u açın ve yeniden tarayın.
- *"Cora için Bluetooth izni kapalı. Ayarlar'dan etkinleştirin, ardından tekrar Tara'ya dokunun."* Telefonunuzun ayarlarında Cora için Bluetooth'a izin verin. Cora Mobile'daki **Ayarlar → Cihaz erişimi** sizi oraya götürür.
- *"Bluetooth üzerinden yakında Cora kurulum cihazı bulunamadı."* Cora Max'in yanında durun, kurulum ekranını gösterdiğini kontrol edin ve yeniden tarayın.
- **Akvaryum Bulunamadı**: önce Cora Mobile'da bir akvaryum oluşturun, sonra eşleştirin.
- *"Telefonunuz Wi-Fi'nizdeki Cora Max'e ulaşamadı."* Telefonunuzu ve Cora Max'i aynı Wi-Fi ağına koyun. iPhone'da Cora'nın Yerel Ağ erişimi olduğunu da kontrol edin (**Ayarlar → Cihaz erişimi**). Sonra **Tekrar dene**'ye dokunun.
- *"Cora Max bu eşleştirme oturumunu kabul etmedi."* Yeniden denemek işe yaramaz. Ekranı kapatın ve **Cihazlar → Cihaz Ekle → Cora** yolundan yeniden başlayın.

Diğer her mesaj için **Tekrar dene**'ye dokunun. Kurulumun tamamı [Cora Max'i kurma](/help/max-setup) sayfasında.

### Cora Max eski veri gösteriyor {#cora-max-shows-old-data}

Üst çubuktaki durum etiketine bakın. **Çevrimiçi** ve **Bulut** ikisi de sorunsuzdur. Birden fazla Cora Max'iniz varsa veriyi toplamayan **Bulut** gösterir ve ölçümleri aynı derecede günceldir. **Eski** ya da **Çevrimdışı**, Cora Max'in kaynağını kaybettiği ve aldığı son veriyi gösterdiği anlamına gelir.

- **Ayarlar → Cora Max Ayarları → Wi-Fi** altından Wi-Fi'ı kontrol edin.
- Ağınızın kendisinin çalıştığını kontrol edin.
- Etikette **Çevrimiçi** ya da **Bulut** yazıyor ve veri yine de eskiyse sorun Cora Max'ten öncedir. Aynı akvaryumu telefonunuzda kontrol edin.

### Cora Max "Apex şifresi" gösteriyor {#cora-max-shows-apex-password}

Apex'iniz Cora'nın kaydettiği girişi reddetti, genellikle Apex şifresi değiştirildiği için. Telefonunuzda **Cihazlar**'ı, ardından Apex'inizi açın ve yenisini girmek için **Bağlantı** altında **Bağlantıyı düzenle**'ye dokunun.

### Cora Max "Bulut kaydı reddedildi" gösteriyor {#cora-max-shows-cloud-save-refused}

Cora Cloud bu ekranın bazı verilerini kaydetmeyi reddediyor. Akvaryumunuzda ya da Cora Max'te bir sorun yok ve ekranda değiştirilmesi gereken bir şey yok. Çözüm bir Cora Cloud güncellemesidir.

1. **Ayarlar → Cora Max Ayarları**'nı açın ve **DURUM**'a kaydırın. **Bulut kaydı** satırı hangi verilerin reddedildiğini söyler, örneğin bir cihazın ölçümleri ya da prizleri.
2. [Destekle iletişime geçin](/support.html) ve o satırda ne yazdığını bize söyleyin.

Bu arada ölçümleriniz Cora Max'te görünmeye devam eder. Yalnızca çözüm gelene kadar hesabınıza kaydedilmezler.

### İkinci bir Cora Max "Ana Cora çevrimdışı" gösteriyor {#a-secondary-cora-max-shows-main-cora-offline}

Bu akvaryumun Birincil Cora Max'i çevrimdışı oldu. Bu ekran aldığı son veriyi gösteriyor, bu yüzden canlı değil.

1. Birincil Cora Max'in elektriğini ve Wi-Fi'ını kontrol edin.
2. Yeniden bağlanmasını bekleyin ya da **Birincil Cora Max**'i çevrimiçi olan bir cihaza değiştirin.

### Cora Max bir Wi-Fi kesintisinden sonra hemen yeniden bağlanmıyor {#cora-max-wont-reconnect-right-away-after-a-wi-fi-outage}

Bağlantısını kaybettikten sonra Cora Max, ağınızı boğmamak için her denemeden önce biraz daha uzun bekler. Bekleme yaklaşık bir dakikaya kadar çıkar.

1. Ağınız geri geldikten sonra ona yaklaşık bir dakika verin.
2. Hâlâ yeniden bağlanmadıysa **Ayarlar → Cora Max Ayarları → Wi-Fi**'ı kontrol edin.

### Telefonda bir Cora Max'in adını değiştirmek gösterdiğini değiştirmiyor {#renaming-a-cora-max-on-the-phone-doesnt-change-what-the-tabl}

Telefonunuzda ayarladığınız ad, hesabın o cihaz için kullandığı etikettir. Cora Max'in kendi eşleştirme ekranında gösterdiği ad farklı olabilir.

1. Hangi ada baktığınızı kontrol edin: telefonunuzun cihaz listesindekine mi, Cora Max'in eşleştirme ekranındakine mi.
2. Hesap etiketini değiştirmek için telefonunuzun cihaz listesinden adını değiştirin.

### Uyandırma sözcüğünü nereden kapatacağımı bulamıyorum {#i-cant-find-where-to-turn-off-the-wake-word-on-cora-max}

Uyandırma sözcüğü kontrolleri Cora Assistant ayarlarında değil, ses ayarlarındadır.

1. Cora Max'te **Ayarlar → Cora Max Ayarları**'na gidin ve **SES VE KONUŞMA** altında **Uyandırma sözcüğü**'nü bulun.
2. Kapatın. Konuşmaya başlamak için **Cora Assistant** simgesine yine dokunabilirsiniz.

Ayrıntılar [Cora ile konuşma](/help/max-voice) sayfasında.

### Çocuk kilidi kimsenin Ayarlar'a girmesine izin vermiyor {#child-lock-wont-let-anyone-into-settings}

Çocuk kilidinin yaptığı budur. Belirli bir süre dokunulmadığında, kimsenin bu ekrandan dokunarak ya da sesle ekipman değiştirmesini önler. Ölçümler güncellenmeye devam eder ve Cora'ya yine soru sorabilirsiniz. Kilidi açmak için:

1. İki saniye içinde **Ses Açma** ya da **Ses Kısma** tuşuna üç kez basın ya da
2. Ekranın sağ üst köşesinde beş parmağınızı on saniye basılı tutun.

Ayrıntılar [Cora Max ayarları](/help/max-settings#child-lock) sayfasında.

### Telefonda yapılan bir sahne Cora Max'te düzenlenemiyor {#a-scene-made-on-the-phone-doesnt-show-up-as-editable-on-cora}

Yalnızca daha yeni Cora Max sürümleri ekranda sahne düzenleyebilir. Eski sürümler telefonunuzda yaptığınız sahneleri yine çalıştırır ama düzenleyemez.

1. Cora Max'i güncelleyin ([Güncellemeler ve kurtarma](/help/max-updates)) ya da
2. O sahneyi telefonunuzda düzenlemeye devam edin. Her iki durumda da Cora Max'te çalışır.

## Uyarılar, bildirimler ve günlük özet {#alerts-and-notifications}

### Bir uyarı kapanmıyor {#an-alert-is-not-clearing}

Bir uyarı, ölçüm aralığa döndüğünde kapanır. Kapanmıyorsa üç olası neden vardır.

- Ölçüm gerçekten aralığın dışında. Widget'ın geçmişine bakın.
- Aralık akvaryumunuza uymuyor. [Uyarılar ve eşikler](/help/mobile-alerts) sayfasına bakın.
- Kaynak yanlış. Kalibrasyon gereken bir prob gerçekten aralık dışında olan bir sayı bildirir. Probu düzeltin ve aralığa dokunmayın.

### Onayladığım bir uyarı bildirim göndermeyi bırakmıyor {#an-alert-wont-stop-notifying-even-after-ive-acknowledged-it}

Cora Max'teki **Ertele** ve **Kapat** yalnızca o Cora Max'i susturur. Ölçüm aralığın dışında kaldığı sürece telefonunuz bildirim almaya devam eder.

1. Onu daha seyrek duymak için uyarı kuralını Cora Mobile'da açın ve daha uzun bir **Uyarılar arası bekleme süresi** (1 haftaya kadar) ayarlayın.
2. Aralık akvaryumunuza uymuyorsa aralığın kendisini değiştirin.

### Bildirim almıyorum {#im-not-getting-notifications}

1. **Ayarlar → Bildirimler** içinde kategorinin bildirim göndermesine izin verildiğini kontrol edin.
2. Telefonunuzun Cora için kendi bildirim iznini kontrol edin.
3. Günlük özet hiçbir şeyin değişmediği günlerde sessiz kalır. Tamamen durduysa sonraki maddeye bakın.

Ayrıntılar [Bildirimler](/help/mobile-notifications) sayfasında.

### Günlük özetim durdu {#my-daily-briefing-stopped}

- Deneme süreniz bitti. Reef Buddy ücretli planların bir parçasıdır. 30 günlük denemeden sonra ücretsiz bir hesap günlük özeti almayı bırakır. [Planlar ve abonelikler](/help/mobile-plans) sayfasına bakın.
- Akvaryum planınızın kapsamında değil. Her plan, **Ayarlar → Akvaryumları yeniden sırala** sırasına göre sayılan belli sayıda akvaryumu kapsar. Dahil etmek için bir akvaryumu yukarı taşıyın.
- Bugün hiçbir şey değişmedi. Özet sakin bir günde sessiz kalır.

Ayrıntılar [Reef Buddy](/help/mobile-reef-buddy) sayfasında.

### Kaldırdığım bir akvaryumdan uyarılar gelmeye devam ediyor {#alerts-from-a-removed-tank}

Kaldırılan bir akvaryum geçmişi için saklanır, ama uyarı ya da hatırlatıcı göndermez ve otomasyonları durur. Yine de biri gelirse:

1. **Ayarlar → Kaldırılan akvaryumlar** yolunu açın. Akvaryum orada yoksa kaldırılmamıştır.
2. Cora Mobile'ı ve Cora Max'inizi en son sürüme güncelleyin.
3. Uyarılar hâlâ geliyor mu? Uyarının metni ve geldiği saatle destek ekibine yazın. Bkz. [Sorun bildirme](/help/mobile-support).

Ayrıntılar [Akvaryumlarınızı yönetme](/help/mobile-tanks) sayfasında.


## Cora Assistant ve ses {#cora-assistant-and-voice}

### Cora Assistant yanlış akvaryum hakkında yanıt veriyor {#cora-assistant-answers-about-the-wrong-tank}

Sormadan önce bir akvaryum seçmediniz ya da yanlış olan seçili. Kastettiğiniz akvaryumu seçin, sonra yeniden sorun. Ayrıntılar [Cora'ya sorun](/help/mobile-assistant) sayfasında.

### Cora Assistant yanıt vermeyi reddediyor ya da izin ekranını yeniden gösteriyor {#cora-assistant-refuses-to-answer-or-shows-a-consent-screen-a}

**Cora Assistant'ın kayıtlı akvaryum verilerini kullanmasına izin ver** kapalıdır, bu yüzden yanıt verecek bir şeyi yoktur. İzin ekranında **Kabul Et ve Devam Et**'e dokunun ya da **Ayarlar → Cora Assistant** içinde anahtarı açın.

### Cora Max "Sesli asistan onayınızı bekliyor" diyor {#voice-needs-your-ok}

Cora Max'teki ses, telefonunuzdaki Cora Assistant ile aynı veri paylaşım seçimini kullanır. Cora Mobile'da **Ayarlar → Cora Assistant**'ı açın ve **Cora Assistant'ın kayıtlı akvaryum verilerini kullanmasına izin ver**'i açın, sonra tekrar deneyin. Ayrıntılar [Cora ile konuşma](/help/max-voice) sayfasında.

## Laboratuvar sonuçları ve sağlık raporları {#lab-results-and-health-reports}

### Bir laboratuvardan ya da e-postayla gelen ICP sonucu hiç görünmedi {#a-lab-or-emailed-icp-result-never-showed-up}

Bir sonuç ancak bir akvaryumu olduğunda eklenir, Cora'nın bazen göndereni de tanıması gerekir ve Cora'nın onu okumak için onayınıza ihtiyacı vardır.

1. *"Cora Assistant bunu okumak için onayınıza ihtiyaç duyuyor."* görüyorsanız **Ayarlar → Cora Assistant**'ı açın ve **Cora Assistant'ın kayıtlı akvaryum verilerini kullanmasına izin ver**'i açın. Kabul ettiğinizde sonuç gelir.
2. Ona ilk kez bir sonuç gönderdiğinizde Cora'nın gösterdiği ipucunu kontrol edin.
3. Cora sorduğunda sonucun hangi akvaryuma ait olduğunu onaylayın.
4. Daha önce bir sonuç gönderdiyseniz bunu da aynı e-posta adresinden gönderin.

Ayrıntılar [ICP ve sağlık raporları](/help/mobile-icp-health) sayfasında.

### ICP dosyam yüklenmiyor {#my-icp-file-wont-upload}

Cora laboratuvarınızın gönderdiği PDF raporu okur. Fotoğraflar ve ekran görüntüleri okunamaz. Önce PDF'i laboratuvarınızdan indirin, sonra yeniden **ICP Yükle**'ye dokunun.

### Bir sağlık raporu ya da ICP yüklemesinden sonra ekran kararıyor {#black-screen-after-a-report}

Bu, Cora Mobile 1.2 ve öncesinde olabiliyordu ve Cora Mobile 1.3 bunu düzeltir: Cora Mobile'ı App Store'dan ya da Google Play'den güncelleyin. Güncellemeden önce görürseniz Cora Mobile'ı kapatın ve yeniden açın. Rapor kaydedilmiştir ve onu **Zeka** altında bulursunuz.

## Dil, birimler ve giriş yapma {#language-units-and-signing-in}

### Her şey birden yanlış dilde {#everything-is-suddenly-in-the-wrong-language}

Biri cihazlarınızdan birinde hesap dilini değiştirdi. Tüm hesap için tek bir ayardır.

1. Cora Mobile'da ya da Cora Max'te **Ayarlar → Dil**'i açın.
2. Geri ayarlayın. Değişiklik her yerde geçerli olur.

### Dil değiştirdikten sonra eski bir uyarı ya da rapor farklı bir dilde {#an-old-alert-or-report-is-still-in-a-different-language-afte}

Bu beklenen bir durumdur. Cora daha önce yazdığı hiçbir şeyi yeniden çevirmez. Yeni uyarılar, raporlar ve özetler yeni dili kullanır.

### "Cora'ya ulaşılamadı. Wi-Fi veya mobil verinizi kontrol edip tekrar deneyin." {#could-not-reach-cora-check-your-wi-fi-or-mobile-data-then-tr}

Telefonunuz giriş yapmak için Cora Cloud'a ulaşamıyor. Bu, akvaryum ekipmanınızla değil telefonunuzun bağlantısıyla ilgilidir.

1. Telefonunuzun çalışan bir Wi-Fi ya da mobil veri bağlantısı olduğunu kontrol edin.
2. Varsa farklı bir ağ deneyin.
3. **Tekrar dene**'ye dokunun.

Diğer giriş sorunları [Giriş yapma ve hesap kurtarma](/help/mobile-account) sayfasında.

## Hâlâ takıldınız mı {#still-stuck}

**[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin ya da [Sorun bildirme](/help/mobile-support) sayfasında anlatıldığı gibi Cora Mobile'dan bildirin. Hangi akvaryum, hangi cihaz, hangi ekran olduğunu ve ne görmeyi beklediğinizi bize söyleyin.
