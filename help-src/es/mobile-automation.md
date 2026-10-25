---
title: Automatizaciones y escenas
description: Haz que Cora actúe sola ante una lectura, una alerta, una hora o un dispositivo que se desconecta, y agrupa acciones en escenas que ejecutas con un toque.
section: Cora Mobile
reviewed: 2026-10-24
order: 25
group: Alerts and automation
twin: max-automation
---

Una automatización es una regla que Cora ejecuta por ti: *cuando pase esto, comprueba aquello y luego haz esto otro.* Una escena reúne varias acciones en una sola cosa que ejecutas cuando quieres.

Ve a **Ajustes → Automatizaciones**.

![La pantalla Automatización en Cora Mobile, con las pestañas Automatizaciones y Escenas](img/mobile-automation.webp "Automatizaciones y Escenas son pestañas distintas. Cada regla tiene su propio interruptor.")

La pantalla tiene dos pestañas, **Automatizaciones** y **Escenas**, con un botón **Nueva automatización** o **Nueva escena**. Cada regla muestra un resumen de una línea, un interruptor para activarla y un menú para **Editar** o **Eliminar**. Una regla que todavía no se ha ejecutado lo indica.

:::warning Las reglas actúan sobre equipos reales
Si una regla apaga una bomba, la bomba se apaga aunque no estés mirando. Crea las reglas de una en una y comprueba que cada una hace lo que esperas antes de añadir la siguiente.
:::

## Cómo es una regla {#shape}

Cada automatización tiene tres partes.

- El disparador la pone en marcha.
- Las condiciones también tienen que cumplirse.
- Las acciones son lo que hace después, en orden.

![Un formulario Nueva automatización vacío en Cora Mobile](img/mobile-rule-builder.webp "Una automatización nueva: disparadores, condiciones Si, acciones Entonces, O si y Si no, y después el tiempo de espera y la franja horaria.")

## Qué pone en marcha una regla {#triggers}

Añade uno o más disparadores en **Cuando: cualquier detonante**. Cualquiera de ellos pone en marcha la regla.

| Disparador | Se activa cuando |
|---|---|
| **Cuando un parámetro cambia** | Un parámetro pasa de un valor que tú fijas. Elige la **Dirección**: **Subida**, **Bajada** o **Cualquier cambio** |
| **Cuando se activa una alerta** | Una alerta queda **Activada**, **Resuelta**, o cualquiera de las dos. Puedes limitarlo a alertas de **Umbral** o de **Tasa de cambio**. |
| **A una hora del día** | Una hora del día, en tu propia zona horaria |
| **Cuando un dispositivo se desconecta** | Tu Cora Max queda **Sin conexión**, vuelve a estar **En línea**, o cualquiera de las dos |

:::tip Entérate cuando tu Cora Max se desconecta
Una regla con **Cuando un dispositivo se desconecta** y **Notificarme** te avisa cuando el Cora Max que lee tus equipos se queda sin corriente o sin Wi-Fi.
:::

## Condiciones {#conditions}

Las condiciones deciden si se ejecutan las acciones. Toca **Agregar condición** y elige:

- **Comparación de parámetro**, una lectura por encima, por debajo o igual a un valor
- **Parámetro dentro / fuera de un rango**
- **Alerta activa**
- **La toma está encendida / apagada**, para una toma del Apex
- **Hora del día**, una franja como de 22:00 a 06:00
- **Cómo fue un paso anterior**, que comprueba si un paso anterior salió **Correcto** u **Omitido**. Úsala para "prueba esto y, si no funciona, haz esto otro"

Con varias condiciones, pon **Coincidir** en **Todas (Y)** o **Cualquiera (O)**.

## Ramas y comprobaciones por paso {#branches}

Una automatización puede hacer cosas distintas en casos distintos. Su primer bloque es **Si**. Toca **O si** para añadir otro caso, o añade un bloque **Si no** para todo lo demás. Cora ejecuta el primer bloque cuyas condiciones se cumplen.

También puedes condicionar una sola acción. Toca **Solo si…** en ese paso y dale su propia condición. Sin condición, el paso siempre se ejecuta.

## Cuándo puede ejecutarse {#when-it-may-run}

- **Tiempo de espera entre ejecuciones** impide que una regla vuelva a saltar demasiado pronto. Empieza en 10 min.
- **Ejecutar solo entre** limita la regla a una franja horaria, por ejemplo solo de día.
- **Probar con valores en vivo** comprueba la regla con las lecturas actuales de tu acuario, sin hacer nada. Te dice qué *se ejecutaría*, o por qué no se ejecutaría nada.

## Qué puede hacer una regla {#actions}

Una acción que necesita un equipo solo aparece en un acuario que tiene ese equipo.

