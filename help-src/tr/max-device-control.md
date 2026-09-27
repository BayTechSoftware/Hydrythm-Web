---
title: Cora Max'ten ekipman kontrolü
description: Büyük ekrandaki cihaz sayfaları: problar, prizler, dozaj kafaları, test cihazları ve pompalar.
section: Cora Max
reviewed: 2026-09-27
order: 6
group: Equipment
---

Cora Max, telefonunuzla aynı ekipmana, her cihaz için bir sayfayla ulaşır. Bunları **Ayarlar → Cihazlar**'dan, veya panodaki bir cihaz kutusuna dokunarak açın.

![Cora Max'te bir Apex sayfası](img/max-device-control.webp "Besleme döngüleri ve her priz, bir duvar ekranı için düzenlenmiş.")

:::warning Bu kontroller canlı ekipman üzerinde etkilidir
Önizleme ve geri alma yoktur. Dokunduğunuz anda bir komut gider, ama *gönderildi* demek *yapıldı* demek değildir: **Onaylandı**, **Onaylanmadı**, **Reddedildi** veya **Değişiklik yok** olarak geri döner ve hangisi olduğunu [Etkinlik](/help/max-activity)'te görürsünüz.
:::

## Sayfası olanlar

| Cihaz | Gösterdiği |
|---|---|
| **Neptune Apex** | Her biri açılıp kapatılabilen problar ve prizler |
| **Trident** | Test durumu, reaktif ve atık seviyeleri, ve bir test başlatma yeteneği |
| **DŌS**, DŌS QD dahil | Her kafanın dozajı, zamanlaması, kalan süresi ve kap hacmi (duraklat, doldur, şimdi dozajla ve tek seferlik yirmi saniyelik ölçüm ile) |
| **Red Sea ReefBeat** | Birim ne ise: dozaj kafaları, rezervuar, rulo günleri, pompa modu |
| **Jecod** | Pompa modu ve yoğunluğu, ve günlük programı |
| **Maxspect** *(beta)* | **Gyre A** ve **Gyre B** için mod ve hız, **Pompa sağlığı** (temizlik geri sayımı, kafa A akımı, takılı kafalar, yazılım), ve zamanlaması, salt görüntüleme |

Bir Red Sea birimi kendini durdurursa, sayfası neyin yanlış olduğunu söyler ve düzeltmeyi yanına koyar: **Sürdür**, **Acil durumu temizle**, **Sensör temizlendi**, **Zaten yeni bir rulo yükledim**, veya bir dozaj kafası için **Sıfırla**.

## DŌS kafaları

Bir DŌS kafası, Cora onu elle dozajlamadan önce bir kez ölçülmüş olmalıdır. **Dozajlamak için ölç**, kafayı ölçüm kabına yirmi saniye çalıştırır ve siz ne kadar çıktığını girersiniz. Cora, kafa başına bir ölçüm tutar ve hangi Cora Max aldıysa en yenisini kullanır; kafanın sayfası nerede ve ne zaman ölçüldüğünü gösterir.

Elle bir dozajdan sonra, Apex Fusion'da Kapalı'ya ayarladığınız bir kafa Kapalı kalır. Diğer her kafa Otomatik'e geri döner.

### Bir kafa ne için kullanılır

Her kafa ayarlar formundan bir **kullanım türüne** ayarlanabilir: **Takviye**, **Su değişimi: yeni tuzlu su girişi**, **Su değişimi: eski su çıkışı**, **Kalkwasser**, **Kalsiyum reaktörü**, **Besin** veya **Tamamlama**, veya **Diğer**. Kullanım türü iki şeyi değiştirir:

- **Ne kadar büyük bir kabı takip edebileceğini.** Bir Takviye kafası 20 litreye kadar takip eder; diğer her kullanım türü çok daha büyük bir kabı, 500 litreye kadar takip edebilir; böylece bir su değişimi veya kalsiyum reaktörü çalıştıran bir kafa küçük bir dozaj şişesi gibi ele alınmaz.
- **Elle büyük bir dozaj alıp alamayacağını.** Takviye ve Besin kafaları bugünkü küçük, dikkatli tavanı korur. Diğer her kullanım türüne, 10 litre sert tavana kadar kendi **Elle verilecek en büyük dozaj** sınırı ve kendi **otomasyonlar ve Assistant için günlük sınırı** verilebilir.

Bir su değişimi çifti (yeni tuzlu su girişi, eski su çıkışı), bir **Denge uyarısı üstünde** miktarıyla **Eşleştirilmiş kafa** olarak bağlanabilir: iki kafanın günlük toplamları bu miktardan fazla birbirinden uzaklaşırsa Cora sizi uyarır, çünkü dengesi bozuk bir çift genellikle bir tarafın beklendiği gibi pompalamadığı anlamına gelir.

### Büyük bir dozaj kesintiye uğrarsa

Büyük bir dozaj, kafanın Apex'te yaptığını geçici olarak değiştirir, ardından sonrasında normal zamanlamasını geri koyar. Bağlantı ortasında düşerse, Cora Max o kafanın sayfasında bir banner gösterir: *"[kafa] üzerindeki büyük bir dozaj temiz şekilde bitmedi. Cora programını geri koymayı denemeyi sürdürüyor; Apex Fusion'da kontrol edin."*

Kafayı Apex Fusion'da kendiniz kontrol edin, ardından banner'ı kapatmak için **Kafayı Fusion'da kontrol ettim**'e dokunun. Bunu yalnızca gerçekte çalışanın Cora'nın dozaj programı değil kafanın kendi zamanlaması olduğunu doğruladıktan sonra yapın.

**Çalışmazsa:** banner kapanmıyorsa, veya tekrar tekrar geri geliyorsa, bkz. [Sorun giderme](/help/troubleshooting).

## Zamanlamalar

Jecod pompa günlük programları duvarda da telefonda da yazılabilir. Düzenleyici aynıdır: bir gün grafiği, bir periyot listesi ve bir eylem satırı. Bkz. [Ekipman zamanlama](/help/mobile-schedules).

Bir Maxspect gyre'nin zamanlaması *(beta)* burada görüntülenebilir ama kaydedilemez. Onu Maxspect uygulamasında ayarlayın.

## Prizler

Prizlere, panonun altındaki **Prizler ve Besleme** çekmecesinden de ulaşılabilir; bu, bu pano için etkinleştirilmiş prizleri tek bir yerde listeler (hiçbiri seçilmemişse tümünü). Bkz. [Prizler ve kontroller](/help/max-controls).

DŌS kafaları hiçbir zaman priz listesinde görünmez; böylece bir kafa orada açılıp çalışır halde bırakılamaz, kendi sayfasından dozajlayın. Birkaç modülü olan büyük bir Apex, tüm prizlerini ve problarını gösterir.

## Sarf malzemeleri

Yeniden doldurma eşikleri (reaktif, kaplar, rezervuarlar) burada, tam olarak telefonda olduğu gibi, cihazın kendi sayfasından ayarlanır. Bkz. [Sarf malzemeleri](/help/mobile-consumables).

## Akvaryumda kaydetme ve hesaplama

İki şey genellikle bir telefonda olduğundan duvarda daha kullanışlıdır:

- **Parametreleri kaydet**: akvaryum menüsünden, ekrandaki klavyeyle test sonuçlarını girin
- **Dozaj hesaplayıcı**: bir parametrenin sayfasından, akvaryumun hacmini ve ürün güçlerinizi kullanarak bir düzeltme hesaplayın. Telefonla aynı hacmi ve ürün güçlerini kullanır; böylece burada hesaplanan bir dozaj orada hesaplananla eşleşir. Bkz. [Dozaj](/help/mobile-dosing).

## İkinci bir Cora Max'te

Birden fazla Cora Max bir akvaryumu gösterdiğinde, biri o akvaryumun ekipmanını okur; cihaz sayfaları ona akvaryumdaki Cora Max der. Diğerleri hâlâ cihaz sayfalarını açar (**Bulut** okuyan bir durum hapı, bu ekranın bunlardan biri olduğu anlamına gelir). Bunlar, akvaryumdaki Cora Max'in son okuduğunu ve ne kadar önce okuduğunu gösterir ve her komutu Cora Cloud üzerinden yerine getirmesi için o Cora Max'e geçirir.

Birkaç şey akvaryumdaki Cora Max'te kalır:

- **Dozajlamak için ölç** ve **Yeniden ölç** yalnızca orada görünür. Bir kafa ölçüldükten sonra, **Şimdi dozajla** herhangi bir Cora Max'ten çalışır.
- Bir Jecod zamanlaması, akvaryumdaki Cora Max pompayı son bir saat içinde okuduysa ve sadece Bluetooth üzerinden konuşan bir pompa için asla olmamak üzere, başka bir Cora Max'ten değiştirilebilir. Oradan bir **Pompaya uygula**, en fazla 12 değişiklik gönderir; bu yüzden daha büyük bir düzenlemeyi parçalar halinde gönderin.

## Ne değişti ve ne tarafından

Her eylem, nedeniyle birlikte kaydedilir. Bkz. [Etkinlik ve zaman çizelgesi](/help/mobile-activity).
