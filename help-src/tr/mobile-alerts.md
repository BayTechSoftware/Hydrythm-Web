---
title: Uyarılar ve eşikler
description: Her ölçüm için sağlıklı aralığı ayarlayın, bir uyarının sizi ne sıklıkla bilgilendirebileceğini seçin ve bir cihazın neden "bildirim yapmıyor" olduğunu öğrenin.
section: Cora Mobile
reviewed: 2026-10-24
order: 23
group: Alerts and automation
twin: max-alerts
---

Bir ölçüm onun için belirlediğiniz aralığın dışına çıktığında bir uyarı alırsınız. Bu sayfa bu aralıkları ayarlamayı, bir uyarı tetiklendiğinde ne olduğunu ve Cora'nın bir cihazın bildirmeyi bıraktığını söylemeden önce ne kadar beklediğini anlatır.

**Uyarı Merkezi**'ni açmak için panonun altındaki düğme satırında **Uyarılar**'a dokunun. Aynı ekran Ayarlar → akvaryumunuz → **Uyarı eşikleri** yolunda da var.

![Cora Mobile'da Uyarı Merkezi'nin Etkin sekmesi](img/mobile-alerts.webp "Etkin uyarılar, her biri önem düzeyi, onu neyin tetiklediği ve ne zaman tetiklendiğiyle, ayrıca Kuralı görüntüle ve Bu uyarıyı açıkla.")

## Uyarı Merkezi {#alert-center}

İki sekmesi vardır. **Etkin**, şu anda açık olan uyarıları bir sayı rozetiyle listeler. **Kurallar**, onları oluşturan kuralları tutar.

Her etkin uyarı parametreyi ve akvaryumu, onu tetikleyen ölçümü, kısa bir açıklamayı, bir önem düzeyi çipini, tetiklenen kuralın türünü (**Eşik** ya da **Değişim Hızı**) ve ne zaman tetiklendiğini gösterir. İki düğmesi vardır:

- **Kuralı görüntüle**, aralığı ayarlayabilmeniz için arkasındaki kuralı açar. Bir DŌS ya da ReefDose kafasının azalması ya da kaçırılan bir doz gibi bir dozaj pompası uyarısında bu düğme bunun yerine **Dozaj pompasını aç**'tır. O dozaj pompasının uyarılarıyla birlikte sayfasını açar.
- **Bu uyarıyı açıkla**, uyarı hakkında gönderilmeye hazır bir soruyla Cora Assistant'ı açar. Kontrol edin, isterseniz değiştirin, sonra gönderin.

## Kurallar sekmesi {#rules}

![Kurallar sekmesi](img/mobile-alert-rules.webp "Parametreye göre gruplanmış kurallar, her biri kendi anahtarıyla.")

Kurallar parametreye göre gruplanır. Her kuralın satırında kendi anahtarı vardır, böylece birini açmadan kapatabilirsiniz. Bir satır, uyarısı açıkken **Şu anda tetikleniyor**'u ya da en son ne zaman tetiklendiğini (veya **Hiç tetiklenmedi**) de gösterir.

