---
title: Güncellemeler ve kurtarma
description: Cora Max kendini nasıl günceller, yükleme penceresi ve güncelleme kanalı, sürümü kontrol etme, Kurtarma PIN'i ve Cora Max açılmazsa ne yapılacağı.
section: Cora Max
reviewed: 2026-10-17
order: 15
group: Settings and account
---

Cora Max kendini güncel tutar. Bu sayfa güncellemelerin ne zaman yüklendiğini, sürümünüzü nasıl kontrol edeceğinizi ve Cora Max normal açılmazsa onu nasıl yeniden çalıştıracağınızı anlatır.

## Otomatik güncellemeler

Yeni sürümler çıkar çıkmaz arka planda iner. Siz değiştirmedikçe sabah 3 ile 5 arasındaki **Yükleme penceresi** içinde yüklenirler, böylece siz ekrana bakarken yeniden başlamaz. Bir sürüm sürüm notlarıyla geliyorsa Cora Max onları gösterir.

Güncel kalmak için bir şey yapmanız gerekmez.

## Sürümü ve güncelleme ayarlarını kontrol etme {#checking-the-version-and-update-settings}

![Cora Max'te ağ ve güncellemeler](img/max-updates.webp "Yazılım Güncellemesi, Cora Max Ayarları'nın AĞ VE GÜNCELLEMELER bölümünde.")

Sürümünüz **Ayarlar → Cora Max Ayarları** ekranının en üstündeki kartta (*Cora Max · yazılım 0.28.x*) ve **YARDIM VE HAKKINDA → Hakkında** altında yazar.

**Ayarlar → Cora Max Ayarları → Yazılım Güncellemesi** (**AĞ VE GÜNCELLEMELER** içinde), kullandığınız sürümü ve bekleyen bir güncelleme olup olmadığını gösterir. Hemen bakmak için **Güncellemeleri kontrol et**'e, bir güncelleme varsa **İndir ve yükle**'ye dokunun.

Aynı ekranda **Güncelleme ayarları** altında:

- **Yükleme penceresi**, güncellemelerin yüklenebileceği saatleri bu ekranın yerel saatine göre bir **Başlangıç** ve **Bitiş** saatiyle belirler. Saat dilimi Cora Mobile'da **Cihazlar →** Cora Max'iniz **→ Saat dilimi** altında ayarlanır.

Bu ekranın cihazlarınızı okuyup okumadığını ve Cora Cloud'a kaydedip kaydetmediğini görmek için **Cora Max Ayarları**'na dönün ve **DURUM**'a kaydırın. Her akvaryum için **Yoklama durumu**, **Son yoklama**, **Son bulut yazımı** ve **Bulut kaydı** gösterilir.

Bir güncelleme yavaş iniyorsa aynı ekrandaki **Ağ hız testi** ile bağlantınızı kontrol edin. **Testi başlat**, güncelleme dosyasının en fazla 16 MB'ını Cora Cloud'dan en çok 20 saniye boyunca indirir ve hızı MB/s olarak gösterir.

## Bir güncelleme olduğunda

Bir pencere yenilikleri anlatır ve size iki seçenek sunar.

- **Şimdi güncelle** hemen yükler ve yeniden başlatır. Yaklaşık bir dakika sürer. Cora Max'in güç bağlantısını kesmeyin.
- **24 saat ertele** pencereyi gizler ve bir gün sonra yeniden sorar.

Bir güncelleme beklerken üst çubuktaki **Ayarlar** simgesinde ve **Yazılım Güncellemesi** satırında küçük bir nokta görünür. Nokta ertelemeden sonra da kalır, böylece bir güncelleme olduğunu yine görebilirsiniz. Güncelleme yüklenirken kaybolur.

Hiçbir şey yapmazsanız güncelleme **Yükleme penceresi** içinde kendiliğinden yüklenir.

Güncellemeyi telefonunuzdan da başlatabilirsiniz: Cora Mobile'da **Cihazlar →** Cora Max'iniz yolunu açın ve **v… sürümüne güncelle**'ye dokunun.

:::note Güncelleme sırasında ölçüm kaybetmezsiniz
Verileriniz hesabınızda saklanır. Cora Max yeniden başladığında aynı akvaryumlar, panolar ve geçmişle geri gelir.
:::

## Kurtarma {#recovery}

Kurtarma, Cora Max normal açılmadığında ya da kurulumunu dizüstü bilgisayar olmadan düzeltmeniz gerektiğinde kullanılan bir bakım modudur.

1. Ekranın sağ üst köşesinde **beş parmağınızı** **on saniye** basılı tutun.
2. **Kurtarma PIN'i** kutusu açılır. 6 haneli PIN'i yazın ve **Gir**'e dokunun.

PIN'i Cora Max'i eşleştirdiğinizde görmüştünüz. Onu Cora Mobile'da **Cihazlar →** Cora Max'iniz **→ Kurtarma PIN'i** altında da bulursunuz. Cora Max'in kendisi onu hiçbir zaman göstermez, böylece bir misafir ya da ekrana yaslanan bir çocuk kurtarmaya giremez.

PIN'i üç kez yanlış yazarsanız kurtarma 30 saniye, sonraki her yanlış denemede daha uzun süre kilitlenir. **Çok fazla deneme yapıldı** ne kadar beklemeniz gerektiğini söyler. Cora Max eşleştirmeden beri hiç çevrimiçi olmadıysa henüz bir PIN'i yoktur ve **Kurtarma kullanılamıyor** gösterir. Önce onu Wi-Fi'ye bağlayın.

**Kurtarma** ekranından şunları yapabilirsiniz:

- **Wi-Fi kurulumunu yeniden yap**: yeni bir Wi-Fi ağı ve şifre seçin
- **Bu cihazı yeniden eşleştir**: eşleştirmeyi temizleyin ve Cora Mobile ile yeniden kurun
- **OTA kontrolünü zorla**: güncellemeleri hemen kontrol edin
- **Fabrika ayarlarına sıfırla**: eşleştirmeyi ve ekrandaki her ayarı kaldırın

Cora Cloud'a zaten kaydedilmiş akvaryum verileri her durumda korunur.

Cora Max üst üste birkaç kez açılamazsa kendini önceki sürüme de geri alabilir.

:::note Aynı hareket çocuk kilidini de açar
[Çocuk kilidi](/help/max-settings#child-lock) açıksa köşede beş parmağınızı basılı tutmak ekranın kilidini de açar. Yalnızca kilidi açmak istediyseniz **Kurtarma PIN'i** kutusunda **İptal**'e dokunun.
:::

:::warning Kurtarma modundaki ekran hiçbir şeyi kontrol etmez
Kontrolörünüz kendi programını çalıştırmaya devam eder. Ama **bu Cora Max**'in yürütmesi gereken bir [otomasyon](/help/mobile-automation) adımı, Cora Max kurtarma modundayken çalışamaz. Kural tetiklenir ama adım ekipmana hiç ulaşmaz.
:::

## Cora Max "Cora Max hit a problem" gösterirse

Bu ekran (İngilizce olarak görünür), Cora Max açılırken ya da çalışırken bir şeyin ters gittiği anlamına gelir. Bir **Support code** (destek kodu) gösterir. Kod *CXB-* ile başlar.

1. Destek kodunu not edin.
2. Bekleyin. Cora Max yaklaşık 10 dakika içinde kendini yeniden başlatır. Hemen yeniden başlatmak için sağ üst köşede beş parmağınızı 10 saniye basılı tutun.
3. Bu tekrar ederse destek koduyla birlikte **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-posta gönderin.

## Bir ünite yeniden başlamazsa

Ekranda görünen sürümü ve gösterdiği mesajı **[cora@coraiq.tech](mailto:cora@coraiq.tech)** adresine e-postayla gönderin. Önce yeniden eşleştirmeyin. Eşleştirme durumu, ne olduğunu anlamamıza çoğu zaman yardım eder.
