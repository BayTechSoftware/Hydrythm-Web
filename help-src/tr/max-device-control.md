---
title: Cora Max'ten ekipman kontrolü
description: Büyük ekrandaki cihaz sayfaları: problar, prizler, dozaj kafaları, test cihazları ve pompalar.
section: Cora Max
reviewed: 2026-09-27
order: 6
group: Equipment
---

Cora Max telefonunuzun ulaştığı tüm ekipmana ulaşır. Her cihazın kendi sayfası var. Sayfaları **Ayarlar → Cihazlar**'dan ya da panodaki cihaz kutucuğuna dokunarak açın.

![Cora Max'te bir Apex sayfası](img/max-device-control.webp "Besleme döngüleri ve tüm prizler, duvardaki ekrana göre yerleştirilmiş.")

:::warning Bu kontroller çalışan ekipmanı etkiler
Önizleme de geri alma da yoktur. Dokunduğunuz anda komut gider. Ama *gitti* demek *yapıldı* demek değildir. Sonuç **Onaylandı**, **Onaylanmadı**, **Reddedildi** ya da **Değişiklik yok** olarak döner. Hangisi olduğunu [Etkinlik](/help/max-activity) ekranında görürsünüz.
:::

## Hangi cihazların sayfası var

| Cihaz | Sayfada neler var |
|---|---|
| **Neptune Apex** | Problar ve prizler. Her prizi açıp kapatabilirsiniz |
| **Trident** | Test durumu, reaktif ve atık seviyeleri. Buradan test de başlatabilirsiniz |
| **DŌS** (DŌS QD dahil) | Her kafanın dozajı, zamanlaması, ne kadar yeteceği ve kap hacmi. Duraklatma, doldurma, hemen dozaj verme ve tek seferlik yirmi saniyelik ölçüm de burada |
| **Red Sea ReefBeat** | Cihaz neyse ona göre: dozaj kafaları, rezervuar, rulonun kaç gün yeteceği, pompa modu |
| **Jecod** | Pompa modu, yoğunluğu ve günlük programı |
| **Maxspect** *(beta)* | **Gyre A** ve **Gyre B** için mod ve hız, **Pompa sağlığı** (temizlik geri sayımı, A kafasının akımı, takılı kafalar, yazılım) ve zamanlaması. Zamanlama yalnızca görüntülenir |

Bir Red Sea cihazı kendini durdurursa sayfasında sorunun ne olduğu yazar. Çözüm düğmesi de hemen yanındadır: **Sürdür**, **Acil durumu temizle**, **Sensör temizlendi**, **Zaten yeni bir rulo yükledim** ya da dozaj kafası için **Sıfırla**.

## DŌS kafaları

Cora bir DŌS kafasıyla elle dozaj yapmadan önce kafanın bir kez ölçülmesi gerekir. **Dozajlamak için ölç**'e dokununca kafa yirmi saniye boyunca ölçüm kabına pompalar. Siz de kaba ne kadar geldiğini girersiniz. Cora her kafa için tek bir ölçüm tutar ve hangi Cora Max'te alınmış olursa olsun en yenisini kullanır. Kafanın ne zaman ve nerede ölçüldüğü sayfasında yazar.

Elle dozajdan sonra, Apex Fusion'da Kapalı'ya ayarladığınız kafa Kapalı kalır. Diğer tüm kafalar Otomatik'e döner.

### Kafanın kullanım amacı

Her kafa için ayar penceresinden bir **kullanım türü** seçebilirsiniz: **Takviye**, **Su değişimi: yeni tuzlu su girişi**, **Su değişimi: eski su çıkışı**, **Kalkwasser**, **Kalsiyum reaktörü**, **Yem**, **Su tamamlama** ya da **Diğer**. Kullanım türü iki şeyi değiştirir:

- **Takip edilebilecek kabın büyüklüğü.** Takviye kafası en fazla 20 litrelik kabı takip eder. Diğer kullanım türlerinde bu sınır 500 litreye çıkar. Böylece su değişimi ya da kalsiyum reaktörü için çalışan bir kafa küçük bir dozaj şişesi gibi görülmez.
- **Elle büyük dozaj verilip verilemeyeceği.** Takviye ve Yem kafalarında bugünkü küçük ve temkinli üst sınır geçerlidir. Diğer kullanım türleri için ayrı bir **Elle verilecek en büyük dozaj** sınırı belirleyebilirsiniz. Bu sınır en fazla 10 litre olabilir. Ayrıca **Otomasyonlar ve Asistan için günlük limit** de ayrıca ayarlanır.

Su değişimi için kullanılan iki kafayı (yeni tuzlu su girişi ve eski su çıkışı) **Eşleştirilmiş kafa** olarak bağlayabilir ve bir **Denge uyarısı üstünde** miktarı girebilirsiniz. İki kafanın günlük toplamları arasındaki fark bu miktarı aşarsa Cora sizi uyarır. Dengesi bozulan bir çift genellikle taraflardan birinin beklendiği gibi pompalamadığını gösterir.

### Büyük dozaj yarıda kalırsa

Büyük dozaj sırasında kafanın Apex'teki programı geçici olarak değişir. Dozaj bitince normal zamanlaması geri yüklenir. Bağlantı dozajın ortasında koparsa Cora Max o kafanın sayfasında bir uyarı bandı gösterir: *"[kafa] üzerindeki büyük bir dozaj düzgün bitmedi. Cora programını geri koymayı denemeye devam ediyor; bunu Apex Fusion'da kontrol edin."*

Kafayı Apex Fusion'da kendiniz kontrol edin. Sonra bandı kapatmak için **Kafayı Fusion'da kontrol ettim**'e dokunun. Bunu ancak şu anda çalışan programın Cora'nın dozaj programı değil, kafanın kendi zamanlaması olduğundan emin olduktan sonra yapın.

Bant kapanmıyorsa ya da tekrar tekrar çıkıyorsa [Sorun giderme](/help/troubleshooting) sayfasına bakın.

## Zamanlamalar

Jecod pompalarının günlük programlarını telefonda da duvardaki ekranda da yazabilirsiniz. Düzenleyici aynıdır: günlük grafik, zaman dilimleri listesi ve eylem satırı. Ayrıntılar [Ekipman programları](/help/mobile-schedules) sayfasında.

Maxspect gyre zamanlamasını *(beta)* burada görebilirsiniz ama kaydedemezsiniz. Zamanlamayı Maxspect uygulamasında ayarlayın.

## Prizler

Prizlere panonun altındaki **Prizler ve Besleme** çekmecesinden de ulaşırsınız. Çekmecede bu pano için seçilen prizler bir arada durur. Hiç seçim yapılmadıysa tüm prizler görünür. Ayrıntılar [Prizler ve kontroller](/help/max-controls) sayfasında.

DŌS kafaları priz listesinde hiç görünmez. Böylece bir kafa orada açılıp çalışır halde unutulamaz. Dozajı kafanın kendi sayfasından verin. Birkaç modülü olan büyük bir Apex'in tüm prizleri ve probları görünür.

## Sarf malzemeleri

Reaktif, kap ve rezervuarların yeniden doldurma eşiklerini burada da cihazın kendi sayfasından, telefondakiyle aynı şekilde ayarlarsınız. Ayrıntılar [Sarf malzemeleri](/help/mobile-consumables) sayfasında.

## Akvaryumun başında kayıt ve hesaplama

İki iş duvardaki ekranda çoğu zaman telefondan daha pratiktir:

- **Parametreleri kaydet**: Akvaryum menüsünden test sonuçlarını ekran klavyesiyle girin
- **Dozaj hesaplayıcı**: Bir parametrenin sayfasından, akvaryumun hacmine ve ürünlerinizin konsantrasyonuna göre düzeltme dozajını hesaplayın. Telefondaki hacim ve ürün değerlerinin aynısını kullanır. Burada hesaplanan dozaj telefonda hesaplananla aynı çıkar. Ayrıntılar [Dozaj](/help/mobile-dosing) sayfasında.

## İkinci bir Cora Max'te

Bir akvaryum birden çok Cora Max'te görünüyorsa, o akvaryumun ekipmanını yalnızca biri okur. Cihaz sayfaları bu cihaza akvaryumdaki Cora Max der. Diğer ekranlar da cihaz sayfalarını açabilir. Durum etiketinde **Bulut** yazıyorsa bu ekran onlardan biridir. Bu ekranlar, akvaryumdaki Cora Max'in en son ne okuduğunu ve bunun ne kadar önce olduğunu gösterir. Verdiğiniz komutları da uygulaması için Cora Cloud üzerinden o Cora Max'e iletirler.

Bazı işler yalnızca akvaryumdaki Cora Max'te yapılır:

- **Dozajlamak için ölç** ve **Yeniden ölç** yalnızca orada görünür. Kafa bir kez ölçüldükten sonra **Şimdi dozajla** her Cora Max'te çalışır.
- Jecod zamanlamasını başka bir Cora Max'ten değiştirmek için akvaryumdaki Cora Max'in pompayı son bir saat içinde okumuş olması gerekir. Yalnızca Bluetooth ile bağlanan bir pompanın zamanlaması başka bir Cora Max'ten hiç değiştirilemez. Oradan tek bir **Pompaya uygula** en fazla 12 değişiklik gönderir. Daha büyük bir düzenlemeyi parça parça gönderin.

## Ne değişti, kim değiştirdi

Her eylem, nedeniyle birlikte kaydedilir. Ayrıntılar [Etkinlik ve zaman çizelgesi](/help/mobile-activity) sayfasında.
