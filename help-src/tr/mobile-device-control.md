---
title: Ekipmanınızı kontrol etme
description: Canlı durumunu görmek ve çalıştırmak için bir cihazın kendi sayfasını açın: prizler, pompalar, dozaj kafaları ve test cihazları.
section: Cora Mobile
reviewed: 2026-09-27
order: 11
group: Equipment
---

Bağlı ekipmanın Cora'da kendi sayfası vardır; canlı durumu gösterir ve o cihazın desteklediği her kontrolü sunar. Birini **Cihazlar** sekmesinden açın.

![Bir cihaz sayfası](img/mobile-device-detail.webp "Üstte canlı okumalar, ardından o cihazın desteklediği kontroller.")

Her cihaz sayfası aynı şekli takip eder: üstte tanımlama, bir canlı okuma satırı, cihazın bildirdiği herhangi bir durum, ardından kontrolleri. Başlık çubuğundaki zil, o cihaz için uyarı eşiklerini belirler; bkz. [Sarf malzemeleri](/help/mobile-consumables).

:::warning Bu kontroller canlı ekipman üzerinde etkilidir
Önizleme ve geri alma yoktur. Bazı kontroller de önce onaylamanızı ister.
:::

## Bir komut gönderdiğinizde ne olur

Bir komut her zaman başarılı olmaz ve Cora, varsaymak yerine dört şeyden hangisinin gerçekleştiğini söyler:

| Sonuç | Anlamı |
|---|---|
| **Onaylandı** | Ekipman değişikliği kabul etti ve yeni durumunu bildirdi |
| **Onaylanmadı** | Komut gönderildi ama hiçbir şey bildirilmedi. **Bu "bilmiyoruz" anlamına gelir, "çalıştı" değil**; cihazın kendi durumunu kontrol edin |
| **Reddedildi** | Bir şey onu reddetti (bir güvenlik kuralı, bir kilit veya ekipmanın kendisi), veya zamanında hiçbir Cora cihazı onu almadı, bu yüzden iptal edildi ve hiçbir şey çalışmadı |
| **Değişiklik yok** | Ekipman zaten istediğiniz durumdaydı |

Her sonuç, nedeniyle birlikte [Etkinlik](/help/mobile-activity)'te kaydedilir.

## Neptune Apex

Apex sayfası problarınızı ve prizlerinizi listeler.

- **Problar**, Cora'ya kaynak olarak bildirir ve bir panoya yerleştirilebilir.
- **Prizler**, **Otomatik**, **Kapalı** ve **Açık** arasında değişir. Otomatik, kontrolü Apex programlamanıza geri verir.
- **Takılı modüllerin** (Trident, DŌS ve diğerleri) her birinin kendi sayfası vardır.

## Trident

Geçerli test durumunu, kalan reaktif ve atık su seviyelerini gösterir ve bir test başlatmanızı sağlar.

Bu sayfadan kalan testler için bir uyarı eşiği belirleyebilirsiniz; böylece reaktif bitmeden Cora sizi uyarır. Bkz. [Sarf malzemeleri](/help/mobile-consumables).

## DŌS

Bir DŌS QD tam olarak bir DŌS gibi çalışır ve buradaki her şey ikisi için de geçerlidir. Bir Cora Max Apex'inizi okuduğunda, dozaj kafaları priz listesinde değil DŌS sayfasında görünür.

Her dozaj kafası, neyi dozajladığını, zamanlamasını, bugün ne dozajladığını, kapta ne kadar kaldığını ve **kalan süresini** gösterir: bunun geçerli hızda kaç gün süreceği.

Kafa başına şunları yapabilirsiniz:

- Zamanlamasını **Duraklat** ve **Sürdür**
- **Doldur**: kabın yeniden dolu olduğunu Cora'ya söyleyin, veya içindeki hacmi belirleyin
- **Şimdi dozajla**: ölçülmüş elle bir dozaj

:::note Zamanlamalar burada değil Apex Fusion'da düzenlenir
Cora zamanlamayı gösterir ve dozajlananı takip eder, ama onu değiştirmez. Zamanlamayı, dozaj hızını veya dozaj sayısını düzenlemek Apex Fusion uygulamasında yapılır. Duraklatma, doldurma ve elle dozajlama burada desteklenir.
:::

