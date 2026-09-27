---
title: Problembehebung
description: Keine neuen Messwerte, ein Gerät offline, eine Warnung, die nicht verschwindet, oder etwas sieht falsch aus. Fang hier an.
section: Help
reviewed: 2026-09-27
order: 1
---

Such dir das Symptom heraus, das zu deinem Problem passt.

## Ein Widget zeigt keinen Wert

Geh diese Punkte der Reihe nach durch:

1. **Schau dir das Alter der Widgets daneben an.** Ist alles veraltet, liegt es an der Verbindung und nicht am Wasserwert.
2. **Öffne den Tab Geräte.** Ist ein Gerät nicht erreichbar, steht das in seiner Zeile.
3. **Prüf, zu welchem Becken das Gerät gehört.** Ein Gerät, das an das falsche Becken meldet, sieht genauso aus wie eines, das gar nicht meldet. Öffne das Gerät und prüf sein Becken.
4. **Prüf, ob es überhaupt eine Quelle gibt.** Phosphat erscheint nur, wenn ein Gerät es misst oder du es von Hand einträgst.

## Ein Messwert ist veraltet

Die Altersanzeige stimmt. Es ist einfach nichts Neues angekommen.

- **Von Hand eingetragene Wasserwerte** veralten, wenn du keinen neuen Wert einträgst. Trag einen ein.
- **Veraltet ein Messwert von einem Gerät**, meldet das Gerät nicht mehr. Prüf seine Zeile unter **Geräte**.
- **Manche Geräte messen von sich aus selten.** Ein Titrator, der einmal pro Stunde misst, zeigt normalerweise `1h`. Das ist kein Fehler.

## Ein Gerät ist nicht erreichbar

Meist liegt es am Netzwerk.

1. Ist das Gerät eingeschaltet, und funktioniert es in seiner eigenen App?
2. Ist es noch im selben Netzwerk wie beim Hinzufügen?
3. Hat sich an deinem Router etwas geändert, etwa neue Hardware, ein neuer Netzwerkname oder ein abgeschottetes Gastnetz?

Geräte, die sich über dein lokales Netzwerk verbinden, müssen in diesem Netzwerk erreichbar sein. Geräte, die sich über ein Herstellerkonto verbinden, brauchen das nicht. Dafür muss das Konto weiter gültig sein.

## Ein Gerät meldet, dass die Anmeldung abgelehnt wurde

Der Hersteller hat die gespeicherten Anmeldedaten abgelehnt. Fast immer liegt es daran, dass du dort dein Passwort geändert hast.

Öffne die Zeile des Geräts und melde dich neu an.

## Das Koppeln eines Cora Max klappt nicht

Bleibt das Hinzufügen eines Cora Max mittendrin stehen, zeigt Cora Mobile, welcher Schritt gescheitert ist und warum. Darunter stehen **Abbrechen** und **Erneut versuchen**.

- *„Dein Handy konnte das Cora Max in deinem WLAN nicht erreichen.“* Verbinde Handy und Cora Max mit demselben WLAN. Auf dem iPhone prüf außerdem, ob Cora auf das lokale Netzwerk zugreifen darf. Über **Einstellungen → Gerätezugriff** kommst du dorthin (mehr dazu unter [Einstellungen](/help/mobile-settings)). Tippe dann auf **Erneut versuchen**.
- *„Das Cora Max hat diese Kopplungssitzung nicht angenommen.“* Ein neuer Versuch hilft hier nicht. Schließ den Bildschirm und fang über **Geräte → Gerät hinzufügen** von vorne an.

Bei jeder anderen Meldung tippe auf **Erneut versuchen**.

## Cora Max zeigt alte Daten

Schau auf den Status-Chip in der oberen Leiste. **Online** und **Cloud** heißen beide, dass alles in Ordnung ist. Hast du mehrere Cora, zeigt der Bildschirm, der nicht selbst sammelt, **Cloud**, und seine Werte sind genauso aktuell. **Veraltet** oder **Offline** heißt, dass der Bildschirm seine Quelle verloren hat. Er zeigt dann die letzten Daten, die er bekommen hat. Das ist richtig so, aber sie sind eben nicht aktuell.

