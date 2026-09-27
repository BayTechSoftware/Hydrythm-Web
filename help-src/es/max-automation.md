---
title: Escenas en Cora Max
description: Crea, ejecuta y edita escenas directamente en la pantalla de Cora Max.
section: Cora Max
reviewed: 2026-09-27
order: 15
group: Automation
---

Una **escena** es un grupo de acciones sobre el equipo que se ejecutan juntas, durante un tiempo fijo o hasta que la detengas. Funcionan igual si las creas en el teléfono o en Cora Max. Aquí verás cómo hacerlo desde la pantalla de pared.

## Dónde están las escenas

En **Ajustes → Automatizaciones** tienes todas las escenas de todos tus acuarios. Si tienes más de uno, arriba aparece un filtro por acuario. La lista es la misma, da igual dónde se creara cada escena.

Toca una escena para editarla o toca **+** para crear una nueva. Si tienes varios acuarios y no has elegido ningún filtro, Cora Max te pregunta a qué acuario pertenece la escena nueva.

## Crear una escena

1. Ponle un **nombre**.
2. Añade **pasos**. Desde Cora Max, un paso puede cambiar una toma del Apex (**Encendido**, **Apagado** o **Auto**) o un enchufe Zigbee (**encendido**, **apagado** o **alternar**). Si añadiste desde el teléfono pasos para otros equipos, también aparecen aquí y puedes reordenarlos o quitarlos, aunque desde esta pantalla no puedas añadir otro igual.
3. Elige cuánto dura: unos minutos fijos o **permanente** (sigue hasta que la detengas).
4. Decide si la escena pide **confirmación** antes de ejecutarse. Déjalo activado salvo que tengas claro que la escena nunca toca nada que sea peligroso cambiar sin revisarlo.
5. Guarda.

:::note Los cabezales DŌS nunca pueden ser un paso de escena
Ninguna escena, creada en Cora Max o en el teléfono, puede activar un cabezal de dosificación. Una dosis no debe poder dispararse por accidente desde una escena.
:::

## Ejecutar una escena

Las escenas aparecen como casillas en el panel. Toca **Ejecutar** para iniciar una.

Si la escena pide confirmación, Cora Max te enseña antes lo que va a hacer, una línea por paso. Léelo y elige si ejecutarla o cancelar.

Mientras está en marcha una escena de duración fija, su casilla muestra una cuenta atrás y un botón **Detener** para acabarla antes. La casilla de una escena permanente se muestra en marcha hasta que la detienes.

Iniciar o detener una escena siempre pasa por Cora Cloud, como cualquier otra orden. El resultado queda registrado en [Actividad](/help/max-activity).

Si una escena no se inicia o no se detiene, consulta [Solución de problemas](/help/troubleshooting).

:::note El bloqueo infantil también afecta a las escenas
Con el [bloqueo infantil](/help/max-voice) activado, no puedes iniciar ni detener escenas desde esta pantalla, igual que pasa con los demás controles. Por voz puedes seguir preguntando por una escena, pero no iniciarla ni detenerla.
:::

## Editar o borrar una escena

Abre la escena desde **Ajustes → Automatizaciones**, o mantén pulsada su casilla en el panel. Ahí puedes cambiar el nombre, los pasos, la duración o la confirmación, o borrarla.

:::note Un Cora Max antiguo puede ejecutar escenas pero no editarlas
Crear y editar escenas en la pantalla de pared es una función reciente de Cora Max. Un Cora Max más antiguo de la misma cuenta puede mostrar y ejecutar escenas creadas en el teléfono o en un Cora Max más nuevo, pero no cambiarlas. Si te pasa, actualiza Cora Max o edita la escena desde el teléfono o desde una pantalla más nueva.
:::

Qué puede hacer una escena y cómo se crea en el teléfono se explica en [Escenas y automatizaciones](/help/mobile-automation).
