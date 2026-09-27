---
title: Problembehebung
description: Messwerte sind ausgeblieben, ein Gerät ist offline gegangen, Warnungen verschwinden nicht, oder etwas sieht falsch aus. Hier anfangen.
section: Help
reviewed: 2026-09-27
order: 1
---

Beginne mit dem Symptom.

## Ein Widget zeigt keinen Wert

Geh diese Liste durch:

1. **Prüfe das Alter benachbarter Widgets.** Wenn alles veraltet ist, liegt das Problem an der Verbindung, nicht am Wasserwert.
2. **Öffne den Tab Geräte.** Ein nicht erreichbares Gerät sagt das in seiner Zeile.
3. **Prüfe die Beckenzuweisung.** Ein Gerät, das an das falsche Becken meldet, sieht genauso aus wie eines, das nicht meldet. Öffne das Gerät und bestätige sein Becken.
4. **Prüfe, ob die Quelle existiert.** Nichts meldet Phosphat, sofern du keine Ausrüstung hast, die es misst, oder du es von Hand protokollierst.

## Ein Messwert ist veraltet

Das Alters-Abzeichen sagt dir die Wahrheit: nichts Neues ist eingetroffen.

- **Von Hand protokollierte Wasserwerte** veralten, wenn kein Messwert eingetragen wurde. Protokolliere einen.
- **Ausrüstungsmesswerte, die veralten**, bedeutet, dass das Gerät aufgehört hat zu melden; prüfe seine Zeile unter **Geräte**.
- **Manche Ausrüstung soll langsam sein.** Ein Titrator, der stündlich misst, zeigt normalerweise `1h`. Das ist kein Fehler.

## Ein Gerät ist nicht erreichbar

Meist das Netzwerk.

1. Ist die Ausrüstung eingeschaltet und funktioniert sie in ihrer eigenen App?
2. Ist sie im selben Netzwerk, in dem sie hinzugefügt wurde?
3. Hat sich dein Router geändert (neue Hardware, neuer Netzwerkname, Gastnetzwerk-Isolierung)?

Ausrüstung, die sich über dein lokales Netzwerk verbindet, muss in diesem Netzwerk erreichbar sein. Ausrüstung, die sich über ein Herstellerkonto verbindet, muss das nicht, braucht aber dieses Konto weiterhin gültig.

## Ein Gerät sagt, die Anmeldung wurde abgelehnt

Der Hersteller hat die gespeicherte Anmeldung abgelehnt. Fast immer, weil du dein Passwort bei ihm geändert hast.

Öffne die Gerätezeile und melde dich erneut an.

## Ein Cora Max zu koppeln schlägt fehl

Wenn das Hinzufügen eines Cora Max mitten im Vorgang stoppt, sagt Cora Mobile, welcher Schritt fehlgeschlagen ist und warum, mit **Abbrechen** und **Erneut versuchen** darunter.

- *"Dein Handy konnte das Cora Max in deinem WLAN nicht erreichen."* Bring dein Handy und das Cora Max ins selbe WLAN-Netzwerk. Auf dem iPhone prüfe außerdem, dass Cora Zugriff auf das lokale Netzwerk hat: **Einstellungen → Gerätezugriff** bringt dich dorthin (siehe [Einstellungen](/help/mobile-settings)). Tippe dann auf **Erneut versuchen**.
- *"Das Cora Max hat diese Kopplungssitzung nicht angenommen."* Erneut zu versuchen hilft nicht. Schließe den Bildschirm und beginne erneut über **Geräte → Gerät hinzufügen**.

Für jede andere Meldung, tippe auf **Erneut versuchen**.

## Cora Max zeigt alte Daten

Prüfe die Status-Pille in der oberen Leiste. **Online** und **Cloud** sind beide gesund: Bei mehr als einem Cora zeigt der Bildschirm, der nicht sammelt, **Cloud**, und seine Messwerte sind genauso aktuell. **Veraltet** oder **Offline** bedeutet, dass der Bildschirm seine Quelle verloren hat und die letzten erhaltenen Daten zeigt (korrektes Verhalten, aber nicht aktuell).

- Prüfe WLAN unter **Einstellungen → Cora Max → Netzwerk**
- Prüfe, ob das Netzwerk selbst läuft
- Wenn die Pille **Online** oder **Cloud** liest und die Daten trotzdem alt sind, liegt das Problem vorgelagert: Prüfe dasselbe Becken auf deinem Handy

## Eine Warnung verschwindet nicht