- Prüf das WLAN unter **Einstellungen → Cora Max-Einstellungen → Wi-Fi**.
- Prüf, ob das Netzwerk selbst läuft.
- Steht im Chip **Online** oder **Cloud** und die Daten sind trotzdem alt, liegt das Problem vor Cora Max. Schau dir dasselbe Becken auf deinem Handy an.

## Eine Warnung verschwindet nicht

Eine Warnung verschwindet, sobald der Messwert wieder im Bereich ist. Bleibt sie trotzdem, kann das drei Gründe haben:

- **Der Messwert liegt wirklich außerhalb des Bereichs.** Schau dir den Verlauf im Widget an.
- **Der Schwellenwert passt nicht zu deinem Becken.** Mehr dazu unter [Warnungen und Schwellenwerte](/help/mobile-alerts).
- **Die Quelle liefert falsche Werte.** Eine Sonde, die kalibriert werden muss, meldet eine Zahl, die tatsächlich außerhalb des Bereichs liegt. Bring die Sonde in Ordnung und lass den Schwellenwert, wie er ist.

## Zwei Quellen widersprechen sich

Dann macht Cora genau das, was es soll. Widersprechen sich Sonde und Testkit, erfährst du damit etwas Echtes über dein System.

Ein ICP-Ergebnis ist hier eine nützliche dritte Meinung, entscheidet den Streit aber nicht. Labore messen unterschiedlich, und wie die Probe behandelt und verschickt wird, beeinflusst das Ergebnis. Zwei Tests, die übereinstimmen, sagen viel mehr als einer.

Meist muss die Sonde kalibriert werden, manchmal ist das Testkit zu alt. Kalibriere die Sonde, teste noch einmal mit frischem Reagenz und vergleiche beide unter denselben Bedingungen. Ein [ICP-Ergebnis](/help/mobile-icp-health) liefert dir dabei einen dritten Vergleichswert.

## Ich bekomme keine Benachrichtigungen

1. Prüf unter **Einstellungen → Benachrichtigungen**, ob diese Kategorie Benachrichtigungen senden darf.
2. Prüf in den Einstellungen deines Handys, ob Cora Benachrichtigungen senden darf.
3. Denk daran, dass die tägliche Zusammenfassung an Tagen ohne Änderungen still bleibt. Das ist so gewollt.

## Herausfinden, warum sich etwas geändert hat

Unter **Einstellungen → Aktivität** steht jedes Schalten einer Steckdose, jede Fütterung, jede Dosierung und jede Änderung an einer Steckdose. Dazu siehst du, wer es ausgelöst hat: Cora Mobile, ein Cora-Bildschirm, die Sprachsteuerung, der Assistent, eine Automationsregel, eine Smart-Taste oder dein Konto.

## Mein Dashboard sieht nach dem Bearbeiten falsch aus

Lade ein gespeichertes Design. Öffne dazu **Meine Dashboards** und wähle eines aus.

Hast du noch keines gespeichert, bau das Layout neu auf und speichere es als Design. Ab dann kommst du mit einem Tipp dorthin zurück.

Messwerte, Verlauf und Tagebucheinträge werden getrennt vom Layout gespeichert. Hinter dem Dashboard geht also nichts verloren.

## „Red Sea-Messwerte haben aufgehört, sich zu aktualisieren“

Im Netzwerk dieses Beckens fragt gerade kein Gerät deine Red Sea-Geräte ab. Deshalb werden die Werte auf dem Bildschirm nicht mehr aktualisiert.

1. Öffne **Einstellungen → Primäres Cora Max** und prüf, ob ein Cora Max festgelegt oder **Jedes aktive (automatisch)** gewählt ist.
2. Öffne das Becken auf einem Gerät, das im selben WLAN ist wie deine Red Sea-Geräte.
3. Prüf, ob die Red Sea-Geräte eingeschaltet und in ihrer eigenen App online sind.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** und nenn uns den Namen von Becken und Gerät.

## „Die Pumpe konnte nicht erreicht werden: nichts wurde gesendet“

Ein Befehl an eine Jecod- oder Jebao-Pumpe hat die App nie verlassen. Meist ist die Pumpe ausgeschaltet oder nicht im Netzwerk.

