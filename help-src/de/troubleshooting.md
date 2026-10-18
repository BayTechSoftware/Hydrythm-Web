---
title: Problembehebung
description: Einen veralteten Messwert, ein Gerät, das offline gegangen ist, einen Befehl, der nicht durchkam, ein Cora Max, das sich nicht koppeln lässt, oder eine Warnung, die nicht verschwindet, beheben.
section: Help
reviewed: 2026-10-18
order: 1
---

Such den Bereich, zu dem dein Problem gehört, und dann die Meldung oder das Symptom, das du siehst. Überschriften in Anführungszeichen sind genau die Worte, die Cora dir zeigt.

- [Messwerte und Widgets](#readings-and-widgets)
- [Ein Gerät meldet sich nicht mehr oder ist nicht erreichbar](#device-not-reporting)
- [Ein Befehl ist nicht durchgekommen](#command-did-not-go-through)
- [Cora Max](#cora-max)
- [Warnungen, Benachrichtigungen und das tägliche Briefing](#alerts-and-notifications)
- [Cora Assistant und Sprache](#cora-assistant-and-voice)
- [Laborergebnisse und Gesundheitsberichte](#lab-results-and-health-reports)
- [Sprache, Einheiten und Anmelden](#language-units-and-signing-in)


## Messwerte und Widgets {#readings-and-widgets}

### Ein Widget zeigt keinen Wert {#a-widget-shows-no-value}

Geh diese Punkte der Reihe nach durch.

1. Sieh dir das Alter auf den Widgets daneben an. Sind sie auch alle alt, liegt es an der Verbindung, nicht am Wasserwert.
2. Öffne den Tab **Geräte**. Ist ein Gerät nicht erreichbar, hat seine Zeile einen roten Punkt oder sagt es.
3. Prüf, an welchem Becken das Gerät ist. Ein Gerät, das an das falsche Becken meldet, sieht genauso aus wie eins, das nicht meldet. Öffne das Gerät und prüf sein Becken.
4. Prüf, ob überhaupt etwas den Wert misst. Phosphat meldet nichts, außer du hast Ausrüstung, die es misst, oder trägst es von Hand ein.

### Ein Widget ist grau {#a-widget-is-grey}

Grau heißt, dass Cora diesen Messwert nicht bewertet. Es gibt drei übliche Gründe.

1. Die Warnung dafür ist ausgeschaltet. Schalte sie im Tab **Regeln** der Warnzentrale wieder ein.
2. Es gibt keinen Bereich, an dem er gemessen werden kann. Drück lange auf das Widget und leg einen Bereich fest.
3. Der Messwert ist zu alt. Prüf das Alter auf dem Widget und trag dann einen neuen Messwert ein oder prüf das Gerät.

Was jede Farbe bedeutet, steht unter [Dein Dashboard lesen](/help/mobile-dashboard#colours).

### Ein Messwert ist veraltet {#a-reading-is-stale}

Das Alter auf dem Widget stimmt. Es ist einfach nichts Neues angekommen.

- Von Hand eingetragene Wasserwerte veralten, wenn niemand einen Messwert eingetragen hat. Trag einen ein.
- Messwerte von Ausrüstung veralten, wenn das Gerät sich nicht mehr meldet. Prüf seine Zeile unter **Geräte**.
- Manche Ausrüstung meldet nur ab und zu. Ein Titrator, der stündlich misst, zeigt meist `1h`. Das ist normal.

### Zwei Quellen widersprechen sich {#two-sources-disagree}

Es ist nichts kaputt. Widersprechen sich deine Sonde und dein Testkit, sagt dir das etwas Echtes über dein System.

Meist muss die Sonde kalibriert werden. Manchmal ist das Testkit alt. Kalibriere die Sonde, teste noch einmal mit frischem Reagenz und vergleich beide unter denselben Bedingungen. War ein Messwert eindeutig falsch, kannst du ihn ausschließen. Siehe [Einen Wasserwert genauer ansehen](/help/mobile-metric-detail).

Ein [ICP-Ergebnis](/help/mobile-icp-health) gibt dir eine dritte Zahl zum Vergleichen, entscheidet die Frage aber nicht allein. Labore unterscheiden sich, und wie eine Probe behandelt und verschickt wird, verändert das Ergebnis.

### Ein Widget zeigt die falschen Einheiten {#a-widget-shows-the-wrong-units}

Das sind die Anzeigeeinheiten des Beckens. Deine Daten sind in Ordnung, und die Werte werden gleich gespeichert, egal wie sie angezeigt werden.

1. Öffne **Einstellungen**, öffne das Becken und wähl **Einheiten**.
2. Ändere sie dort. Jedes Handy und jedes Cora Max, das dieses Becken zeigt, passt sich an.

### Eine Anzeige oder ein Schwellenwert sieht nach dem Ändern der Einheiten anders aus {#a-gauge-or-threshold-looks-different-after-changing-display-}

Das ist zu erwarten. Anzeigen, Kacheln und Verlauf werden in der Einheit neu gezeichnet, die du gewählt hast. Die Werte darunter haben sich nicht geändert.

### Mein Dashboard sieht nach dem Bearbeiten falsch aus {#my-dashboard-looks-wrong-after-editing}

Deine Messwerte, dein Verlauf und dein Tagebuch werden getrennt vom Layout gespeichert, du hast also nichts verloren.

- **Auf dem Handy** hat der Editor kein Rückgängig und keine gespeicherten Designs. Öffne **Dashboard bearbeiten** und setz die Widgets wieder an ihren Platz. Mehr dazu unter [Dein Dashboard bearbeiten](/help/mobile-dashboard-editing).
- **Auf Cora Max** lädst du ein gespeichertes Design: Öffne **Dashboard-Layout**, tippe auf **Meine Dashboards** und wähl eins. Hast du keins gespeichert, bau das Layout neu und tippe auf **Dieses Design speichern**, dann reicht beim nächsten Mal ein Tippen. Mehr dazu unter [Das Cora Max-Dashboard bearbeiten](/help/max-dashboard-editing#saving-layouts).

### Herausfinden, warum sich etwas geändert hat {#establishing-why-something-changed}

**Einstellungen → Aktivität** listet jedes Schalten einer Steckdose, jede Fütterung und jede Dosierung auf und was sie ausgelöst hat: Cora Mobile, ein Cora Max, Sprache, der Assistent, eine Automation oder dein Konto. Mehr dazu unter [Aktivität und Zeitleiste](/help/mobile-activity).

## Ein Gerät meldet sich nicht mehr oder ist nicht erreichbar {#device-not-reporting}

### "[Gerät]: meldet sich nicht mehr" {#device-stopped-reporting}

Cora schickt das, wenn ein Gerät still wird. Es heißt nicht, dass das Gerät kaputt ist, nur, dass Cora eine Weile nichts von ihm gehört hat. Wie lange Cora bei jeder Marke wartet, steht unter [Warnungen und Schwellenwerte](/help/mobile-alerts#stopped-reporting).

1. Prüf den Strom des Geräts und seine WLAN- oder Bluetooth-Reichweite.
2. Prüf, ob das Cora Max, das es abfragt, eingeschaltet und online ist. Ohne Cora Max liest dein Handy ein Neptune Apex-, Red Sea- oder Jecod-Gerät nur, solange Cora Mobile im selben WLAN geöffnet ist.
3. Warte auf den nächsten Messwert. Du bekommst eine zweite Benachrichtigung, sobald es sich wieder meldet.


### "Gerät ist offline. Der letzte bekannte Status wird angezeigt." {#device-is-offline-showing-last-known-state}

Das Gerät meldet sich nicht mehr, und Cora zeigt die letzten Werte, die es hatte. Sie sind nicht aktuell.

1. Prüf die eigene Netzwerkverbindung des Geräts.
2. Betrachte die Werte nicht als live, bis in der Zeile nicht mehr offline steht.

### Ein Gerät ist nicht erreichbar {#a-device-cannot-be-reached}

Meist liegt es am Netzwerk.

1. Ist die Ausrüstung eingeschaltet und funktioniert sie in ihrer eigenen App?
2. Ist sie im selben Netzwerk, in dem du sie hinzugefügt hast?
3. Hat sich an deinem Router etwas geändert (neue Hardware, neuer Netzwerkname, Isolierung im Gastnetz)?

Ausrüstung in deinem lokalen Netzwerk muss in diesem Netzwerk erreichbar sein. Ausrüstung, die sich über ein Konto beim Hersteller verbindet, muss das nicht, aber dieses Konto muss gültig sein. Hat sich die Adresse des Geräts geändert, öffne es im Tab **Geräte** und tippe unter **Verbindung** auf **Verbindung bearbeiten**.

### Ein Gerät sagt, die Anmeldung wurde abgelehnt {#a-device-says-the-sign-in-was-refused}

Der Hersteller hat die gespeicherte Anmeldung abgelehnt. Fast immer liegt es daran, dass du dort dein Passwort geändert hast. Öffne die Zeile des Geräts und melde dich erneut an.

### "Die Red Sea-Messwerte werden nicht mehr aktualisiert" {#red-sea-readings-have-stopped-updating}

Gerade fragt nichts an diesem Becken deine Red Sea-Ausrüstung ab, die Messwerte auf dem Bildschirm werden also nicht aufgefrischt.

1. Öffne **Einstellungen**, öffne das Becken und dann **Primäres Cora Max**. Prüf, ob ein Cora Max festgelegt oder **Jedes aktive (automatisch)** gewählt ist.
2. Hast du kein Cora Max, öffne das Becken in Cora Mobile, während dein Handy im selben WLAN ist wie die Red Sea-Ausrüstung.
3. Prüf, ob die Red Sea-Ausrüstung eingeschaltet und in ihrer eigenen App online ist.

### Manche ReefBeat-Einstellungen sind ausgegraut oder fehlen {#some-reefbeat-settings-are-greyed-out-or-missing}

Das ist normal. Die eigenen Einstellungen eines Red Sea-Geräts öffnen sich nur, wenn dein Handy im selben Netzwerk ist wie das Gerät. Außerhalb dieses Netzwerks siehst du nur Messwerte.

1. Verbinde dich mit dem WLAN des Beckens, um diese Einstellungen zu ändern.
2. Messwerte und Verlauf funktionieren weiter, wenn du unterwegs bist.


## Ein Befehl ist nicht durchgekommen {#command-did-not-go-through}

Jeder Befehl endet als **Bestätigt**, **Unbestätigt**, **Abgelehnt** oder **Keine Änderung**. Was jedes davon bedeutet, steht unter [Deine Ausrüstung steuern](/help/mobile-device-control).

### "Diese Pumpe konnte nicht erreicht werden: Es wurde nichts gesendet" {#could-not-reach-this-pump-nothing-was-sent}

Ein Befehl an deine Jecod- oder Jebao-Pumpe hat Cora nie verlassen. Auf dem Handy lautet die Meldung *"Diese Pumpe konnte nicht erreicht werden. Sie muss im selben WLAN wie dein Telefon sein."* Meist ist die Pumpe aus oder nicht in ihrem Netzwerk.

1. Prüf, ob die Pumpe eingeschaltet ist.
2. Prüf, ob sie im selben Netzwerk ist, in dem du sie hinzugefügt hast, und ob dein Handy oder Cora Max auch in diesem Netzwerk ist.
3. Tippe auf **Erneut versuchen**.

### "Diese Pumpe konnte über Bluetooth nicht erreicht werden. Steh in ihrer Nähe und versuch es erneut." {#could-not-reach-this-pump-over-bluetooth-stand-near-it-and-t}

Dein Handy ist außer Reichweite einer Jecod-Pumpe, die nur Bluetooth nutzt. Geh näher an die Pumpe und tippe auf **Erneut versuchen**.


### "Der Apex war nicht erreichbar: nichts wurde geändert" / "nichts wurde dosiert" {#could-not-reach-the-apex-nothing-changed-nothing-was-dosed}

Ein Neptune Apex, Trident oder DŌS-Kopf hat auf einen Befehl oder eine Dosieranfrage nicht reagiert.

1. Öffne die eigene App des Apex und prüf, ob er online ist.
2. Prüf die Netzwerkverbindung des Handys oder Cora Max, das du nutzt. Einen DŌS-Kopf vom Handy aus zu ändern, braucht das Handy im selben Netzwerk wie der Apex.
3. Tippe auf **Erneut versuchen**.

### "… konnte nicht gesendet werden: Dieses Cora Max hat keine Apex-Zugangsdaten" {#this-could-not-be-sent-no-device-on-this-tank-can-send-it}

Cora Max zeigt das, wenn es keinen Weg hat, deinen Apex zu erreichen, und kein anderes Gerät am Becken den Befehl für es senden kann. Die Meldung sagt, du sollst die Apex-Daten in den Einstellungen hinzufügen, aber die legst du inzwischen auf dem Handy fest.

1. Öffne auf dem Handy **Geräte**, dann deinen Apex, und prüf seine Adresse und Anmeldung unter **Verbindung**. Korrigier sie mit **Verbindung bearbeiten**.
2. Oder mach ein funktionierendes Cora Max zum **Primäres Cora Max** für dieses Becken: **Einstellungen**, das Becken öffnen, dann **Primäres Cora Max**.

### Füttern startet nicht vom Handy aus {#feed-does-not-start}

Auf dem Handy erscheint **Füttern** nur bei einem Becken mit Neptune Apex, und es startet einen der Fütterungszyklen, die auf dem Apex programmiert sind.

- *"Kein Cora an diesem Becken kann den Apex erreichen, und du bist nicht in seinem Netzwerk."* Verbinde dich mit dem WLAN des Apex oder koppel ein Cora Max mit dem Becken.
- *"Der Apex hat nicht geantwortet, füttert aber möglicherweise schon."* Prüf den Controller, bevor du es noch einmal versuchst.

### Eine Dosierung hat mittendrin aufgehört, und eine Wiederherstellungswarnung ist erschienen {#a-dose-stopped-partway-through-and-a-restore-alert-appeared}

Der DŌS-Kopf hat während der Dosierung die Verbindung verloren. Cora sagt es dir, damit es nicht davon ausgehen muss, dass die volle Dosis hineingegangen ist.

1. Öffne die Warnung und prüf, wie viel dosiert wurde, bevor es aufgehört hat.
2. Entscheide anhand dieser Menge, ob du fortsetzt oder die Dosis anpasst.

## Cora Max {#cora-max}

### Mein Cora Max ist offline {#my-cora-max-is-offline}

Auf dem Handy hat seine Zeile im Tab **Geräte** einen roten Punkt. Solange es offline ist, wird Ausrüstung, die es abfragt, nicht mehr aktualisiert, du bekommst vielleicht Warnungen, dass sich diese Ausrüstung nicht mehr meldet, und Befehle, die du von unterwegs schickst, können mit *"Es wurde nichts gesendet"* zurückkommen.

1. Prüf, ob Cora Max Strom hat und der Bildschirm an ist.
2. Prüf auf Cora Max **Einstellungen → Cora Max-Einstellungen → WLAN** und ob dein Router funktioniert.
3. Ist ein weiteres Cora Max am Becken, stell **Primäres Cora Max** auf **Jedes aktive (automatisch)**, damit es übernehmen kann. Siehe [Mehr als ein Cora-Gerät](/help/mobile-multi-device#primary-cora-max).
4. Startet es nicht richtig, siehe [Updates und Wiederherstellung](/help/max-updates).

:::tip Lass es dir beim nächsten Mal sagen
Öffne in Cora Mobile **Einstellungen → Automationen** und leg eine Regel mit dem Auslöser **Wenn ein Gerät offline geht** an, wähl dein Cora Max und füg die Aktion **Mich benachrichtigen** hinzu. Mehr dazu unter [Automationen und Szenen](/help/mobile-automation).
:::

### Das Koppeln eines Cora Max schlägt fehl {#pairing-a-cora-max-fails}

Cora Mobile findet ein neues Cora Max über Bluetooth und gibt ihm dann dein WLAN. Bevor du anfängst, brauchst du mindestens ein Becken in Cora Mobile, eingeschaltetes Bluetooth und dein Handy in der Nähe des Bildschirms. Bleibt das Koppeln mittendrin stehen, sagt dir Cora Mobile, warum, mit **Abbrechen** und **Erneut versuchen** darunter.

- *"Bluetooth ist aus. Schalte es ein und tippe dann erneut auf Scannen."* Schalte Bluetooth ein und scanne noch einmal.
- *"Bluetooth-Berechtigung ist für Cora deaktiviert. Aktiviere sie in den Einstellungen und tippe dann erneut auf Scannen."* Erlaube Cora in den Einstellungen deines Handys Bluetooth. **Einstellungen → Gerätezugriff** in Cora Mobile bringt dich dorthin.
- *"Es wurden keine Cora Einrichtungsgeräte in der Nähe über Bluetooth gefunden."* Stell dich neben Cora Max, prüf, ob es seinen Einrichtungsbildschirm zeigt, und scanne noch einmal.
- **Keine Becken gefunden**: Leg zuerst ein Becken in Cora Mobile an und koppel dann.
- *"Dein Telefon konnte das Cora Max in deinem WLAN nicht erreichen."* Bring dein Handy und Cora Max ins selbe WLAN. Prüf auf dem iPhone außerdem, ob Cora Zugriff auf das lokale Netzwerk hat (**Einstellungen → Gerätezugriff**). Tippe dann auf **Erneut versuchen**.
- *"Das Cora Max hat diese Kopplungssitzung nicht akzeptiert."* Erneut versuchen hilft nicht. Schließ den Bildschirm und fang wieder bei **Geräte → Gerät hinzufügen → Cora** an.

Bei jeder anderen Meldung tippe auf **Erneut versuchen**. Die ganze Einrichtung steht unter [Cora Max einrichten](/help/max-setup).

### Cora Max zeigt alte Daten {#cora-max-shows-old-data}

Sieh dir die Statusanzeige in der oberen Leiste an. **Online** und **Cloud** sind beide in Ordnung. Hast du mehr als ein Cora Max, zeigt das, das die Daten nicht sammelt, **Cloud**, und seine Messwerte sind genauso aktuell. **Veraltet** oder **Offline** heißt, dass Cora Max seine Quelle verloren hat und die letzten Daten zeigt, die es bekommen hat.

- Prüf das WLAN unter **Einstellungen → Cora Max-Einstellungen → WLAN**.
- Prüf, ob dein Netzwerk selbst funktioniert.
- Steht in der Anzeige **Online** oder **Cloud** und sind die Daten trotzdem alt, liegt das Problem vor Cora Max. Prüf dasselbe Becken auf deinem Handy.

### Cora Max zeigt "Apex-Passwort" {#cora-max-shows-apex-password}

Dein Apex hat die Anmeldung abgelehnt, die Cora gespeichert hat, meist weil das Apex-Passwort geändert wurde. Öffne auf dem Handy **Geräte**, dann deinen Apex, und tippe unter **Verbindung** auf **Verbindung bearbeiten**, um das neue einzugeben.

### Cora Max zeigt "Cloud-Speichern abgelehnt" {#cora-max-shows-cloud-save-refused}

Cora Cloud lehnt es ab, einen Teil der Daten dieses Bildschirms zu speichern. Mit deinem Becken und mit Cora Max ist alles in Ordnung, und auf dem Bildschirm musst du nichts ändern. Die Lösung ist ein Update von Cora Cloud.

1. Öffne **Einstellungen → Cora Max-Einstellungen** und scroll zu **STATUS**. Die Zeile **Cloud-Speichern** sagt, welche Daten abgelehnt werden, zum Beispiel die Messwerte oder Steckdosen eines Geräts.
2. [Wende dich an den Support](/support.html) und sag uns, was in dieser Zeile steht.

Deine Messwerte erscheinen in der Zwischenzeit weiter auf Cora Max. Sie werden nur nicht in deinem Konto gespeichert, bis die Lösung da ist.

### Ein zweites Cora Max zeigt "Haupt-Cora offline" {#a-secondary-cora-max-shows-main-cora-offline}

Das Primäre Cora Max für dieses Becken ist offline gegangen. Dieser Bildschirm zeigt die letzten Daten, die er bekommen hat, er ist also nicht live.

1. Prüf Strom und WLAN des primären Cora Max.
2. Warte, bis es sich wieder verbindet, oder stell das **Primäres Cora Max** auf ein Gerät um, das online ist.

### Cora Max verbindet sich nach einem WLAN-Ausfall nicht sofort wieder {#cora-max-wont-reconnect-right-away-after-a-wi-fi-outage}

Nachdem es seine Verbindung verloren hat, wartet Cora Max vor jedem neuen Versuch etwas länger, damit es dein Netzwerk nicht überflutet. Die Wartezeit wächst auf etwa eine Minute.

1. Gib ihm etwa eine Minute, nachdem dein Netzwerk zurück ist.
2. Hat es sich dann immer noch nicht verbunden, prüf **Einstellungen → Cora Max-Einstellungen → WLAN**.

### Ein Cora Max auf dem Handy umzubenennen ändert nicht, was es zeigt {#renaming-a-cora-max-on-the-phone-doesnt-change-what-the-tabl}

Der Name, den du auf dem Handy festlegst, ist die Bezeichnung des Kontos für dieses Gerät. Der Name, den Cora Max auf seinem eigenen Kopplungsbildschirm zeigt, kann ein anderer sein.

1. Prüf, welchen Namen du ansiehst: den in der Geräteliste deines Handys oder den auf dem Kopplungsbildschirm von Cora Max.
2. Um die Bezeichnung des Kontos zu ändern, benenn es in der Geräteliste deines Handys um.

### Ich finde nicht, wo ich das Weckwort ausschalte {#i-cant-find-where-to-turn-off-the-wake-word-on-cora-max}

Die Einstellungen fürs Weckwort stehen bei den Toneinstellungen, nicht bei den Einstellungen von Cora Assistant.

1. Geh auf Cora Max zu **Einstellungen → Cora Max-Einstellungen** und such **Weckwort** unter **TON & SPRACHE**.
2. Schalte es aus. Du kannst weiterhin auf das Symbol **Cora Assistant** tippen, um zu sprechen.

Mehr dazu unter [Mit Cora sprechen](/help/max-voice).

### Die Kindersicherung lässt niemanden in die Einstellungen {#child-lock-wont-let-anyone-into-settings}

Genau das tut die Kindersicherung. Nach einer festgelegten Zeit ohne Berührung verhindert sie, dass jemand an diesem Bildschirm Ausrüstung schaltet, per Berührung oder per Sprache. Messwerte werden weiter aktualisiert, und du kannst Cora weiter Fragen stellen. Zum Entsperren:

1. Drück innerhalb von zwei Sekunden dreimal **Lauter** oder **Leiser**, oder
2. halte fünf Finger zehn Sekunden lang in die obere rechte Ecke des Bildschirms.

Mehr dazu unter [Cora Max-Einstellungen](/help/max-settings#child-lock).

### Eine auf dem Handy angelegte Szene lässt sich auf Cora Max nicht bearbeiten {#a-scene-made-on-the-phone-doesnt-show-up-as-editable-on-cora}

Nur neuere Cora Max-Versionen können Szenen am Bildschirm bearbeiten. Ältere Versionen starten weiterhin Szenen, die du auf dem Handy angelegt hast, können sie aber nicht bearbeiten.

1. Aktualisiere Cora Max ([Updates und Wiederherstellung](/help/max-updates)), oder
2. bearbeite diese Szene weiter auf dem Handy. Auf Cora Max läuft sie so oder so.

## Warnungen, Benachrichtigungen und das tägliche Briefing {#alerts-and-notifications}

### Eine Warnung verschwindet nicht {#an-alert-is-not-clearing}

Eine Warnung verschwindet, wenn der Messwert wieder im Bereich ist. Verschwindet sie nicht, gibt es drei wahrscheinliche Gründe.

- Der Messwert liegt wirklich außerhalb des Bereichs. Sieh dir den Verlauf des Widgets an.
- Der Bereich passt nicht zu deinem Becken. Siehe [Warnungen und Schwellenwerte](/help/mobile-alerts).
- Die Quelle liegt daneben. Eine Sonde, die kalibriert werden muss, meldet eine Zahl, die wirklich außerhalb des Bereichs liegt. Reparier die Sonde und lass den Bereich in Ruhe.

### Eine Warnung benachrichtigt weiter, obwohl ich sie bestätigt habe {#an-alert-wont-stop-notifying-even-after-ive-acknowledged-it}

**Verschieben** und **Verwerfen** auf Cora Max machen nur dieses eine Cora Max still. Dein Handy bekommt weiter Benachrichtigungen, solange der Messwert außerhalb des Bereichs liegt.

1. Um seltener davon zu hören, öffne die Warnregel in Cora Mobile und stell eine längere **Abklingzeit zwischen Warnungen** ein (bis zu 1 Woche).
2. Passt der Bereich nicht zu deinem Becken, ändere den Bereich selbst.

### Ich bekomme keine Benachrichtigungen {#im-not-getting-notifications}

1. Prüf unter **Einstellungen → Benachrichtigungen**, ob die Kategorie Benachrichtigungen schicken darf.
2. Prüf die eigene Benachrichtigungsberechtigung deines Handys für Cora.
3. Das tägliche Briefing bleibt an Tagen still, an denen sich nichts geändert hat. Kommt es gar nicht mehr, siehe den nächsten Eintrag.

Mehr dazu unter [Benachrichtigungen](/help/mobile-notifications).

### Mein tägliches Briefing kommt nicht mehr {#my-daily-briefing-stopped}

- Deine Testphase ist zu Ende. Reef Buddy gehört zu den kostenpflichtigen Abos. Nach der 30-tägigen Testphase bekommt ein kostenloses Konto kein tägliches Briefing mehr. Siehe [Pläne und Abos](/help/mobile-plans).
- Das Becken ist nicht von deinem Abo abgedeckt. Jedes Abo deckt eine feste Zahl von Becken ab, gezählt in der Reihenfolge unter **Einstellungen → Becken neu anordnen**. Schieb ein Becken nach oben, um es aufzunehmen.
- Heute hat sich nichts geändert. An einem ruhigen Tag bleibt das Briefing still.

Mehr dazu unter [Reef Buddy](/help/mobile-reef-buddy).

### Von einem entfernten Becken kommen weiter Warnungen {#alerts-from-a-removed-tank}

Ein entferntes Becken bleibt wegen seines Verlaufs erhalten, sendet aber keine Warnungen oder Erinnerungen, und seine Automationen stoppen. Kommt trotzdem noch eine:

1. Öffne **Einstellungen → Entfernte Becken**. Steht das Becken dort nicht, wurde es nicht entfernt.
2. Aktualisiere Cora Mobile und dein Cora Max auf die neueste Version.
3. Kommen weiter Warnungen? Schreib dem Support mit dem Text der Warnung und der Uhrzeit. Siehe [Ein Problem melden](/help/mobile-support).

Mehr dazu unter [Deine Becken verwalten](/help/mobile-tanks).


## Cora Assistant und Sprache {#cora-assistant-and-voice}

### Cora Assistant antwortet zum falschen Becken {#cora-assistant-answers-about-the-wrong-tank}

Du hast vor der Frage kein Becken gewählt, oder das falsche ist ausgewählt. Wähl das Becken, das du meinst, und frag noch einmal. Mehr dazu unter [Cora fragen](/help/mobile-assistant).

### Cora Assistant antwortet nicht oder zeigt wieder einen Zustimmungsbildschirm {#cora-assistant-refuses-to-answer-or-shows-a-consent-screen-a}

**Cora Assistant erlauben, gespeicherte Beckendaten zu nutzen** ist ausgeschaltet, Cora hat also nichts, woraus es antworten kann. Tippe auf dem Zustimmungsbildschirm auf **Zustimmen und fortfahren** oder schalte den Schalter unter **Einstellungen → Cora Assistant** ein.

### Cora Max sagt "Sprachsteuerung braucht deine Zustimmung" {#voice-needs-your-ok}

Die Sprache auf Cora Max nutzt dieselbe Entscheidung zum Teilen von Daten wie Cora Assistant auf deinem Handy. Öffne in Cora Mobile **Einstellungen → Cora Assistant**, schalte **Cora Assistant erlauben, gespeicherte Beckendaten zu nutzen** ein und versuch es dann noch einmal. Mehr dazu unter [Mit Cora sprechen](/help/max-voice).

## Laborergebnisse und Gesundheitsberichte {#lab-results-and-health-reports}

### Ein ICP-Ergebnis vom Labor oder per E-Mail ist nie aufgetaucht {#a-lab-or-emailed-icp-result-never-showed-up}

Ein Ergebnis wird erst zugeordnet, wenn es ein Becken hat, manchmal muss Cora außerdem den Absender erkennen, und Cora braucht dein OK, um es zu lesen.

1. Siehst du *"Cora Assistant braucht deine Zustimmung, um es zu lesen."*, öffne **Einstellungen → Cora Assistant** und schalte **Cora Assistant erlauben, gespeicherte Beckendaten zu nutzen** ein. Das Ergebnis kommt durch, sobald du zustimmst.
2. Prüf den Hinweis, den Cora zeigt, wenn du ihm zum ersten Mal ein Ergebnis schickst.
3. Wenn Cora fragt, bestätige, zu welchem Becken das Ergebnis gehört.
4. Hast du schon einmal ein Ergebnis geschickt, schick dieses von derselben E-Mail-Adresse.

Mehr dazu unter [ICP und Gesundheitsberichte](/help/mobile-icp-health).

### Meine ICP-Datei lässt sich nicht hochladen {#my-icp-file-wont-upload}

Cora liest den PDF-Bericht, den dein Labor schickt. Fotos und Screenshots lassen sich nicht lesen. Lade zuerst das PDF von deinem Labor herunter und tippe dann noch einmal auf **ICP hochladen**.

### Der Bildschirm wird nach einem Gesundheitsbericht oder ICP-Upload schwarz {#black-screen-after-a-report}

Das konnte in Cora Mobile 1.2 und früher passieren, und Cora Mobile 1.3 behebt es: Aktualisiere Cora Mobile aus dem App Store oder von Google Play. Siehst du es vor dem Update, schließ Cora Mobile und öffne es wieder. Der Bericht wurde gespeichert, und du findest ihn unter **Intelligenz**.

## Sprache, Einheiten und Anmelden {#language-units-and-signing-in}

### Plötzlich ist alles in der falschen Sprache {#everything-is-suddenly-in-the-wrong-language}

Jemand hat die Kontosprache auf einem deiner Geräte geändert. Sie ist eine Einstellung für das ganze Konto.

1. Öffne **Einstellungen → Sprache** in Cora Mobile oder auf Cora Max.
2. Stell sie zurück. Die Änderung gilt überall.

### Eine alte Warnung oder ein alter Bericht ist nach dem Wechsel in einer anderen Sprache {#an-old-alert-or-report-is-still-in-a-different-language-afte}

Das ist zu erwarten. Cora übersetzt nichts neu, was es schon geschrieben hat. Neue Warnungen, Berichte und Briefings nutzen die neue Sprache.

### "Cora konnte nicht erreicht werden. Prüfe dein WLAN oder deine mobilen Daten und versuche es erneut." {#could-not-reach-cora-check-your-wi-fi-or-mobile-data-then-tr}

Dein Handy erreicht Cora Cloud nicht, um dich anzumelden. Das betrifft die Verbindung deines Handys, nicht die Ausrüstung deines Beckens.

1. Prüf, ob dein Handy funktionierendes WLAN oder mobile Daten hat.
2. Probier ein anderes Netzwerk, wenn du eins hast.
3. Tippe auf **Erneut versuchen**.

Andere Probleme beim Anmelden stehen unter [Anmelden und Konto wiederherstellen](/help/mobile-account).

## Immer noch nicht gelöst {#still-stuck}

Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** oder melde es aus Cora Mobile heraus, wie unter [Ein Problem melden](/help/mobile-support) beschrieben. Sag uns, welches Becken, welches Gerät, welcher Bildschirm und was du erwartet hast.
