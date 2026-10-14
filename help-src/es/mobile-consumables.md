---
title: Consumibles y alertas de reposición
description: Configura alertas de reposición para reactivos, envases de dosificación, depósitos de reposición y rollos de filtro, y avisa a Cora cuando hayas rellenado.
section: Cora Mobile
reviewed: 2026-10-13
order: 16
group: Equipment
---

Usa las alertas de reposición para que Cora te avise antes de que se acabe el reactivo, el líquido de dosificación, el agua de reposición o el rollo de filtro. Abre el dispositivo desde **Dispositivos** (o toca su casilla en el panel) y después toca la **campana** de la barra superior.

## Configurar una alerta de reposición {#setting-a-refill-alert}

![La hoja de alertas de una ReefDose 4, con un umbral de días restantes y un interruptor para cada cabezal](img/mobile-consumables.webp "Un umbral por cabezal, cada uno con su propio interruptor.")

La hoja se llama **Alertas:** seguido del nombre del dispositivo. Si el equipo tiene más de un envase, cada uno tiene su propio umbral y su propio interruptor, así que puedes configurar de forma distinta un cabezal que vigilas de cerca y otro que casi no tocas. Si desactivas un interruptor, el valor se guarda para más adelante.

Dónde se configura:

- **La mayoría de los dispositivos**: la campana de la barra superior de la página del dispositivo.
- **DŌS**: la tarjeta **Alertas** de la página del DŌS, o la campana. Consulta [Alertas de dosificadores](/help/mobile-device-control#doser-alerts).
- **Dosificadoras AquaWiz**: su regla en la pestaña **Reglas** del [Centro de alertas](/help/mobile-alerts).

La mayoría de los umbrales van en días, no en volumen. Cora calcula cuánto te durará lo que queda según lo que estás gastando. "Quedan cuatro días de calcio" es algo con lo que puedes actuar. "Quedan 180 mL", no.

## De qué te puede avisar {#thresholds}

| Dispositivo | Umbral | Empieza en |
|---|---|---|
| Trident | **Pruebas restantes** (el reactivo más bajo) | 10 pruebas |
| Trident | **Botella de residuos** (con la botella llena falla la siguiente prueba) | 85% llena |
| Cabezal DŌS | *[cabezal] · días restantes* | 7 días |
| Cabezal DŌS | *[cabezal] · restante*, en mL | 100 mL |
| Cabezal DŌS que saca agua vieja | **Espacio restante en el contenedor de residuos** | |
| Cabezal DŌS | **Alertas de dosis omitida** (un interruptor) | |
| Cabezal ReefDose | Días de suplemento que quedan | 7 días |
| ReefATO+ | **Autonomía del depósito**, calculada según el uso reciente de la reposición | 2 días |
| ReefMat | **Rollo restante**, calculado según lo rápido que avanza el rodillo | 3 días |
| AquaWiz | Suplemento de alcalinidad que queda | 100 mL |


Una alerta de consumible funciona como cualquier otra alerta. Aparece en el [Centro de alertas](/help/mobile-alerts) y puede llegarte como notificación al teléfono. Recibes **una** sola notificación cuando se cruza un nivel, y la alerta desaparece cuando el nivel vuelve a estar por encima del umbral.

## Elegir un umbral {#choosing-a-threshold}

Ponlo con margen suficiente para poder reaccionar. Si salta el mismo día en que algo se acaba, no te sirve de aviso.

:::warning Algunos equipos siguen funcionando vacíos
Un cabezal DŌS con el envase vacío sigue con su programa y registra dosis que nunca dio. No tiene ningún aviso propio de nivel bajo. La alerta de reposición es la forma de detectarlo, así que configura una para cada cabezal con el que dosifiques.
:::

## Después de rellenar {#after-refilling}

Díselo a Cora en la página del dispositivo, para que la alerta desaparezca y el siguiente aviso se calcule desde el nivel correcto.

| Dispositivo | Toca |
|---|---|
| Cabezal DŌS | **Llenar** y después **Lleno**, o pon el **Volumen restante** |
| Contenedor de residuos del DŌS | Restablece su espacio libre a lleno después de vaciarlo |
| Cabezal ReefDose | **Restante en la botella** |
| ReefMat | **Nuevo rollo** después de poner un rollo nuevo |

Trident, ReefATO+ y AquaWiz informan de sus propios niveles, así que no hay nada que restablecer en Cora.
