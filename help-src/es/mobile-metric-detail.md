---
title: Ver un parámetro a fondo
description: Toca un widget para ver todo el historial de un parámetro, comparar fuentes y parámetros, excluir una lectura errónea y registrar el cuidado de una sonda.
section: Cora Mobile
reviewed: 2026-10-13
order: 7
group: Your dashboard
---

Un widget te da un número. Tócalo para ver la historia que hay detrás de ese número.

Hay dos formas de entrar. Toca un widget del panel, o toca **Historial de parámetros** en la fila de botones bajo los widgets y elige un parámetro. **Historial de parámetros** lista todos los parámetros que tienen datos, aunque no tengan widget en el panel.

## Qué encuentras {#what-you-get}

![Ver un parámetro a fondo](img/mobile-metric-detail.webp "Arriba los desplegables y luego el gráfico con tu franja de alerta sombreada.")

- Un gráfico de historial. La fila de encima fija lo que muestra. **Parámetro** pasa a cualquier otro parámetro que tenga datos y conserva tu periodo. **Periodo** va de 1h, pasando por 6h, 12h, 24h, 3d, 7d, 15d, 30d, 90d, 180d y 360d, hasta Todo. **Fuente** empieza en **Todas las fuentes** y lista las fuentes que informan de este parámetro en este acuario, como *Apex*, *Cora*, *Red Sea* o *Manual*. Elige una para ver solo sus lecturas.
- **Comparar**, al final de la misma fila, dibuja un segundo parámetro en el gráfico, como alcalinidad con calcio o pH con temperatura. El botón pasa a decir **vs** y el nombre del otro parámetro. Vuelve a tocarlo para quitar la segunda línea.
- Una fila con **Más reciente**, **Mín**, **Prom** y **Máx** del periodo que tienes en pantalla.
- Iconos en la barra superior: **Lecturas** abre la lista de lecturas sin procesar, y **Registrar cuidado de sonda** anota una calibración o una limpieza. Para la alcalinidad, el calcio y el magnesio también está la calculadora de dosis, que usa el volumen del acuario de tu [perfil del acuario](/help/mobile-tank-profile) y las concentraciones de [Dosificación](/help/mobile-dosing).

La pantalla siempre se abre en 24h y **Todas las fuentes**. No recuerda lo que elegiste la última vez.

## Leer el gráfico {#reading-the-chart}

- La franja verde es tu rango de alerta, así que ves cada lectura junto a él. Para cambiar el rango, mantén pulsado el widget en el panel. Más información en [Alertas y umbrales](/help/mobile-alerts).
- Una línea discontinua marca una dosis registrada, para que puedas relacionar un cambio con lo que dosificaste.
- **Máximo 30 d** y **Mínimo 30 d** son líneas discontinuas con los extremos de los últimos 30 días.
- Un punto hueco es una lectura que excluiste.
- Con **Comparar** activado, el segundo parámetro usa el eje de la derecha.

## Elegir un periodo {#choosing-a-range}

Elige el periodo que encaje con el ritmo del parámetro.

| Parámetro | Periodo útil |
|---|---|
| pH | 24 horas, porque sube y baja en un ciclo diario |
| Temperatura | 24 horas o 7 días |
| Alcalinidad | 7 o 30 días |
| Oligoelementos | 30 días o un año |

:::note ¿Línea plana? Mira la antigüedad de la lectura
Una línea que no se ha movido puede significar que el parámetro es estable. También puede significar que la fuente ha dejado de informar. La antigüedad junto al valor en el widget te dice cuál de las dos es.
:::

## Comparar fuentes {#comparing-sources}

Cuando varias fuentes informan de un parámetro, Cora las mantiene separadas y no hace la media. Usa el desplegable **Fuente** para mirar cada una. Es la forma más rápida de comparar una sonda con un kit de pruebas.

La que sale en el panel es la más reciente. Un valor en directo solo lo reemplaza una lectura con una hora de medición posterior, de cualquier fuente. Una lectura más antigua va al historial y no sobrescribe lo que hay en el widget. Si fijaste una fuente en **Asignación de parámetros**, Cora sigue esa fuente.

Si una sonda y tus pruebas anotadas a mano se mantienen separadas por la misma cantidad, normalmente hay que calibrar la sonda.

Un [resultado de ICP](/help/mobile-icp-health) es una tercera opinión útil, pero no zanja la cuestión. Los laboratorios difieren entre sí, y la forma de manipular, guardar y enviar la muestra cambia el resultado. Toma un solo ICP como un indicio. Dos análisis que coinciden valen mucho más que uno.

## Elegir qué fuente sigue una lectura {#choosing-which-source-a-widget-trusts}

La fuente se elige para cada acuario y cada parámetro, no para cada widget. Ve a **Ajustes**, toca el acuario, toca **Asignación de parámetros** y después la pestaña **Fuentes**. Elige una sonda, o **Automático (gana la lectura más reciente)**. La elección se aplica a ese parámetro en todo el acuario. Más información en [Asignación de parámetros](/help/mobile-probes).

## Excluir una lectura errónea {#excluding-a-bad-reading}

Puede que una sonda diera un pico, que leyeras mal una prueba o que tomaras la muestra en pleno cambio de agua. Una sola lectura errónea deforma el gráfico, las medias y todo lo que se calcula a partir de ellas.

![La lista de lecturas de pH en Cora Mobile](img/mobile-readings.webp "Cada lectura que forma la línea, con su hora y su fuente. Toca una para excluirla.")

Toca **Lecturas** en la barra superior y después toca una lectura. Cora pregunta **¿Excluir esta lectura?** y explica que se queda en tu registro pero deja de contar para las medias, las tendencias, los análisis y el asistente. Toca **Excluir**. No se borra nada, y puedes recuperarla de la misma forma.

Las lecturas de hace más de 90 días no se pueden excluir ni recuperar.

:::warning Excluye lecturas erróneas, no lecturas que no te gustan
Excluye solo una lectura que sepas que no es válida. Si una lectura no te gusta pero no le encuentras nada raro, es un dato real. Quitarla hace que todas las comparaciones posteriores sean menos honestas.
:::

## Registrar el cuidado de una sonda {#recording-probe-care}

Toca **Registrar cuidado de sonda** (el icono del sensor en la barra superior) y elige lo que hiciste: calibrar, limpiar, cambiar, mover o comparar. Cora pone la fecha en esa fuente, para que una calibración reciente no se confunda con una desviación. Más adelante, si la sonda no coincide con algo, puedes ver cuándo se revisó por última vez. Más información en [Asignación de parámetros](/help/mobile-probes).

## Registrar una lectura a mano {#logging-a-reading-by-hand}

Las lecturas se registran desde el panel, no desde esta pantalla. Toca **Registrar parámetros** debajo de los widgets e introduce lo que marca tu kit de pruebas. La lista está agrupada, y el grupo **Oligoelementos** incluye yodo, hierro y cobre en µg/L, y potasio en mg/L. Las lecturas a mano cuentan igual que las demás. Tienen su propia fuente y su hora, aparecen en el gráfico y Reef Buddy las usa. También son con lo que Cora compara tus equipos.

:::note Cora revisa los valores que parecen raros
Si un valor está muy lejos de lo que viene marcando el acuario, Cora te pide que lo confirmes antes de guardarlo. Así se detecta una coma decimal fuera de sitio o una lectura puesta en el parámetro equivocado. Cuando la confirmas, la lectura se guarda con normalidad.
:::