Eine Warnung verschwindet, wenn der Messwert wieder in den Bereich zurückkehrt. Wenn sie nicht verschwindet:

- **Der Messwert ist wirklich außerhalb des Bereichs.** Sieh dir die Historie des Widgets an.
- **Der Schwellenwert passt nicht zu deinem Becken.** Siehe [Warnungen und Schwellenwerte](/help/mobile-alerts).
- **Die Quelle ist falsch.** Eine Sonde, die kalibriert werden muss, meldet eine Zahl, die wirklich außerhalb des Bereichs liegt. Behebe die Sonde, nicht den Schwellenwert.

## Zwei Quellen widersprechen sich

Das ist Cora, das funktioniert, nicht Cora, das versagt. Wenn sich deine Sonde und dein Testkit widersprechen, ist das eine echte Tatsache über dein System.

Ein ICP-Ergebnis ist hier eine nützliche dritte Meinung, entscheidet den Streit aber nicht: Laboratorien unterscheiden sich voneinander, und die Handhabung und der Transport einer Probe verändern das Ergebnis. Zwei übereinstimmende Tests sind weit mehr wert als einer.

Meist muss die Sonde kalibriert werden; manchmal ist das Testkit alt. Kalibriere die Sonde, führe den Test mit frischem Reagenz erneut durch, und vergleiche beide unter denselben Bedingungen. Ein [ICP-Ergebnis](/help/mobile-icp-health) fügt diesem Vergleich einen dritten Datenpunkt hinzu.

## Ich bekomme keine Benachrichtigungen

1. **Einstellungen → Benachrichtigungen**: prüfe, ob diese Kategorie senden darf
2. Prüfe die eigenen Benachrichtigungsberechtigungen deines Handys für Cora
3. Denk daran, dass die tägliche Zusammenfassung an Tagen, an denen sich nichts geändert hat, bewusst still ist

## Herausfinden, warum sich etwas geändert hat

**Einstellungen → Aktivität** listet jede Steckdosenschaltung, Fütterung, Dosierung und Steckdosenänderung, mit dem, was danach gefragt hat: Cora Mobile, ein Cora-Bildschirm, Sprache, der Assistent, eine Automationsregel, eine Smart-Taste, oder dein Konto.

## Mein Dashboard sieht nach dem Bearbeiten falsch aus

Lade ein gespeichertes Design: **Meine Dashboards**, dann eines auswählen.

Wenn du noch keines gespeichert hast, bau das Layout neu auf und speichere es dann als Design. Von diesem Zeitpunkt an ist die Rückkehr dazu ein einziger Tipp.

In jedem Fall werden Messwerte, Historie und Tagebucheinträge getrennt vom Layout gespeichert, daher geht nichts hinter dem Dashboard verloren.

## "Red Sea-Messwerte haben aufgehört, sich zu aktualisieren"

**Was es bedeutet:** Kein Gerät im Netzwerk dieses Beckens fragt derzeit deine Red Sea-Ausrüstung ab, daher wurden die Messwerte auf dem Bildschirm nicht aktualisiert.

**Was zu tun ist:**
1. Öffne **Einstellungen → Primäres Cora Max** und prüfe, ob ein Cora Max festgelegt ist (oder **Jedes aktive (automatisch)** gewählt ist).
2. Öffne das Becken auf einem Gerät, das im selben WLAN wie die Red Sea-Ausrüstung ist.
3. Bestätige, dass die Red Sea-Ausrüstung eingeschaltet und online in ihrer eigenen App ist.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** mit dem Becken- und Gerätenamen.

## "Die Pumpe konnte nicht erreicht werden: nichts wurde gesendet"

**Was es bedeutet:** Ein Befehl an eine Jecod- oder Jebao-Pumpe hat die App nie verlassen, meist weil die Pumpe aus ist oder nicht im Netzwerk ist.

**Was zu tun ist:**
1. Prüfe, ob die Pumpe eingeschaltet ist.
2. Prüfe, ob sie im selben Netzwerk ist, in dem sie hinzugefügt wurde.
3. Tippe auf **Erneut versuchen**.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** mit dem Becken- und Gerätenamen.

## "Konnte diese Pumpe nicht über Bluetooth erreichen. Steh in ihrer Nähe und versuch es erneut."

**Was es bedeutet:** Ein reines Bluetooth-Jecod-Gerät ist außer Reichweite deines Handys.

**Was zu tun ist:**
1. Geh näher an die Pumpe heran.
2. Tippe auf **Erneut versuchen**.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** mit dem Becken- und Gerätenamen.