Bir dozaj kafasının kuralları kafanın adıyla ve neyi izlediğiyle adlandırılır, örneğin *İyot · kalan gün* ya da *İyot · kalan*. Kaçırılan bir doz *İyot · kaçırılan dozaj* olarak görünür. Her DŌS'un ve her ReefDose'un burada kendine ait tek bir satırı vardır ve kafa uyarıları tek tek listelenmez. O dozaj pompasının sayfasını açmak için satıra dokunun. [Dozaj pompası uyarıları](/help/mobile-device-control#doser-alerts) bölümüne bakın.

En altta:

- **Önerilen kuralları ekle**, Cora'nın önerdiği kurallardan eksik olanları ekler. Zaten kuralı olan bir parametreyi atlar. Hiç kuralı olmayan bir akvaryumda bu düğmede **Varsayılan Kuralları Ekle** yazar.
- **Özel Kural Ekle**, kendi kuralınızı kurar. Parametreyi ve **Kural türü**'nü, **Eşik** ya da **Değişim Hızı**, seçin. Sağ alttaki **Kural Ekle** düğmesi de aynı şeyi yapar.

### Bir kuralı düzenleme {#editing-a-rule}

Açmak için bir kuralın satırına dokunun. Şunları bulursunuz:

- Aralığın kendisi olan **Uyarı minimumu** ve **Uyarı maksimumu**. Üst ya da alt sınır için birini boş bırakın.
- Cora'nın önerdiği aralığı geri getiren **Önerilen**.
- **Gösterge min** ve **Gösterge maks** ile **Gösterge Aralığı (Cora ekranı)**. Bunlar yalnızca Cora Max'teki göstergenin ölçeğini ayarlar. Asla uyarı oluşturmaz.
- [Aşağıda](#cooldowns) açıklanan **Uyarılar arası bekleme süresi**.
- **Etkin** ve bir silme düğmesi.

Reaktifi biten bir Trident gibi bir cihaz arızası kuralının aralığı yoktur. Yalnızca bekleme süresini seçersiniz.

## Aralık ayarlama {#setting-a-range}

Cora'nın değerlendirebildiği parametrelerin bir hedef aralığı vardır. Varsayılanlar akvaryumu kurduğunuzda akvaryum türünüzden ve yaşından gelir ve mantıklı bir başlangıçtır. Bir parametrenin kullanılabilir bir aralığı yoksa Cora onu değerlendirmez ve widget'ı nötr gri kalır.

Bir aralığı değiştirmenin en hızlı yolu panoda parametrenin widget'ına uzun basmaktır. Bu, eşiklerini açar. Normal bir dokunuş ise parametre görünümünü açar.

![Cora Mobile'da pH için Eşiği Düzenle sayfası](img/mobile-threshold-sheet.webp "Uyarı minimumu ve maksimumu, Cora Max için gösterge aralığı ve uyarılar arası bekleme süresi.")

Parametrenin henüz kuralı yoksa alanlar Cora'nın varsayılanıyla başlar ve altındaki bir not bunu söyler. Kendi değerinizi ayarlamak için herhangi bir değeri değiştirin.

Şunları ayarlayabilirsiniz:

- alkalinite ya da sıcaklık gibi şeyler için alt ve üst değeri olan bir aralık
- nitrat ya da fosfat gibi düşük olmasının sorun olmadığı şeyler için yalnızca üst değeri olan bir üst sınır
- yalnızca alt değeri olan bir alt sınır

:::tip Akvaryumunuzun gerçekte çalıştığı aralığı ayarlayın
Varsayılanlar yalnızca bir başlangıç noktasıdır. 6 dKH'de çalışan düşük besinli bir akvaryum, bir tablo 8–9 diyor diye "yanlış" değildir. Çalıştığınız aralığı ayarlayın, Cora da *siz* kaydığınızda size söylesin.
:::

## Bir uyarıyı ne tetikler {#what-triggers-an-alert}

Bir uyarı, bir ölçüm bir eşiği geçtiğinde tetiklenir. Cora her ölçümü geldikçe kontrol eder, bu yüzden aralığınızın dışındaki tek bir ölçüm yeterlidir.

Değişim hızı kuralı bir parametrenin nerede durduğu yerine ne kadar hızlı hareket ettiğini izler. Bir değişimin hızı sayıdan daha önemli olduğunda kullanın.

Bir uyarı açıldığında aynı şey hakkında sizi bilgilendirmeye devam etmez. Sizi ne zaman yeniden bilgilendirebileceğine kuralın [bekleme süresi](#cooldowns) karar verir.

## Uyarılar nerede görünür

- Ana sekmelerin sağ üstündeki zil geçmişinizi tutar. Sayı kaç tanesini okumadığınızı gösterir. Ayrıntılar [Bildirimler](/help/mobile-notifications) sayfasında.
- O kategori açıksa telefonunuza bir anlık bildirim ulaşır.
- Panodaki widget turuncuya ya da kırmızıya döner.
- Cora Max aynı uyarıları ekranında gösterir.

## Ekipman ilgi gerektirdiğinde {#equipment-faults}

Bazı uyarılar bir ölçümle değil ekipmanla ilgilidir. Bir Trident ya da Jecod pompası gibi bir cihaz arıza bildirdiğinde Cora akvaryumu ve cihazı adlandıran bir bildirim gönderir, örneğin *"Salon: Ana pompa dikkat gerektiriyor"*. Ayrıca sıkışmış bir rotor gibi neyin yanlış olduğunu da söyler. Arıza giderildiğinde ikinci bir bildirim alırsınız: *"Salon: Ana pompa tekrar normal"*. İkisi de **Ayarlar → Bildirimler** içinde **Ekipman Arızaları** altına girer.

Bir AquaWiz KH Controller, her AquaWiz için ve Cora Max olmadan da, şu durumlarda aynı türde uyarı verir:

- dozaj pompası arıza bildirdiğinde;
- pH probu bozulduğunda ya da ömrünün sonuna yaklaştığında.

Alkalinite takviyesi azaldığında uyarı, kontrolörde belirlediğiniz uyarı seviyesini kullanır. Bunu yine Uyarı Merkezi'nden değiştirebilirsiniz. Su kutusu seviyesi bir saatten uzun süre düşük ya da yüksek kalırsa da uyarı gelir, ancak bunun için Cora Max'in saatlik okuması gerekir (bkz. [Cora Max'ten ekipman kontrolü](/help/max-device-control#aquawiz-hourly)): AquaWiz'in 12 saatlik bulut okuması bunu taşımaz.


## Bir cihaz bildirmeyi bıraktı {#stopped-reporting}

Bağlı bir cihaz sessizleştiğinde Cora *"[Cihaz]: bildirim yapmıyor"* gönderir. Bu cihazın bozuk olduğu anlamına gelmez, yalnızca Cora'nın bir süredir ondan haber almadığı anlamına gelir. Geri geldiğinde ikinci bir bildirim alırsınız: *"[Cihaz]: tekrar bildiriyor"*.

Cora'nın ne kadar beklediği cihaza bağlıdır:

| Cihaz | Cora'nın beklediği süre |
|---|---|
| Neptune Apex | Güncelleme olmadan yaklaşık 30 dakika |
| Red Sea ReefBeat | Yaklaşık 30 dakika |
| AquaWiz | Yaklaşık 25 saat, çünkü AquaWiz Cora'nın bulutunu yalnızca 12 saatte bir okumasına izin verir |
| Jecod pompaları | Pompanın okuma aralığına göre üst üste üç kaçırılan ölçüm (varsayılan 30 ile 90 dakika) |
| Zigbee akıllı prizi | Hub yeniden başladıktan 30 dakika sonra hâlâ dönmemişse. Uyarının onu adıyla anması için **Yeniden adlandır** ile ad verin |

Neyi kontrol edeceğiniz Cora'nın cihazı nasıl okuduğuna bağlıdır.

- Apex, ReefBeat ve Jecod'u bir Cora Max Wi-Fi üzerinden okur. Cihazın gücünü ve Wi-Fi'ını, ayrıca onu okuyan Cora Max'in açık ve çevrimiçi olduğunu kontrol edin.
- AquaWiz, üreticideki hesabınız üzerinden okunur. Cora Mobile'da cihazın sayfasındaki hesap bağlantısını kontrol edin.


Bu bildirimler **Ayarlar → Bildirimler** içinde **Ekipman Arızaları** altına girer.


Bir Red Sea akvaryumu, hiçbir telefon ya da Cora Max ReefBeat ekipmanını okumadığında *"Red Sea değerleri güncellenmiyor"* şeridini de gösterebilir. Bir **Birincil Cora Max** seçmek için ona dokunun. Tam çözüm [Sorun giderme](/help/troubleshooting#red-sea-readings-have-stopped-updating) sayfasında.

## Size nelerin ulaşacağını seçme {#choosing-what-reaches-you}

**Ayarlar → Bildirimler** içinde hangi kategorilerin size anlık bildirim gönderebileceğini seçersiniz. [Geceleri sessiz tutmayı](/help/mobile-notifications#quiet-at-night) da anlatan [Bildirimler](/help/mobile-notifications) sayfasına bakın.

Reef Buddy'nin kendine ait bir anahtarı yoktur. Zamanlaması, Ayarlar'da Bildirimler'in hemen altındaki **Özet saati** satırıdır. Ücretsiz planda özet bildirimi yoktur.

:::note Bir şey değişmedikçe Cora sessiz kalır
Günlük özet, akvaryum başına günde bir bildirimdir. Size ihtiyaç olmayan bir günde genellikle her şeyin yolunda olduğunu söylemek yerine sessiz kalır. Cora bildirim gönderiyorsa bir şey değişmiştir.
:::

## Bekleme süreleri: aynı uyarının sizi ne sıklıkla bilgilendirebileceği {#cooldowns}

Her kuralın kendi **Uyarılar arası bekleme süresi** vardır. Onu kuralı eklerken ya da düzenlerken ayarlarsınız. Hiç ayarlanmamış bir kural 1 sa kullanır.

Bekleme süresi uyarıyı gizlemez. Yalnızca Cora'nın onun hakkında ne sıklıkla bildirim göndereceğini sınırlar. Ölçüm yine değerlendirilir ve uyarı bütün süre boyunca widget'ta ve zilin altında kalır.

15 dk, 30 dk, 1 sa, 2 sa, 4 sa, 8 sa, 1 gün, 3 gün ya da 1 hafta seçebilirsiniz.

Kısa bir bekleme süresi sıcaklık gibi hızlı değişen bir ölçüme uyar. Bir haftaya kadar uzun bir süre ise bir parça beklerken günlerce yanlış kalan bir şeye uyar, örneğin reaktifi biten bir Trident ya da boş bir dozaj kabı.

:::note Ertele Cora Max'tedir
Cora Mobile'da etkin bir uyarıda Ertele düğmesi yoktur. Ertele akvaryumdaki Cora Max ekranındadır ve uyarıyı burada seçtiğiniz bekleme süresi boyunca susturur. Telefonunuzda bir şey hakkında ne sıklıkla haber alacağınızı kural başına bekleme süresiyle değiştirirsiniz.
:::

## Bir uyarının temizlenmesi {#clearing-an-alert}

Bir uyarı, ölçüm aralığa geri döndüğünde kendiliğinden temizlenir. Sizin kapatmanız gereken bir şey yoktur. Temizlendiğinde tek bir bildirim alırsınız, örneğin *"Salon: Alkalinite normale döndü"*. Sorun daha sonra geri gelirse yeni bir uyarı alırsınız.

:::note Kısa sıçramalar da uyarı oluşturur
Aralık dışındaki tek bir ölçüm uyarı oluşturmaya yeter, bu yüzden sıçrayan bir prob bir uyarı tetikler. Bir kaynak güvenilmezse onu yeniden kalibre edin ya da widget'ı farklı bir kaynağa yönlendirin. Eşiği genişletmeyin.
:::

Bazen ölçüm yanlıştır ve akvaryum iyidir, örneğin bir probun kalibrasyona ihtiyacı olduğunda. Bu durumda kaynağı düzeltin. Kötü bir probu susturmak için bir eşiği genişletirseniz bir sonraki gerçek sorunu da kaçırırsınız.

## Bir uyarıyı kapatma {#turning-an-alert-off}

**Kurallar** sekmesinde kuralın satırındaki anahtarı kapatın. Cora kuralı ve aralığını saklar, böylece onu yeniden kurmadan tekrar açabilirsiniz.

Bir kural kapalıyken Cora o ölçümü değerlendirmez. Widget'ı nötr gri kalır ve asla uyarı vermez.

:::warning Bir parametreyi aralığını silmeden kapatın
Bir kuralı silmek Cora'nın o ölçümü değerlendirmesini her zaman durdurmaz. Varsayılan referans bantları değeri yine renklendirir ve özeti yine besleyebilir. Kuralın anahtarını kullanın.
:::
