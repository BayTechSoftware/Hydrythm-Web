---
title: Produkty dozujące i kalkulator dawek
description: Sprawdź stężenie swoich produktów do alkaliczności, wapnia i magnezu, dodaj własne i użyj kalkulatora dawek, żeby policzyć, ile dodać.
section: Cora Mobile
reviewed: 2026-10-13
order: 27
group: Records
---

Cora policzy dawki tylko wtedy, gdy wie, jak mocne są Twoje produkty. Ta strona opisuje listę produktów i korzystający z niej kalkulator dawek.

Przejdź do **Ustawienia → Produkty dozujące**.

![Produkty dozujące](img/mobile-dosing.webp "Każdy produkt ma stężenie, z którego Cora liczy dawki i zużycie.")

## Biblioteka produktów {#the-product-library}

Ekran **Produkty dozujące** ma już na liście popularne produkty, pogrupowane w **Alkaliczność (dKH)**, **Wapń (ppm)** i **Magnez (ppm)**. Znajdź swój i dotknij go, żeby sprawdzić stężenie.

Każde stężenie mówi, o ile 1 ml (albo 1 g produktu sypkiego) podnosi parametr w określonej objętości wody. To ta liczba zamienia „5 ml” w „+0,2 dKH w Twoim akwarium”. Na górze przełączasz między **na 100 l** a **na 100 gal**.

Zmieniaj wbudowane stężenie tylko wtedy, gdy na Twojej butelce jest inna wartość. Dotknij produktu, żeby otworzyć **Dostosuj stężenie**. **Przywróć domyślne** przywraca wartość Cory.

## Własny produkt {#adding-your-own}

Jeśli Twojego produktu nie ma na liście, dotknij **+** (**Dodaj własny produkt**). Wpisz **Nazwę produktu**, wybierz **Płyn (ml)** albo **Suchy (g)** i podaj jego stężenie dla alkaliczności, wapnia albo magnezu. Zostaw pole puste, jeśli produkt nie zmienia danego parametru. Produkt dwuskładnikowy wypełnia po jednym polu w każdej części, a produkt zbilansowany kilka.

Stężenie jest prawie zawsze na etykiecie, na przykład „1 ml na 100 litrów podnosi alkaliczność o 0,1 dKH”.

:::warning Wpisz stężenie podane przez producenta
Jeśli stężenie jest złe, każda dawka, którą Cora policzy dla tego produktu, będzie błędna w tej samej proporcji. Jeśli nie możesz znaleźć tej liczby, nie dodawaj produktu. Nie zgaduj.
:::

Produkty do azotanów i fosforanów pochodzą z własnej listy Cory w kalkulatorze. Nie możesz dodać ich tutaj.

**Mieszanka soli** w Twoim akwarium nie jest produktem dozującym. Ustawiasz ją w profilu akwarium, a Cora ma katalog popularnych soli morskich z wartościami podanymi przez producentów, ze źródłami, z którego możesz wybierać. Zobacz [Profil akwarium](/help/mobile-tank-profile).

## Kalkulator dawek {#the-dose-calculator}

Kalkulator liczy, ile produktu trzeba, żeby podnieść parametr do wartości docelowej. Działa dla alkaliczności, wapnia, magnezu, azotanów i fosforanów.

1. Na panelu dotknij widżetu parametru, żeby go otworzyć.
2. Dotknij ikony kalkulatora na górze. Kropka na niej oznacza, że odczyt jest poniżej wartości docelowej.
3. Sprawdź liczby, które wpisała Cora:
   - Bieżąca to Twój ostatni odczyt. Zaktualizuj ją, jeśli właśnie robisz test.
   - Docelowa to środek zakresu alertu dla tego parametru albo typowy zakres rafowy, jeśli go nie ustawiono.
   - **Objętość netto wody (l)** to 90% objętości akwarium, z poprawką na skały i piasek. Zmień ją, jeśli znasz prawdziwą wartość.
4. Wybierz **Produkt**. Najpierw są Twoje produkty z profilu akwarium, potem gotowe ustawienia marek. Możesz też wpisać **Własne stężenie**.

Cora pokazuje całkowitą ilość potrzebną, żeby dojść do wartości docelowej.

:::warning Rozłóż dużą korektę w czasie
Kalkulator podaje całkowitą ilość, a nie dawkę dzienną. Jeśli całość to większy skok, niż jest bezpieczny w ciągu dnia, kalkulator o tym mówi, a Ty dzielisz to na kilka dni. **Zapytaj Cora** otwiera Cora Assistant z Twoimi liczbami, jeśli chcesz pomocy w zaplanowaniu ilości na dzień.
:::

Po podaniu dawki dotknij **Zapisz podaną dawkę**. Doda to wpis do [dziennika](/help/mobile-journal).

Jeśli już jesteś na poziomie docelowym albo powyżej, kalkulator powie, że nie ma czego dodawać. Parametru nie da się obniżyć dozowaniem. Pomoże podmiana wody, wymiana mediów albo zmiana tego, co już dozujesz.

Objętość ma tu znaczenie. Jeśli różni się o 20%, dawki też będą o 20% nietrafione.

## Zużycie {#consumption}

Gdy Cora widzi i dawki, i odczyty, potrafi policzyć, co zużywa Twoje akwarium, i dać znać, gdy to się zmienia.

Gdy zmienia się zapotrzebowanie, przyjrzyj się temu, zanim wyciągniesz wniosek. Rosnące zapotrzebowanie na alkaliczność często oznacza wzrost, ale nagła zmiana w którąkolwiek stronę może też wynikać z pominiętej dawki, błędu testu, wytrącania, podmiany wody albo zmiany sprzętu. Sprawdź, co jeszcze zmieniło się w okolicach tej daty.

## Sprzęt dozujący {#dosing-equipment}

Jeśli masz podłączony dozownik, na przykład Neptune DŌS albo Red Sea ReefDose, jego głowice pojawiają się z własnymi odczytami, w tym z tym, ile zostało w każdej głowicy i co dozowała. Jak je uruchamiać i uzupełniać, opisuje [Sterowanie sprzętem](/help/mobile-device-control), a ich alerty o niskim poziomie w pojemniku i pominiętej dawce są w [Alertach dozownika](/help/mobile-device-control#doser-alerts).

Automatyzacja też może dozować z głowicy DŌS, z limitem 10 mL na głowicę dziennie. Zobacz [Automatyzacje i sceny](/help/mobile-automation#actions).
