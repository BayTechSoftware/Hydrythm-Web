---
title: Escenas en Cora Max
description: Crear, ejecutar y editar escenas directamente en la pantalla de Cora Max.
section: Cora Max
reviewed: 2026-09-27
order: 15
group: Automation
---

Una **escena** es un conjunto guardado de acciones sobre el equipo que se ejecuta junto, ya sea durante un tiempo fijo o hasta que la detengas. Las escenas funcionan igual tanto si las creas en tu teléfono como en Cora Max; esta página trata de hacerlo en la pared.

## Dónde encontrar las escenas

**Ajustes → Automatizaciones** lista todas las escenas de todos los acuarios que tienes, con un chip de filtro por cada acuario cuando tienes más de uno. Abre la misma lista tanto si la escena se creó en el teléfono como en Cora Max.

Toca una escena para editarla, o toca **+** para crear una nueva. Si tienes más de un acuario y no hay ningún filtro elegido, Cora Max pregunta a qué acuario pertenece la escena nueva.

## Crear una escena

1. Dale un **nombre** a la escena.
2. Añade **pasos**. Desde Cora Max, un paso puede cambiar una toma del Apex (**Encendido**, **Apagado** o **Auto**) o un enchufe Zigbee (**encendido**, **apagado** o **alternar**). Los pasos añadidos en el teléfono para otros tipos de equipo también se muestran aquí, y se pueden reordenar o eliminar igualmente, aunque esta pantalla no pueda añadir otro paso de ese tipo.
3. Elige cuánto dura: un número fijo de minutos, o **permanente** (sigue en marcha hasta que la detengas).
4. Elige si ejecutar la escena necesita un paso de **confirmación**. Déjalo activado a menos que estés seguro de que la escena nunca toca nada que sería inseguro cambiar sin una segunda mirada.
5. Guarda.

:::note Los cabezales de dosificación DŌS nunca son un paso de escena
Una escena, creada en Cora Max o en el teléfono, nunca puede activar un cabezal de dosificación. Esto es intencionado: una dosis no es el tipo de acción que una escena debería poder desencadenar por accidente.
:::

## Ejecutar una escena

Las escenas aparecen como casillas en el panel. Toca **Ejecutar** para iniciar una.

Si la escena necesita confirmación, Cora Max lista exactamente lo que está a punto de hacer, una línea por paso, antes de que ocurra nada. Léelo, y luego elige ejecutarla o cancelar.

Mientras una escena programada está en marcha, su casilla muestra una cuenta atrás hasta que termina, y un botón **Detener** para acabarla antes de tiempo. La casilla de una escena permanente se queda en su estado de ejecución hasta que la detienes.

Ejecutar o detener una escena siempre pasa por Cora Cloud, igual que cualquier otra orden; consulta [Qué se cambió, y con qué](/help/max-activity) para saber dónde se registra el resultado.

**Si no funciona:** si una escena no se ejecuta o no se detiene, consulta [Solución de problemas](/help/troubleshooting).

:::note El bloqueo infantil también cubre las escenas
Si el [bloqueo infantil](/help/max-voice) está activado, ejecutar o detener una escena desde esta pantalla queda bloqueado junto con cualquier otro control. Las preguntas sobre una escena siguen funcionando por voz; iniciarla o detenerla no.
:::

## Editar o eliminar una escena

Abre la escena desde **Ajustes → Automatizaciones**, o mantén pulsada su casilla en el panel, para cambiar su nombre, sus pasos, su duración o su ajuste de confirmación, o para eliminarla.

:::note Las pantallas Cora Max más antiguas pueden ejecutar una escena pero no editarla
Crear y editar escenas en la pared es una funcionalidad más reciente de Cora Max. Un Cora Max más antiguo en la misma cuenta todavía puede mostrar y ejecutar una escena creada en el teléfono o en un Cora Max más reciente; simplemente no puede cambiarla. Actualiza Cora Max, o edita la escena desde el teléfono o desde una pantalla más reciente, si esto surge.
:::

Consulta [Escenas y automatizaciones](/help/mobile-automation) para más detalle sobre qué puede hacer una escena, y cómo se crean en el teléfono.
