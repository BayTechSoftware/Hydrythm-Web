---
title: Escenas en Cora Max
description: Crea, ejecuta, edita y elimina escenas en Cora Max, desde Ajustes → Automatizaciones o desde una tarjeta de escena en el panel.
section: Cora Max
reviewed: 2026-10-24
order: 9
group: Alerts and automation
twin: mobile-automation
---

Una **escena** es un conjunto guardado de acciones sobre los equipos que se ejecutan juntas, durante un tiempo fijo o hasta que la detienes. Puedes crear, ejecutar y editar escenas en Cora Max. Las escenas creadas en tu teléfono y en Cora Max son las mismas. Las reglas de automatización (las de "cuando pase esto, haz aquello") se configuran en tu teléfono. Más información en [Automatizaciones y escenas](/help/mobile-automation).

![La lista de escenas en Cora Max, con una etiqueta de filtro para cada acuario y un botón Nueva escena](img/max-automation.webp "La lista de escenas, filtrada por acuario. Si todavía no hay escenas, lo dice y ofrece Nueva escena.")

## Dónde están las escenas

**Ajustes → Automatizaciones** abre **Escenas**, la lista de todas las escenas de todos tus acuarios. Si tienes más de un acuario, hay una etiqueta de filtro para cada uno, además de **Todos los acuarios**.

Toca una escena para editarla, o toca **Nueva escena** para crear una. Si tienes más de un acuario y no hay ningún filtro elegido, Cora Max pregunta **¿Para qué acuario es esta escena?**

## Crear una escena

![Un formulario Nueva escena vacío en Cora Max](img/max-scene-builder.webp "Una escena nueva: un nombre, Permanente o Temporizada, Preguntar antes de ejecutar y después Añadir paso.")

1. Escribe un **Nombre de la escena**.
2. Toca **Añadir paso** y elige qué hace el paso. Solo ves los tipos de equipo que tiene este acuario:
   - **Toma de Apex**: pon una toma de Neptune Apex en **ENCENDIDO**, **APAGADO** o **AUTO**.
   - **Controlar un equipo Red Sea**: por ejemplo **ReefDose: dosificar ahora**, **ReefDose: configurar dosis diaria**, **ReefRun: configurar velocidad de la bomba**, **ATO: iniciar un llenado manual** o **ReefMat: avanzar el rollo**.
   - **Controlar una bomba de circulación**: fija el caudal o el modo de olas de una bomba Jecod, enciéndela o apágala, o usa **Pausar para alimentar**.
   - **Iniciar una prueba Trident**: alcalinidad, combinada o nutrientes. Cada ejecución gasta reactivo.
   - **Iniciar un ciclo de alimentación Apex**: elige el ciclo. El Apex lleva el temporizador y se reanuda solo.
3. Añade más pasos de la misma forma. Puedes reordenarlos o quitarlos. Un paso que esta pantalla no puede editar dice **No editable aquí**. Edítalo en tu teléfono.
4. Elige cuánto dura. **Temporizada** dura los minutos que pongas en **Ejecutar durante (minutos)**. **Permanente** dura hasta que la detienes.
5. Deja **Preguntar antes de ejecutar** activado salvo que estés seguro de que la escena nunca toca nada que necesite una segunda mirada.
6. Toca **Guardar**.

:::note Dosis en una escena
Un cabezal Neptune DŌS nunca puede ser un paso de escena. Un paso **ReefDose: dosificar ahora** sí puede, y tiene su propio **Máximo por dosis (ml)**. Déjalo vacío para 10 mL. Una dosis por encima de ese tope se rechaza, nunca se reduce. Deja **Preguntar antes de ejecutar** activado en cualquier escena que dosifique.
:::


## Ejecutar una escena

Las escenas aparecen como tarjetas en el panel. Toca **Ejecutar** para empezar una.

Si la escena pregunta antes de ejecutarse, Cora Max lista primero lo que va a hacer, una línea por paso. Léelo y después ejecútala o cancela.

Mientras una escena temporizada está en marcha, su tarjeta hace una cuenta atrás hasta el final y muestra **Detener** por si quieres terminarla antes. La tarjeta de una escena permanente la muestra en marcha hasta que tocas **Detener**. Cuando una escena termina o la detienes, la tarjeta muestra **Restaurando…** mientras Cora devuelve los equipos a como estaban.

Ejecutar o detener una escena pasa por Cora Cloud, como cualquier otra orden. Encontrarás el resultado en [Actividad](/help/max-activity).

También puedes ejecutar una escena por voz: *"Ejecuta la escena de cambio de agua."* El bloqueo infantil lo impide como cualquier otro control. Si no, usa la tarjeta, **Ajustes → Automatizaciones** o tu teléfono.

Si una escena no se ejecuta o no se detiene, echa un vistazo a [Solución de problemas](/help/troubleshooting).

:::note El bloqueo infantil también cubre las escenas
Mientras el [Bloqueo infantil](/help/max-settings#child-lock) tiene la pantalla bloqueada, no puedes ejecutar, detener ni editar una escena desde ella, igual que cualquier otro control.
:::

Un paso que falla o que tendría que esperar no se queda pendiente. Caduca al instante, la ejecución se registra como fallida y recibes una notificación que nombra la automatización, el paso y el motivo. Un paso falla, por ejemplo, si su dispositivo está sin conexión, si ningún Cora Max puede ejecutarlo, si el dispositivo lo rechaza o no responde, o si un calentador o enfriador se acaba de conmutar. Por un paso en un acuario eliminado no recibes notificaciones.

## Editar o eliminar una escena

Para cambiar una escena, ábrela desde **Ajustes → Automatizaciones** o mantén pulsada su tarjeta en el panel. Cambia lo que necesites y toca **Guardar**. Para quitarla, toca **Eliminar escena**. No se puede deshacer.

:::note Un Cora Max más antiguo puede ejecutar una escena pero no editarla
Las versiones antiguas de Cora Max siguen mostrando y ejecutando todas las escenas, pero no pueden cambiar ninguna. Actualiza Cora Max ([Actualizaciones y recuperación](/help/max-updates)), o edita la escena en tu teléfono.
:::
