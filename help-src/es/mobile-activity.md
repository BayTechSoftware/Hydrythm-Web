---
title: Actividad y línea de tiempo
description: Todo lo que ha pasado con tus equipos y qué lo provocó.
section: Cora Mobile
reviewed: 2026-09-09
order: 22
group: Records
---

Actividad guarda cada **solicitud de actuación**, es decir, cada intento de cambiar algo. Para cada una ves qué la pidió y qué pasó con ella.

Algunas solicitudes no cambian nada. Las rechazadas no se ejecutaron, con una excepción: *Ningún dispositivo respondió a tiempo* significa que la acción podría haberse ejecutado. Revisa el equipo antes de repetirla. **Sin cambios** indica que el equipo ya estaba en el estado solicitado. Si una solicitud quedó sin confirmar, Cora no sabe si llegó al dispositivo. Todos los resultados quedan registrados.

**Ajustes → Actividad.**

![El registro de actividad](img/mobile-activity.webp "Cada acción, con la superficie que la solicitó.")

## Qué se registra

Se registran todas las **solicitudes**, también las que no funcionaron. Eso incluye encender o apagar tomas, ciclos de alimentación, dosis, cambios de enchufe y todo lo que haya hecho una escena o una automatización.

Una solicitud **rechazada**, **sin cambios** o que volvió **sin confirmar** se registra igual que una que se ejecutó. Una orden que no hizo nada sin avisar es justo lo que te interesa encontrar aquí.

## Qué la provocó

Cada entrada indica su origen:

| Origen | Qué significa |
|---|---|
| **Esta aplicación** | La tocaste aquí |
| **Voz en esta aplicación** | La pediste con la voz en este teléfono |
| **Toque en un Cora** | Alguien usó una pantalla Cora. La fila indica cuál |
| **Voz en un Cora Max** | Alguien le habló a una pantalla |
| **Cora Assistant** | Le pediste a Cora que lo hiciera |
| **Regla de automatización** | Se activó una regla |
| **Botón inteligente** | Alguien pulsó un botón físico |
| **Enviado desde Cora Cloud** | La solicitud llegó desde tu cuenta a través de Cora Cloud |
| **Origen desconocido** | Se registró antes de que se pudiera identificar el origen |

## Por dónde llegó

Cada fila lleva también una etiqueta de ruta. Saber *cómo* llegó una solicitud a tu equipo ayuda mucho a entender qué falló cuando algo sale mal:

| Etiqueta | Qué significa |
|---|---|
| **LAN** | Se envió por tu propia red, directamente al equipo |
| **VÍA LA NUBE** | Se envió a través de tu cuenta porque no se podía llegar al equipo directamente |
| **¿RUTA?** | Se registró antes de que se guardaran las rutas. No se sabe, y Cora no lo supone |

Si tienes más de un Cora, la fila también indica cuál de ellos hizo la solicitud.

## La línea de tiempo del acuario

Además de las acciones sobre los equipos, cada acuario tiene una **línea de tiempo**. En ella ves por orden las lecturas, las alertas, las entradas del diario, los resultados de ICP y los cambios de fauna.

Usa Actividad cuando quieras saber *"¿qué hizo este equipo?"*. Usa la línea de tiempo cuando quieras saber *"¿qué estaba pasando por estas fechas?"*.

:::note La línea de tiempo y el diario se complementan
La línea de tiempo guarda lo que registró Cora. El [diario](/help/mobile-journal) guarda lo que hiciste tú. Si los lees juntos, verás qué causó qué alrededor de una fecha.
:::
