---
title: Parametre Eşlemesi
description: Her ölçümü hangi probun beslediğini her kontrol cihazında görün, kalibrasyon ve temizliği kaydedin.
section: Cora Mobile
reviewed: 2026-10-12
order: 13
group: Equipment
---

Birden fazla kontrol cihazınız varsa, ya da aynı şeyi ölçen iki probunuz varsa, Cora hangi ölçüme güveneceğini bilmek zorundadır. **Parametre Eşlemesi** bunu ayarladığınız, ve her probun ne olduğunu Cora'ya ilk kez söylediğiniz yerdir.

**Ayarlar**'a gidin, akvaryumu açın ve **Parametre Eşlemesi**'ni seçin. **Akvaryumu düzenle** ile **Uyarı eşikleri** arasında yer alır. Panonun üstündeki kalem **Akvaryumu düzenle**'yi açar ve onda yoktur. Ona Neptune Apex ve GHL (Beta) cihaz sayfalarından da ulaşabilirsiniz. GHL yalnızca Beta kullanıcılarına açıktır. Bkz. [Beta özellikleri](/help/mobile-beta).

Ekranda bir arama alanı (**Parametre ara**) ve iki sekme var: **Eşleme** ve **Kaynaklar**. Arama parametre adlarına, prob adlarına, cihazlara ve markalara bakar. Aynı arama alanı her parametre seçicisinde bulunur.

## Her ölçüm nereden geliyor

Bu, **Kaynaklar** sekmesidir.

![Her ölçüm nereden geliyor](img/mobile-probes.webp "Her parametre, onu besleyen prob ve değiştirmek için bir Seç düğmesi.")

Bu bölüm, bu akvaryum için Cora'nın izlediği pH ya da sıcaklık gibi her parametreyi listeler ve şu anda hangi probun onu beslediğini gösterir.

Bir ölçüme dokunduğunuzda, bağladığınız her kontrol cihazında onu bildiren bütün probları görürsünüz. Her biri markasını, kontrol cihazındaki kendi adını ve canlı değerini gösterir. Birini seçerek sabitleyin, ya da Cora'nın raporlayan hangi probu kullanacağına kendisinin karar vermesi için **Otomatik (en yeni ölçüm kazanır)** seçeneğini seçin.

Her ölçümün yanındaki etiket hangisinin geçerli olduğunu gösterir: **Otomatik**, ya da bir prob sabitlediyseniz **Siz seçtiniz**.

Sabitlediğiniz prob bildirim göndermeyi bırakırsa Cora en son ne zaman haber aldığını gösterir ve **Otomatiğe dön** seçeneğini sunar. Böylece ölü bir prob ölçümü kilitli bırakamaz.

Bir ölçüme kendi görünen adını vermek için **Yeniden adlandır**'a dokunun. Bu, probun kendisine verdiğiniz addan ayrıdır. Panonuzda, uyarılarda ve Reef Buddy'de görünen bu addır.

:::note Bir sızıntı sensörü burada yeniden atanamaz
Sızıntı sensörünün alarmı kendi adına bağlıdır, bu yüzden bu seçiciden hariç tutulur. Her zamanki gibi çalışmaya devam eder.
:::

## Problar: her birinin ne olduğunu Cora'ya söyleme

**Eşleme** sekmesi ilk açılır. Cora'nın bildiği her probu, onu bildiren cihaza göre gruplanmış ve güncel ölçümüyle birlikte görürsünüz. Cora standart prob adlarını kendisi tanır ve her satırda neyle eşleştirdiğini gösterir. Genellikle Cora'nın tanıyamadığı birkaçını düzeltmeniz yeterlidir.

Her satırda üç seçenek var:

- **Cora parametresi**: probun ölçtüğü değer.
- **Özel**: Cora'da standart karşılığı olmayan problar için. Proba büyük harfle kısa bir kod verirsiniz, Cora onu bu adla takip eder.
- **Yok say**: hiç kaydedilmesini istemediğiniz problar için.

Yok sayılan ya da eşlenmemiş prob panoda görünmez ve uyarı üretmez.

Eşlemeler bir sonraki ölçüm kaydından itibaren geçerli olur. Burada yaptığınız düzeltme geçmişi değiştirmez, yalnızca bundan sonra kaydedilenleri etkiler. Uygulamak için **Kaydet**'e dokunun.

:::warning Cora eşlenmemiş probu görmez
Prob çalıştığı hâlde bir parametrede hiç ölçüm görünmüyorsa ilk iş onun eşlemesini kontrol edin.
:::

## Aynı parametre için birden fazla prob

İki sıcaklık probunuz varsa, ister aynı kontrol cihazında ister iki ayrı cihazda olsunlar, ikisini de eşleyin. Cora bunları ayrı kaynaklar olarak tutar, ve **Kaynaklar** sekmesi hangisinin ölçümü besleyeceğini seçtiğiniz ya da Otomatik bıraktığınız yerdir. İkisini [parametre ekranında](/help/mobile-metric-detail) karşılaştırabilirsiniz.

İki kaynak aynı parametreyi bildirdiğinde en yeni ölçüm kazanır. Ekrandaki bir değerin yerini, hangi cihazdan gelirse gelsin yalnızca daha geç bir ölçüm zamanına sahip bir ölçüm alır. Daha eski bir ölçüm ya da eski bir ölçümü yeniden gönderen bir cihaz geçmişe girer ve güncel değerin üzerine yazmaz. Bir kaynağı sabitlediyseniz Cora onun yerine o kaynağı izler.

## Prob bakımını kaydetme

Problar zamanla kayar. Cora her probun en son ne zaman kalibre edildiğini ya da temizlendiğini takip eder. Böylece gerçek bir değişimi, bakıma ihtiyacı olan bir probdan ayırt edebilirsiniz.

Kalibrasyonu ya da temizliği probun kaydından girin. Bunu düzenli bir [bakım görevi](/help/mobile-maintenance) olarak da ekleyebilirsiniz.

:::note Kalibrasyon geçmişi farkları açıklar
Probla test kiti farklı sonuç veriyorsa önce probun en son ne zaman kalibre edildiğine bakın.
:::
