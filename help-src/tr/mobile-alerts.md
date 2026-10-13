---
title: Uyarılar ve eşikler
description: Her parametrenin aralığını belirleyin, hangi durumlarda haber alacağınızı seçin ve bir uyarının neden geldiğini anlayın.
section: Cora Mobile
reviewed: 2026-10-13
order: 15
group: Alerts and automation
---

Bir ölçüm, belirlediğiniz aralığın dışına çıktığında uyarı verilir. Aralıkları siz belirlersiniz. Hangi uyarıların telefonunuza geleceğini de siz seçersiniz.

**Uyarı Merkezi**'ni panonun altındaki kısayol satırından açın.

![Uyarı Merkezi](img/mobile-alerts.webp "Etkin uyarılar. Her birinde önem derecesi, uyarıya neyin yol açtığı ve zamanı görünür.")

## Uyarı Merkezi

İki sekme var:

- **Etkin**: şu an açık olan uyarılar. Sekmedeki rozet kaç uyarı olduğunu gösterir
- **Kurallar**: bu uyarıları üreten eşik ve değişim hızı kuralları

Her etkin uyarıda şunlar görünür: parametre ve akvaryum, uyarıya yol açan ölçüm, sade açıklama, önem derecesi etiketi, uyarıyı veren kuralın türü (**Eşik** ya da **Değişim Hızı**) ve uyarının zamanı.

Her uyarıda iki düğme var:

- **Kuralı görüntüle**: uyarıyı veren kuralı açar. Aralığı buradan değiştirebilirsiniz. Bir dozaj pompası uyarısında, örneğin bir DŌS ya da ReefDose kafasında sıvı azaldığında veya bir dozaj kaçırıldığında, bu düğmenin yerinde **Dozaj pompasını aç** bulunur. O dozaj pompasının sayfasını uyarılarıyla birlikte açar
- **Bu uyarıyı açıkla**: asistandan uyarıyı akvaryumunuzun geçmişine bakarak yorumlamasını ister

## Kurallar sekmesi

Kurallar parametreye göre gruplanır. Her kuralın kendi satırında bir açma kapama anahtarı vardır, böylece kuralı açmadan kapatabilirsiniz. Aralığını ya da bekleme süresini değiştirmek için satıra dokunun.

Bir dozaj kafasının kuralları, kafanın adını ve neyi izlediğini taşır, örneğin *İyot · kalan gün* ya da *İyot · kalan*. Kaçırılan bir dozaj *İyot · kaçırılan dozaj* olarak görünür.

Her DŌS ve her ReefDose'un burada kendine ait tek bir satırı vardır. Kafa uyarıları tek tek listelenmez. O dozaj pompasının sayfasını uyarılarıyla açmak için satıra dokunun. Bkz. [Dozaj pompası uyarıları](/help/mobile-device-control#doser-alerts).

Cora'nın önerdiği kurallardan bazıları eksikse en alttaki **Önerilen kuralları ekle** onları ekler. Zaten kuralı olan parametreleri atlar. **Özel Kural Ekle** ile kendi kuralınızı kurarsınız.

## Aralık belirleme

Cora'nın değerlendirebildiği parametrelerin hedef aralığı vardır. Varsayılan aralıklar, akvaryumu kurarken girdiğiniz türe ve yaşa göre belirlenir. Başlangıç için genellikle uygundur. Kullanılabilir bir aralığı olmayan parametre hiç değerlendirilmez. Cora tahmin yürütmez, parametre nötr gri renkte kalır.

Bir aralığı değiştirmek için panodaki widget'a **uzun basın**. Bu, o parametrenin eşiklerini doğrudan açar. Kısa dokunuş ise parametre ekranını açar. İki hareket farklı yerlere gider. Uzun basma, aklınızda tutmanız gereken kısayoldur.

Parametrenin henüz kuralı yoksa alanlarda Cora'nın varsayılan değerleri yazar ve altındaki notta bu belirtilir. Kendi aralığınızı belirlemek için herhangi bir değeri değiştirin.

Bütün aralıkları bir arada görmek için panonun altındaki düğme satırından **Uyarılar**'a dokunun.

Şunları belirleyebilirsiniz:

- **Aralık**: alkalinite ya da sıcaklık gibi değerler için alt ve üst sınır
- **Üst sınır**: nitrat ya da fosfat gibi düşük olmasında sakınca olmayan değerler için yalnızca üst sınır
- **Alt sınır**: yalnızca alt sınır

