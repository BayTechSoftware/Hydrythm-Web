---
title: Actividad y línea de tiempo
description: Ve cada cambio enviado a tus equipos, quién o qué lo pidió y si funcionó, y lee la línea de tiempo del acuario alrededor de una fecha.
section: Cora Mobile
reviewed: 2026-10-13
order: 30
group: Records
twin: max-activity
---

Actividad muestra cada intento de cambiar algo en tus equipos: encender o apagar tomas, ciclos de alimentación, dosis y todo lo que haya hecho una escena o una automatización. Cada fila muestra qué lo pidió y qué pasó después, incluidas las solicitudes que no funcionaron.


Ve a **Ajustes → Actividad**. Si tienes más de un acuario, elígelo con las etiquetas de acuario de arriba.

![Actividad en Cora Mobile](img/mobile-activity.webp "La leyenda de resultados arriba y después cada acción con su resultado, su origen y su ruta.")

## Qué significan los resultados {#outcomes}

Cada fila lleva un resultado. La misma leyenda está arriba en la pantalla, en **QUÉ SIGNIFICAN LOS RESULTADOS**.

| Resultado | Significa |
|---|---|
| **Confirmado** | El dispositivo dijo que lo hizo |
| **Sin confirmar** | Se envió, pero no llegó respuesta. Puede que haya llegado al dispositivo o puede que no |
| **Rechazado** | Se denegó y no se ejecutó. Lee la fila para ver por qué |
| **Sin cambios** | El equipo ya estaba en ese estado, así que no se envió nada |

Hay un rechazo distinto. *Ningún dispositivo respondió a tiempo* significa que la solicitud podría haberse ejecutado. Revisa el equipo antes de volver a intentarlo.

Una orden que no hizo nada sin avisar es justo lo que te interesa encontrar aquí, así que las solicitudes fallidas y sin cambios se guardan junto a las que funcionaron.

## Qué lo provocó {#causes}

Cada fila indica su origen:

| Origen | Significa |
|---|---|
| **Esta aplicación** | Lo tocaste en Cora Mobile |
| **Voz en esta aplicación** | Lo pediste con la voz, en este teléfono |
| **Toque en un Cora** | Alguien usó la pantalla de un Cora Max. La fila indica cuál |
| **Voz en un Cora Max** | Alguien le habló a un Cora Max |
| **Cora Assistant** | Le pediste a Cora Assistant que lo hiciera en un chat |
| **Regla de automatización** | Lo hizo una [automatización o escena](/help/mobile-automation) |
| **Enviado desde Cora Cloud** | Llegó desde tu cuenta a través de Cora Cloud |
| **Origen desconocido** | Se registró antes de que Cora pudiera saber de dónde venía |

## Por dónde llegó {#route}

Cada fila lleva también una etiqueta de ruta. Cuando algo sale mal, cómo llegó la solicitud a tu equipo suele explicar por qué.

| Etiqueta | Significa |
|---|---|
| **LAN** | Se envió por tu propia red, directamente al equipo |
| **VÍA LA NUBE** | Se envió a través de tu cuenta, para equipos a los que Cora no llega directamente |
| **¿RUTA?** | Se registró antes de que se guardaran las rutas, así que no se sabe la ruta |

Si tienes más de un Cora Max, la fila también indica cuál ejecutó la solicitud.

## La línea de tiempo del acuario {#tank-timeline}

Actividad trata de los equipos. La línea de tiempo del acuario, llamada **Historia del acuario** en pantalla, trata del acuario. Ordena por fecha las entradas del diario, el mantenimiento, los cambios de fauna, las pruebas de agua y las alertas, con hitos por el camino.

Para abrirla, ve al [diario](/help/mobile-journal) y toca el icono **Línea de tiempo del acuario** de arriba. Usa las etiquetas de arriba para mostrar solo **Diario**, **Mantenimiento**, **Fauna**, **Pruebas de agua** o **Alertas**, o **Todos**. **Cargar historia anterior** va más atrás. Desde aquí también puedes añadir una **Nueva entrada** o dictarla.

Usa Actividad cuando quieras saber *"¿qué hizo algo?"*. Usa la línea de tiempo cuando quieras saber *"¿qué estaba pasando por estas fechas?"*.

:::note Usa la línea de tiempo con el diario
La línea de tiempo reúne lo que registró Cora. El diario guarda lo que hiciste tú y por qué. Léelos juntos para ver qué causó qué alrededor de una fecha.
:::