## "Konnte diese Gyre nicht erreichen. Keine Fütterung wurde gestartet."

**Was es bedeutet:** Eine Maxspect-Gyre (Beta-Integration) hat nicht geantwortet, als Cora versuchte, den Fütterungsmodus darauf zu starten.

**Was zu tun ist:**
1. Prüfe, ob die Gyre eingeschaltet und im Netzwerk ist.
2. Tippe auf **Erneut versuchen**.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** mit dem Becken- und Gerätenamen.

## "Konnte diese Gyre nicht erreichen. Ihr Programm wurde nicht geändert."

**Was es bedeutet:** Ein Zeitplan, der an eine Maxspect-Gyre (Beta-Integration) gesendet wurde, hat sie nicht erreicht.

**Was zu tun ist:**
1. Prüfe, ob dein Handy oder Cora Max im Netzwerk der Gyre ist.
2. Tippe auf **Erneut versuchen** vom Zeitplan-Bildschirm aus.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** mit dem Becken- und Gerätenamen.

## "Konnte den Apex nicht erreichen: nichts geändert" / "nichts dosiert"

**Was es bedeutet:** Ein Neptune Apex, Trident, oder DŌS-Kopf hat nicht auf einen Befehl oder eine Dosieranfrage geantwortet.

**Was zu tun ist:**
1. Öffne die eigene App des Apex und bestätige, dass er online ist.
2. Prüfe die Netzwerkverbindung auf dem Gerät, das du nutzt.
3. Tippe auf **Erneut versuchen**.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** mit dem Becken- und Gerätenamen.

## "Das konnte nicht gesendet werden: kein Gerät an diesem Becken kann es senden"

**Was es bedeutet:** Kein Cora-Gerät an diesem Becken hat die Apex-Verbindungsdaten, die nötig sind, um den Befehl auszuführen, oder das Gerät, das sie hat, ist offline.

**Was zu tun ist:**
1. Füge die Apex-Details unter **Einstellungen** auf einem Gerät hinzu, das derzeit online ist, oder
2. Lege ein anderes, funktionierendes Cora Max als **Primäres Cora Max** für dieses Becken fest.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** mit dem Becken- und Gerätenamen.

## Ein sekundäres Cora Max zeigt "Haupt-Cora offline"

**Was es bedeutet:** Das primäre Tablet für dieses Becken ist offline gegangen, daher zeigt dieser sekundäre Bildschirm die letzten erhaltenen Daten statt Live-Daten.

**Was zu tun ist:**
1. Prüfe Strom und WLAN des primären Tablets.
2. Warte, bis es sich wieder verbindet, oder ändere das **Primäre Cora Max** auf ein Gerät, das derzeit online ist.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** mit dem Becken- und Gerätenamen.

## "Gerät ist offline. Zeigt letzten bekannten Zustand."

**Was es bedeutet:** Normale Offline-Behandlung: Das Gerät hat aufgehört zu melden, und Cora zeigt die letzten Werte, die es hatte, statt vorzugeben, dass sie aktuell sind.

**Was zu tun ist:**
1. Prüfe die eigene Netzwerkverbindung des Geräts.
2. Behandle die gezeigten Werte als nicht live, bis die Zeile nicht mehr offline sagt.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** mit dem Becken- und Gerätenamen.

## Manche ReefBeat-Einstellungen sind ausgegraut oder fehlen

**Was es bedeutet:** Das ist so gestaltet, kein Fehler. Geräteeigene Einstellungen (im Gegensatz zu Messwerten) öffnen sich nur, wenn dein Handy im selben Netzwerk wie das Gerät selbst ist; fern von diesem Netzwerk zeigen sich nur Messwerte.

**Was zu tun ist:**
1. Besuch das eigene WLAN des Beckens, um diese Einstellungen zu ändern.
2. Messwerte und Historie funktionieren fern vom Becken weiterhin normal.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## "Konnte Cora nicht erreichen. Prüfe dein WLAN oder deine Mobildaten, und versuch es erneut."

**Was es bedeutet:** Dein Handy hat bei der Anmeldung keine nutzbare Verbindung zu Cora Cloud. Das betrifft die eigene Konnektivität deines Handys, nicht deine Beckenausrüstung.

**Was zu tun ist:**
1. Prüfe, ob dein Handy eine funktionierende WLAN- oder Mobildatenverbindung hat.
2. Versuch ein anderes Netzwerk, falls eines verfügbar ist.
3. **Erneut versuchen**.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Auf einmal ist alles in der falschen Sprache