:::tip Akvaryumunuzun gerçekte çalıştığı aralığı girin
Varsayılanlar yalnızca başlangıç noktasıdır, kesin hüküm değildir. 6 dKH'de düşük besinle çalışan bir akvaryum, bir tabloda 8–9 yazıyor diye "yanlış" değildir. Gerçekte çalıştığınız aralığı girin. Cora da *sizin* aralığınızdan kaydığınızda size haber verir.
:::

## Uyarıya ne yol açar

Bir ölçüm eşiği geçtiğinde uyarı verilir. Cora her ölçümü geldiği anda kontrol eder. Bu yüzden aralığın dışındaki tek bir ölçüm bile uyarı için yeterlidir.

Uyarı verildikten sonra aynı konuda size tekrar tekrar bildirim gelmez. Yeniden bildirim için bekleme süresinin dolması gerekir. Ölçüm aralığa geri döndüğü anda uyarı da **kendiliğinden kapanır**. Onaylamanız gereken bir şey yoktur.

**Değişim hızı** kuralı da kurabilirsiniz. Bu kural parametrenin şu anki değerine değil, ne kadar hızlı değiştiğine bakar. Sayının kendisinden çok değişimin hızının önemli olduğu durumlar için bu kuralı kullanın.

## Uyarılar nerede görünür

- Her ekranın sağ üstündeki **zil**, uyarı geçmişinizi tutar. Üstündeki sayı okumadığınız uyarıların sayısıdır.
- **Anlık bildirimler**, izin verdiyseniz telefonunuza gelir.
- Panodaki **widget** turuncu ya da kırmızı olur.
- **Cora Max** aynı uyarıları büyük ekranda gösterir.

## Ekipman sorun bildirdiğinde

Bazı uyarılar bir ölçümle değil, ekipmanla ilgilidir. Trident ya da Jecod pompası gibi bir cihaz arıza bildirdiğinde Cora, akvaryumun ve cihazın adının geçtiği bir bildirim gönderir. Örneğin *"Salon akvaryumu: Ana pompa dikkat gerektiriyor"*. Bildirimde sıkışmış rotor gibi sorunun ne olduğu da yazar. Arıza giderilince ikinci bildirim gelir: *"Salon akvaryumu: Ana pompa tekrar normal"*. İki bildirim de **Ayarlar → Bildirimler** altında **Ekipman Arızaları** kategorisindedir.

Maxspect gyre (Beta) için de aynı uyarı gelebilir. Aynı ağdaki bir Cora Max, iki kafanın da %0'a ayarlı olduğunu görürse ya da gyre üst üste iki kez yanıt vermezse bu uyarı verilir. Bunu güvenlik önlemi değil, uyarı olarak görün. Cora Max gyre'yi sürekli değil, ara ara kontrol eder. Bunu da yalnızca çalışırken ve gyre'ye ulaşabildiğinde yapar.

## Bir cihaz bildirim göndermeyi kesti

Bir Neptune Apex, Red Sea ReefBeat cihazı, AquaWiz, Jecod pompası, Maxspect gyre, EcoTech cihazı ya da Inkbird oda havası monitörü sessiz kalırsa Cora size haber verir: *"[Cihaz]: bildirim göndermeyi kesti."* Cihazın gücünü ve Wi-Fi (ya da Bluetooth menzili) bağlantısını, bir de onu okuyan Cora Max'in açık olduğunu kontrol edin. Cihaz yeniden bildirim göndermeye başladığında ikinci bir bildirim alırsınız.

Cora'nın ne kadar bekleyeceği cihaza göre değişir.

- Neptune Apex ve Red Sea ReefBeat: güncelleme gelmeden yaklaşık 30 dakika.
- AquaWiz: daha seyrek kontrol edildiği için yaklaşık 3 saat.
- Jecod ve Maxspect: üst üste üç ölçüm kaçırılması. Cihazın kendi ölçüm aralığına göre sayılır.
- EcoTech ve Inkbird: üst üste üç ölçüm kaçırılması. O ağ ya da monitör için belirlediğiniz aralığa göre sayılır.

Maxspect, EcoTech ve Inkbird, yalnızca Beta kullanıcılarının ekleyebildiği Beta entegrasyonlardır. Ayrıntılar [Beta özellikleri](/help/mobile-beta) sayfasında.

Bu da yukarıdaki arıza uyarıları gibi **Ayarlar → Bildirimler** altında **Ekipman Arızaları** kategorisindedir.

## "Red Sea değerleri güncellenmiyor"

Bir akvaryumun parametre sayfasında şu şeridi görebilirsiniz:

> Red Sea değerleri güncellenmiyor. Bu akvaryumun Red Sea cihazlarını şu anda hiçbir cihaz okumuyor: Ayarlar'da birincil Cora Max'i kontrol edin veya bu akvaryumu aynı Wi-Fi ağındaki bir cihazda açın.

