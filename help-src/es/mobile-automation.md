---
title: Automatizaciones y escenas
description: Crea reglas que funcionan solas (disparadores, condiciones y acciones) y agrúpalas en escenas.
section: Cora Mobile
reviewed: 2026-09-27
order: 17
group: Alerts and automation
---

Una automatización es una regla que Cora ejecuta por ti: *cuando pase esto, comprueba aquello y luego haz esto otro.* Una escena reúne varias acciones en una sola que puedes ejecutar o programar.

**Ajustes → Automatización.**

![La lista de automatizaciones](img/mobile-automation.webp "Automatizaciones y Escenas son pestañas distintas. Cada regla tiene un interruptor para activarla.")

La pantalla tiene dos pestañas, **Automatizaciones** y **Escenas**, y un botón **Nueva automatización**. Cada regla muestra en una línea lo que hace, un interruptor para activarla y un menú para editarla o eliminarla. Las reglas que aún no se han ejecutado llevan una marca.

:::warning Estas reglas mueven equipos de verdad
Si una regla apaga una bomba, la apaga aunque no estés mirando. Crea las reglas de una en una y comprueba que cada una funciona como esperas antes de añadir la siguiente.
:::

## Cómo es una regla

Todas las reglas tienen tres partes:

**Disparador**: lo que la pone en marcha
**Condiciones**: lo que también tiene que cumplirse
**Acciones**: lo que hace después, en orden

## Qué pone en marcha una regla

Hay cuatro disparadores:

| Disparador | Se activa cuando |
|---|---|
| **Parámetro** | Un parámetro pasa de un valor que tú fijas, en la dirección que elijas |
| **Alerta** | Salta una alerta, se resuelve, o cualquiera de las dos cosas |
| **Horario** | Llega una hora del día, en tu zona horaria |
| **Estado del dispositivo** | Un dispositivo se desconecta o vuelve a conectarse |

## Condiciones

Las condiciones deciden si las acciones se ejecutan o no. Tienes las comparaciones de siempre (igual, distinto, mayor que, menor que, etc.) y puedes combinarlas con **y**, **o** y **no**.

También hay una condición de **paso**, que mira cómo salió el paso *anterior*. Con ella puedes escribir "prueba esto y, si no funciona, haz esto otro".

## Qué puede hacer una regla

Las acciones que necesitan un equipo solo aparecen en los acuarios que lo tienen:

| Acción | Qué hace |
|---|---|
| **Controlar equipo del Apex** | Enciende o apaga una toma |
| **Controlar un equipo Red Sea** | Maneja una unidad ReefBeat |
| **Controlar una bomba de circulación** | Ajusta el caudal, el modo de olas o la potencia de una bomba Jecod, o usa **Pausar para alimentar**. El Cora Max del acuario vuelve a poner la bomba como estaba al terminar la alimentación |
| **Controlar un equipo Cora** | Enciende o apaga un enchufe inteligente |
| **Controlar dispositivo IR** | Envía una orden por infrarrojos |
| **Ejecutar ciclo de alimentación del Apex** | Empieza una alimentación |
| **Ejecutar una prueba del Trident** | Lanza una prueba |
| **Notificarme** | Te envía una notificación push |
| **Esperar antes del siguiente paso** | Hace una pausa antes de seguir |
| **Ejecutar una escena** | Ejecuta otra escena desde esta regla |
| **Gestionar una automatización** | Activa o desactiva otra regla |
| **Dosificar una cabeza DŌS** | Da una dosis medida con un cabezal DŌS |

:::warning Dosificar con una regla no tiene vuelta atrás y tiene un límite
Una dosis ya no se puede sacar del acuario. El cabezal tiene que estar **calibrado** para que una regla pueda dosificar con él. La dosificación sin supervisión tiene un máximo de **10 mL por cabezal al día**, y ninguna regla puede pasar de ahí, esté como esté escrita. Las acciones de dosificación solo aparecen cuando Cora reconoce tus cabezales como cabezales de dosificación.
:::

:::note Usa Esperar para ordenar pasos en una regla
Con una pausa, una sola regla puede seguir un procedimiento por pasos. Por ejemplo, apagar una toma, esperar y volver a encenderla. No hace falta una segunda regla ni un horario.
:::

## Escenas

Una escena es un grupo de acciones con nombre, como "Cambio de agua", "Modo foto" o "Noche". Puedes ejecutarla cuando quieras, con un horario o desde otra regla.

Una escena puede llamar a otra. Cora no ejecuta escenas anidadas por encima de su límite de niveles, ni una escena que se llame a sí misma. Así evita un bucle que seguiría actuando sobre el acuario sin parar.

Cuando termina una escena, Cora te cuenta paso a paso qué ha pasado, incluido lo que haya fallado.

Si ejecutas una escena a mano, antes tienes que confirmarlo, porque puede encender o apagar varios equipos a la vez.

## Escenas creadas en Cora Max

También puedes crear y editar escenas directamente en Cora Max. Las escenas son las mismas en el teléfono y en Cora Max, y se comparten en toda la cuenta. Un Cora Max más antiguo puede ejecutar una escena creada en el teléfono. Lo nuevo es poder editarlas en el propio dispositivo, así que un Cora Max antiguo puede mostrar una escena sin dejarte cambiarla. En ese caso, edítala desde el teléfono.

## Desactivar una regla

Cada regla tiene un interruptor para activarla o desactivarla. Si la desactivas, se guarda tal cual. Te viene bien si quieres recuperarla la próxima temporada sin tener que crearla otra vez.

## Ver qué hizo una regla

Cada acción de una regla queda registrada con esa regla como causa. Consúltalo en **[Actividad](/help/mobile-activity)**.