**Was es bedeutet:** Die Kontosprache wurde von einem beliebigen Gerät aus geändert. Sprache ist eine Einstellung für das ganze Konto, nicht pro Gerät.

**Was zu tun ist:**
1. Öffne **Einstellungen → Sprache** in einer der beiden Apps.
2. Stell sie zurück, falls sie versehentlich geändert wurde; die Änderung gilt überall gleichzeitig.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Eine alte Warnung oder ein alter Bericht ist nach dem Wechsel noch in einer anderen Sprache

**Was es bedeutet:** Das ist erwartet, kein Fehler. Cora übersetzt bereits erstellte Inhalte nicht neu; nur neue Warnungen, Berichte und Zusammenfassungen folgen der neuen Sprache.

**Was zu tun ist:**
1. Nichts zu beheben. Warte auf neue Inhalte, die die aktuelle Sprache verwenden.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Eine Warnung hört nicht auf zu benachrichtigen, auch nachdem ich sie bestätigt habe

**Was es bedeutet:** Verwechslung zwischen **Verwerfen** (schließt die Warnung endgültig) und **Schlummern** (schaltet sie vorübergehend stumm, bis zu einer Woche).

**Was zu tun ist:**
1. Wenn du den Zustand verstehst und akzeptierst, nutze **Verwerfen**.
2. Wenn du nur für eine Weile Ruhe willst, nutze **Schlummern** und wähle eine Dauer.

**Funktioniert es immer noch nicht?** Siehe [Warnungen und Schwellenwerte](/help/mobile-alerts), oder schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Eine Dosierung stoppte mitten in der Ausführung, und eine "Wiederherstellungs"-Warnung erschien

**Was es bedeutet:** Der DŌS-Kopf hat mitten in der Dosierung den Kontakt verloren, daher sagt Cora dir das absichtlich, statt anzunehmen, dass die volle Dosis abgegeben wurde.

**Was zu tun ist:**
1. Öffne die Warnung und prüfe, wie viel tatsächlich dosiert wurde, bevor sie stoppte.
2. Setze fort oder passe die Dosierung basierend auf dieser Menge an, nicht der ursprünglich geplanten.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** mit dem Becken- und Gerätenamen.

## Eine auf dem Handy erstellte Szene erscheint auf Cora Max nicht als bearbeitbar

**Was es bedeutet:** Szenen direkt auf dem Tablet zu bearbeiten ist eine neuere Cora Max-Fähigkeit. Ältere Firmware kann trotzdem auf dem Handy erstellte Szenen ausführen, sie dort nur nicht bearbeiten.

**Was zu tun ist:**
1. Aktualisiere Cora Max, oder
2. Bearbeite diese Szene weiterhin vom Handy aus; sie läuft in jedem Fall trotzdem auf dem Tablet.

**Funktioniert es immer noch nicht?** Siehe [Updates und Wiederherstellung](/help/max-updates), oder schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant antwortet zum falschen Becken

**Was es bedeutet:** Vor dem Fragen wurde kein Becken gewählt, oder das falsche Becken ist derzeit aktiv.

**Was zu tun ist:**
1. Wähle zuerst das Becken, das du meinst.
2. Frag erneut.

**Funktioniert es immer noch nicht?** Siehe [Der Assistent](/help/mobile-assistant), oder schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant weigert sich zu antworten, oder zeigt erneut einen Zustimmungsbildschirm

**Was es bedeutet:** "Cora Assistant erlauben, gespeicherte Beckendaten zu nutzen" wurde ausgeschaltet, daher hat er nichts, wovon aus er antworten kann.

**Was zu tun ist:**
1. Tippe auf **Zustimmen und fortfahren** auf dem Zustimmungsbildschirm, um es wieder einzuschalten.

**Funktioniert es immer noch nicht?** Siehe [Der Assistent](/help/mobile-assistant), oder schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Ein Labor- oder per E-Mail gesendetes ICP-Ergebnis ist nie erschienen

**Was es bedeutet:** Ein Ergebnis in Cora zu bekommen braucht ein dafür gewähltes Becken, und manchmal einen erkannten Absender, bevor es irgendwo angehängt wird.

**Was zu tun ist:**
1. Prüfe den Einführungshinweis, der beim ersten Senden eines Ergebnisses an Cora angezeigt wird.
2. Bestätige, zu welchem Becken das Ergebnis gehören soll, wenn du gefragt wirst.
3. Stell sicher, dass die E-Mail von derselben Adresse gesendet wurde, mit der du zuvor gesendet hast, falls du schon einmal eine gesendet hast.

