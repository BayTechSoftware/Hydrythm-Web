---
title: Parameterzuordnung und Sonden
description: Alle Messwerte der Geräte in einer Liste, wählen, als welcher Parameter jeder erscheint und welches Gerät ihn liefert, und Sondenkalibrierung und -reinigung festhalten.
section: Cora Mobile
reviewed: 2026-11-03
order: 15
group: Equipment
---

Mit der **Parameterzuordnung** legst du fest, als welcher Parameter jeder Messwert angezeigt wird und, wenn zwei Geräte dasselbe melden, welchem du vertraust. Geh zu **Einstellungen**, öffne das Becken und tippe auf **Parameterzuordnung**.

![Beckeneinstellungen in Cora Mobile, mit Parameterzuordnung und Verbundene Partner](img/mobile-tank-settings.webp "Einstellungen, dann dein Becken: Die Parameterzuordnung ist die zweite Zeile.")

Sie steht zwischen **Becken bearbeiten** und **Warnschwellen**. Der Stift oben auf dem Dashboard öffnet **Becken bearbeiten**, wo es sie nicht gibt. Du erreichst sie auch über die Geräteseiten von Neptune Apex.

Der Bildschirm ist eine einzige Liste von Geräten, darüber ein Suchfeld (**Parameter suchen**). Die Suche durchsucht Namen von Parametern, Namen von Messwerten, Geräte und Marken. Dasselbe Suchfeld gibt es in jeder Parameterauswahl.

## Eine Liste aller Geräte {#mapping}

![Parameterzuordnung in Cora Mobile, mit einem geöffneten Gerät](img/mobile-probe-mapping.webp "Eine Liste aller Geräte. Öffne ein Gerät, um seine Messwerte zu sehen und als was jeder angezeigt wird.")

Unter dem Suchfeld erklärt Cora den Bildschirm in einer Zeile: die Messwerte jedes Geräts und als welcher Beckenparameter sie angezeigt werden. Tippe auf einen Messwert, um ihn zu ändern.

