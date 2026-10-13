---
title: Tomas y controles
description: Enciende y apaga tomas del Apex desde Cora Max, inicia o cancela el modo alimentación, usa el cajón Tomas y alimentación y mira qué significan Auto, Apagado y Encendido.
section: Cora Max
reviewed: 2026-10-13
order: 5
group: Equipment
---

Esta página explica cómo encender y apagar tomas e iniciar el modo alimentación desde Cora Max. Puedes hacerlo desde las casillas de tomas del panel, desde el cajón **Tomas y alimentación** o por voz.

:::warning Estos controles actúan sobre tu acuario
No hay forma de deshacer. Las tomas con candado te piden que confirmes primero. Las demás cambian en cuanto tocas. Una orden puede volver **Confirmado**, **Sin confirmar** (enviada, pero sin respuesta), **Rechazado** o **Sin cambios**. Más información en [Controlar tus equipos](/help/mobile-device-control).
:::

## Los tres estados {#the-three-states}

Cada toma está en uno de tres estados.

**Auto** devuelve la toma a su programación del Apex. La mayor parte del tiempo, ahí es donde debe estar una toma.

**Apagado** y **Encendido** son cambios manuales. Se aplican al momento y **se mantienen hasta que los vuelvas a cambiar**. No caducan, y nada los restablece por ti.

:::warning Un cambio manual no caduca
Vuelve a ponerla en **Auto** cuando termines, porque nada más lo hará. Eso sí, un cambio manual no es un bloqueo. Tú, tu voz o una automatización podéis cambiarlo más tarde.
:::

## Cambiar desde el panel {#switching-from-the-dashboard}

Las casillas de tomas muestran los tres estados, con el actual resaltado. Toca el que quieras.

Algunas tomas tienen un **candado**. Significa que la toma te pide que confirmes antes de cambiar, para que un toque accidental no apague algo crítico. Cuando la tocas, un cuadro de diálogo muestra la toma, su estado actual, el cambio que vas a hacer y lo que eso puede provocar en el acuario. No hay ningún bloqueo que desactivar en otro sitio.

Por defecto, el candado está en calentadores, enfriadores, bombas de retorno, reposición (ATO), comederos y cualquier toma que Cora no sepa clasificar. Las luces, los skimmers, las bombas de circulación, las bombas dosificadoras, los reactores, el UV y los ventiladores cambian con un solo toque.

## El cajón Tomas y alimentación {#the-controls-drawer}

Solo lo verás en un acuario con un Neptune Apex. Toca la pequeña etiqueta **Tomas y alimentación** en la parte de abajo del panel, o desliza hacia arriba en cualquier parte del panel. Se abre **Controles**, con **ALIMENTACIÓN** arriba y **TOMAS** debajo.

![El cajón Controles](img/max-controls.webp "Los ciclos de alimentación arriba y después las tomas elegidas para este panel.")

Muestra las tomas y los ciclos de alimentación que elegiste en **Tomas y alimentación** en el [editor del panel](/help/max-dashboard-editing#outlets-feed), o todos si no elegiste ninguno. Las tomas con candado también te piden que confirmes aquí. Los enchufes de otros controladores se manejan desde sus propias páginas de dispositivo, consulta [Controlar equipos desde Cora Max](/help/max-device-control).

Si al tocar una toma aparece *El Apex no respondió: puede que ya se haya aplicado*, revisa la toma antes de volver a intentarlo.

## Modo alimentación {#feed-mode}

El modo alimentación es la forma segura de detener el caudal mientras alimentas. Tu Apex pausa los equipos que deben pausarse, deja el resto como está y **lo vuelve a poner todo como estaba por sí solo** cuando se acaba el tiempo.

Úsalo en lugar de apagar bombas a mano. Devuelve el sistema a su estado aunque se te olvide.

Los ciclos de alimentación son Feed A, Feed B, Feed C y Feed D, que aparecen como **A**, **B**, **C** y **D** en **ALIMENTACIÓN**. Son los ciclos programados en tu Apex, y cada uno puede pausar un conjunto distinto de equipos. Elige el que encaje con lo que estás haciendo. **Cancelar** termina antes un ciclo en marcha y lo vuelve a poner todo como estaba al momento.

Empieza uno desde el cajón, o di *"empieza el modo alimentación"*.

Si Cora Max dice que el Apex no respondió, puede que la alimentación ya esté en marcha. Revisa la bomba de retorno antes de volver a empezarla.

## Por voz {#by-voice}

Puedes cambiar tomas por voz, por ejemplo *"apaga el skimmer"* o *"vuelve a poner el ventilador en auto"*.

Antes de que nada llegue a tus equipos, Cora **lo comprueba primero contigo**. Te dice lo que va a hacer y espera a que des el visto bueno. Si no está segura de lo que pediste, no actúa.

Más información en [Hablar con Cora](/help/max-voice).

## Ver qué ha pasado {#seeing-what-happened}

Cada solicitud queda registrada, con lo que la pidió y cómo fue, venga de Cora Mobile, de un Cora Max, de la voz, del Asistente o de una automatización. En Cora Max, toca el nombre del acuario en la barra superior y elige **Actividad**. En tu teléfono, está en **Ajustes → Actividad**. Más información en [Actividad en Cora Max](/help/max-activity).

Cuando algo ha cambiado y no sabes por qué, mira ahí primero.
