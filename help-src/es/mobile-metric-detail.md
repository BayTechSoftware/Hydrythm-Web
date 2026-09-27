---
title: Profundizar en un parámetro
description: Toca cualquier widget para ver el historial completo, cada fuente que lo informa y dónde cambiar su rango.
section: Cora Mobile
reviewed: 2026-09-09
order: 8
group: Your dashboard
---

Un widget te muestra un número. Tocarlo te muestra la historia detrás del número.

## Qué obtienes

![Profundizar en un parámetro](img/mobile-metric-detail.webp "Rangos en la parte superior, luego las fuentes que informan este parámetro, luego el gráfico con tu franja de alerta sombreada.")

**Un gráfico de historial**, con su propio selector de rango: **1h · 6h · 12h · 24h · 3d · 7d** y más.

**Un filtro de fuente.** Debajo de los rangos hay una fila de chips: **Todas**, más una por cada fuente que informa este parámetro, como *Apex*, *Cora*, *Red Sea* o *Manual*. Selecciona una para ver solo sus lecturas. Así comparas una sonda con un kit de pruebas directamente: cambia entre ellas en el mismo gráfico.

**Un enlace a la calculadora de dosis**, para parámetros que dosificas. Usa el volumen del acuario de tu [perfil del acuario](/help/mobile-tank-profile) y las concentraciones de [Dosificación](/help/mobile-dosing).

**Una superposición de comparación.** *Comparar con* dibuja un segundo parámetro en el mismo gráfico (alcalinidad frente a calcio, pH frente a temperatura), así una relación que sospechas se vuelve visible en lugar de recordada.

**Estadísticas de resumen** para la ventana en pantalla: **MÍN**, **PROM** y **MÁX**, mostradas en una fila bajo el valor actual.

**Marcadores de dosis** en el gráfico, para poder alinear un movimiento con lo que realmente dosificaste.

**La lista de lecturas en bruto**: cada lectura individual detrás de la línea, con su fuente y marca de tiempo.

**Tu franja de alerta**, sombreada en el gráfico, para que una lectura se lea frente a su rango en lugar de aislada. Para cambiar el rango en sí, mantén pulsado el widget en el panel. Consulta [Alertas y umbrales](/help/mobile-alerts).

**Registrar una lectura** a mano.

## Elegir un rango

El rango adecuado depende del ritmo del parámetro:

| Parámetro | Ventana útil |
|---|---|
| pH | 24 horas; oscila en un ciclo diario |
| Temperatura | 24 horas o 7 días |
| Alcalinidad | 7 o 30 días |
| Elementos traza | 30 días o un año |

:::note Revisa la antigüedad de la lectura en una tendencia plana
Una línea que no se ha movido puede indicar un parámetro estable o una fuente que ha dejado de informar. La antigüedad mostrada junto al valor distingue entre las dos.
:::

## Comparar fuentes

Cuando más de una fuente informa un parámetro, Cora las mantiene separadas en lugar de promediarlas. Usa los chips de fuente para ver cada una por turno.

Un desajuste persistente entre una sonda y una prueba registrada a mano suele indicar que la sonda necesita calibrarse.

Un [resultado de ICP](/help/mobile-icp-health) es una tercera opinión útil, pero no un árbitro. Los laboratorios difieren entre sí, y la manipulación, el almacenamiento y el transporte de la muestra también mueven el resultado. Trata un solo ICP como evidencia, no como el valor verdadero; que dos pruebas coincidan vale mucho más que una sola.

## Elegir qué fuente sigue un widget

Si quieres que un widget siga una fuente concreta, fíjalo en los ajustes del widget. Consulta **[Editar tu panel](/help/mobile-dashboard-editing)**.

## Excluir una lectura errónea

Una sonda que se disparó, una prueba mal leída, una muestra tomada a mitad de un cambio de agua: una sola lectura errónea distorsiona el gráfico, los promedios y cualquier cosa que razone a partir de ellos.

![La lista de lecturas en bruto](img/mobile-readings.webp "Cada lectura detrás de la línea, con su fuente y hora.")

Abre la lista de lecturas desde el icono en la barra superior, y luego toca una lectura para excluirla. La pantalla lo indica claramente: *excluida de promedios y análisis, pero se queda en tu registro.* No se elimina nada, y se puede restaurar.

:::warning Excluye una lectura equivocada, no una que no te gusta
Excluir es para lecturas que sabes que no son válidas. Una lectura que no te gusta pero que no puedes cuestionar es un dato, y quitarla hace menos honesta cualquier comparación posterior.
:::

## Registrar el cuidado de la sonda

Registrar una calibración o limpieza desde aquí marca la fecha contra esa fuente, así una discrepancia posterior se puede leer en función de cuándo se atendió por última vez la sonda. Consulta [Sondas](/help/mobile-probes).

## Registrar una lectura a mano

Introduce lo que dice tu kit de pruebas. Las lecturas registradas a mano son de primera clase: tienen su propia fuente y marca de tiempo, aparecen en el gráfico, alimentan a Reef Buddy, y son con lo que Cora compara tu equipo.

:::note Cora revisa las entradas que parecen inverosímiles
Si un valor está muy lejos de lo que ha estado dando el acuario, se te pide que lo confirmes antes de guardarlo. Esto detecta un punto decimal en el lugar equivocado o una lectura introducida en el parámetro equivocado. Confírmala y la lectura se guarda con normalidad.
:::