1. Prüf, ob die Pumpe eingeschaltet ist.
2. Prüf, ob sie im selben Netzwerk ist wie beim Hinzufügen.
3. Tippe auf **Erneut versuchen**.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** und nenn uns den Namen von Becken und Gerät.

## „Konnte diese Pumpe nicht über Bluetooth erreichen. Steh in ihrer Nähe und versuch es erneut.“

Ein Jecod-Gerät, das nur Bluetooth kann, ist außer Reichweite deines Handys.

1. Geh näher an die Pumpe heran.
2. Tippe auf **Erneut versuchen**.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** und nenn uns den Namen von Becken und Gerät.

## „Konnte diese Gyre nicht erreichen. Keine Fütterung wurde gestartet.“

Eine Maxspect-Gyre (Anbindung in der Beta) hat nicht geantwortet, als Cora den Fütterungsmodus starten wollte.

1. Prüf, ob die Gyre eingeschaltet und im Netzwerk ist.
2. Tippe auf **Erneut versuchen**.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** und nenn uns den Namen von Becken und Gerät.

## „Konnte diese Gyre nicht erreichen. Ihr Programm wurde nicht geändert.“

Ein Zeitplan für eine Maxspect-Gyre (Anbindung in der Beta) ist nicht bei ihr angekommen.

1. Prüf, ob dein Handy oder Cora Max im Netzwerk der Gyre ist.
2. Tippe im Zeitplan-Bildschirm auf **Erneut versuchen**.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** und nenn uns den Namen von Becken und Gerät.

## „Konnte den Apex nicht erreichen: nichts geändert“ / „nichts dosiert“

Ein Neptune Apex, ein Trident oder ein DŌS-Kopf hat nicht auf einen Befehl oder eine Dosieranfrage geantwortet.

1. Öffne die App des Apex und prüf, ob er online ist.
2. Prüf die Netzwerkverbindung des Geräts, das du gerade benutzt.
3. Tippe auf **Erneut versuchen**.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** und nenn uns den Namen von Becken und Gerät.

## „Das konnte nicht gesendet werden: kein Gerät an diesem Becken kann es senden“

Kein Cora-Gerät an diesem Becken hat die Verbindungsdaten für den Apex, die es für den Befehl braucht. Oder das Gerät, das sie hat, ist offline.

1. Trag die Apex-Daten unter **Einstellungen** auf einem Gerät ein, das gerade online ist, oder
2. leg ein anderes Cora Max, das funktioniert, als **Primäres Cora Max** für dieses Becken fest.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** und nenn uns den Namen von Becken und Gerät.

## Ein zweites Cora Max zeigt „Haupt-Cora offline“

Das primäre Tablet für dieses Becken ist offline. Dieser zweite Bildschirm zeigt deshalb die zuletzt empfangenen Daten und keine Live-Daten.

1. Prüf Strom und WLAN des primären Tablets.
2. Warte, bis es wieder verbunden ist, oder stell das **Primäre Cora Max** auf ein Gerät um, das gerade online ist.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** und nenn uns den Namen von Becken und Gerät.

## „Gerät ist offline. Zeigt letzten bekannten Zustand.“

So geht Cora mit Geräten um, die offline sind. Das Gerät meldet nichts mehr, und Cora zeigt die letzten Werte, die es hatte, ohne so zu tun, als wären sie aktuell.

1. Prüf die Netzwerkverbindung des Geräts.
2. Betrachte die angezeigten Werte nicht als live, bis in der Zeile nicht mehr offline steht.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** und nenn uns den Namen von Becken und Gerät.

## Manche ReefBeat-Einstellungen sind ausgegraut oder fehlen

Das ist gewollt und kein Fehler. Gerätespezifische Einstellungen öffnen sich nur, wenn dein Handy im selben Netzwerk ist wie das Gerät. Bist du nicht in diesem Netzwerk, siehst du nur die Messwerte.

1. Verbinde dich mit dem WLAN am Becken, um diese Einstellungen zu ändern.
2. Messwerte und Verlauf funktionieren auch unterwegs ganz normal.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## „Konnte Cora nicht erreichen. Prüfe dein WLAN oder deine Mobildaten, und versuch es erneut.“

Dein Handy hat bei der Anmeldung keine brauchbare Verbindung zu Cora Cloud. Das liegt an der Verbindung deines Handys und nicht an den Geräten am Becken.

