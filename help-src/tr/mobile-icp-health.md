---
title: ICP ve sağlık raporları
description: ICP testinizi yükleyin, her elementi zaman içinde izleyin ve sisteminizin kapsamlı sağlık değerlendirmesini alın.
section: Cora Mobile
reviewed: 2026-10-12
order: 26
group: Intelligence
---

Laboratuvar sonuçlarınız ve uzun vadeli takibiniz **Zeka** sekmesinde.

![Zeka sekmesi](img/mobile-intelligence.webp "ICP yükleyin, sağlık raporu alın ve son rapordan bu yana nelerin değiştiğini görün.")

## ICP testi yükleme

**ICP Yükle**'ye dokunun, akvaryumunuzu seçin ve laboratuvardan gelen sonucu ekleyin. Cora raporu okur, her elementi kaydeder ve önceki testlerinizle yan yana koyar.

Elle hiçbir şey yazmanız gerekmez. Cora yaygın laboratuvar formatlarını tanır.

## Bir laboratuvar hangi e-postayı kullanabilir

Bir laboratuvar ya da e-postayla gelen bir sonuç, hesabınızı bildiği e-posta adresiyle bulur. Bu, giriş e-postanız ile **Ayarlar → hesap kartınız → Laboratuvar ve ICP e-postaları** altından eklediğiniz laboratuvar e-postalarıdır.

1. **Laboratuvar e-postası ekle**'ye dokunun ve laboratuvarınızın kullandığı adresi yazın.
2. **Kodu gönder**'e dokunun. Cora o adrese 6 haneli bir kod gönderir. Kod 10 dakika içinde sona erer.
3. Kodu girin ve **Doğrula**'ya dokunun. Gelmediyse **Kodu yeniden gönder**'e dokunun.

En fazla 3 laboratuvar e-postası ekleyebilirsiniz. Her biri **Doğrulandı** ya da **Kod bekleniyor** gösterir ve **Kaldır** birini çıkarır. Bundan sonra o adrese gönderilen sonuçlar hesabınıza ulaşmaz. Başka bir Cora hesabına ait bir adres eklenemez.

Gizli bir Apple e-postasıyla giriş yaptıysanız laboratuvarlar hesabınızı bulamaz. ICP ekranında bu ayara götüren **Laboratuvar sonuçlarını otomatik alın** kartı görünür. Apple ile giriş yaparken bu sorunu yaşamamak için **E-postamı Paylaş**'ı seçin.

## Cora'ya gönderim: laboratuvarın ya da e-postanın sizin yerinize ilettiği sonuçlar

Bazı laboratuvarlar sonucu doğrudan Cora'ya gönderebilir. E-postayla gelen ICP sonuçları da aynı yoldan iletilebilir. Sizin hiçbir şey yüklemenize gerek kalmaz.

Sonuç geldiğinde bir bildirim şeridi çıkar: *"{lab} laboratuvarından bir sonuç sizi bekliyor."* **Tank seç**'e dokunun ve sonucun hangi akvaryumunuza ait olduğunu seçin. Cora bunu kendisi tahmin edemez. Seçiminizden sonra Cora sonucu, yüklediğiniz bir rapor gibi o akvaryuma ekler.

Raporun başlığının yakınında **{lab} tarafından gönderildi** yazar. Böylece kendi yüklediğiniz raporlardan ayırt edersiniz.

:::note İlk sefer
Bu yoldan ilk sonuç geldiğinde Cora neler olduğunu anlatan kısa ipucu gösterir. Böylece durum bir hata gibi görünmez.
:::

### Yeni bir laboratuvardan gelen ilk sonuç

Bir laboratuvar size ilk kez sonuç gönderdiğinde Cora, tek akvaryumunuz olsa bile, sonucu herhangi bir yere eklemeden önce onayınızı ister. Sonucu kimin gönderdiğini görürsünüz ve bir sonraki sefer bu kontrolü atlamak için **Bu laboratuvara güven** kutusunu işaretleyebilirsiniz.

Sonucu içeri almak için **Onayla**'ya, hiçbir akvaryuma eklemeden silmek için **Reddet**'e dokunun. **Ayarlar → Güvenilen laboratuvarlar** bu şekilde güvendiğiniz her laboratuvarı listeler. **Geri al** bir laboratuvarı listeden çıkarır, böylece sonraki sonucu için yeniden onayınız gerekir.

İşe yaramıyorsa [Sorun giderme](/help/troubleshooting) sayfasına bakın.

![ICP raporu](img/mobile-icp-report.webp "Her raporda puan ve akvaryumunuza göre yazılmış özet bulunur.")

## Raporda neler var

**100 üzerinden bir puan** ve bunun sizin sisteminiz için ne anlama geldiğini anlatan sade özet. Özet akvaryumunuzun türüne, yaşına ve canlılarına göre yazılır.

Puan, sonuçlarınızın hedef aralıklarına göre hesaplanır. Kendi belirlediğiniz aralıklar da hesaba katılır. Aralığın dışında tek bir sonuç bile varsa, diğerleri ne kadar iyi olursa olsun puan en fazla 70 olur, yani **Sağlıklı** görünemez. Aralığın çok dışında bir sonuç varsa puan en fazla 40 olur. Puanın altındaki etiket 71 ile 100 arasında **Sağlıklı**, 40 ile 70 arasında (ikisi de dahil) **Dikkat Gerekiyor**, 0 ile 39 arasında **Kritik** olur. Sağlık Raporları da aynı şekilde puanlanır.

**Takip edilen bütün elementler**: yalnızca ana parametreler değil, eser elementler ve kirleticiler de. Cora, bir laboratuvarın bildirebileceği 71 elementin hepsini kaydeder ve bazı laboratuvarların *Acidity* dediği satır pH'tır.

