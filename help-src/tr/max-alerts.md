---
title: Cora Max'te uyarılar
description: Cora Max'te bir uyarı çıktığında ne yapacağınız, onu nasıl erteleyeceğiniz ya da kapatacağınız, uyarı eşiklerini duvardaki ekrandan değiştirme ve uyarı sesini ayarlama.
section: Cora Max
reviewed: 2026-10-13
order: 8
group: Alerts and automation
twin: mobile-alerts
---

Bu sayfa, bir şey dikkatinizi gerektirdiğinde Cora Max'in ne yaptığını ve duvardaki ekranda neleri değiştirebileceğinizi anlatır. Aralıkların, kuralların ve telefon bildirimlerinin nasıl çalıştığı [Uyarılar ve eşikler](/help/mobile-alerts) sayfasında.

## Bir uyarı çıktığında

Bir ölçüm aralık dışına çıktığında, bir cihaz arıza bildirdiğinde, bir doz kaçırıldığında ya da bir sarf malzemesi azaldığında Cora Max uyarıyı ekranın ortasında gösterir. Altında üç düğme vardır.

1. **Sesle yanıtla**, bu uyarı hakkında Cora ile bir konuşma başlatır, böylece başka hiçbir şeye dokunmanız gerekmez. Ayrıntılar [Cora ile konuşma](/help/max-voice) sayfasında.
2. **Ertele**, uyarıyı bu Cora Max'te bir süreliğine susturur. Düğme ne kadar süre olduğunu gösterir, örneğin **1 sa ertele**. Bu, Cora Mobile'ın uyarı ayarlarında bu uyarı için belirlenen bekleme süresidir ve 1 haftaya kadar uzun olabilir (günlerce değişmeyecek düşük bir reaktif seviyesi gibi durumlarda işe yarar).
3. **Kapat**, uyarıyı hemen kapatır. Sorun geçene kadar bu ekranda sessiz kalır. Daha sonra geri gelirse yeni bir uyarı alırsınız.

Uyarı bir dozaj pompasıyla ilgiliyse, örneğin bir DŌS ya da ReefDose kafası azaldıysa ya da bir doz kaçırıldıysa, kartta ayrıca bir **DŌS aç** ya da **ReefDose aç** düğmesi bulunur. Sizi uyarılarının ayarlandığı o dozaj pompasının sayfasına götürür.


