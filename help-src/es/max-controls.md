---
title: Tomas y controles
description: Cambiar el estado de las tomas desde Cora Max, usar el modo alimentación, y qué significa Auto en realidad.
section: Cora Max
reviewed: 2026-09-09
order: 5
group: Equipment
---

Cora Max puede cambiar el estado del equipo de tu sistema: desde los widgets de control en el panel, desde el cajón Tomas y alimentación, o por voz.

:::warning Estos controles actúan sobre tu acuario
No hay deshacer. Las tomas marcadas con un candado te piden confirmar primero; el resto se aplica en cuanto tocas. Una orden puede volver como **Confirmado**, **Sin confirmar** (enviado, no llegó ninguna respuesta), **Rechazado** o **Sin cambios**; consulta [Cómo controlar tu equipo](/help/mobile-device-control).
:::

## Los tres estados

Cada toma está en uno de tres estados.

**Auto** devuelve la toma a su programación del Apex. Aquí es donde debería estar una toma la mayor parte del tiempo.

**Apagado** y **Encendido** son anulaciones manuales. Surten efecto de inmediato y **se quedan así hasta que las cambies de vuelta**. No caducan, y nada las devuelve por ti.

:::warning Una anulación manual no caduca
Vuelve a poner **Auto** cuando termines; nada lo hace por ti. Todavía se puede cambiar más tarde por ti, por voz o por una automatización; una anulación no es un bloqueo.
:::

## Cambiar el estado desde el panel

Los widgets de control muestran los tres estados con el actual resaltado. Toca el estado que quieras.

Algunas tomas llevan un **candado**. No significa que haya que desactivarlo en algún sitio; significa que la toma te pide confirmar antes de cambiar, así que un toque accidental no puede cambiar algo crítico. Consulta más abajo.

## El cajón de controles

Tira hacia arriba de la pestaña en la parte inferior del panel para abrir **Controles**: todas las tomas del sistema en un solo lugar, tengan o no un widget, más los ciclos de alimentación.

![El cajón de controles](img/max-controls.webp "Ciclos de alimentación en la parte superior, y después cada toma.")

Una toma que lleva un **candado** requiere una confirmación explícita antes de cambiar. Tocarla abre un cuadro de diálogo que nombra la toma, su estado actual y la anulación que estás a punto de aplicar. Es un paso de confirmación, no un bloqueo que haya que desactivar en otro sitio.

## Modo alimentación

El modo alimentación es la forma segura de pausar el flujo para alimentar. Pausa el equipo que debe pausarse, deja en paz el que no debe pausarse, y **lo restaura todo por sí solo** cuando se cumple el tiempo.

Úsalo en lugar de apagar las bombas a mano, porque restaura el sistema sin depender de que lo recuerdes.

Los ciclos de alimentación se identifican con letras **A**, **B**, **C** y **D**: los ciclos que define tu controlador, cada uno pausando un conjunto distinto de equipo. Elige el que corresponda a lo que estás haciendo. **Cancelar** termina un ciclo en curso antes de tiempo y lo restaura todo de inmediato.

Inícialo desde el cajón de controles, o di *"inicia el modo alimentación"*.

## Por voz

Puedes cambiar el estado de las tomas por voz: *"apaga el skimmer"*, *"vuelve a poner el ventilador en auto"*.

Cualquier cosa que llegue a tu equipo se **confirma antes de que ocurra**: Cora te dice qué está a punto de hacer y espera a que estés de acuerdo. No actuará sobre una instrucción de la que no esté segura.

Consulta **[Hablar con Cora](/help/max-voice)**.

## Ver qué pasó

Cada solicitud se registra, junto con qué la pidió (esta aplicación, una pantalla Cora, la voz, el Assistant, una regla de automatización, un botón inteligente o tu cuenta) y cómo viajó. En tu teléfono eso es **Ajustes → Actividad**.

Es el primer sitio donde mirar cuando algo cambió y no sabes por qué.
