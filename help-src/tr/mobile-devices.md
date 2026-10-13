---
title: Cihaz ekleme, düzenleme ve kaldırma
description: Cihazlar sekmesinden ekipmanı Cora'ya ekleyin, bir akvaryuma atayın, adını değiştirin, sağlıklı çalışıp çalışmadığını kontrol edin ve kaldırın.
section: Cora Mobile
reviewed: 2026-10-13
order: 11
group: Equipment
twin: max-devices
---

**Cihazlar** sekmesi, her ekipmanı eklediğiniz, atadığınız, adını değiştirdiğiniz, kontrol ettiğiniz ve kaldırdığınız yerdir. Cihazlar markaya göre gruplanır ve her grubu daraltabilirsiniz.

![Cihazlar sekmesi](img/mobile-devices.webp "Ekipman markaya göre gruplanır. Her grup daraltılabilir.")

## Ekipman ekleme {#adding-equipment}

1. **Cihazlar** sekmesinde **Cihaz Ekle**'ye dokunun.
2. Markayı seçin: **Cora**, **Neptune Apex**, **Red Sea**, **Jecod** ya da **AquaWiz**. Beta kullanıcıları ayrıca her birinde bir **Beta** çipiyle **Maxspect**, **GHL**, **HYDROS**, **Focustronic**, **EcoTech**, **Inkbird** ve **Kamera** görür.
3. Markanın adımlarını izleyin. Markaya göre bu bir ağ taraması, bir IP adresi, bir giriş ya da bir cihaz anahtarıdır. Her markanın adımları [Ekipmanınızı bağlama](/help/mobile-connections) sayfasında.
4. Ait olduğu akvaryumu seçin.

![Bir Beta kullanıcısı için Cihaz Ekle listesi](img/mobile-add-device-beta.webp "Beta markalarında bir Beta çipi bulunur.")

:::note Beta
**Beta.** Beta entegrasyonları yalnızca Beta kullanıcılarına açıktır. Beta kullanıcısı değilseniz bunları **Cihaz Ekle** içinde görmezsiniz. Beta erişimi istemek için [destek](/support.html) ile iletişime geçin. Ayrıntılar [Beta özellikleri](/help/mobile-beta) sayfasında.
:::

Akvaryumda bir Cora Max gerektiren bir satır (Maxspect, GHL, EcoTech, Inkbird ve Kamera), akvaryumda bir Cora Max olana kadar soluk görünür ve **Cora Max Gerektirir** yazar.

:::note Cora Max olmadan bazı ekipmanlar yalnızca yereldir
Neptune Apex, Red Sea ve Jecod ekipmanına ev ağınız ya da Bluetooth üzerinden ulaşılır. Cora Max yoksa ekleme ekranında *Bu entegrasyon, Cora Max olmadan yalnızca Mobile uygulamasında yerel olarak çalışır.* yazar. Telefonunuz onu yalnızca aynı ağdayken (ya da Bluetooth menzilindeyken) okur ve kontrol eder. Evden uzaktayken telefonunuzun kaydettiği son ölçümleri görürsünüz ve onu kontrol edemezsiniz. Akvaryumdaki bir Cora Max onu gece gündüz okur ve komutlarınızı iletir. Ayrıntılar [Ekipmanınızı bağlama](/help/mobile-connections#local-only) sayfasında.
:::

Ağınızdan ekipman eklerken telefonunuzun ekipmanla aynı ağda olması gerekir.

## Cora Max eşleştirme {#pairing-a-cora-max}

![Cora Mobile'da cihaz arayan Cora'nızı Ekleyin ekranı](img/mobile-add-device.webp "Cihaz Ekle, ardından Cora. Cora Mobile Wi-Fi'ınızda ve Bluetooth üzerinden arar, altta IP Adresini Elle Girin bulunur.")

Yeni bir Cora Max'i **Cora** ile eşleştirirsiniz. Wi-Fi'ınızda zaten bulunan üniteleri ya da yakındakileri Bluetooth üzerinden bulur. Sizinkini bulamazsa aynı ekrandaki **IP Adresini Elle Girin**'i kullanın. Adım adım anlatım [Cora Max'i kurma](/help/max-setup) sayfasında.

## Bir cihazın sayfası {#a-devices-page}

Sayfasını açmak için listedeki herhangi bir cihaza dokunun. Önce kontrolleri, ardından her markada aynı çalışan bölümler gelir.

- **Durum**, **Model**, **Seri no**, **Yazılım** bilgilerini ve Cora'nın ondan en son ne zaman haber aldığını (**Son görülme**) gösterir.
- **Akvaryumlar**, hangi akvaryuma (ya da akvaryumlara) atandığını gösterir. Yeniden atamak için **Değiştir**'e dokunun.
- **Bağlantı**, IP adresini, giriş bilgisini ya da cihaz anahtarını düzenlediğiniz yerdir.
- En altta **Cihazı kaldır**.

