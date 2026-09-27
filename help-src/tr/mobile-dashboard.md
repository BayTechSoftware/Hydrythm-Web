---
title: Panonuzu okuma
description: Cora'nın panosunu nasıl okumalı: widget'lar, tazelik, kaynaklar ve renklerin ne anlama geldiği.
section: Cora Mobile
reviewed: 2026-09-09
order: 5
group: Your dashboard
---

Pano, her biri bir akvaryum hakkında bir şey gösteren **widget'lardan** oluşan bir ızgaradır. Üzerinde ne olduğu tamamen size bağlıdır; bkz. **[Panonuzu düzenleme](/help/mobile-dashboard-editing)**.

![Bir Cora Mobile panosu](img/mobile-dashboard.webp "Bir ekranda göstergeler, sayılar, eğilimler ve kontroller.")

## Akvaryum başlığı

Her panonun üstünde:

- **Akvaryum adı**, yanında küçük bir simgeyle: bu sadece bir **hızlı yeniden adlandırmadır**, başka bir şey değil
- **Besle**: bir besleme için akışı ve skimmerlamayı duraklatır, ardından her şeyi geri koyar
- **Reef Buddy**: bu sabahın briefingini açar
- **Paylaş**: panonun bir görüntüsünü gönderir
- **Sağdaki kalem**: [akvaryum profilini](/help/mobile-tank-profile) açar

:::note Üç benzer kontrol, üç hedef
Adın yanındaki simge akvaryumu yeniden adlandırır. Sağdaki kalem akvaryum **profilini** açar. Panonun kendisini düzenlemek bunların hiçbiri değildir; bu, widget'ların *altında*, panonun *altındaki* **Gösterge panelini düzenle**'dir.
:::

Birden fazla akvaryumunuz varsa, aralarında geçmek için yana kaydırın.

## Reef Buddy kartı

Başlığın altında, bir kart en son briefingi özetler: bir başlık, **Kararlılık** ve **Veri** puanları, ve içgörü sayısı. Tam briefingi açmak için dokunun, veya **×** ile kapatın. Bir sonraki briefingle yeni bir kart görünür.

## Bir parametre widget'ı nasıl okunur

**Ölçülen bir parametreyi** gösteren bir widget, aynı üç şeyi aynı yerlerde taşır. Cihaz ve kontrol kutuları (bir priz, bir dozaj birimi, bir pompa) bunun yerine kendi durumlarını gösterir, çünkü arkalarında tek bir okuma yoktur.

**Değer**, okumanın kendisidir, büyük ve ortada.

**Yaş**, altında veya yanında oturur: `şimdi`, `1s`, `2g`. Bu, okumanın ne kadar önce alındığıdır, ekranın ne kadar önce yenilendiği değil. İki gündür değişmemiş bir sayı `2g` der, ve bu bir bilgidir.

**Kaynak rozeti**, yaşın yanındaki küçük işarettir. Sayının nereden geldiğini söyler: bir prob, bir kontrolcü, bir lab sonucu, veya bir test kitiyle siz. Kaynağın açıkça belirtildiğini ve son geçmişini görmek için herhangi bir widget'a dokunun.

:::note Yaş neden bu kadar önemli
Dört gün önceki mükemmel bir alkalinite okuması, geçerli bir alkalinite okuması değildir. Yaş, farkı bir bakışta anlayabilmeniz için her değerin yanında oturur.
:::

## Renkler

Cora rengi tutumlu kullanır ve her zaman aynı şeyi ifade eder:

| Renk | Anlamı |
|---|---|
| Yeşil | Bu parametre için aralığın rahatça içinde |
| Amber | Bir kenara yakın: **genellikle hâlâ aralığın içinde**, son onda biri içinde |
| Kırmızı | Kenarın ötesinde ve harekete geçmeye değer |
| Gri | Bir hüküm yok: yakın zamanda okuma yok, veya karşılaştırılacak kullanılabilir bir aralık yok |

:::note Amber genellikle "hâlâ iyi ama bir yere gidiyor" demektir
Amber bir *pay*dır, bir ihlal değil. Aralığının içinde ama son %10'unda olan bir okuma bilerek amberlenir; böylece kayma, bir sorun haline geldiği anda değil, hâlâ harekete geçecek zaman varken görünür olur.

Bundan iki ayrıntı çıkar.

**Kendinizin belirlediği bir aralık, beyan edilmiş bir sınır olarak ele alınır.** Onu geçin ve widget doğrudan kırmızıya döner: amber pay yoktur, çünkü o çizgiyi bilerek siz çizdiniz. **Cora'nın sağladığı** bir aralık daha yumuşak bir referanstır: onu geçmek, kenarın ötesindeki ilk %10 için amber gösterir ve bunun ötesinde kırmızıya döner.

**Tek taraflı bir sınır** (bir kirletici tavanı veya bir besin zemini) yalnızca üst kenarında derecelendirilir; böylece sıfırdaki bakır, ölçeğin dibine yakın olduğu için amberlenmek yerine yeşil okur.
:::

Amber veya kırmızıyla çevrelenmiş bir widget, ilgi gerektiren bir widget'tır. Çevre çizgisi sadece sayıda değil widget'ın kendisindedir, böylece kaydırırken görünür kalır.

## Widget'ların altında

![Panonun altı](img/mobile-dashboard-foot.webp "Gösterge panelini düzenle, Parametreleri Kaydet ve dört kayıt alanına kısayollar.")

Panonun altında:

- **Gösterge panelini düzenle**: [pano düzenleyicisini](/help/mobile-dashboard-editing) açar
- **Parametreleri Kaydet**: test kiti okumalarını elle girin
- **Günlük · Uyarılar · Bakım · Canlılar**: bu akvaryum için o alanlara kısayollar

Üstlerindeki bir satır, panonun son ne zaman güncellendiğini ve hangi kaynaklardan beslendiğini gösterir.

## Dokunarak açma

Ayrıntısını açmak için herhangi bir widget'a dokunun: tam geçmiş bir grafik olarak, onu bildiren her kaynak ve şu anda uygulanan eşikler. Oradan elle yeni bir okuma kaydedebilir, aralığı değiştirebilir veya daha geriye bakabilirsiniz.

## Bir widget'ta değer yoksa

Bir widget, bir değer aldığında onu gösterir. Boşsa, neden genellikle şunlardan biridir:

- Cihaz çevrimdışı; **Cihazlar** sekmesini kontrol edin
- Parametrenin henüz bir kaynağı yok; elle kaydedin, veya onu bildiren ekipman bağlayın
- Parametre hiç bildirilmedi veya kaydedilmedi; henüz onun için hiçbir şey kaydedilmedi

Grafik penceresi yaşından daha kısa olduğu için eski bir okuma kaybolmaz. Yaşı gösterilerek widget'ta kalır; böylece eski bir değer eksik gibi değil eski gibi okunur.

Bunların dışında herhangi bir şey için bkz. **[Sorun giderme](/help/troubleshooting)**.