1. Prüf, ob dein Handy funktionierendes WLAN oder mobile Daten hat.
2. Probier ein anderes Netzwerk, wenn du eines hast.
3. Tippe auf **Erneut versuchen**.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Plötzlich ist alles in der falschen Sprache

Jemand hat die Kontosprache auf irgendeinem Gerät geändert. Die Sprache gilt für das ganze Konto und nicht für einzelne Geräte.

1. Öffne in einer der beiden Apps **Einstellungen → Sprache**.
2. Stell die Sprache zurück, falls sie versehentlich geändert wurde. Die Änderung gilt sofort überall.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Eine alte Warnung oder ein alter Bericht ist nach dem Wechsel noch in der alten Sprache

Das ist so vorgesehen. Cora übersetzt nichts neu, was schon erstellt ist. Nur neue Warnungen, Berichte und Zusammenfassungen kommen in der neuen Sprache.

1. Du musst nichts tun. Neue Inhalte erscheinen in der aktuellen Sprache.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Eine Warnung meldet sich immer wieder, obwohl ich sie bestätigt habe

**Schlummern** und **Verwerfen** auf Cora Max machen nur dieses eine Cora Max still. Dein Handy bekommt weiter Benachrichtigungen, solange der Messwert außerhalb des Bereichs liegt.

1. Willst du auf dem Handy seltener davon hören, öffne die Warnregel in Cora Mobile und stell eine längere **Abklingzeit zwischen Warnungen** ein (bis zu 1 Woche).
2. Passt der Schwellenwert nicht zu deinem Becken, ändere den Schwellenwert selbst.

Hilft das nicht, schau unter [Warnungen und Schwellenwerte](/help/mobile-alerts) nach oder schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Eine Dosierung hat mittendrin aufgehört, und eine Warnung zur Wiederherstellung ist erschienen

Der DŌS-Kopf hat mitten in der Dosierung die Verbindung verloren. Cora sagt dir das, damit du nicht von der vollen Dosis ausgehst.

1. Öffne die Warnung und prüf, wie viel vor dem Abbruch tatsächlich dosiert wurde.
2. Setz die Dosierung fort oder pass sie an. Rechne dabei mit dieser Menge und nicht mit der geplanten.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** und nenn uns den Namen von Becken und Gerät.

## Eine auf dem Handy erstellte Szene lässt sich auf Cora Max nicht bearbeiten

Szenen direkt am Tablet bearbeiten kann erst ein neueres Cora Max. Mit älterer Firmware laufen Szenen vom Handy trotzdem, nur bearbeiten kannst du sie dort nicht.

1. Aktualisiere Cora Max, oder
2. bearbeite die Szene weiter auf dem Handy. Auf dem Tablet läuft sie so oder so.

Hilft das nicht, schau unter [Updates und Wiederherstellung](/help/max-updates) nach oder schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant antwortet zum falschen Becken

Vor der Frage wurde kein Becken gewählt, oder gerade ist das falsche Becken aktiv.

1. Wähl zuerst das Becken, das du meinst.
2. Frag noch einmal.

Hilft das nicht, schau unter [Der Assistent](/help/mobile-assistant) nach oder schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant antwortet nicht oder zeigt wieder die Zustimmung an

Die Einstellung „Cora Assistant erlauben, gespeicherte Beckendaten zu nutzen“ ist ausgeschaltet. Ohne diese Daten kann Cora nichts beantworten.

1. Tippe auf dem Bildschirm zur Zustimmung auf **Zustimmen und fortfahren**, um sie wieder einzuschalten.

Hilft das nicht, schau unter [Der Assistent](/help/mobile-assistant) nach oder schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Ein ICP-Ergebnis vom Labor oder per E-Mail ist nie angekommen

Damit ein Ergebnis in Cora landet, muss ein Becken dafür gewählt sein. Manchmal muss Cora außerdem den Absender kennen, bevor das Ergebnis zugeordnet wird.

1. Lies den Hinweis, der erscheint, wenn du zum ersten Mal ein Ergebnis an Cora schickst.
2. Bestätige das passende Becken, wenn Cora danach fragt.
3. Hast du schon einmal ein Ergebnis geschickt, prüf, ob die E-Mail von derselben Adresse kam wie damals.

