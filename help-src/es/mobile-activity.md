---
title: Actividad y línea de tiempo
description: Todo lo que le ha pasado a tu equipo, y qué lo causó.
section: Cora Mobile
reviewed: 2026-09-09
order: 22
group: Records
---

Actividad registra cada **solicitud de actuación** (cada intento de cambiar algo) junto con qué la pidió y qué pasó con ella.

Una solicitud no es lo mismo que un cambio. Las solicitudes rechazadas no se ejecutaron, con una excepción: una entrada que dice *Ningún dispositivo respondió a tiempo* puede haberse ejecutado igualmente, así que revisa el equipo antes de repetirla. Las solicitudes sin cambios encontraron el equipo ya como se pedía, y una sin confirmar puede o no haber llegado al dispositivo. Todas se registran.

**Ajustes → Actividad.**

![El registro de actividad](img/mobile-activity.webp "Cada acción, con la superficie que la solicitó.")

## Qué se registra

Cada **solicitud**, no solo las que funcionaron: cambios de estado de tomas, ciclos de alimentación, dosis, cambios de enchufe, y cualquier cosa que hiciera una escena o una automatización.

Una solicitud que fue **rechazada**, que **no produjo cambios**, o que salió y volvió **sin confirmar** se registra igual que una ejecutada. Ese es el propósito: una orden que en silencio no hizo nada es exactamente lo que quieres encontrar aquí.

## Qué la causó

Cada entrada nombra su causa:

| Causa | Significa |
|---|---|
| **Esta aplicación** | La tocaste aquí |
| **Voz en esta aplicación** | La pediste, en este teléfono |
| **Toque en un Cora** | Alguien usó una pantalla Cora; la fila indica cuál |
| **Voz en un Cora Max** | Alguien le habló a una pantalla |
| **Cora Assistant** | Le pediste a Cora que lo hiciera |
| **Regla de automatización** | Se activó una regla |
| **Botón inteligente** | Se pulsó un botón físico |
| **Enviado desde Cora Cloud** | Emitido por tu cuenta en lugar de por un dispositivo delante de ti |
| **Origen desconocido** | Registrado antes de poder identificar el origen |

## Cómo viajó

Cada fila también lleva un chip de ruta, porque *cómo* llegó una solicitud a tu equipo explica buena parte de lo que salió mal cuando algo lo hizo:

| Chip | Significa |
|---|---|
| **LAN** | Enviado por tu propia red, directamente al equipo |
| **VÍA LA NUBE** | Enviado a través de tu cuenta, para equipo no accesible directamente |
| **¿RUTA?** | Registrado antes de que se hiciera seguimiento de las rutas: realmente desconocido, no supuesto |

En un sistema con más de un Cora, la fila también indica cuál llevó a cabo la solicitud.

## La línea de tiempo del acuario

Aparte de las acciones sobre el equipo, cada acuario tiene una **línea de tiempo**: lecturas, alertas, entradas del diario, resultados de ICP y cambios de fauna, ordenados en el tiempo.

Usa actividad cuando te preguntes *"¿qué hizo algo?"* y la línea de tiempo cuando te preguntes *"¿qué estaba pasando alrededor de esta fecha?"*

:::note La línea de tiempo y el diario son complementarios
La línea de tiempo guarda lo que registró Cora; el [diario](/help/mobile-journal) guarda lo que hiciste tú. Leídos juntos establecen causa y efecto alrededor de una fecha dada.
:::
