---
title: Uyarılar ve eşikler
description: Her parametre için aralığı belirleyin, ne hakkında bilgilendirileceğinizi seçin ve bir uyarının neden tetiklendiğini anlayın.
section: Cora Mobile
reviewed: 2026-09-27
order: 15
group: Alerts and automation
---

Bir okuma, onun için belirlediğiniz aralığın dışına çıktığında bir uyarı yükseltilir. Aralıkları siz belirlersiniz ve hangi uyarıların telefonunuza ulaştığını siz kontrol edersiniz.

**Uyarı Merkezi**'ni panonun altındaki kısayol satırından açın.

![Uyarı Merkezi](img/mobile-alerts.webp "Etkin uyarılar, her biri önem derecesi, onu tetikleyen ve zamanıyla.")

## Uyarı Merkezi

İki sekme:

- **Etkin**: şu anda yükseltilmiş uyarılar, bir sayaç rozetiyle
- **Kurallar**: onları üreten eşikler ve değişim hızı kuralları

Her etkin uyarı, parametreyi ve akvaryumu, onu tetikleyen okumayı, düz bir açıklamayı, bir önem derecesi çipini, tetiklenen kural türünü (**Eşik** veya **Değişim Hızı**) ve tetiklendiği zamanı gösterir.

Her birinde iki eylem:

- **Kuralı görüntüle**: onu yükselten kuralı açar, böylece aralığı ayarlayabilirsiniz
- **Bu uyarıyı açıkla**: Assistant'tan onu akvaryumunuzun geçmişine karşı yorumlamasını ister

## Bir aralık belirleme

Cora'nın derecelendirebildiği parametrelerin bir hedef aralığı vardır ve varsayılanlar, akvaryumu kurduğunuzda akvaryum türünüzden ve yaşınızdan gelir, genellikle başlamak için makul bir yerdir. Kullanılabilir bir aralığı olmayan bir parametre hiç derecelendirilmez: tahmin edilmek yerine tarafsız gri kalır.

Birini değiştirmek için: panodaki widget'ına **uzun basın**, bu doğrudan o parametrenin eşiklerini açar. Düz bir dokunuş bunun yerine parametre görünümünü açar; iki hareket farklı yerlere gider ve uzun basış hatırlanmaya değer kısayoldur.

Parametrenin henüz bir kuralı yoksa, alanlar Cora'nın varsayılanıyla başlar ve altındaki bir not bunu söyler. Kendi değerinizi belirlemek için herhangi bir değeri değiştirin.

Hepsini bir arada görmek için, panonun altındaki düğme satırında **Uyarılar**'ı kullanın.

Şunları belirleyebilirsiniz:

- **Bir aralık**: alkalinite veya sıcaklık gibi şeyler için bir alt ve bir üst
- **Bir tavan**: düşük olmasının sorun olmadığı, nitrat veya fosfat gibi şeyler için yalnızca bir üst
- **Bir zemin**: yalnızca bir alt

:::tip Akvaryumunuzun gerçekte çalıştığı aralığı belirleyin
Varsayılanlar bir başlangıç noktasıdır, bir hüküm değil. 6 dKH'de düşük besinli çalışan bir akvaryum, bir grafik 8-9 dediği için "yanlış" değildir. Gerçekte çalıştığınız aralığı belirleyin ve Cora *siz* kaydığınızda size söyler.
:::

## Bir uyarıyı ne tetikler

Bir okuma bir eşiği geçtiğinde bir uyarı tetiklenir. Cora her okumayı geldiği anda kontrol eder, bu yüzden aralığınızın dışında tek bir okuma birini yükseltmeye yeterlidir.

Bir uyarı yükseldikten sonra sizi aynı şey hakkında tekrar tekrar bildirmeyi sürdürmez; yeniden tetiklenebilmesinden önce bir bekleme süresi vardır. Ve bir okuma aralığın içine geri döndüğü anda **kendini kapatır**; onaylanacak bir şey yoktur.

Bir **değişim hızı** kuralı da belirleyebilirsiniz; bu, bir parametrenin şu anda nerede olduğuna değil, ne kadar hızlı hareket ettiğine bakar. Bir sayıdan çok değişimin hızının önemli olduğu şeyler için kullanılacak olan budur.

## Uyarılar nerede görünür

- Her ekranın sağ üstündeki **zil**, geçmişinizi tutar. Sayı, okumadığınız kadarıdır.
- **Push bildirimleri**, izin verdiğinizde telefonunuza ulaşır.
- **Widget**, panoda amber veya kırmızıya döner.
- **Cora Max**, aynı uyarıları büyük ekranda gösterir.

## Ekipman ilgi gerektirdiğinde

Bazı uyarılar bir okuma hakkında değil ekipman hakkındadır. Bir Trident veya bir Jecod pompası gibi bir cihaz bir arıza bildirdiğinde, Cora akvaryumu ve cihazı adlandıran bir bildirim gönderir, örneğin *"Sergi akvaryumu: Ana pompa ilgi gerektiriyor"*, ve sıkışmış bir rotor gibi neyin yanlış olduğunu söyler. Arıza temizlendiğinde, ikinci bir bildirim gelir: *"Sergi akvaryumu: Ana pompa yine iyi"*. İkisi de **Ayarlar → Bildirimler**'de **Ekipman Arızaları** altındadır.

