---
title: Leer tu panel
description: Cómo leer el panel de Cora: widgets, actualidad, fuentes y qué significan los colores.
section: Cora Mobile
reviewed: 2026-09-09
order: 5
group: Your dashboard
---

El panel es una cuadrícula de **widgets**, cada uno mostrando una cosa sobre un acuario. Qué hay en él depende totalmente de ti; consulta **[Editar tu panel](/help/mobile-dashboard-editing)**.

![Un panel de Cora Mobile](img/mobile-dashboard.webp "Medidores, números, tendencias y controles en una pantalla.")

## La cabecera del acuario

En la parte superior de cada panel:

- **El nombre del acuario**, con un pequeño icono junto a él: eso es un **renombrado rápido**, nada más
- **Alimentar**: pausa el flujo y el skimming para una alimentación, y luego lo devuelve todo a su estado
- **Reef Buddy**: abre el resumen de esta mañana
- **Compartir**: envía una instantánea del panel
- **El lápiz a la derecha**: abre [el perfil del acuario](/help/mobile-tank-profile)

:::note Tres controles parecidos, tres destinos
El icono junto al nombre renombra el acuario. El lápiz a la derecha abre el **perfil** del acuario. Editar el propio panel no es ninguno de los dos; es **Editar panel**, al *pie* del panel, debajo de los widgets.
:::

Con más de un acuario, desliza hacia los lados para moverte entre ellos.

## La tarjeta de Reef Buddy

Debajo de la cabecera, una tarjeta resume el resumen más reciente: un titular, sus puntuaciones de **Estabilidad** y **Datos**, y el número de análisis. Tócala para abrir el resumen completo, o descártala con **×**. Aparece una tarjeta nueva con el siguiente resumen.

## Cómo leer un widget de parámetro

Un widget que muestra un **parámetro medido** lleva las mismas tres cosas en los mismos lugares. Las casillas de dispositivo y control (una toma, una unidad de dosificación, una bomba) muestran su propio estado en su lugar, porque no hay una sola lectura detrás de ellas.

**El valor** es la lectura en sí, grande y central.

**La antigüedad** está debajo o al lado: `now`, `1h`, `2d`. Es cuánto hace que se tomó la lectura, no cuánto hace que se actualizó la pantalla. Un número que no se ha movido en dos días dice `2d`, y eso es información.

**La insignia de fuente** es la pequeña marca junto a la antigüedad. Te indica de dónde vino el número: una sonda, un controlador, un resultado de laboratorio, o tú con un kit de pruebas. Toca cualquier widget para ver la fuente detallada junto con su historial reciente.

:::note Por qué importa tanto la antigüedad
Una lectura de alcalinidad perfecta de hace cuatro días no es una lectura de alcalinidad actual. La antigüedad está junto a cada valor para que puedas notar la diferencia de un vistazo.
:::

## Colores

Cora usa el color con moderación, y siempre para significar lo mismo:

| Color | Significado |
|---|---|
| Verde | Cómodamente dentro del rango para este parámetro |
| Ámbar | Cerca de un límite: **normalmente todavía dentro del rango**, dentro de su último décimo |
| Rojo | Más allá del límite, y algo sobre lo que vale la pena actuar |
| Gris | Sin veredicto: sin lectura reciente, o sin rango utilizable frente al que juzgar |

:::note Ámbar normalmente significa "todavía bien, pero yendo hacia algo"
Ámbar es un *margen*, no una infracción. Una lectura dentro de su rango pero dentro del último 10% de este se marca en ámbar deliberadamente, así la desviación es visible mientras todavía hay tiempo para actuar en lugar de en el momento en que se convierte en un problema.

De ahí se derivan dos matices.

**Un rango que fijas tú mismo se trata como un límite declarado.** Cruzarlo lleva el widget directo a rojo: sin margen ámbar, porque tú trazaste esa línea deliberadamente. Un rango **proporcionado por Cora** es una referencia más suave: cruzarlo muestra ámbar durante el primer 10% más allá del límite, y se vuelve rojo a partir de ahí.

**Un límite unilateral** (un techo de contaminante, o un suelo de nutriente) se gradúa solo en su borde alto, así que el cobre a cero se lee en verde en lugar de marcarse en ámbar por estar cerca del extremo bajo de la escala.
:::

Un widget con contorno ámbar o rojo es uno que necesita atención. El contorno está en el widget, no solo en el número, así que es visible mientras te desplazas.

## Debajo de los widgets

![El pie del panel](img/mobile-dashboard-foot.webp "Editar panel, Registrar parámetros, y accesos directos a las cuatro áreas de registro.")

En la parte inferior del panel:

- **Editar panel**: abre el [editor de panel](/help/mobile-dashboard-editing)
- **Registrar parámetros**: introduce lecturas de kit de pruebas a mano
- **Diario · Alertas · Mantenimiento · Fauna**: accesos directos a esas áreas para este acuario

Una línea encima de ellos muestra cuándo se actualizó el panel por última vez y de qué fuentes se surtió.

## Tocar para profundizar

Toca cualquier widget para abrir su detalle: el historial completo como gráfico, cada fuente que lo ha reportado y los umbrales actualmente aplicados. Desde ahí puedes registrar una lectura nueva a mano, cambiar el rango o mirar más atrás.

## Si un widget no tiene valor

Un widget muestra un valor en cuanto recibe uno. Cuando está en blanco, el motivo suele ser uno de estos:

- El dispositivo está sin conexión; revisa la pestaña **Dispositivos**
- El parámetro todavía no tiene fuente; regístralo a mano, o conecta un equipo que lo reporte
- El parámetro nunca se ha reportado ni registrado; todavía no se ha guardado nada para él

Una lectura antigua no desaparece porque la ventana del gráfico sea más corta que su antigüedad. Se queda en el widget con su antigüedad mostrada, así que un valor desactualizado se lee como desactualizado en lugar de como ausente.

Consulta **[Solución de problemas](/help/troubleshooting)** para cualquier cosa más allá de esto.
