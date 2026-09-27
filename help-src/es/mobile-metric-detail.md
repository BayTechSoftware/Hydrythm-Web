---
title: Ver un parámetro a fondo
description: Toca cualquier widget para ver el historial completo, todas las fuentes que lo informan y dónde cambiar su rango.
section: Cora Mobile
reviewed: 2026-09-09
order: 8
group: Your dashboard
---

Un widget te da un número. Si lo tocas, ves la historia que hay detrás.

## Qué encuentras

![Ver un parámetro a fondo](img/mobile-metric-detail.webp "Arriba los rangos, después las fuentes que informan el parámetro y luego el gráfico con tu franja de alerta sombreada.")

Un **gráfico de historial** con su propio selector de rango: **1h · 6h · 12h · 24h · 3d · 7d** y periodos más largos.

Un **filtro de fuente**. Debajo de los rangos hay una fila de chips con **Todos** y uno por cada fuente que informa el parámetro, como *Apex*, *Cora*, *Red Sea* o *Manual*. Elige uno para ver solo sus lecturas. Así comparas directamente una sonda con un kit de pruebas, cambiando de una a otra en el mismo gráfico.

Un **acceso a la calculadora de dosis** en los parámetros que dosificas. Usa el volumen de tu [perfil del acuario](/help/mobile-tank-profile) y las concentraciones de [Dosificación](/help/mobile-dosing).

**Comparar con** dibuja un segundo parámetro en el mismo gráfico, por ejemplo alcalinidad y calcio, o pH y temperatura. Si sospechas que dos cosas van unidas, aquí lo ves.

**MÍN**, **PROM** y **MÁX** del periodo que tienes en pantalla, en una fila debajo del valor actual.

**Marcas de dosis** en el gráfico, para relacionar un cambio con lo que dosificaste de verdad.

La **lista de lecturas**, con cada lectura que forma la línea, su fuente y su hora.

Tu **franja de alerta**, sombreada en el gráfico, para que veas cada lectura junto a su rango. Para cambiar el rango, mantén pulsado el widget en el panel. Lo explicamos en [Alertas y umbrales](/help/mobile-alerts).

Y la opción de **registrar una lectura** a mano.

## Elegir un rango

El rango que te conviene depende del ritmo del parámetro:

| Parámetro | Periodo útil |
|---|---|
| pH | 24 horas, porque sube y baja cada día |
| Temperatura | 24 horas o 7 días |
| Alcalinidad | 7 o 30 días |
| Oligoelementos | 30 días o un año |

:::note Si la línea está plana, mira la antigüedad
Una línea que no se mueve puede ser un parámetro estable o una fuente que ha dejado de informar. La antigüedad que aparece junto al valor te dice cuál de las dos es.
:::

## Comparar fuentes

Cuando varias fuentes informan el mismo parámetro, Cora las muestra por separado y no hace la media. Usa los chips de fuente para verlas una a una.

Si una sonda y tus pruebas a mano no coinciden durante un tiempo, lo normal es que haya que calibrar la sonda.

Un [resultado ICP](/help/mobile-icp-health) es una buena tercera opinión, pero no tiene la última palabra. Los laboratorios no coinciden entre sí, y la forma de manipular, guardar y enviar la muestra también cambia el resultado. Toma un solo ICP como un indicio, no como el valor exacto. Dos análisis que coinciden valen mucho más que uno.

## Elegir qué fuente sigue un widget

Si quieres que un widget siga una fuente concreta, elígela en los ajustes del widget. Lo tienes en [Editar tu panel](/help/mobile-dashboard-editing).

## Excluir una lectura errónea

Un pico de la sonda, una prueba mal leída, una muestra tomada en pleno cambio de agua. Una sola lectura errónea deforma el gráfico, las medias y todo lo que se calcula a partir de ellos.

![La lista de lecturas](img/mobile-readings.webp "Cada lectura que forma la línea, con su fuente y su hora.")

Abre la lista de lecturas con el icono de la barra superior y toca una lectura para excluirla. La pantalla lo explica: la lectura deja de contar en los promedios y análisis, pero sigue en tu registro. No se borra nada y puedes recuperarla.

:::warning Excluye lecturas erróneas, no lecturas que no te gustan
Excluir sirve para lecturas que sabes que no son válidas. Si una lectura no te gusta pero no tiene nada de raro, es un dato. Quitarla hace que todas las comparaciones posteriores sean menos fiables.
:::

## Anotar el cuidado de la sonda

Si registras aquí una calibración o una limpieza, la fecha queda asociada a esa fuente. Así, si más adelante hay una diferencia, sabes cuándo se revisó la sonda por última vez. Más información en [Sondas](/help/mobile-probes).

## Registrar una lectura a mano

Introduce lo que marca tu kit de pruebas. Las lecturas a mano cuentan igual que las demás. Tienen su propia fuente y su hora, aparecen en el gráfico, Reef Buddy las usa y Cora compara tus equipos con ellas.

:::note Cora revisa los valores que parecen raros
Si un valor está muy lejos de lo que viene marcando el acuario, Cora te pide que lo confirmes antes de guardarlo. Así se detecta una coma decimal fuera de sitio o una lectura puesta en el parámetro equivocado. Si la confirmas, se guarda con normalidad.
:::