Ertele ya da Kapat bir hata gösterirse bir kez daha deneyin. Başarısız olmaya devam ederse [Bir uyarı kapanmıyor](/help/troubleshooting#an-alert-is-not-clearing) bölümüne bakın.

:::note Ertele yalnızca bu Cora Max'i etkiler
Bir uyarı ertelenmiş ya da kapatılmışken bu Cora Max onu açmayı, ses çıkarmayı ve sesli okumayı bırakır, uyarı üst çubuktan da çıkar. Telefonunuz bildirimlerini almaya devam eder, diğer Cora Max ekranları uyarıyı göstermeye devam eder, uyarı **Bildirim geçmişi**'nde kalır ve uyarı ayarlarınız değişmez.
:::

## Üst çubuktaki uyarılar

Her etkin uyarı üst çubukta odanın öbür ucundan fark edilecek büyüklükte küçük bir etiket olarak da görünür. Sığandan fazlası varsa **+2** (ya da kaç tane varsa) görürsünüz.

- O uyarıyı yeniden ekranın ortasına getirmek için bir etikete dokunun.
- Etkin olan her şeyin listesi **Etkin alarmlar**'ı açmak için **+2**'ye dokunun. Açmak için listede birine dokunun.

## Bildirim gelen kutusu

**Ayarlar → Cora Max Ayarları → Bildirim geçmişi**, tüm hesabınızın gelen kutusudur. Sisteminizin her özetini, alarmını ve hesap bildirimini tutar. Bu ekranın vermedikleri ve telefonunuzun kaçırdıkları da buna dahildir. Bir ölçüm aralık dışına çıkıp geri döndüğünde ikisini de görürsünüz.

## Eşikleri düzenleme {#editing-thresholds}

![Cora Max'te bir akvaryumun ayarları: Uyarı eşikleri, Birimler ve Birincil Cora Max](img/max-tank-settings.webp "Önce Uyarı eşikleri ve Birimler, ardından bu akvaryumun Birincil Cora Max'i.")

Üst çubukta akvaryum adına dokunun ve **Uyarı eşikleri**'ni seçin ya da **Ayarlar → [akvaryumunuz] → Uyarı eşikleri** yoluna gidin. İkisi de telefonunuzda gördüğünüz aralıkların aynısını açar ve burada yaptığınız bir değişiklik her yerde geçerli olur.

Bir eşiği panodaki widget'ına uzun basarak ya da sesle de değiştirebilirsiniz: *"Hey Cora, pH uyarısını 7.9 ile 8.4 arasına ayarla."* Cora değişikliği söyler ve onayınızı bekler.

Listedeki her parametrenin kendi anahtarı vardır. Kapattığınız bir uyarıda **Uyarı kapalı** yazar. Cora aralığını saklar ama uyarı kapalıyken o ölçümü değerlendirmez. Widget nötr gri kalır ve hiç uyarı vermez. Bir parametrenin henüz uyarısı yoksa **Uyarı ayarlanmadı** yazar ve **Uyarı ekle**, gösterilen aralıkla bir uyarı kurar.

![Cora Max'te Uyarı eşikleri listesi](img/max-alerts.webp "Her ölçümün kendi anahtarı var. Uyarısı olmayan bir ölçüm Uyarı ayarlanmadı ve bir Uyarı ekle düğmesi gösterir.")

Eşik sayfasının üstünde, **Uyarı açık** ya da **Uyarı kapalı** yazısının yanında aynı anahtar vardır. Kapalı bir uyarıya yeni bir aralık kaydederseniz Cora **Bu uyarı açılsın mı?** diye sorar. Uyarıyı yeni değerlerle açmak için **Aç**'a, değerleri kaydedip uyarıyı kapalı bırakmak için **Kapalı kalsın**'a dokunun.

## Cihaz ve sarf malzemesi uyarıları {#doser-alerts}

Bir şeyi tükenen ekipmanın Cora Max'teki sayfasında bir **Uyarı ayarları** düğmesi bulunur. Bunlar şunlardır: Trident (reaktifler ve atık), DŌS kafaları, Red Sea ReefDose, ReefATO+ ve ReefMat. Haber almak istediğiniz seviyeyi seçin, seviye aşıldığında tek bir bildirim alırsınız. Bir DŌS kafasında **Kaçırılan dozaj uyarıları**, kafa zamanlanmış dozlarını kaçırdığında da size haber verir.

Her dozaj pompası uyarısının ne anlama geldiği [Dozaj pompası uyarıları](/help/mobile-device-control#doser-alerts) bölümünde.


## Uyarı sesi, sesli uyarılar ve ekranı uyandırma

Bunlar yalnızca bu ekrana aittir. Onları **Ayarlar → Cora Max Ayarları** içinde bulun.

- **Uyarı sesi** (**SES VE KONUŞMA** altında), yeni bir uyarı geldiğinde bir ses çalar. Kaydırıcısı ses seviyesini ayarlar.
- **Sesli uyarılar** (**SES VE KONUŞMA** altında), Cora'nın uyarıyı yüksek sesle söylemesini sağlar.
- **Alarmda ekranı uyandır** (**EKRAN** altında), bir uyarı geldiğinde kararmış ekranı aydınlatır. Kritik uyarılar ekranı her zaman uyandırır.

Bir Cora Max'in uyarıları ekranında hiç göstermemesi için Cora Mobile'ı açın, **Cihazlar →** Cora Max'iniz yoluna gidin ve **Uyarılar**'ı kapatın. Bildirim geçmişi ve telefonunuzun bildirimleri değişmez.

:::note Tüm hesap için tek uyarı
Her cihaz bir uyarının kendi kopyasını vermez. Cora Max, telefonunuz ve diğer ekranlar aynı uyarıyı gösterir ve ölçüm aralığa döndüğünde uyarı hepsinde kapanır.
:::
