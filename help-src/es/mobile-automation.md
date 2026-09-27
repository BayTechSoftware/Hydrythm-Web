---
title: Automatizaciones y escenas
description: Crea reglas que se ejecutan solas (disparadores, condiciones, acciones) y agrúpalas en escenas.
section: Cora Mobile
reviewed: 2026-09-27
order: 17
group: Alerts and automation
---

Una automatización es una regla que Cora ejecuta por ti: *cuando pasa esto, comprueba aquello, y luego haz esto.* Las escenas agrupan varias acciones en una sola cosa que puedes ejecutar o programar.

**Ajustes → Automatización.**

![La lista de automatizaciones](img/mobile-automation.webp "Automatizaciones y Escenas son pestañas separadas. Cada regla tiene un interruptor de activación.")

La pantalla tiene dos pestañas (**Automatizaciones** y **Escenas**) y un botón de **Nueva automatización**. Cada regla muestra un resumen de una línea de lo que hace, un interruptor de activación y un menú para editarla o eliminarla. Una regla que todavía no se ha ejecutado se marca como tal.

:::warning Esto actúa sobre equipo real
Una regla que cambia el estado de una bomba lo cambia tanto si estás mirando como si no. Crea una a la vez y comprueba que cada una hace lo que esperas antes de añadir la siguiente.
:::

## La forma de una regla

Toda regla tiene las mismas tres partes:

**Disparador**: qué la activa
**Condiciones**: qué también tiene que ser cierto
**Acciones**: qué hace después, en orden

## Qué puede activar una regla

Cuatro cosas:

| Disparador | Se activa cuando |
|---|---|
| **Parámetro** | Un parámetro cruza un valor que fijaste, en una dirección que elijas |
| **Alerta** | Se genera una alerta, se cierra, o cualquiera de las dos |
| **Horario** | Una hora del día, en tu propia zona horaria |
| **Estado del dispositivo** | Un dispositivo se desconecta o vuelve a conectarse |

## Condiciones

Las condiciones deciden si las acciones se ejecutan de verdad. Tienes las comparaciones habituales (igual, distinto, mayor que, menor que, y así sucesivamente) y puedes combinarlas con **y**, **o** y **no**.

También hay una condición de **paso**, que comprueba cómo resultó el paso *anterior*. Eso es lo que te permite escribir "intenta esto; si no funcionó, haz aquello en su lugar".

## Qué puede hacer una regla

Una acción que necesita equipo solo se ofrece en un acuario que tenga ese equipo:

| Acción | Qué hace |
|---|---|
| **Controlar equipo del Apex** | Cambiar el estado de una toma |
| **Controlar un equipo Red Sea** | Manejar una unidad ReefBeat |
| **Controlar una bomba de circulación** | Fijar el flujo, el modo de olas o la potencia de una bomba Jecod, o **Pausar para alimentar**: el Cora Max del acuario devuelve la bomba a su estado cuando termina la alimentación |
| **Controlar un equipo Cora** | Cambiar el estado de un enchufe inteligente |
| **Controlar dispositivo IR** | Enviar una orden por infrarrojos |
| **Ejecutar ciclo de alimentación del Apex** | Iniciar una alimentación |
| **Ejecutar una prueba del Trident** | Activar una prueba |
| **Notificarme** | Enviarte un aviso push |
| **Esperar antes del siguiente paso** | Pausar antes de continuar |
| **Ejecutar una escena** | Ejecutar otra escena desde dentro de esta regla |
| **Gestionar una automatización** | Activar o desactivar otra regla |
| **Dosificar una cabeza DŌS** | Ejecutar una dosis medida en una cabeza DŌS |

:::warning Dosificar desde una regla es irreversible y tiene un límite
Una dosis no se puede sacar de nuevo del acuario. El cabezal debe estar **calibrado** antes de que una regla pueda dosificar desde él, y la dosificación sin supervisión tiene un límite de **10 mL por cabezal al día**; una regla no puede superarlo sea como sea que esté escrita. Las acciones de dosificación solo aparecen una vez que tus cabezales se reconocen como cabezales de dosificación.
:::

:::note Usa Esperar para secuenciar pasos dentro de una regla
Una pausa permite que una sola regla realice un procedimiento ordenado (por ejemplo, apagar una toma, esperar y luego volver a encenderla) sin una segunda regla y un horario.
:::

## Escenas

Una escena es un grupo con nombre de acciones que puedes ejecutar a demanda, desde un horario, o desde dentro de otra regla: "Cambio de agua", "Modo foto", "Noche".

Una escena puede llamar a otra escena. Cora se niega a ejecutar una escena anidada más allá de su límite de profundidad, y se niega a una escena que se llamaría a sí misma, para evitar un bucle que seguiría actuando sobre el acuario de forma indefinida.

Después de que una escena se ejecuta, se te informa de qué pasó, paso a paso, incluido cualquier fallo.

Ejecutar una escena a mano te pide confirmar primero, ya que una escena puede cambiar el estado de varios equipos a la vez.

## Escenas creadas en Cora Max

Las escenas también se pueden crear y editar directamente en una tableta Cora Max, no solo en el teléfono: es el mismo conjunto de escenas de cualquier forma, compartido en toda la cuenta. Si un hogar tiene un Cora Max más antiguo, todavía puede ejecutar una escena creada en el teléfono; solo la edición en el propio dispositivo es una funcionalidad más reciente, así que una tableta más antigua puede mostrar una escena sin permitirte cambiarla ahí. Edítala desde el teléfono en su lugar.

## Desactivar una regla

Cada regla tiene un interruptor de activación. Desactivar una conserva su definición, útil cuando quieres recuperar una regla la próxima temporada en lugar de crearla de nuevo.

## Ver qué hizo una regla

Cada acción que realiza una regla se registra con la regla como su causa. Consulta **[Actividad](/help/mobile-activity)**.