Bu, şu an o akvaryumun ReefBeat ekipmanını hiçbir telefonun ya da Cora Max'in yoklamadığı anlamına gelir. Gösterilen ölçümler eskidir ama yanlış olmak zorunda değildir. Şeride dokunarak **Birincil Cora Max** ayarını açın. Açık olan bir cihaz seçin ya da ayarı **Aktif olan herhangi biri (otomatik)** yapın. Ayrıntılar [Birden fazla Cora cihazı](/help/mobile-multi-device) sayfasında. Şerit kaybolmazsa [Sorun giderme](/help/troubleshooting) sayfasına bakın.

## Size nelerin geleceğini seçme

**Ayarlar → Bildirimler.** Burada şunu ayarlarsınız:

- Hangi bildirim kategorilerinin telefonunuza gelebileceği

Reef Buddy'nin ayrı anahtarı yoktur. İlgilenmeniz gereken bir şey olduğunda özet gönderir, yoksa sessiz kalır.

:::note Cora gereksiz yere rahatsız etmez
Günlük özet, her akvaryum için günde tek bildirimdir. Dikkatinizi gerektiren bir şey olmayan günlerde "her şey yolunda" demek için bildirim göndermez, genellikle sessiz kalır. Cora bildirim gönderiyorsa bir şey değişmiş demektir.
:::

## Bekleme süresi: aynı uyarı ne sıklıkla bildirim gönderir

Her kuralın kendi **Uyarılar arası bekleme süresi** var. Bu süreyi kuralı eklerken ya da düzenlerken (Uyarı Merkezi'nin **Kurallar** sekmesinde) seçersiniz. Bekleme süresi uyarıyı gizlemez. Yalnızca Cora'nın o uyarı için ne sıklıkla bildirim göndereceğini sınırlar. Ölçüm bu süre boyunca da değerlendirilir. Uyarı da widget'ta ve zilde görünmeye devam eder.

Şu sürelerden birini seçebilirsiniz: 15 dk, 30 dk, 1 sa, 2 sa, 4 sa, 8 sa, 1 gün, 3 gün ya da **1 hafta**.

Kısa bekleme süresi, sıcaklık gibi hızlı değişen ölçümlere uyar. Bir haftaya kadar çıkan uzun süreler ise, bir parça beklerken günlerce düzelmeyecek sorunlar içindir. Örneğin reaktifi biten bir Trident ya da boşalmış bir dozaj kabı. Uzun bekleme süresi olmasa Cora aynı bilinen sorun için günde birkaç kez bildirim gönderirdi.

:::note Etkin uyarıyı ertelemek Cora Max'ten yapılır
Cora Mobile'da etkin uyarı için ayrı Ertele düğmesi yoktur. Bu düğme akvaryumun yanındaki Cora Max ekranındadır ve uyarıyı burada seçtiğiniz bekleme süresi kadar susturur. Telefondan bir konuda ne sıklıkla haber alacağınızı değiştirmek için uyarıyı ertelemezsiniz, kuralın bekleme süresini değiştirirsiniz.
:::

## Uyarının kapanması

Ölçüm aralığa geri dönünce uyarı kapanır. Kapatmanız gereken bir şey yoktur. Uyarı sizden bir iş beklemez, akvaryumun durumunu bildirir.

:::note Anlık sıçramalar da uyarıya yol açar
Aralık dışındaki tek bir ölçüm uyarı için yeterlidir. Bu yüzden anlık sıçrama yapan prob da uyarı verdirir. Kaynak güvenilmezse eşiği genişletmeyin. Kaynağı yeniden kalibre edin ya da widget'ı başka bir kaynağa bağlayın.
:::

Sorun akvaryumda değil de ölçümdeyse (örneğin kalibrasyon isteyen bir prob) kaynağı düzeltin. Hatalı probu susturmak için eşiği genişletirseniz bir sonraki gerçek sorunu da gizlemiş olursunuz.

## Bir uyarıyı kapatma

Uyarı Merkezi'nin **Kurallar** sekmesinde kuralın satırındaki anahtarı kapatın. Kural ve aralığı silinmez. İstediğinizde baştan kurmadan yeniden açabilirsiniz.

Kural kapalıyken Cora o ölçümü değerlendirmez. Widget'ı nötr gri kalır ve hiç uyarı vermez.

:::warning Parametreyi susturmak için aralığı silmeyin
Eşiği silmek o ölçümün değerlendirilmesini tamamen durdurmayabilir. Varsayılan referans aralıklar değeri yine renklendirir ve özete de yansıyabilir. Bunun yerine kuralın anahtarını kullanın.
:::