**Funktioniert es immer noch nicht?** Siehe [ICP und Zustandsberichte](/help/mobile-icp-health), oder schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Eine per E-Mail gesendete ICP-Benachrichtigung nennt kein Labor

**Was es bedeutet:** Ein bekanntes Problem, bei dem der Name des Labors in der Push-Benachrichtigung "Becken wählen" fehlt. Es wurde in aktuellen Builds behoben.

**Was zu tun ist:**
1. Stell sicher, dass Cora Mobile auf die neueste Version aktualisiert ist.
2. Das Ergebnis selbst ist nicht betroffen; nur im Benachrichtigungstext fehlte ein Name.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Ein Widget zeigt die falschen Einheiten

**Was es bedeutet:** Das ist die Anzeigeeinheiten-Einstellung des Beckens, kein Datenproblem. Werte werden unabhängig davon, wie sie angezeigt werden, gleich gespeichert.

**Was zu tun ist:**
1. Öffne **Einstellungen** für dieses Becken und prüfe seine Anzeigeeinheiten.
2. Ändere sie dort; jedes Handy und Cora Max, das dieses Becken zeigt, aktualisiert sich entsprechend.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Eine Anzeige oder ein Schwellenwert sieht nach dem Ändern der Anzeigeeinheiten anders aus

**Was es bedeutet:** Erwartet. Anzeigen, Kacheln und Historie zeichnen sich in der von dir gewählten Einheit neu; die zugrunde liegenden Werte haben sich nicht geändert.

**Was zu tun ist:**
1. Nichts zu beheben; das ist nur kosmetisch.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Max verbindet sich nach einem WLAN-Ausfall nicht sofort neu

**Was es bedeutet:** Nach dem Verbindungsverlust wartet Cora Max vor jedem erneuten Versuch etwas länger, statt das Netzwerk zu bombardieren, und dehnt das auf etwa eine Minute aus, bevor es erneut versucht.

**Was zu tun ist:**
1. Warte etwa eine Minute, nachdem dein Netzwerk zurück ist.
2. Wenn es sich danach immer noch nicht neu verbunden hat, prüfe WLAN unter **Einstellungen → Netzwerk**.

**Funktioniert es immer noch nicht?** Siehe [Der Cora Max Startbildschirm](/help/max-tour), oder schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Ein Cora Max auf dem Handy umzubenennen ändert nicht, was das Tablet zeigt

**Was es bedeutet:** Der Name, den du vom Handy aus festlegst, ist eine Bezeichnung auf Kontoebene für dieses Gerät. Der auf dem Tablet selbst während der Kopplung gezeigte Name kann etwas anderes sein.

**Was zu tun ist:**
1. Prüfe, welchen "Namen" du gerade betrachtest: den in deiner Geräteliste auf dem Handy, oder den auf dem eigenen Kopplungsbildschirm des Tablets.
2. Benenne über die Geräteliste des Handys um, wenn es die Kontobezeichnung ist, die du ändern willst.

**Funktioniert es immer noch nicht?** Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** mit dem Gerätenamen.

## Ich finde nicht, wo ich das Wake-Word auf Cora Max ausschalte

**Was es bedeutet:** Der Wake-Word-Schalter liegt unter **Ton**, nicht unter der Einstellungsgruppe Cora Assistant, was die meisten überrascht.

**Was zu tun ist:**
1. Geh zu **Einstellungen → Ton → Weckwort-Erkennung**.
2. Schalte es aus; du kannst weiterhin auf das Cora-Symbol tippen, um eine Sprachsitzung zu starten.

**Funktioniert es immer noch nicht?** Siehe [Einstellungen auf Cora Max](/help/max-settings), oder schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Die Kindersicherung lässt niemanden in die Einstellungen

**Was es bedeutet:** Das funktioniert wie beabsichtigt. Die Kindersicherung sperrt den Touchscreen und die Sprachsteuerung nach einer festgelegten Zeit ohne Berührung; Messwerte aktualisieren sich darunter weiterhin.

**Was zu tun ist:**
1. Drücke **Lauter** oder **Leiser** dreimal innerhalb von zwei Sekunden, oder
2. Halte fünf Finger zehn Sekunden lang in die obere rechte Ecke des Bildschirms.

**Funktioniert es immer noch nicht?** Siehe [Sprache auf Cora Max](/help/max-voice), oder schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Immer noch nicht weiter

Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**. Sag uns, welches Becken, welcher Bildschirm, und was du erwartet hast zu sehen; das bringt dir schneller eine nützliche Antwort.