:::note Elle dozajlamadan önce bir kafayı ölçün
Cora, ölçülene kadar bir kafayı elle dozajlamaz. **Dozajlamak için ölç** ve **Yeniden ölç**, akvaryum için dozajlayan Cora Max'tedir: Cora kafayı yirmi saniye çalıştırır, ne çıktığını ölçersiniz ve Cora kafanın gerçek hızını hesaplar. Bir ölçüm her Cora Max ve Cora Mobile'a hizmet eder, bu yüzden her kafayı bir kez ölçün ve borusunu değiştirdikten sonra yeniden ölçün.
:::

:::warning Bir DŌS, kabı boşken de dozajlamayı sürdürür
Birimin bir seviye sensörü yoktur ve kendiliğinden durmaz. Kap kurumadan Cora'nın sizi uyarması için kafanın sayfasından bir yeniden doldurma uyarısı belirleyin.
:::

### Her kafa ne için kullanılır

Her kafa, Cora'nın ne yaptığını bilmesi ve onun hakkında doğru konuşabilmesi için bir **kullanım türüne** ayarlanır: **Takviye**, **Su değişimi: yeni tuzlu su girişi**, **Su değişimi: eski su çıkışı**, **Kalkwasser**, **Kalsiyum reaktörü**, **Besin**, **Tamamlama**, veya **Diğer**. Bunu kafanın ayarlarında **Kullanım amacı** altında belirleyin.

İki su değişimi kullanım türü **eşleştirilmek** üzere tasarlanmıştır: bir kafanın **Eşleştirilmiş kafa**'sını, suyu ters yönde hareket ettiren diğer kafaya ayarlayın ve Cora bunları iki ilgisiz kafa yerine bir su değişimi çifti olarak ele alır.

Her kafa, yanlış yazılmış elle bir dozajın istenenden çok daha büyük olmasını durdurmak için bir **Elle verilecek en büyük dozaj** tavanına da sahiptir. Büyük elle dozajlar, kafanın hızı akvaryumda gerçek bir teste karşı ölçüldükten sonra kullanılabilir hale gelir.

## Red Sea ReefBeat

Her birimin ne olduğuna uygun bir sayfası vardır:

| Birim | Sayfa gösterir | Yapabilirsiniz |
|---|---|---|
| **ReefDose** | Her kafa, kabı ve dozajladığı | Her kafa için: **Günlük dozaj**, **Şişede kalan**, **Şimdi dozajla** ve **Zaman planını etkinleştir**. Kafa başına yeniden doldurma uyarıları belirleyin |
| **ReefATO+** | Rezervuar seviyesi ve tamamlama etkinliği | Bir rezervuar uyarısı belirleyin |
| **ReefMat** | Kalan rulo, gün ve metre olarak | Ruloyu ilerletin, bir yeniden doldurma uyarısı belirleyin |
| **ReefRun** | Ana pompa ve skimmer pompası hızı ve durumu | Hızı değiştirin, bir pompayı açıp kapatın, skimmer ayarlarını değiştirin |

**ReefRun bir ana pompa ve skimmer pompası kontrolcüsüdür**, bir dalga pompası değil.

Bir birim kendini durdurabilir, örneğin skimmer kupası dolduğunda bir ReefRun pompası. Bu olduğunda, sayfası nedenini söyler ve düzeltmeyi sunar:

| Birim | Sayfa söyler | Dokunun |
|---|---|---|
| ReefRun | Hangi pompanın ve neden durduğunu, örneğin *Kupa dolu. Boşaltın, ardından sürdürün.* | **Sürdür** |
| ReefRun veya ReefMat | **Acil durdurma** | **Acil durumu temizle** |
| ReefMat | **Mat sıkıştı**, **Kurulum hatası** veya **Ayar hatası** | **Sürdür** |
| ReefMat | *Yeni bir rulo yükleyin, ardından Red Sea'nin uygulamasında onaylayın.* | **Zaten yeni bir rulo yükledim** |
| ReefMat | **Sensör temizlenmeli** | **Sensör temizlendi** |
| ReefDose | Kafanın adıyla **Kafa arızası** | **Sıfırla** |
| ReefATO+ | **Arızayı Temizle** | **Sürdür** |