Hilft das nicht, schau unter [ICP und Zustandsberichte](/help/mobile-icp-health) nach oder schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## In einer ICP-Benachrichtigung per E-Mail fehlt der Name des Labors

Das war ein bekannter Fehler. In der Push-Benachrichtigung „Becken wählen“ fehlte der Name des Labors. In aktuellen Versionen ist das behoben.

1. Prüf, ob Cora Mobile auf dem neuesten Stand ist.
2. Das Ergebnis selbst ist nicht betroffen, nur im Text der Benachrichtigung fehlte der Name.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Ein Widget zeigt die falschen Einheiten

Das liegt an den Anzeigeeinheiten des Beckens und nicht an den Daten. Die Werte werden immer gleich gespeichert, egal wie sie angezeigt werden.

1. Öffne die **Einstellungen** dieses Beckens und prüf die Anzeigeeinheiten.
2. Ändere sie dort. Alle Handys und Cora Max, die dieses Becken zeigen, übernehmen die Änderung.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Eine Anzeige oder ein Schwellenwert sieht nach dem Ändern der Einheiten anders aus

Das ist normal. Anzeigen, Kacheln und Verlauf werden in der neuen Einheit dargestellt. Die Werte dahinter haben sich nicht geändert.

1. Du musst nichts tun. Es ändert sich nur die Darstellung.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Max verbindet sich nach einem WLAN-Ausfall nicht sofort neu

Nach einem Verbindungsabbruch wartet Cora Max vor jedem neuen Versuch etwas länger, damit es das Netzwerk nicht mit Anfragen überhäuft. Die Pause wächst bis auf etwa eine Minute.

1. Warte etwa eine Minute, nachdem dein Netzwerk wieder da ist.
2. Ist Cora Max danach immer noch nicht verbunden, prüf das WLAN unter **Einstellungen → Cora Max-Einstellungen → Wi-Fi**.

Hilft das nicht, schau unter [Der Cora Max-Startbildschirm](/help/max-tour) nach oder schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Ich habe ein Cora Max auf dem Handy umbenannt, aber das Tablet zeigt den alten Namen

Der Name, den du auf dem Handy vergibst, gilt für dieses Gerät in deinem Konto. Das Tablet kann beim Koppeln selbst einen anderen Namen anzeigen.

1. Prüf, welchen Namen du gerade siehst: den in der Geräteliste auf dem Handy oder den auf dem Kopplungsbildschirm des Tablets.
2. Willst du den Namen in deinem Konto ändern, benenne das Gerät in der Geräteliste auf dem Handy um.

Hilft das nicht, schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** und nenn uns den Namen des Geräts.

## Ich finde nicht, wo ich das Weckwort auf Cora Max ausschalte

Der Schalter für das Weckwort liegt im Bereich **Ton & Sprache** und nicht bei Cora Assistant, wo die meisten zuerst suchen.

1. Öffne **Einstellungen → Cora Max-Einstellungen → Ton & Sprache → Weckwort-Erkennung**.
2. Schalte sie aus. Mit einem Tipp auf das Cora-Symbol kannst du trotzdem ein Gespräch starten.

Hilft das nicht, schau unter [Cora Max-Einstellungen](/help/max-settings) nach oder schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Wegen der Kindersicherung kommt niemand in die Einstellungen

Die Kindersicherung arbeitet so, wie sie soll. Nach einer festgelegten Zeit ohne Berührung kann niemand mehr Geräte von diesem Bildschirm aus schalten, weder per Touch noch per Sprache. Die Messwerte aktualisieren sich weiter, und du kannst Cora weiterhin Fragen stellen. So entsperrst du:

1. Drück dreimal innerhalb von zwei Sekunden auf **Lauter** oder **Leiser**, oder
2. halte fünf Finger zehn Sekunden lang in die obere rechte Ecke des Bildschirms.

Hilft das nicht, schau unter [Mit Cora sprechen](/help/max-voice) nach oder schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Immer noch nicht weiter?

Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**. Sag uns, um welches Becken und welchen Bildschirm es geht und was du erwartet hast. Dann können wir dir schneller helfen.
