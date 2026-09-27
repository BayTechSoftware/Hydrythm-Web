---
title: La pantalla de inicio de Cora Max
description: Qué significa todo en la pantalla de Cora Max: la barra superior, la cuadrícula del panel y el cajón de tomas.
section: Cora Max
reviewed: 2026-09-27
order: 2
group: Getting started
---

Cora Max muestra un acuario a la vez, llenando la pantalla con lecturas en vivo que puedes leer desde el otro lado de la sala.

![La pantalla de inicio de Cora Max](img/max-home.webp "Un acuario, llenando la pantalla.")

## La barra superior

De izquierda a derecha:

- **El icono de cuadrícula** abre el Cuarto de los Acuarios, el resumen de todos los acuarios que muestra esta pantalla
- **El nombre del acuario**, con una flecha. Tocarlo abre el **menú del acuario**: cada pantalla para el acuario en pantalla, desde registrar un resultado de prueba hasta ordenar el panel. La lista completa está más abajo.
- **Píldoras de alerta**: cualquier cosa que esté actualmente fuera de rango, con un **+n** cuando hay más de las que caben. Toca para verlas todas.
- **El reloj**
- **La píldora de estado**: qué está haciendo esta pantalla en este momento. Verde es saludable, ámbar necesita atención, rojo es un fallo. El vocabulario completo está más abajo.
- **Batería y Wi-Fi**
- **El icono de dispositivos**: todo lo conectado, y cómo le va
- **El icono de Reef Buddy**: abre el resumen de hoy. Un punto significa que el resumen todavía no se ha leído.
- **El icono de Cora Assistant**: inicia una conversación de voz
- **El engranaje**: ajustes

### Qué significa la píldora de estado

| Píldora | Significado |
|---|---|
| **En línea** | Esta pantalla está recopilando tus lecturas, y son actuales |
| **Nube** | Otro Cora está recopilando las lecturas de este acuario y esta pantalla las muestra. Igual de actual que **En línea**; con más de un Cora, la pantalla que no está recopilando muestra esto |
| **Sondeando Apex**, **Voz activa** | Trabajando en algo en este momento |
| **Sondeo desactivado** | La recopilación está desactivada para este acuario. Puedes volver a activarla desde Cora Mobile |
| **Actualizando** | La recopilación está en pausa mientras se instala una actualización |
| **Desactualizado** | Las lecturas han dejado de llegar. La pantalla muestra lo último que recibió |
| **Reintento de Apex 12s** | Tu Apex no respondió. Cora Max lo intenta de nuevo cuando termina la cuenta atrás |
| **Falló la sincronización con la nube** | Tu Apex respondió, pero sus lecturas no se pudieron guardar en Cora Cloud, así que el panel se queda atrás. Cora Max sigue reintentando |
| **Sin conexión** | Sin conexión. La pantalla muestra los últimos datos que recibió |
| **Sin conexión, reintentando en 45s** | Tu red funciona, pero Cora Cloud ha estado fuera de alcance durante más de 30 segundos. Cora Max se reconecta por sí solo; la cuenta atrás es el tiempo hasta su próximo intento |
| **Cora principal sin conexión** | Esta pantalla es un segundo Cora Max para este acuario, y el **Cora Max principal** (el fijado para consultar el equipo de este acuario) se ha quedado sin conexión. Esta pantalla sigue mostrando los últimos datos que tiene hasta que el principal vuelva, o hasta que elijas un Cora Max principal distinto. Consulta [Más de un dispositivo Cora](/help/mobile-multi-device) |
| **Contraseña de Apex** | Tu Apex rechazó la contraseña guardada. Consulta [Solución de problemas](/help/troubleshooting) |

:::note Cómo funciona la cuenta atrás de reintento
Cora Max intenta reconectarse a un ritmo fijo: unos 15 segundos después de la primera caída, 15 segundos después de eso, luego dos veces a los 30 segundos, y después una vez por minuto hasta que tiene éxito. No reintenta al instante y no se rinde; una pantalla que muestra **Sin conexión, reintentando en 45s** está haciendo exactamente lo que debe.
:::

:::warning Cora Assistant empieza a escuchar de inmediato
Tocar el icono de Cora Assistant inicia una sesión de voz en vivo. Si querías abrir ajustes, ese es el engranaje en el extremo derecho.
:::

## El panel

El resto de la pantalla es el panel: una cuadrícula fija de widgets, todos visibles a la vez. El panel de Cora Max no se desplaza.

Los widgets funcionan igual que en tu teléfono, en un tamaño que puedes leer desde lejos. Consulta **[Referencia de widgets](/help/mobile-widgets)** para saber qué muestra cada forma, y **[Editar el panel de Cora Max](/help/max-dashboard-editing)** para cambiar lo que hay en él.

Cada widget que muestra un parámetro medido lleva su **antigüedad** y su **fuente**, igual que en el teléfono. Un número con `2d` al lado tiene dos días, y se muestra como tal. Las casillas de dispositivo y control muestran su propio estado en su lugar.

## El menú del acuario

![El menú del acuario](img/max-menu.webp "Todo para el acuario actual, desde el nombre del acuario en la barra superior.")

Tocar el nombre del acuario abre el menú del acuario que está en pantalla en ese momento:

| Elemento | Abre |
|---|---|
| **Registrar parámetros** | Introduce lecturas de kit de pruebas en el teclado en pantalla |
| **Diario** | [El diario](/help/mobile-journal) de este acuario |
| **Reef Buddy** | El [resumen](/help/mobile-reef-buddy) actual |
| **Informes de salud** | Evaluaciones de salud |
| **Mantenimiento** | La [lista de tareas](/help/mobile-maintenance) |
| **Informes ICP** | [Resultados de laboratorio](/help/mobile-icp-health) subidos |
| **Alertas** | La banda saludable para cada parámetro de este acuario |
| **Fauna** | El [inventario](/help/mobile-livestock) de este acuario, de solo lectura en esta pantalla |
| **Actividad** | [Cada toma, alimentación y dosis](/help/max-activity), y qué resultó de ello |
| **Diseño del panel** | [Ordena los widgets en esta pantalla](/help/max-dashboard-editing) |
| **Ajustes del acuario** | La pantalla de ajustes completa de este acuario |

## Cambiar de acuario

Usa el **icono de cuadrícula** en el extremo izquierdo de la barra superior para llegar a [el Cuarto de los Acuarios](/help/max-reef-room), y luego abre el acuario que quieras. Cada acuario mantiene su propio diseño de panel, así que la pantalla entera cambia al moverte entre ellos.

## El cajón de tomas y alimentación

La pestaña en la parte inferior de la pantalla despliega un cajón con todas las tomas del sistema y los controles de alimentación.

- **Tomas**: cada una conmutable entre Auto, Apagado y Encendido
- **Alimentación**: pausa el equipo adecuado para una alimentación y lo devuelve todo a su estado después

:::warning Este cajón controla equipo real
Todo en él actúa sobre equipo real. Una orden se envía en el momento en que tocas, pero *enviado* no es *hecho*; vuelve como Confirmado, Sin confirmar, Rechazado o Sin cambios, y [Actividad](/help/max-activity) es donde ves cuál. El modo alimentación es la forma segura de pausar el flujo para alimentar, porque lo restaura todo por sí solo; un Apagado manual se queda apagado hasta que lo cambies de vuelta.
:::

## Si algo parece fuera de lugar

Si las lecturas parecen desactualizadas, o la píldora de estado está en ámbar o rojo, empieza por **[Solución de problemas](/help/troubleshooting)**.