- **Jedes Gerät steht unter dem Namen, den du ihm gegeben hast.** Ein Gerät ohne Namen steht unter seiner Marke, und zwei unbenannte Geräte derselben Marke werden nummeriert („AquaWiz 1“, „AquaWiz 2“). Seriennummern und Geräte-IDs dienen nie als Namen; sie stehen hinter **Details anzeigen** auf der Seite des Geräts. Siehe [Die Seite eines Geräts](/help/mobile-devices#a-devices-page).
- **Jeder Messwert steht unter dem Gerät, das ihn wirklich meldet.** Jede Zeile zeigt den eigenen Namen des Geräts für den Messwert, seinen letzten Wert und **Angezeigt als**, den Beckenparameter, den er speist. Ein Messwert, den du ausgeblendet hast, zeigt **Nicht angezeigt**.
- **Ein Becken hat ein Neptune Apex**, egal wie viele Cora-Geräte es auslesen. Seine Sonden stehen in einer Liste unter einem Abschnitt **Apex** (oder unter dem Namen, den du ihm gegeben hast). Ein Apex-Erweiterungsmodul wie DŌS oder Trident steht unter seinem eigenen Namen. Seine Messwerte lassen sich nicht umlenken; ein Tipp darauf benennt stattdessen den Parameter um.
- **Ein Gerät, das mit anderen Becken geteilt wird, steht in der Liste jedes Beckens, mit dem es verbunden ist.** Sein Abschnitt sagt *Auch in* und die Namen der anderen Becken, danach *Änderungen hier gelten nur für dieses Becken.*
- **Ein Gerät mit höchstens zwei Messwerten ist von Anfang an offen**; ein längeres ist zunächst zugeklappt und zeigt die Anzahl seiner Messwerte, es sei denn, einer seiner Messwerte teilt sich einen Parameter mit einem anderen Gerät. Tippe auf den Namen eines Geräts, um es zu öffnen oder zu schließen. Während du suchst, sind alle Treffer offen.

Cora erkennt Standardnamen von Messwerten selbst, daher zeigen die meisten Zeilen schon den richtigen Parameter. Korrigiere nur die wenigen, die es nicht einordnen konnte.

Eine Änderung wird gespeichert, sobald du sie wählst; es gibt keinen Speichern-Knopf. Sie wirkt, sobald das nächste Mal Messwerte ankommen. Eine Korrektur hier schreibt den Verlauf nicht um: frühere Messwerte bleiben, wo sie sind, und es ändert sich nur, was ab dann gespeichert wird. Zuordnungen, die du vor diesem Aufbau gemacht hast, bleiben unverändert erhalten.

:::warning Cora sieht einen ausgeblendeten Messwert nicht
Zeigt ein Parameter keine Messwerte, obwohl das Gerät funktioniert, prüf, ob sein Messwert **Nicht angezeigt** sagt.
:::

:::note Ein Lecksensor lässt sich hier nicht neu zuordnen
Der Alarm eines Lecksensors hängt von seinem eigenen Namen ab, daher sagt seine Zeile *Der Leckalarm hängt von diesem Namen ab und kann hier nicht geändert werden.* Er funktioniert wie immer.
:::

:::note Geräte, die noch ein Update brauchen
Ein Gerät, das auf ein Firmware-Update wartet, sagt *Änderungen hier wirken erst nach dem Firmware-Update dieses Geräts.* Deine Wahl wird gespeichert und gilt, sobald das Update installiert ist.
:::

## Festlegen, als was ein Messwert angezeigt wird {#shows-as}

So änderst du, als was ein Messwert angezeigt wird:

1. Geh zu **Einstellungen**, tippe unter **Becken** auf dein Becken und dann auf **Parameterzuordnung**.
2. Tippe auf den Namen eines Geräts, um es zu öffnen. Um einen Messwert schneller zu finden, gib einen Teil seines Namens in **Parameter suchen** ein.
3. Tippe auf den Messwert. **Diesen Messwert anzeigen als** öffnet sich.
4. Tippe auf den Parameter, als der er angezeigt werden soll. Deine Wahl wird sofort gespeichert und das Blatt schließt sich.
5. Prüfe in der Liste die Bezeichnung **Angezeigt als** des Messwerts. Sie nennt jetzt den Parameter, den du gewählt hast.

![Diesen Messwert anzeigen als, mit deinen Parametern und der Angabe, woher jeder seine Messwerte bekommt](img/mobile-probes-shows-as.webp "Jeder Parameter sagt, woher seine Messwerte kommen: von einem Gerät, gerade von keinem oder aus deinen ICP-Ergebnissen.")

Tippe auf einen Messwert, um **Diesen Messwert anzeigen als** zu öffnen. Oben steht der Messwert selbst: das Gerät, der Name des Messwerts und sein Wert. Darunter:

- **Deine Parameter** listet jeden Parameter dieses Beckens auf. Jede Option sagt, woher ihre Messwerte kommen, damit du nie zwischen zwei ähnlichen Namen raten musst:
  - *Kommt von* und der Name des Geräts, das ihn liefert, oder *Kommt auch von* und der Name eines anderen Geräts, wenn dieser Messwert bereits als dieser Parameter angezeigt wird.
  - *Kein Gerät liefert ihn gerade. Letzter Wert …* mit der Zeitangabe, für einen Parameter, dessen Gerät verstummt ist.
  - *Aus deinen Testergebnissen* oder *Aus ICP-Ergebnissen*, mit dem letzten Wert, für einen Parameter, der nur deine eigenen Ergebnisse hat.

  Der Stift (**Umbenennen**) neben einem Parameter gibt ihm deinen eigenen Namen. Er erscheint auf deinem Dashboard, in Warnungen und in Reef Buddy. Lass den Namen leer, um ihn zurückzusetzen.
- **Weitere Parameter** ist eingeklappt. Dort stehen die Standardparameter, die dieses Becken noch nicht hat.
- **Neuer Parameter…** erstellt einen eigenen Parameter, getrennt von deinen anderen Parametern. Siehe unten.
- **Diesen Messwert nicht anzeigen** (*Cora ignoriert ihn*) verhindert, dass der Messwert als irgendein Parameter aufgezeichnet wird. Ein ausgeblendeter Messwert erscheint auf keinem Dashboard und löst keine Warnungen aus.

Das Blatt endet mit *Wird gespeichert, sobald du wählst. Frühere Messwerte bleiben, wo sie sind.*

![Das Ende von Diesen Messwert anzeigen als, mit Weitere Parameter, Neuer Parameter und Diesen Messwert nicht anzeigen](img/mobile-probes-shows-as-end.webp "Scrolle ans Ende für Weitere Parameter, Neuer Parameter… und Diesen Messwert nicht anzeigen.")

### Neuer Parameter {#new-parameter}

Nutze **Neuer Parameter…**, wenn ein Messwert nicht mit einem anderen gleichen Namens vermischt werden soll, zum Beispiel eine zweite pH-Sonde im Technikbecken. Cora öffnet **Neuer Parameter** und erklärt, dass der Messwert dieses Geräts als eigener Parameter angezeigt wird und dass seine Einheit vom Gerät kommt.

1. Scrolle in **Diesen Messwert anzeigen als** ans Ende und tippe auf **Neuer Parameter…**.
2. Gib einen **Namen** ein. Ein beliebiger Name, zum Beispiel *pH Technikbecken* oder *pH 2*, bis zu 32 Zeichen.
3. Tippe auf **Erstellen**. **Erstellen** bleibt grau, bis der Name etwas enthält. **Abbrechen** schließt das Fenster und ändert nichts.

![Das Fenster Neuer Parameter](img/mobile-probes-new-parameter.webp "Neuer Parameter: Der Messwert bekommt einen eigenen Parameter, mit der Einheit vom Gerät.")

Der Messwert speist nun den neuen Parameter. Der Name behält die Schreibweise, die du eingegeben hast. Gibst du den Namen eines Parameters ein, den du schon hast, wird der Messwert diesem zugeordnet, und sein Name bleibt unverändert. Es wird kein Warnbereich von einem anderen Parameter übernommen.

## Tests und Laborergebnisse {#tests-and-lab-results}

Deine eigenen Testkit-Ergebnisse und deine ICP-Ergebnisse stehen ganz unten unter **Tests und Laborergebnisse**. Der Abschnitt ist zunächst zugeklappt, weil allein ein ICP-Bericht Dutzende Elemente hat. Tippe darauf, um ihn zu öffnen. Die Ergebnisse sind gruppiert unter **ICP-Ergebnisse** und **Deine Testergebnisse**.

Jedes Ergebnis wird wie der Messwert eines Geräts einem Parameter zugeordnet. Tippe auf eines, um **Diesen Messwert anzeigen als** zu öffnen und den Parameter zu wählen, als der es angezeigt wird, zum Beispiel um den pH-Wert eines Testkits getrennt von dem einer Sonde zu halten. Cora sagt es im Abschnitt: Neue Ergebnisse folgen deiner Wahl, frühere bleiben, wo sie sind. Ein Test- oder ICP-Ergebnis wird nie verworfen, deshalb gibt es dafür kein **Diesen Messwert nicht anzeigen**.

Parameter, die kein Messwert oben speist und die keine Tests sind, stehen unter **Andere Parameter**. Tippe auf einen, um ihn umzubenennen.

## Mehrere Sonden für einen Parameter {#multiple-probes}

Werden zwei Messwerte als derselbe Parameter angezeigt, ob von zwei Sonden an einem Gerät oder von zwei verschiedenen Geräten, erscheint oben in der Liste ein Banner. Es sagt zum Beispiel *pH erhält Messwerte von 2 Geräten* (oder *2 Sonden*), gefolgt davon, was Cora tut: *Der neueste wird angezeigt.* oder *Verwendet* das Gerät, das du gewählt hast. Tippe darauf oder auf **Einen wählen**, um das Blatt zu öffnen.

- **Neuester Messwert** (*Das Gerät, das zuletzt gemeldet hat*) lässt Cora das Gerät nehmen, das zuletzt gemeldet hat. Die anderen bleiben im Verlauf.
- Wähl ein Gerät oder eine Sonde, um nur ihr zu folgen. Jede zeigt ihren Wert und vor wie vielen Minuten sie gemeldet hat. Deine Wahl gilt für diesen Parameter überall im Becken: Kachel, Diagramm und Alarme, nicht nur ein Widget.
- **Einen davon separat anzeigen** (*Zum Beispiel eine zweite Sonde im Technikbecken*) fragt **Welcher soll separat angezeigt werden?** und öffnet dann **Diesen Messwert anzeigen als** für den, den du wählst.

Meldet sich ein gewähltes Gerät nicht mehr, sagt das Banner *Meldet sich nicht mehr seit* und die Zeit und bietet **Neuesten verwenden** an, damit eine tote Sonde einen Messwert nicht festhalten kann.

Vergleichen kannst du die Quellen in [der Parameteransicht](/help/mobile-metric-detail).

Melden zwei Quellen denselben Parameter, gewinnt die neueste Messung. Ein Wert auf dem Bildschirm wird nur durch einen Messwert mit späterem Messzeitpunkt ersetzt, egal von welchem Gerät. Ein älterer Messwert, oder ein Gerät, das einen alten noch einmal schickt, geht in den Verlauf und überschreibt den aktuellen Wert nicht. Hast du ein Gerät gewählt, folgt Cora stattdessen diesem Gerät.

Das Beckenprofil hat außerdem einen Bereich **Wasserwert-Quellen** (er ist ausgeblendet, während du ein neues Becken anlegst). Er legt dasselbe in kürzerer Form fest. Nutze die Parameterzuordnung, wenn du alle Geräte und Messwerte an einem Ort haben willst.

## Sondenpflege erfassen {#recording-probe-care}

Sonden driften. Wenn du eine Sonde kalibrierst, reinigst oder ersetzt, sag es Cora, damit es den Sprung im Messwert nicht für eine echte Änderung im Becken hält.

1. Tippe auf dem Dashboard auf das Widget des Wasserwerts, zum Beispiel pH, Temperatur, Salinität oder ORP.
2. Tippe in der oberen Leiste auf **Sondenpflege erfassen** (das Sensorsymbol).
3. Wähl, was du gemacht hast: **Kalibriert**, **Gereinigt**, **Ersetzt**, **Neu positioniert** oder **Mit Referenz verglichen**. Du kannst einen **Referenzmesswert** und eine Notiz hinzufügen.
4. Tippe auf **Sondenpflege erfassen**.

Die Wasserwert-Ansicht zeigt dann, wie lange es her ist, dass diese Sonde kalibriert wurde. Sondenpflege eignet sich auch gut als wiederkehrende [Wartungsaufgabe](/help/mobile-maintenance).

:::note Kalibrierdaten erklären Abweichungen
Widersprechen sich eine Sonde und ein Testkit, prüf, wann du die Sonde zuletzt kalibriert hast. Das ist meist die Antwort.
:::