| Acción | Qué hace |
|---|---|
| **Controlar equipo del Apex** | Enciende o apaga una toma |
| **Ejecutar ciclo de alimentación del Apex** | Empieza una alimentación. El Apex la termina con su propio temporizador |
| **Ejecutar una prueba del Trident** | Lanza una prueba. Cada ejecución gasta reactivo |
| **Dosificar un cabezal DŌS** | Da una dosis medida con un cabezal DŌS |
| **Controlar un equipo Red Sea** | Maneja una unidad ReefBeat |
| **Controlar una bomba de circulación** | Ajusta el caudal, el modo de olas o la potencia de una bomba Jecod, o usa **Pausar para alimentar**. El Cora Max del acuario vuelve a poner la bomba como estaba cuando termina la alimentación |
| **Notificarme** | Te envía una notificación push con tu propio **Título** y **Mensaje** |
| **Esperar antes del siguiente paso** | Hace una pausa antes de seguir |
| **Ejecutar una escena** | Ejecuta una escena desde dentro de esta regla |
| **Gestionar una automatización** | Activa o desactiva otra regla |
| **Crear una tarea de mantenimiento** | Pone una tarea en la lista de [mantenimiento](/help/mobile-maintenance) del acuario, por ejemplo cambiar el medio del depurador de CO2 cuando el pH baja de un valor |


:::warning Una dosis no se puede deshacer, y tiene un límite
Una dosis no se puede sacar del acuario. Una regla solo puede dosificar con un cabezal que se haya medido con **Medir para dosificar** en un Cora Max. La dosis la ejecuta un Cora Max del acuario. La dosificación desde reglas tiene un máximo de **10 mL por cabezal al día**, esté como esté escrita la regla.
:::

:::note Qué hace Crear una tarea de mantenimiento
Elige el acuario y después **Tarea existente** (una tarea que ya existe pasa a vencer ahora) o **Tarea nueva** (ponle un **Nombre de la tarea**). Una tarea nueva es única, vence enseguida y la regla no la vuelve a crear mientras siga abierta. Recibes una sola notificación, y la tarea única sale de la lista cuando la completas.
:::

:::note La espera es corta
**Esperar antes del siguiente paso** hace una pausa de hasta 60 segundos, y una rama puede esperar 60 segundos en total. Después de la pausa, el siguiente paso ve lecturas nuevas. Para una pausa más larga, como una bomba de retorno apagada 30 minutos durante un cambio de agua, usa una escena con **Ejecutar durante** (más abajo).
:::

## Escenas {#scenes}

Una escena es un grupo de acciones con nombre, como "Cambio de agua", "Modo foto" o "Noche". Toca **Nueva automatización** o **Nueva escena** y elige **Escena** arriba. Una escena no tiene disparador. La ejecutas con **Ejecutar ahora** en la lista, desde dentro de una regla con **Ejecutar una escena**, o con un horario mediante una regla con **A una hora del día**.

**Ejecutar durante** fija cuánto dura una escena: un número de minutos u horas, o **Hasta que yo lo cambie**. Cuando se acaba el tiempo, Cora devuelve las tomas de la escena a como estaban. Los demás equipos se quedan como los dejó la escena. Mientras una escena con tiempo está en marcha, la lista muestra una cuenta atrás y un botón **Detener** que la termina antes.

Si una escena enciende o apaga una toma importante, como un calentador, un enfriador, la bomba de retorno o la reposición, Cora pregunta antes de ejecutarla y lista esos pasos. Puedes desactivarlo con **Preguntar antes de ejecutar** en la escena.

Una escena puede llamar a otra escena, hasta 3 niveles. Cora no ejecuta una escena que se llama a sí misma, porque podría entrar en un bucle y seguir actuando sobre el acuario.

Después de que una escena se ejecuta, ves qué ha pasado paso a paso, incluido lo que haya fallado o no se haya ejecutado.

## Escenas creadas en Cora Max {#scenes-on-cora-max}

También puedes crear y editar escenas en un Cora Max. Es el mismo conjunto de escenas, compartido en toda la cuenta. Un Cora Max más antiguo todavía puede ejecutar una escena creada en el teléfono. Editar en el dispositivo es más reciente, así que un Cora Max antiguo puede mostrar una escena sin dejarte cambiarla. En ese caso, edítala desde el teléfono.

## Desactivar una regla {#turning-a-rule-off}

Cada regla tiene un interruptor para activarla. Desactivar una regla conserva sus ajustes, algo útil cuando quieres recuperarla la próxima temporada.

## Ver qué hizo una regla {#seeing-what-a-rule-did}

Cada acción que hace una regla queda registrada con **Regla de automatización** como origen. La encontrarás en [Actividad](/help/mobile-activity).

Un paso que falla o que tendría que esperar no se queda pendiente. Caduca al instante, la ejecución se registra como fallida y recibes una notificación que nombra la automatización, el paso y el motivo. Un paso falla, por ejemplo, si su dispositivo está sin conexión, si ningún Cora Max puede ejecutarlo, si el dispositivo lo rechaza o no responde, o si un calentador o enfriador se acaba de conmutar. Por un paso en un acuario eliminado no recibes notificaciones.