Bir Maxspect gyre (beta), ağında bir Cora Max her iki kafayı da %0'da bulduğunda, veya gyre'den art arda iki kez yanıt alamadığında aynı uyarıyı yükseltebilir. Bunu bir uyarı olarak ele alın, bir güvenlik önlemi olarak değil: Cora Max sürekli değil zaman zaman kontrol eder ve yalnızca çalışırken ve gyre'ye ulaşabildiğinde.

## "Red Sea okumaları güncellenmeyi durdurdu"

Bir akvaryumun parametre sayfasında bu banner'ı görebilirsiniz:

> Red Sea okumaları güncellenmeyi durdurdu. Şu anda bu akvaryumun Red Sea cihazlarını okuyan bir cihaz yok: Ayarlar'da Birincil Cora Max'i kontrol edin, veya bu akvaryumu aynı Wi-Fi'deki bir cihazda açın.

Bu, şu anda o akvaryumun ReefBeat ekipmanını hiçbir telefonun veya Cora Max'in yoklamadığı anlamına gelir; bu yüzden gösterilen okumalar eski, mutlaka yanlış değil. Banner'a dokunun, **Birincil Cora Max**'i açın ve açık olan bir cihaz seçin, veya onu **Aktif olan herhangi biri (otomatik)**'e ayarlayın. Bkz. [Birden fazla Cora cihazı](/help/mobile-multi-device). Kapanmıyorsa, bkz. [Sorun giderme](/help/troubleshooting).

## Size ne ulaşacağını seçme

**Ayarlar → Bildirimler.** Şunları kontrol edebilirsiniz:

- Hangi bildirim kategorilerinin push gönderebileceği

Reef Buddy'nin kendi anahtarı yoktur: harekete geçmeye değer bir şey olduğunda bir briefing gönderir ve olmadığında sessiz kalır.

:::note Cora sessiz kalmak için tasarlandı
Günlük briefing, akvaryum başına günde bir push'tur ve hiçbir şeyin ilginizi gerektirmediği bir günde, size her şeyin iyi olduğunu söylemek yerine genellikle sessiz kalır. Cora push gönderiyorsa, bir şey değişti demektir.
:::

## Bekleme süreleri: aynı uyarının size ne sıklıkla bildirebileceği

Her kuralın kendi **Uyarılar arası bekleme süresi** vardır, kuralı eklerken veya düzenlerken (Uyarı Merkezi'nin **Kurallar** sekmesinde) belirlenir. Bekleme süresi uyarının kendisini gizlemez: yalnızca Cora'nın onun hakkında size ne sıklıkla push gönderdiğini sınırlar. Okuma boyunca derecelendirilmiş kalır ve uyarı widget'ta ve zilde görünür kalır.

Şunlardan seçebilirsiniz: 15 dk, 30 dk, 1 sa, 2 sa, 4 sa, 8 sa, 1 gün, 3 gün, veya **1 hafta**.

Kısa bir bekleme süresi, sıcaklık gibi hızlı hareket eden bir okumaya uyar. Bir haftaya kadar uzun bir bekleme süresi, bir parça beklerken günlerce yanlış kalan bir şeye uyar, örneğin reaktifi bitmiş bir Trident veya boş bir dozaj kabı: uzun bir bekleme süresi olmadan, Cora aynı bilinen sorun hakkında günde birkaç kez push gönderirdi.

:::note Etkin bir uyarıyı erteleme Cora Max'te yaşar
Cora Mobile'ın etkin bir uyarıda kendi Ertele düğmesi yoktur; o kontrol akvaryumdaki Cora Max ekranındadır ve aynı uyarıyı burada seçtiğiniz bekleme süresi kadar susturur. Telefondan, bir şey hakkında ne sıklıkta bilgilendirileceğinizi değiştirmenin yolu bu kural başına bekleme süresidir, uyarı başına bir erteleme değil.
:::

## Bir uyarıyı temizleme

Okuma aralığa geri döndüğünde bir uyarı kapanır. Kapatılacak bir şey yoktur; bu bir görev değil, akvaryum hakkında bir ifadedir.

:::note Geçici okumalar uyarı yükseltir
Aralık dışında tek bir okuma bir uyarı yükseltmeye yeterlidir, bu yüzden ani bir sıçrama yapan bir prob birini tetikler. Bir kaynak güvenilmezse, onu yeniden kalibre edin veya widget'ı farklı bir kaynağa işaret edin, eşiği genişletmek yerine.
:::

Bir okuma yanlışsa, akvaryum yanlış olduğu için değilse (kalibrasyon gereken bir prob gibi), kaynağı düzeltin. Kötü bir probu susturmak için bir eşiği genişletmek, bir sonraki gerçek sorunu da gizler.

## Bir parametre için uyarıları devre dışı bırakma

Uyarı Merkezi'nin **Kurallar** sekmesinde kuralı açın ve **etkinleştirme anahtarını** kapatın. Kural ve aralığı korunur, böylece onu yeniden oluşturmadan geri açabilirsiniz.

:::warning Bir parametreyi silmeden susturun
Bir eşiği kaldırmak, o okumanın her değerlendirmesini durdurmayabilir; varsayılan referans bantları değeri hâlâ renklendirebilir ve briefingi hâlâ besleyebilir. Kuralın etkinleştirme anahtarını kullanın.
:::
