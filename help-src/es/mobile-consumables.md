---
title: Consumibles
description: Configura alertas de reposición para reactivo, envases de dosificación, depósitos y medios.
section: Cora Mobile
reviewed: 2026-09-09
order: 14
group: Equipment
---

El equipo que consume algo (reactivo, líquido de dosificación, agua de reposición, medio filtrante) puede decirle a Cora cuánto queda. Cora puede avisarte antes de que se acabe.

## Configurar una alerta de reposición

Abre el dispositivo (desde la pestaña **Dispositivos**, o tocando su casilla en el panel), y luego usa la **campana** en la barra superior.

![Alertas de reposición para una unidad de dosificación](img/mobile-consumables.webp "Un umbral por cabezal, cada uno activado o desactivado de forma independiente.")

El equipo con más de un envase tiene un umbral por envase, así que un cabezal que vigilas de cerca y uno que casi no tocas pueden configurarse de forma distinta.

**La mayoría de los umbrales se fijan en días, no en volumen.** Cora calcula cuánto durará lo que queda al ritmo con el que realmente lo estás usando, que es el número sobre el que puedes actuar; "quedan cuatro días de calcio" te dice algo que "quedan 180 mL" no te dice.

| Dispositivo | Umbral en |
|---|---|
| Trident | Pruebas restantes, y cuán llena está la botella de residuos |
| Cabezal de dosificación | Días de suplemento restantes; algunos también ofrecen mililitros restantes |
| ATO | Días de depósito restantes |
| Rodillo de estera | Días de rollo restantes |

Una alerta de consumible se comporta como cualquier otra alerta: aparece en el [Centro de alertas](/help/mobile-alerts) y puede enviarse a tu teléfono. Recibes **una** notificación cuando se supera un nivel, no un flujo repetido, y se cierra cuando el nivel vuelve a estar por encima del umbral.

## Elegir un umbral

Fíjalo con suficiente antelación para poder actuar. Un umbral que se activa el día en que algo se acaba no da ningún aviso.

:::warning Algunos equipos no se detienen al vaciarse
Un cabezal de dosificación con el envase vacío sigue ejecutando su programa e informa de dosis que no llegó a entregar. La alerta de reposición es lo que evita esto, así que configura una para cada cabezal desde el que dosifiques.
:::

## Después de rellenar

Restablece o actualiza el nivel en la página del dispositivo para que la alerta se cierre y el próximo aviso se calcule correctamente.
