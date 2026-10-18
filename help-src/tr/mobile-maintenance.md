---
title: Bakım
description: Skimmer temizliği ya da filtre çorabı değişimi gibi tekrarlanan işler ekleyin, zamanı geldiğinde hatırlatma alın ve onları tamamlandı olarak işaretleyin ya da erteleyin.
section: Cora Mobile
reviewed: 2026-10-17
order: 28
group: Records
twin: max-records
---

Bakım, akvaryumunuzun düzenli olarak ihtiyaç duyduğu işleri her biri için bir hatırlatmayla birlikte tutar.

Panonun altındaki düğme satırında **Bakım**'a dokunun. Aynı ekran Ayarlar → akvaryumunuz → **Bakım** yolunda da var.

![Bakım listesi](img/mobile-maintenance.webp "Uyum oranı, gecikmiş görev sayısı ve her görevin son tamamlanma ve bir sonraki tarihi.")

## Özet {#summary}

En üstte **Bakım Uyumu** (şu anda zamanında olan görevlerin oranı) ve kaç görevin geciktiği yer alır.

Listedeki her görev gecikmiş, yakında ya da zamanlanmış olmasına göre renklenir. Ayrıca onu en son ne zaman yaptığınızı ve bir sonraki tarihini gösterir.

## Görev ekleme {#adding-a-task}

**Görev Ekle**'ye dokunun ve şunlardan birini seçin:

- **Şablondan**: aralığı doldurulmuş yaygın bir iş için. Seçin, sonra bir sonraki tarihini ve hatırlatılmak istediğiniz saati ayarlayın ve **Onayla**'ya dokunun.
- **Özel Görev**: kendi işiniz için. Bir **Görev adı**, bir **Aralık (gün)**, bir **Kategori** ve bir **Sonraki tarih** girin. Bildirim istiyorsanız **Hatırlatıcı**'yı açın ve **Bana şu saatte hatırlat**'ı seçin.

Şablonlardan bazıları ve başlangıç aralıkları:

| Görev | Aralık |
|---|---|
| Filtre çoraplarını değiştir | 3 gün |
| Skimmer kabını temizle | 7 gün |
| Su değişimi | 7 gün |
| Su parametrelerini test et | 7 gün |
| Karbonu değiştir | 30 gün |
| pH probunu kalibre et | 30 gün |
| Dalga pompalarını temizle | 90 gün |
| ICP sonuçlarını yükle | 90 gün |

Her görevin aralığını sonradan değiştirebilirsiniz.

### Cora'nın Red Sea ekipmanı için eklediği görevler {#red-sea-tasks}

Bir Red Sea ReefDose, ReefATO+, ReefMat ya da ReefRun bağladığınızda Cora, o ünitenin ihtiyaç duyduğu bakımı doğru aralıkla ekler:

| Cihaz | Görev | Aralık |
|---|---|---|
| ReefATO+ | ReefATO+ EC sensörünü değiştirin | 42 gün |
| ReefATO+ | ReefATO+ ana pompayı değiştirin | 135 gün |
| ReefMat | ReefMat karbonunu değiştirin | 25 gün |
| ReefRun | ReefRun skimmer venturisini kontrol edin | 35 gün |
| ReefRun | ReefRun skimmer rotorunu değiştirin | 135 gün |
| ReefRun | ReefRun tam kap sensörünü kalibre edin | 28 gün |
| ReefRun | ReefRun aşırı köpük sensörünü kalibre edin | 28 gün |
| ReefRun, pompa başına | ReefRun pompa motorunu bakımdan geçirin | 135 gün |
| ReefRun, pompa başına | ReefRun pompa süzgecini temizleyin | 42 gün |
| ReefDose, kafa başına | ReefDose kafasını kalibre edin | 90 gün |
| ReefDose, kafa başına | ReefDose kafasının hortumunu değiştirin | 450 gün |

Bunlar kendi eklediğiniz görevler gibi çalışır. Adlarını ve aralıklarını değiştirebilir, onları erteleyebilir ya da silebilirsiniz. Birini silerseniz Cora onu o cihaz için yeniden eklemez.

### Suyu test et {#test-water}

