---
title: Cora Max'ten ekipman kontrolü
description: Cora Max'te Neptune Apex, Trident ve DŌS, Red Sea ReefBeat, Jecod ve AquaWiz için cihaz sayfaları, markaya göre.
section: Cora Max
reviewed: 2026-10-18
order: 6
group: Equipment
twin: mobile-device-control
---

Bu sayfa, Cora Max'te her cihazın sayfasında neleri görüp yapabileceğinizi marka marka anlatır. Cora Max telefonunuzla aynı ekipmana ulaşır. Bir cihaz sayfasını üst çubuktaki cihazlar simgesinden, **Ayarlar → Cihazlar** yolundan ya da panoda bir cihaz kutucuğuna dokunarak açın.

![Cora Max'te besleme düğmeleri ve prizleriyle bir Apex sayfası](img/max-device-control.webp "Besleme A–D ve İptal, ardından bir duvar ekranı için yerleştirilmiş prizler.")

:::warning Bu kontroller canlı ekipman üzerinde çalışır
Önizleme ve geri alma yoktur. Dokunduğunuz anda bir komut gider, ama göndermek yapıldığı anlamına gelmez. Sonuç **Onaylandı**, **Onaylanmadı**, **Reddedildi** ya da **Değişiklik yok** olarak döner ve hangisi olduğunu [Etkinlik](/help/max-activity) içinde görebilirsiniz.
:::

Ekipmanı telefonunuzda ekler, atar ve kaldırırsınız. Hesabınızda olduğunda Cora Max onu gösterir. [Ekipmanınızı bağlama](/help/mobile-connections) sayfasına bakın.

## Neyin sayfası var {#what-has-a-page}

| Cihaz | Ne gösterir |
|---|---|
| **Neptune Apex** | Problar ve prizler, her prizi açıp kapatabilirsiniz |
| **Trident** | Test durumu, reaktif ve atık seviyeleri ve bir test başlatma düğmesi |
| DŌS QD dahil **DŌS** | Her kafanın dozajı, zamanlaması, ne kadar yeteceği ve kap hacmi (duraklatma, doldurma, şimdi dozajlama ve tek seferlik yirmi saniyelik bir ölçümle) |
| **Red Sea ReefBeat** | Ünitede ne varsa: dozaj kafaları, depo, rulo günleri, pompa modu, ayrıca tam bir ReefDose planı düzenleyicisi ve ReefMat ayarları |
| **Jecod** | Pompa modu ve yoğunluğu ve günlük programı |
| **AquaWiz** | Kendi sayfası yok. **Cihazlar** içinde listelenir ve ölçümleri panoya gider |

Çoğu cihaz sayfasında cihazın adını değiştirmek için bir kalem bulunur. Yeni ad telefonunuzda da görünür. Ayrıntılar [Cihazlar ve cihaz sağlığı](/help/max-devices) sayfasında.

## Neptune Apex {#neptune-apex}

Apex sayfası problarınızı ve prizlerinizi, en üstte de besleme döngülerinizi listeler. Her priz **Otomatik**, **Kapalı** ve **Açık** arasında geçer, asma kilitli prizler onay ister. Üç durumun ve besleme modunun nasıl çalıştığı [Prizler ve kontroller](/help/max-controls) sayfasında.

Prizlere panonun altındaki **Prizler ve Besleme** çekmecesinden de ulaşabilirsiniz. Bu pano için açılmış prizleri (hiç seçmediyseniz hepsini) listeler.

Birkaç modülü olan büyük bir Apex tüm prizlerini ve problarını gösterir. DŌS kafaları priz listesinde hiçbir zaman görünmez, böylece orada birini açıp çalışır halde bırakamazsınız. Kafanın kendi sayfasından dozaj yapın.

### Trident {#trident}

Trident sayfası test durumunu ve reaktif ve atık seviyelerini gösterir. Buradan bir test başlatabilir ve **Uyarı ayarları** ile bir dolum uyarısı kurabilirsiniz.

## DŌS kafaları {#dos-heads}

Cora'nın bir DŌS kafasıyla elle dozaj yapabilmesi için onu bir kez ölçmeniz gerekir. **Dozajlamak için ölç**, kafayı bir ölçü kabına yirmi saniye çalıştırır ve siz ne kadar çıktığını girersiniz. Cora kafa başına tek bir ölçüm tutar ve hangi Cora Max almış olursa olsun en yenisini kullanır. Kafanın sayfası nerede ve ne zaman ölçüldüğünü gösterir.

Elle bir dozdan sonra, Apex Fusion'da Kapalı'ya ayarladığınız bir kafa Kapalı kalır. Diğer her kafa Otomatik'e döner.

Bir DŌS'un seviye sensörü yoktur ve boş bir kaptan dozaj yapmaya devam eder. DŌS sayfasındaki **Uyarı ayarları** ile bir dolum uyarısı kurun. Ayrıntılar [Dozaj pompası uyarıları](/help/mobile-device-control#doser-alerts) bölümünde.

### Bir kafanın ne için kullanıldığı {#what-a-head-is-used-for}

Bir kafanın ayarlar sayfasında **Kullanım amacı**'nı ayarlayabilirsiniz. Seçenekler **Takviye**, **Su değişimi: yeni tuzlu su girişi**, **Su değişimi: eski su çıkışı**, **Kalkwasser**, **Kalsiyum reaktörü**, **Yem** ya da **Su tamamlama** ve **Diğer**'dir. Kullanım amacı iki şeyi değiştirir.

- Ne kadar büyük bir kabı izleyebileceği. Her kullanım amacı 1.000 litreye kadar bir kabı izleyebilir. Apex'in kendi 150 litrelik sayacının üstünde hacmi Cora kendisi izler ve Apex sayacını her 100 litrede bir sıfırlar.
- Elle büyük bir doz alıp alamayacağı. Takviye ve Yem kafaları bugünkü küçük, dikkatli sınırı korur. Diğer her kullanım amacının 10 litrelik kesin bir tavana kadar kendi **Elle verilecek en büyük dozaj** sınırı ve kendi **Otomasyonlar ve Asistan için günlük sınır** değeri olabilir. Elle büyük bir doz ayrıca kafanın ayarlarında varsayılan olarak kapalı olan **Büyük dozlar**'ın açılmasını gerektirir. Bunu yalnızca ilk büyük dozun çalışmasını akvaryumun başında izledikten sonra açın.

Bir su değişimi çiftini (yeni tuzlu su girişi, eski su çıkışı) **Eşleştirilmiş kafa** olarak bağlayabilir ve bir **Denge uyarısı üstünde** miktarı ayarlayabilirsiniz. İki kafanın gün içindeki toplamları bundan fazla açılırsa Cora sizi uyarır. Dengesiz bir çift genellikle bir tarafın olması gerektiği gibi pompalamadığı anlamına gelir.

### Büyük bir doz yarıda kalırsa {#if-a-large-dose-is-interrupted}

Büyük bir doz, kafanın Apex'te yaptığı şeyi bir süreliğine değiştirir, sonra normal zamanlamasını geri koyar. Bağlantı yarıda koparsa Cora Max o kafanın sayfasında bir şerit gösterir: *"[kafa] üzerindeki büyük bir dozaj düzgün bitmedi. Cora programını geri koymayı denemeye devam ediyor; bunu Apex Fusion'da kontrol edin."*

Kafayı Apex Fusion'da kendiniz kontrol edin, sonra şeridi kaldırmak için **Kafayı Fusion'da kontrol ettim**'e dokunun. Bunu yalnızca kafanın Cora'nın dozaj programını değil kendi zamanlamasını çalıştırdığını doğruladıktan sonra yapın.

Şerit kalkmıyorsa ya da geri gelmeye devam ediyorsa [Sorun giderme](/help/troubleshooting) sayfasına göz atın.

## Red Sea ReefBeat {#red-sea}

Her Red Sea ünitesinin yaptığı işe uyan bir sayfası vardır: ReefDose kafaları ve kapları, ReefATO+ deposu, ReefMat rulo günleri ve ReefRun pompa hızları. ReefDose kafaları, ReefATO+ deposu ve ReefMat rulosu için sarf malzemesi uyarıları ünitenin sayfasındaki **Uyarı ayarları** ile kurulur.

Bir Red Sea ünitesi kendini durdurursa sayfası neyin yanlış olduğunu söyler ve çözümü hemen yanına koyar. Bu **Sürdür**, **Acil durumu temizle**, **Sensör temizlendi**, **Zaten yeni bir rulo yükledim** ya da bir dozaj kafası için **Sıfırla**'dır.

Bir ReefDose planı ve ReefMat'in zamanlanmış ilerletmesi, modeli, konumu ve Yeni rulo burada da telefonunuzdakiyle aynı şekilde çalışır. Ayrıntılar [Ekipmanınızı kontrol etme](/help/mobile-device-control) sayfasında.


## Jecod {#jecod}

Jecod sayfası pompanın modunu ve yoğunluğunu gösterir ve ikisini de değiştirebilirsiniz. Durumu başlık satırında, pompanın adının yanındadır. Üst çubukta güç anahtarı, şu an çalışan desen ve dört etiketli **Besleme** bulunur: **5**, **10**, **15** ve **30** dk. Pompayı o kadar duraklatmak için bir etikete dokunun. Çubuğun altında iki kart vardır:

- **Tüm gün aynı**: bir ayara dokunarak tüm gün çalıştırın.
- **Zamanlama**: gün grafiği ve plan listesi; geçerli planda **şimdi** yazar. **Düzenle** düzenleyiciyi açar, ⋮ menüsünde **Zamanlamayı şuraya kopyala…**, **Zamanlamayı farklı kaydet…** ve **Kayıtlı zamanlamalar…** bulunur.

Çalışan kartın bir çerçevesi ve **Çalışıyor** etiketi vardır. Jecod pompasında **Beslemeyi bitir** düğmesi yoktur. Besleme için duraklayabilen her Jecod pompası **5**, **10**, **15** ve **30** dk düğmelerini gösterir. Bir Jecod Pro pompasında dalga desenlerindeki Besleme kutucuğu aynı işi 10 dakika için yapar. Akvaryumdan uzaktaki bir Cora Max üzerinden ulaşılan Jecod pompası yalnızca 10 dakika besler. Şu anda besleyemeyen bir pompa nedenini düğmelerin altında kısa bir satırda gösterir, uzun basınca tam cümleyi görürsünüz. Telefondan başlatılan bir beslemeyi Cora Max de bitirir: süre dolunca pompa programına döner.

Jecod pompası günlük zamanlamalarını telefonunuzda olduğu gibi duvardaki ekranda da yazabilirsiniz. Düzenleyici aynıdır: bir gün grafiği, bir periyot listesi ve bir eylem satırı. Ayrıntılar [Ekipman zamanlamaları](/help/mobile-schedules) sayfasında.

## AquaWiz {#aquawiz}

Bir AquaWiz KH Controller'ın Cora Max'te kendi sayfası yoktur. **Cihazlar** içinde listelenir, orada adını değiştirebilirsiniz, ölçümleri de diğer kaynaklar gibi panoda görünür. Onu telefonunuzda kurun ve yönetin, [Ekipmanınızı bağlama](/help/mobile-connections) sayfasına bakın.

### Cora Max'ten saatlik okuma {#aquawiz-hourly}

AquaWiz, Cora'nın bulutunu yalnızca 12 saatte bir okumasına izin verir. Alkaliniteyi güncel tutmak için akvaryumun ana Cora Max'i kontrolörü doğrudan da okur, saat başından on dakika önce, saatte bir kez:

- Birkaç saniyeliğine kontrolörün kendi Wi-Fi ağına bağlanır, son sonucu okur ve hemen ev Wi-Fi'nize döner. Bu sırada Cora Max yaklaşık 4 saniye çevrimdışı kalır.
- Ev Wi-Fi şifreniz bu işlem için hiçbir yere kaydedilmez veya gönderilmez.
- Bunu yalnızca akvaryumun ana Cora Max'i yapar. Aynı akvaryumdaki ikinci bir Cora Max yapmaz.
- Cora Max sizinle konuşurken, güncellenirken, eşleşirken ya da Wi-Fi değiştirirken bekler ve bir sonraki saatte yeniden dener.
- Kontrolör Cora Max'in Wi-Fi menzilinde olmalı ve ürün yazılımı yerel erişim sunmalıdır. Üst üste iki okuma başarısız olursa Cora Max günün geri kalanında denemeyi bırakır ve 12 saatlik bulut okuması devam eder.

Cora Max'ten gelen bir ölçüm, telefondaki AquaWiz kartında **Cora Max cihazınızdan saatlik** olarak görünür. Ayrıca [Uyarılar](/help/mobile-alerts#equipment-faults) sayfasında anlatılan pompa, pH probu ve su haznesi uyarılarını da getirir.


## Sarf malzemeleri {#consumables}

Dolum eşiklerini (reaktif, kaplar, depolar) burada da telefonunuzdaki gibi cihazın kendi sayfasında ayarlarsınız. Ayrıntılar [Sarf malzemeleri](/help/mobile-consumables) sayfasında.

## Akvaryumun başında kaydetme ve hesaplama {#logging-and-calculating-at-the-tank}

İki şey duvardaki ekranda çoğu zaman telefondan daha kolaydır.

- **Parametreleri kaydet**, test sonuçlarını ekran klavyesiyle yazmanızı sağlar. Akvaryum menüsündedir.
- **Dozaj hesaplayıcı**, akvaryumun hacminden ve ürün yoğunluklarınızdan bir düzeltme dozu hesaplar. Onu bir parametrenin sayfasından açın. Telefonunuzla aynı hacmi ve ürün yoğunluklarını kullanır, bu yüzden burada hesaplanan bir doz orada hesaplananla aynıdır. Ayrıntılar [Dozaj](/help/mobile-dosing) sayfasında.

## İkinci bir Cora Max'te {#on-a-second-cora-max}

Bir akvaryumu birden fazla Cora Max gösterdiğinde, o akvaryumun ekipmanını bunlardan biri okur. Cihaz sayfaları ona akvaryumdaki Cora Max der. Diğerleri cihaz sayfalarını yine açabilir ve **Bulut** yazan bir durum etiketi bunlardan birinde olduğunuz anlamına gelir. Akvaryumdaki Cora Max'in en son ne okuduğunu ve ne kadar önce okuduğunu gösterirler. Her komut Cora Cloud üzerinden akvaryumdaki Cora Max'e gider ve onu o yerine getirir.

Birkaç şey yalnızca akvaryumdaki Cora Max'te çalışır.

- **Dozajlamak için ölç** ve **Yeniden ölç** yalnızca orada görünür. Bir kafa ölçüldükten sonra **Şimdi dozajla** her Cora Max'ten çalışır.
- Bir Jecod zamanlamasını başka bir Cora Max'ten ancak akvaryumdaki Cora Max pompayı son bir saat içinde okuduysa değiştirebilirsiniz ve yalnızca Bluetooth üzerinden konuşan bir pompa için asla değiştiremezsiniz. Oradan tek bir **Pompaya uygula** en fazla 12 değişiklik gönderir, bu yüzden daha büyük bir düzenlemeyi parçalar halinde gönderin.

## Neyin, neyle değiştirildiği {#what-was-changed-and-by-what}

Her eylem, ona neyin neden olduğuyla birlikte kaydedilir. Ayrıntılar [Cora Max'te etkinlik](/help/max-activity) sayfasında.
