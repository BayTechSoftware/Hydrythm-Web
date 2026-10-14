---
title: Referencia de widgets
description: Todos los tipos de widget del panel de Cora Mobile, desde valor, medidor, gráfico, estado y toma hasta las casillas de dispositivos, y cuándo usar cada uno.
section: Cora Mobile
reviewed: 2026-10-13
order: 9
group: Your dashboard
---

Un widget es una casilla de tu panel, y muestra una sola cosa. Esta página repasa cada tipo y lo que puedes configurar en él.

Los widgets se añaden y se colocan en [el editor del panel](/help/mobile-dashboard-editing). Toca ahí un widget para abrir sus ajustes: **Tipo** y **Parámetro** en un widget de parámetro, la toma o el dispositivo en los demás, después **Ancho** y **Alto**, y **Rango de tiempo** en un gráfico.

![La hoja de ajustes de un widget en Cora Mobile](img/mobile-widget-config.webp "La mitad inferior de los ajustes de un widget: el parámetro, el ancho, el alto y el rango de tiempo, y después Quitar y Listo.")

## Los quince tipos {#the-fifteen-types}

| Tipo | Muestra |
|---|---|
| **Valor** | La lectura actual, con su unidad, su antigüedad y su fuente |
| **Medidor** | Un arco con tu rango marcado en bandas y una marca en el valor |
| **Gráfico** | La tendencia en el rango de tiempo que elijas |
| **Estado** | La lectura en texto, con un punto de color |
| **Toma** | Un control de tres posiciones: Auto, Apagado, Encendido |
| **ReefBeat** | Un equipo Red Sea, con su propio resumen |
| **Módulo del Apex** | Un módulo Apex instalado, como un Trident o un DŌS |
| **Jecod** | Una bomba Jecod, con su modo y su intensidad |

Todo lo que va después de Toma son casillas de **dispositivo**. Cada una pertenece a un equipo en lugar de a un parámetro, y muestra lo que ese equipo informe. Cora Max también tiene una casilla de **Escena**, que se añade en Cora Max. Consulta [Editar el panel de Cora Max](/help/max-dashboard-editing).


## Tamaño {#sizing}

**Ancho** y **Alto** pueden ser **1×** o **2×**, así que un widget ocupa una o dos celdas de ancho y una o dos de alto. Un gráfico nunca ocupa una sola celda de ancho. En un panel de tres columnas, un medidor de dos de ancho ocupa dos tercios de la fila. Suele ser una buena forma para tu parámetro más importante.

## Qué muestra un widget de parámetro {#what-a-parameter-widget-shows}

Los widgets Valor, Medidor, Gráfico y Estado muestran un parámetro medido, y siempre muestran tres cosas. Las casillas de toma y de dispositivo muestran su propio estado, porque no hay una sola lectura detrás.

- **El valor**, en grande
- **La antigüedad** (`now`, `1h`, `2d`), que es cuánto hace que la fuente confirmó el valor por última vez. En una sonda, es cuándo se comunicó su dispositivo por última vez, así que una lectura estable sigue reciente. En un resultado de kit de pruebas o de ICP, es cuándo hiciste la prueba. Más información en [Leer tu panel](/help/mobile-dashboard#how-to-read-a-parameter-widget).
- **La fuente**, una pequeña insignia que indica de dónde viene el número

Un widget de parámetro no tiene ajuste propio de rango ni de fuente. El rango sale de los umbrales de alerta del acuario (mantén pulsado el widget en el panel), y la fuente de [Asignación de parámetros](/help/mobile-probes). Toca el widget en el panel para ver todo su historial, cada fuente que lo informa y tu banda de alerta.

## Valor {#value}

Es el número tal cual. Muestra la lectura actual, su unidad, su antigüedad y de dónde viene.

Úsalo para los parámetros que miras por el número más que por la tendencia, como el calcio, el magnesio o el nitrato.

## Medidor {#gauge}

Un medidor es un arco con tu rango de alerta marcado y una marca en el valor actual. El color de la marca te dice dónde estás: dentro del rango, desviándote o fuera.

Úsalo para los parámetros que controlas de cerca, como la alcalinidad, el pH, la salinidad o la temperatura.

:::note Dale al medidor al menos dos columnas de ancho
En una sola columna el arco queda demasiado pequeño para leerlo de un vistazo. Si te falta espacio, usa un widget **Valor**.
:::

## Gráfico {#graph}

Un gráfico es una línea de tendencia en el rango de tiempo que elijas: 1h, 6h, 24h, 7d, 30d o 1y. Marca el máximo y el mínimo y destaca el valor actual.

En un parámetro que mides con pruebas (con un Trident o un kit), la línea une tus pruebas reales. Si en el periodo solo hay una prueba, la línea llega desde la prueba anterior y no hay máximo ni mínimo. Si no hay ninguna prueba en el periodo, o no hay nada anterior con lo que unir una sola prueba, la casilla muestra **Recopilando…** en lugar de una línea.

Úsalo para todo lo que se mueve, como el pH a lo largo del día, la temperatura en una ola de calor o la alcalinidad entre dosis.

Un gráfico siempre ocupa **al menos dos celdas de ancho**. Una línea de tendencia apretada en una sola celda no dice nada, así que el editor no te deja hacerlo.

:::note Elige el rango que encaje con el parámetro
El pH sube y baja en un ciclo diario, así que con 24 horas ves el patrón. La alcalinidad cambia a lo largo de días, así que con 7 o 30 días ves mucho más.
:::

## Estado {#status}

Muestra la lectura en texto, con un punto de color para dentro del rango, desviándose o fuera. Úsalo para un parámetro que no tiene un rango útil para un medidor.

## Toma {#outlet}

Es un interruptor de tres posiciones para una toma del Apex: **Auto**, **Apagado** y **Encendido**. Tú eliges qué toma controla.

- **Auto** devuelve la toma a lo que la controla normalmente. Puede ser un programa, una regla o el controlador al que pertenece.
- **Apagado** y **Encendido** son cambios manuales. Se mantienen hasta que los vuelvas a cambiar.

:::warning Un cambio manual no caduca
Apagado significa apagado hasta que vuelvas a ponerla en Auto. Si apagas la bomba de retorno para trabajar en el acuario, vuelve a ponerla en Auto al terminar. Cora no lo hace por ti.
:::

## ReefBeat {#reefbeat}

Es una casilla para un equipo completo. Muestra el resumen propio del equipo en lugar de un solo parámetro, por ejemplo el estado y el depósito de un ATO, los cabezales de una dosificadora o los días que le quedan a un rollo de fieltro. Tú eliges qué dispositivo muestra.

Qué dispositivos pueden tener casilla depende de lo que hayas conectado. Consulta [Conectar tus equipos](/help/mobile-connections).

## Casillas de dosificadora {#doser-tiles}

La casilla de una dosificadora (un DŌS de Apex o una ReefDose) muestra una fila por cabezal. El nombre de un cabezal nunca se reduce por debajo de un tamaño legible. En una casilla alta, la fila ocupa dos líneas, con el nombre en la primera y lo que queda en la segunda, por ejemplo *40d* y *2,8 L*. En una casilla baja se quita la línea de detalle y el nombre se mantiene legible.

Elige qué va primero con **Mostrar lo restante como**: **Días** o **Mililitros (mL)**. Un cabezal ReefDose sin nombre propio se muestra como el nombre del dispositivo seguido de "head" y su número. La casilla de una dosificadora Jecod es de solo lectura y muestra el plan diario, porque Jecod no informa de cuánto queda en la botella.