İlk test kartında **Her hafta test etmemi hatırlat**'a dokunursanız Cora, seçtiğiniz **Test günü**'nde zamanı gelen, **Suyu test et** adında haftalık bir görev ekler. Diğer görevler gibi çalışır. [Cora Mobile'ı kurma](/help/mobile-setup) sayfasına bakın. **Su parametrelerini test et** şablonuyla istediğiniz zaman bir test hatırlatıcısı da ekleyebilirsiniz.

### Bir otomasyondan {#from-an-automation}

**Bakım görevi oluştur** eylemi olan bir [otomasyon](/help/mobile-automation), kuralı tetiklendiğinde bu listeye bir iş ekleyebilir ya da var olan bir görevin zamanını şimdiye çekebilir. Yeni eklenen iş, zamanı şimdi olan bir **Tek seferlik görev**dir ve nedeniyle birlikte *Bir otomasyon oluşturdu* gösterir. Tamamladığınızda listeden çıkar. Açık kaldığı sürece aynı otomasyon bir tane daha eklemez. Tek bir bildirim alırsınız.

## Hatırlatmalar {#reminders}

Bir görevi açın, **Hatırlatıcı**'yı açın ve **Bana şu saatte hatırlat**'ı seçin. Zamanı gelmeden bir gün önce ve o gün birer bildirim alırsınız. Görev gecikmiş olduğu sürece birkaç günde bir hatırlatma alırsınız. Bir akvaryumda birkaç görevin zamanı aynı anda gelirse tek bir bildirim olarak gelirler.

Hatırlatmalar [Ayarlar → Bildirimler](/help/mobile-notifications) içinde **Bakım Hatırlatıcıları** altındadır. Bir görevi yalnızca listede görmek istiyorsanız **Hatırlatıcı**'sını kapatın.

## Görevi tamamlandı olarak işaretleme {#marking-done}

Görevi sağa kaydırın ya da açıp **Tamamla**'ya dokunun. Yanlışlıkla kaydırdıysanız çıkan mesajdaki **Geri al**'a dokunun.

Cora işi bitirdiğiniz zamanı kaydeder ve bir sonraki tarihi o andan sayar. Yani bir işi üç gün geç yaparsanız bir sonraki de üç gün ileri kayar. Görevin zamanı geçmişse Cora önce **Ne zaman yaptınız?** diye sorar. **Şimdi**'yi seçin ya da daha önce yaptıysanız **Tarih ve saat seç**'i seçin (aşağıya bakın).

Görevin sayfası, her birinin ne kadar geciktiği dahil **Tamamlama geçmişi**'ni gösterir.

:::note Bir görevi tamamlamak günlüğe de kayıt yazar
Cora sizin için [günlüğünüze](/help/mobile-journal) kısa bir kayıt ekler ve gecikmişse bunu da belirtir. Söyleyecek daha fazla şey varsa, örneğin pompa kumla doluysa ya da çoraplar bir günde simsiyah olduysa, kendi kaydınızı ekleyin.
:::

## Görevi daha önce yapıldı olarak işaretleme {#done-earlier}

İşi dün yaptınız ama işaretlemeyi unuttunuz mu? Görevi açın, **Daha önce yapıldı…**'ya dokunun, sonra tarihi ve saati seçin. Cora tamamlamayı, günlük kaydını ve bir sonraki tarihi o andan başlatır; yani bir sonraki tarih, seçtiğiniz zaman artı aralıktır.

En fazla bir yıl geriye gidebilirsiniz, ama görevi en son tamamladığınız zamandan öncesine gidemezsiniz. Henüz gelmemiş bir zamanı ya da son tamamlamadan önceki bir zamanı seçerseniz Cora bunu söyler ve hiçbir şey kaydetmez.

## Görevi düzenleme {#editing}

Açmak için bir göreve dokunun. **Görev adı**, **Aralık (gün)**, **Notlar (isteğe bağlı)**, **Sonraki tarih** ve hatırlatıcıyı değiştirip **Kaydet**'e dokunabilirsiniz. **Sil** görevi kaldırır.

## Erteleme {#snoozing}

Bir işi şu an yapamıyor musunuz? Açın, **Ertele**'ye dokunun ve **1 Gün**, **3 Gün**, **1 Hafta**, **2 Hafta** ya da **1 Ay**'ı seçin. Görev yeni tarihiyle **Ertelendi** olarak listede kalır ve o zamana kadar hatırlatma almazsınız.

:::warning Görevi yalnızca yaptığınızda tamamlandı olarak işaretleyin
Bir sonraki tarih, görevi yaptığınız andan sayılır. Bekleyen bir görevi tamamlandı olarak işaretlerseniz sonraki tüm tarihler kayar. Daha önce yaptıysanız **Daha önce yapıldı…**'yı kullanıp gerçek zamanı seçin. Yapmadıysanız onun yerine erteleyin.
:::

Bir görevi duraklatmanın yolu yoktur. Bu mevsim geçerli olmayan bir iş için onu **1 Ay** erteleyin ya da silip daha sonra yeniden ekleyin.