Her element satırında laboratuvarın yazdığı aralığı *Laboratuvar aralığı* olarak, Cora'nın o element için kendi aralığının yanında görürsünüz. Cora'nın referans aralığı olmayan bir elementte **Cora aralığı yok** etiketi bulunur. Rapor kaç elementin Cora aralığı olduğunu söyler, kalanları genel resif bilgisine göre değerlendirir. Cora Assistant test edilen her element hakkında yorum yapar ve Cora aralığı olmasa bile yorumu geçerlidir.

Laboratuvar bir element için *t.y.* (tespit edilmedi) yazarsa Cora onu 0 olarak kaydeder ve tespit edilmediğini söyler.

:::note Çözünmüş CO₂ oda CO2'si değildir
Bir ICP raporundaki **Çözünmüş CO₂**, sudaki CO2'dir ve mg/L cinsindendir. Odanızın havasındaki CO2'den farklı bir ölçümdür, onu Beta aşamasındaki Inkbird oda havası monitörü ölçer. İkisinin aralıkları farklıdır ve asla karıştırılmaz. Bkz. [Beta özellikleri](/help/mobile-beta).
:::

**En çok değişenler**: "Son ICP'nizden bu yana" kartı, önceki testten bu yana en çok neyin değiştiğini gösterir. Yeni bir raporu anlamanın genellikle en hızlı yolu budur.

**Eğilimler**: bir elementin yüklediğiniz bütün testlerdeki seyrini görmek için **Eğilimler**'e dokunun. ICP tek seferlik fotoğraf olmaktan burada çıkar ve asıl işe yaramaya başlar.

:::tip Asıl bilgi ikinci testle gelir
Tek bir ICP size nerede olduğunuzu söyler. İkincisi hangi yöne gittiğinizi gösterir ve harekete geçmek için asıl bu bilgi gerekir. Yalnızca bir sorun çıktığında değil, düzenli aralıklarla test ettirin.
:::

## RO/DI ya da kaynak su testi

RO/DI ya da başka bir kaynak su numunesi yüklüyorsanız bunu yüklerken belirtin. Cora onu akvaryumunuzun hedeflerine göre puanlamaz. Suyun kullanılacak kadar temiz olup olmadığı konusunda sade bir karar verir ve bu değerleri akvaryum ölçümlerinizin dışında tutar. Rapor, kaç sonucun kaynak su olduğunu not eder. Cora aynısını yeni karıştırılmış bir tuz karışımı ya da akvaryum suyu olmayan başka bir numune için de yapar: numunenin neye benzediğini söyler ve onu akvaryumunuzmuş gibi puanlamaz.

## Sağlık raporları

**Sağlık Raporu**, tüm sistemi belli aralıklarla daha derinlemesine değerlendirir. Her parametre, her kaynak, dozajınız, geçmişiniz ve son ICP sonuçlarınız birlikte ele alınır.

**Sağlık Raporu**'na dokunun ve bir akvaryum seçin. Raporun hazırlanması biraz sürer.

Günlük özetten daha kapsamlı bir değerlendirme istediğinizde kullanın: büyük bir değişiklikten önce, bir sorundan sonra ya da birkaç haftada bir genel kontrol için.

## ICP ve problarınız

Cora laboratuvar sonuçlarınızı ekipmanınızın ölçümleriyle karşılaştırır. Alkalinite probunuz 8,4, ICP sonucunuz 7,6 diyorsa bunu bilmeniz gerekir. Cora da birini sessizce seçmek yerine farkı size gösterir.

ICP'nin Cora'daki en yararlı işlerinden biri budur. ICP **üçüncü bir görüştür, son sözü söylemez**. Laboratuvarlar birbirinden farklı sonuç verebilir. Numunenin nasıl alındığı, saklandığı ve taşındığı da sonucu değiştirir. Tek ICP'yi kanıt olarak görün. Birbiriyle uyuşan iki test, tek testten çok daha değerlidir. Sürekli fark görüyorsanız bunu probun hatalı olduğunun kanıtı olarak değil, probu kontrol etmek için neden olarak görün.

:::tip Laboratuvar ya da test yöntemi değiştirirken
Laboratuvar değiştirmek ya da aynı laboratuvarda ICP-OES ile ICP-MS arasında geçiş yapmak, akvaryumunuzda hiçbir şey değişmeden sonuçlarınızı değiştirebilir. Cora karşılaştırma yaparken bunu belirtir. ICP-OES çok düşük seviyelerdeki krom, kalay, nikel, bakır, kobalt ve selenyumu ölçemez. Bu yüzden ICP-OES testinde bu elementler için **Tespit sınırının altında** sonucu, akvaryumunuzda hiç olmadıkları anlamına gelmez.
:::

## Kullanım hakkınız

İki özellik de planınıza göre sınırlıdır. Düğmelerin altındaki satır bu ay ne kadar kullandığınızı gösterir.

Planınızdan bağımsız olarak Cora günde en fazla 10 ICP yüklemesi kabul eder. Bu sınır yüzünden reddedilen bir yükleme planınızdaki ICP analiz hakkından düşmez. Ancak Cora Mobile bu durumda yalnızca genel bir yükleme hatası gösterir. Aynı gün çok sayıda yüklemeden sonra yüklemeler başarısız olmaya başlarsa ertesi gün tekrar deneyin.

## Raporlar nerede durur

Zeka ekranı iki rapor türünü ayrı tutar. Laboratuvar sonuçları **ICP Raporları** altında, Cora'nın hazırladığı değerlendirmeler **Sağlık Raporları** altında listelenir. İki liste de en yeniden eskiye sıralanır ve her raporun puanı görünür. Raporun tamamını yeniden açmak için üzerine dokunun.