Bunların bazıları önce onaylamanızı ister. Birimin ağının dışındayken, Cora Mobile bunları akvaryumdaki bir Cora Max üzerinden gönderir; hiçbir Cora Max bunu yapamıyorsa, sayfa bunu söyler ve hiçbir şey gönderilmez.

## Jecod pompaları

Pompa sayfası geçerli modunu ve yoğunluğunu gösterir ve ikisini de değiştirmenizi sağlar.

Ayrıca şunları da yapabilirsiniz:

- **Programı şuraya kopyala…**: bu pompanın programını başka birine koyun
- **Programı farklı kaydet…** ve **Kayıtlı programlar…**: bir programı tutun ve daha sonra yeniden uygulayın
- **Bu zamanlamayı paylaş** ve **Bir zamanlama kodu yapıştır…**: bir zamanlamayı kısa bir kod olarak sistemler arasında taşıyın

## Maxspect

:::note Maxspect desteği beta aşamasında
Maxspect gyre desteği hâlâ test edilip geliştiriliyor, bu yüzden bazı kontroller sınırlı olabilir ve burada gördükleriniz güncellemeler arasında değişebilir. Bir şey açıklandığı gibi çalışmıyorsa, bize [Yardım alma](/help/mobile-support)'dan bildirin.
:::

Gyre sayfası, gyre'nin çalışıp çalışmadığını, **Gyre A** ve **Gyre B**'nin dalga deseni ve hızını, ve bunun son ne zaman okunduğunu gösterir. Ondan şunları yapabilirsiniz:

- Gyre'yi durumunun yanındaki anahtarla açıp kapatın. Cora önce onaylamanızı ister. Kapatmak her iki gyre'yi de durdurur ve zamanlamayı olduğu gibi bırakır.
- Her gyre'nin dalga desenini ve pompa hızını (ve bir deseninkiyse süresini), ve iki gyre'nin bağlı olup olmadığını ayarlamak için **Ayarları değiştir**'e dokunun. Cora neyin değişeceğini listeler ve uygulamadan önce onaylamanızı ister. Alternatif (Alternating) Maxspect uygulamasında ayarlanır: bunu çalıştıran bir gyre kendi rampalarını ve tutma sürelerini korur.
- Gyre'de kayıtlı program okunamıyorsa bunun yerine **Programı ayarla**'ya dokunun. Bu, gyre'nin yeniden başlayabilmesi için her iki gyre'yi de ayarlar.
- Gyre'nin gün programını **Zamanlama** kartında görün. Yalnızca görüntülenir: zamanlamayı Maxspect uygulamasında ayarlayın.
- **Pompa sağlığını** kontrol edin: pompanın bir dahaki sefere ne zaman temizlenmesi gerektiği (pompa bunu kendisi geri sayar), kafa A'nın çektiği akım, hangi kafaların takılı olduğu ve yazılımı. Almak için **Oku**'ya dokunun.

:::note Cora Mobile bir gyre'ye nasıl ulaşır
Bir Cora Max akvaryuma hizmet ettiğinde, Cora Mobile, evden uzaktayken dahil, o Cora Max üzerinden çalışır ve **Ayarları değiştir**, o Cora Max'in son okumasından başlar. Aksi halde telefonunuz doğrudan gyre'yle konuşur ve gyre'nin ağında olmalıdır. Sayfayı açmak sonra gyre'yi okur; sayfa bunun yerine daha eski kaydedilmiş bir okuma gösteriyorsa, yenilemeye dokunana kadar **Ayarları değiştir** gizli kalır.
:::

## Bir şeyi değiştirdikten sonra ne olur

Her değişiklik, onu isteyen yüzeyle birlikte [Etkinlik](/help/mobile-activity)'te kaydedilir. Bir cihaz bir değişikliği kabul etmezse, başarısızlık da orada kaydedilir.
