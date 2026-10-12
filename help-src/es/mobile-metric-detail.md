---
title: Ver un parámetro a fondo
description: Toca cualquier widget para ver el historial completo, todas las fuentes que lo informan y dónde cambiar su rango.
section: Cora Mobile
reviewed: 2026-10-12
order: 8
group: Your dashboard
---

Un widget te da un número. Si lo tocas, ves la historia que hay detrás.

Hay dos formas de entrar. Toca un widget del panel, o toca **Historial de parámetros** en la fila de botones bajo los widgets y elige un parámetro. **Historial de parámetros** lista todos los parámetros que tienen datos, aunque no haya ningún widget en el panel.

## Qué encuentras

![Ver un parámetro a fondo](img/mobile-metric-detail.webp "Arriba los desplegables y luego el gráfico con tu franja de alerta sombreada.")

Un **gráfico de historial**. Tres desplegables encima fijan lo que muestra. **Parámetro** pasa a cualquier otro parámetro que tenga datos y conserva tu periodo. **Periodo** va de 1h, 6h, 12h, 24h, 3d, 7d, 15d, 30d, 90d y 180d a 360d y Todo. **Fuente** empieza en **Todas las fuentes** y lista las fuentes que informan este parámetro en este acuario, como *Apex*, *Cora*, *Red Sea* o *Manual*. Elige una para ver solo sus lecturas. Así comparas directamente una sonda con un kit de pruebas, cambiando de una a otra en el mismo gráfico.

La pantalla siempre se abre en 24h y **Todas las fuentes**. No recuerda lo que elegiste la última vez.

Una fila con **Más reciente**, **Mín**, **Prom** y **Máx** del periodo que tienes en pantalla.

Un **acceso a la calculadora de dosis** en los parámetros que dosificas. Usa el volumen de tu [perfil del acuario](/help/mobile-tank-profile) y las concentraciones de [Dosificación](/help/mobile-dosing).

**Comparar** dibuja un segundo parámetro en el mismo gráfico, por ejemplo alcalinidad y calcio, o pH y temperatura. La lista incluye todos los parámetros del acuario. Si sospechas que dos cosas van unidas, aquí lo ves. Toca el chip otra vez para quitar la segunda línea.

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

Cuando varias fuentes informan el mismo parámetro, Cora las muestra por separado y no hace la media. Usa el desplegable **Fuente** para verlas una a una.

El valor que sale en el panel es el más reciente. Un valor en directo solo lo reemplaza una lectura con una hora de medición posterior, de cualquier fuente. Una lectura más antigua va al historial y no sobrescribe lo que hay en el widget. Si fijaste una fuente para el widget, Cora sigue esa fuente.

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

Introduce lo que marca tu kit de pruebas. La lista está agrupada, y el grupo **Oligoelementos** incluye yodo, hierro y cobre en µg/L, y potasio en mg/L. Las lecturas a mano cuentan igual que las demás. Tienen su propia fuente y su hora, aparecen en el gráfico, Reef Buddy las usa y Cora compara tus equipos con ellas.

:::note Cora revisa los valores que parecen raros
Si un valor está muy lejos de lo que viene marcando el acuario, Cora te pide que lo confirmes antes de guardarlo. Así se detecta una coma decimal fuera de sitio o una lectura puesta en el parámetro equivocado. Si la confirmas, se guarda con normalidad.
:::