Cora Max, Neptune Apex ve GHL birden fazla akvaryuma hizmet edebilir, bu yüzden akvaryum seçicileri bir onay listesidir. Cora Max en fazla dört akvaryuma atanabilir. [Birden fazla Cora cihazı](/help/mobile-multi-device) sayfasına bakın. HYDROS dahil diğer her şey aynı anda tek bir akvaryuma hizmet eder. Farklı birini seçmek cihazı oraya taşır ve eskisinden çıkarır.

:::warning Ölçümlere güvenmeden önce akvaryumu atayın
Akvaryumu olmayan bir cihaz bildirmeye devam eder ama sayılarının gidecek yeri yoktur. Yeni eklediğiniz bir cihaz panoda görünmüyorsa önce bunu kontrol edin.
:::

Her markanın kontrollerinin ne yaptığı [Ekipmanınızı kontrol etme](/help/mobile-device-control) sayfasında.

## Adını değiştirme {#renaming}

Cihazı açın ve adının yanındaki kaleme dokunun. Gündelik hayatta ona ne diyorsanız onu kullanın, "Ana pompa", "Sol gyre" ya da "Sump ısıtıcısı" gibi. Ad widget'larda, uyarılarda ve Cora'ya sorduğunuz her şeyde görünür.

Adlar en fazla 40 karakter olabilir. Cihazın kendi adına dönmek için adı boş bırakın. Aynı türden iki cihazın adı yoksa Cora onları adın arkasındaki kısa bir kodla ayırt eder. Cora seri numarasını hiçbir zaman ad olarak kullanmaz.

Yeni ad yalnızca Cora'da geçerlidir. Üreticinin kendi uygulamasındaki adı değiştirmez.

## Bir cihazın sağlıklı olup olmadığını kontrol etme {#health}

Her cihaz Cihazlar sekmesinde simgesi, adı, modeli ve akvaryumuyla bir satırdır. Satırdaki nokta durumunu gösterir.

| Nokta | Anlamı |
|---|---|
| Gri | Cora henüz bilmiyor |
| Yeşil | Normal çalışıyor |
| Turuncu | Bir uyarı ya da arıza var |
| Kırmızı | Çevrimdışı |

Daha fazlası için cihazı açın. **Durum** bölümü Cora'nın ondan en son ne zaman haber aldığını gösterir. Görmek istediğiniz şey yakın bir saat ve hiç uyarı olmamasıdır.

| Gördüğünüz | Anlamı |
|---|---|
| Yakın bir güncelleme saati | Normal çalışıyor |
| Yalnızca birkaç saatte bir bildiren bir şeyde "3 sa önce güncellendi" | Sorun yok |
| "… ulaşılamadı" | Bir ağ sorunu var ya da cihaz kapalı |
| "… girişi reddetti" | Üretici hesabının yeniden bağlanması gerekiyor. Cihazı açın ve yeniden giriş yapın |
| "Cora Max bekleniyor" | Yeni eklediğiniz bir GHL kontrolcüsü ya da Inkbird monitörü: bir Cora Max onu okuduğunda görünür |
| Uzaktayken daha eski ölçümler | Akvaryumda Cora Max olmayan Apex, Red Sea ve Jecod için normal (yukarıya bakın) |
| Hiçbir şey | Hiç bildirmedi. Akvaryum atamasını ve bağlantıyı kontrol edin |

Bir cihaz bildirmeyi bıraktığında Cora sizi uyarabilir. Süreler [Uyarılar ve eşikler](/help/mobile-alerts) sayfasında. Diğer her şey için [Sorun giderme](/help/troubleshooting) sayfasına bakın.

## Bir cihazı kaldırma {#removing-a-device}

Cihazı açın ve **Cihazı kaldır**'a dokunun ya da Cihazlar sekmesinde satırını sola kaydırın. Cora onaylamanızı ister: *"{name} Cora'dan kaldırılacak. Cihazın kendisi sıfırlanmaz veya değiştirilmez."*

**Ölçümleriniz korunur.** Bir cihazı kaldırmak Cora'nın ondan yeni veri toplamasını durdurur. Daha önce topladığı geçmiş akvaryumda kalır ve onu kullanan her widget geçmiş ölçümlerini tutar.

Canlı bağlantıyı kaybedersiniz. Cihaz bir üretici hesabı üzerinden bağlandıysa kayıtlı giriş bilgisini de kaybedersiniz, bu yüzden onu yeniden eklerseniz tekrar giriş yapmanız gerekir.

:::tip Gürültülü bir cihazı kaldırmadan susturun
Bir cihaz iyi çalışıyor ama çok sık uyarı veriyorsa [Uyarılar ve eşikler](/help/mobile-alerts) içinde eşiklerini ya da bildirim ayarlarını değiştirin. Bağlantıyı ve veriyi korursunuz, gürültü de durur.
:::
