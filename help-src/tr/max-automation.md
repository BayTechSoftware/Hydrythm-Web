---
title: Cora Max'te sahneler
description: Ayarlar → Otomasyonlar yolundan ya da panodaki bir sahne kutucuğundan Cora Max'te sahne oluşturun, çalıştırın, düzenleyin ve silin.
section: Cora Max
reviewed: 2026-10-13
order: 9
group: Alerts and automation
twin: mobile-automation
---

**Sahne**, birlikte çalışan kayıtlı bir ekipman eylemleri setidir. Ya belli bir süre ya da siz durdurana kadar çalışır. Cora Max'te sahne oluşturabilir, çalıştırabilir ve düzenleyebilirsiniz. Telefonunuzda ve Cora Max'te yapılan sahneler aynı sahnelerdir. Otomasyon kuralları ("bu olduğunda şunu yap" türü) telefonunuzda kurulur. Ayrıntılar [Sahneler ve otomasyonlar](/help/mobile-automation) sayfasında.

![Cora Max'te sahne listesi, her akvaryum için bir filtre çipi ve Yeni Sahne düğmesiyle](img/max-automation.webp "Akvaryuma göre süzülmüş sahne listesi. Henüz sahne yoksa bunu söyler ve Yeni Sahne'yi önerir.")

## Sahneler nerede

**Ayarlar → Otomasyonlar**, tüm akvaryumlarınızın tüm sahnelerini listeleyen **Sahneler**'i açar. Birden fazla akvaryumunuz varsa her biri için bir filtre çipi ve ayrıca **Tüm akvaryumlar** çipi bulunur.

Düzenlemek için bir sahneye, yeni bir sahne oluşturmak için **Yeni Sahne**'ye dokunun. Birden fazla akvaryumunuz varsa ve hiçbir filtre seçili değilse Cora Max **Bu sahne hangi akvaryum için?** diye sorar.

## Sahne oluşturma

![Cora Max'te boş bir Yeni Sahne formu](img/max-scene-builder.webp "Yeni bir sahne: ad, Kalıcı ya da Süreli, Çalıştırmadan önce sor, ardından Adım Ekle.")

1. Bir **Sahne adı** yazın.
2. **Adım Ekle**'ye dokunun ve adımın ne yapacağını seçin. Yalnızca bu akvaryumda bulunan ekipman türlerini görürsünüz:
   - **Apex Prizi**: bir Neptune Apex prizini **AÇIK**, **KAPALI** ya da **OTOMATİK** konumuna alır.
   - **Bir Red Sea cihazını kontrol et**: örneğin **ReefDose: şimdi dozla**, **ReefDose: günlük dozu ayarla**, **ReefRun: pompa hızını ayarla**, **ATO: manuel dolum başlat** ya da **ReefMat: ruloyu ilerlet**.
   - **Bir Dalga Pompasını Kontrol Et**: bir Jecod pompasının akışını ya da dalga modunu ayarlar, açar ya da kapatır veya **Besleme için duraklat**.
   - **Gyre için besleme başlat**: besleme için bir Maxspect gyre'yi duraklatır. Kendiliğinden yeniden başlar.
   - **GHL**: besleme duraklatma, bakım, su değişimi, ışık sahnesi ve diğer kontrolcü komutları.
   - **HYDROS**: bir mod, bir çıkış seviyesi, bir doz ya da **HYDROS: programa geri dön**.
3. Başka adımları da aynı şekilde ekleyin. Sıralarını değiştirebilir ya da kaldırabilirsiniz. Bu ekranın düzenleyemediği bir adımda **Burada düzenlenemez** yazar. Onu telefonunuzda düzenleyin.
4. Ne kadar çalışacağını seçin. **Süreli**, **Süre (dakika)** alanına girdiğiniz dakika kadar çalışır. **Kalıcı**, siz durdurana kadar çalışır.
5. Sahnenin ikinci kez bakılması gereken hiçbir şeye dokunmadığından emin değilseniz **Çalıştırmadan önce sor**'u açık bırakın.
6. **Kaydet**'e dokunun.

:::note Sahnede dozaj
Bir Neptune DŌS kafası hiçbir zaman sahne adımı olamaz. **ReefDose: şimdi dozla** adımı olabilir ve kendi **Doz başına maksimum (ml)** alanı vardır. 10 mL için boş bırakın. Bu sınırın üstündeki bir doz reddedilir, asla küçültülmez. Dozaj yapan her sahnede **Çalıştırmadan önce sor**'u açık tutun.
:::

:::note Beta
**Beta.** Maxspect, GHL ve HYDROS Beta aşamasındadır ve yalnızca Beta kullanıcılarına açıktır. Beta kullanıcısı değilseniz bunları **Cihaz Ekle** içinde görmezsiniz. Beta erişimi istemek için [destek](/support.html) ile iletişime geçin.
:::

## Sahne çalıştırma

Sahneler panoda kutucuk olarak görünür. Birini başlatmak için **Çalıştır**'a dokunun.

Sahne çalışmadan önce soruyorsa Cora Max önce ne yapacağını her adım için bir satırda listeler. Okuyun, sonra çalıştırın ya da iptal edin.

Süreli bir sahne çalışırken kutucuğu bitişe kadar geri sayar ve erken bitirmek isterseniz **Durdur**'u gösterir. Kalıcı bir sahnenin kutucuğu, siz **Durdur**'a dokunana kadar onu çalışıyor olarak gösterir. Bir sahne bittiğinde ya da onu durdurduğunuzda, Cora ekipmanı eski haline getirirken kutucukta **Geri yükleniyor…** yazar.

Bir sahneyi çalıştırmak ya da durdurmak, diğer her komut gibi Cora Cloud üzerinden gider. Sonucu [Etkinlik](/help/max-activity) içinde bulursunuz.

Sahneler Cora Max'te sesle çalıştırılamaz. Kutucuğu, **Ayarlar → Otomasyonlar**'ı ya da telefonunuzu kullanın.

Bir sahne çalışmıyor ya da durmuyorsa [Sorun giderme](/help/troubleshooting) sayfasına göz atın.

:::note Çocuk kilidi sahneleri de kapsar
[Çocuk kilidi](/help/max-settings#child-lock) ekranı kilitlediğinde, diğer tüm kontroller gibi bir sahneyi de buradan çalıştıramaz, durduramaz ya da düzenleyemezsiniz.
:::

## Sahneyi düzenleme ya da silme

Bir sahneyi değiştirmek için onu **Ayarlar → Otomasyonlar**'dan açın ya da panodaki kutucuğuna uzun basın. Gerekeni değiştirin ve **Kaydet**'e dokunun. Kaldırmak için **Sahneyi Sil**'e dokunun. Bu geri alınamaz.

:::note Eski bir Cora Max sahneyi çalıştırabilir ama düzenleyemez
Eski Cora Max sürümleri her sahneyi göstermeye ve çalıştırmaya devam eder ama hiçbirini değiştiremez. Cora Max'i güncelleyin ([Güncellemeler ve kurtarma](/help/max-updates)) ya da sahneyi telefonunuzda düzenleyin.
:::
