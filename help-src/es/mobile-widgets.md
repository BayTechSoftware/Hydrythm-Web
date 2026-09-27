---
title: Tipos de widget
description: Los tipos de widget de Cora (valor, medidor, gráfico, estado, toma y las casillas de dispositivo) y cuándo te conviene cada uno.
section: Cora Mobile
reviewed: 2026-09-17
order: 7
group: Your dashboard
---

Un widget es una casilla de tu panel que muestra una sola cosa. Aquí tienes cada tipo y lo que puedes configurar en él.

Los añades y los colocas en [el editor del panel](/help/mobile-dashboard-editing). Toca un widget en el editor para abrir sus ajustes.

![Configurar un widget](img/mobile-widget-config.webp "Tipo, parámetro, y luego ancho y alto.")

## Los nueve tipos

| Tipo | Muestra |
|---|---|
| **Valor** | La lectura actual, con su unidad, su antigüedad y su fuente |
| **Medidor** | Un arco con tu rango marcado en bandas y una marca en el valor |
| **Gráfico** | La tendencia en el periodo que elijas |
| **Estado** | Un estado en texto, como en marcha, inactivo o cerrado |
| **Toma** | Un control de tres posiciones: Auto, Apagado, Encendido |
| **ReefBeat** | Un equipo Red Sea, con su propio resumen |
| **Módulo del Apex** | Un módulo Apex instalado, como un Trident o un DŌS |
| **Jecod** | Una bomba Jecod, con su modo y su intensidad |
| **Maxspect** *(beta)* | Un gyre, con sus dos motores |

Los cuatro últimos son casillas de **dispositivo**. Cada una va ligada a un equipo, no a un parámetro, y muestra lo que ese equipo informe.

## Tamaño

**Ancho** y **Alto** pueden ser **1×** o **2×**. Un gráfico nunca ocupa una sola celda de ancho.

## Valor

El número tal cual. Ves la lectura actual, su unidad, su antigüedad y de dónde viene.

Va bien para los parámetros que miras por el número más que por la tendencia, como el calcio, el magnesio o el nitrato.

Puedes cambiar la etiqueta, la fuente y el tamaño.

## Medidor

Un arco con tu rango objetivo marcado en bandas y una marca en el valor actual. El color de la marca te dice dónde estás. Puede estar dentro de la banda, empezando a desviarse o fuera.

Va bien para los parámetros que controlas de cerca, como la alcalinidad, el pH, la salinidad o la temperatura.

Puedes cambiar la etiqueta, la fuente, el rango y el tamaño. El rango sale de los objetivos de tu acuario, salvo que pongas otro aquí.

:::note Dale al medidor dos columnas o más
En una sola columna el arco queda demasiado pequeño para leerlo de un vistazo. Si te falta espacio, usa un widget de **valor**.
:::

## Gráfico

Una línea de tendencia en el periodo que elijas, con el máximo y el mínimo marcados y el valor actual destacado.

Si el parámetro lo mides con pruebas (con Trident o con un kit), la línea une tus pruebas reales. Cuando en el periodo solo hay una prueba, la línea llega desde la prueba anterior y no se marcan máximo ni mínimo. Si no hay ninguna prueba en el periodo, o no hay una prueba anterior con la que unir la única que hay, la casilla muestra **Recopilando…** y no dibuja línea.

Úsalo para todo lo que cambia: el pH a lo largo del día, la temperatura durante una ola de calor, la alcalinidad entre dosis.

Puedes cambiar la etiqueta, la fuente, el **rango de tiempo** (1 hora, 6 horas, 24 horas, 7 días, 30 días, 1 año) y el tamaño.

Una tendencia ocupa siempre **al menos dos celdas de ancho**. En una sola celda la línea no dice nada, así que el editor no la crea.

:::note Elige el periodo según el ritmo del parámetro
El pH sube y baja cada día, así que con 24 horas ves bien el ciclo. La alcalinidad cambia a lo largo de varios días, y con 7 o 30 días verás mucho más que con 24 horas.
:::

## Estado

Muestra un texto para las cosas que son un estado y no un número. Por ejemplo, en marcha, inactivo, abierto, cerrado o alimentando.

Puedes cambiar la etiqueta, la fuente y el tamaño.

## Toma

Un interruptor de tres posiciones para una toma: **Auto**, **Apagado** y **Encendido**.

- **Auto** devuelve la toma a lo que la controla normalmente, sea un programa, una regla o el controlador al que pertenece.
- **Apagado** y **Encendido** son cambios manuales. Se mantienen hasta que tú los cambies.

Puedes cambiar la etiqueta, la toma y el tamaño.

:::warning Un cambio manual no caduca
Apagado es apagado hasta que vuelvas a ponerla en Auto. Si apagas la bomba de retorno para trabajar en el acuario, vuelve a ponerla en Auto al terminar. Cora no lo hace por ti.
:::

## ReefBeat

Una casilla para un equipo completo, con su propio resumen. Por ejemplo, el estado y el depósito de un ATO, los cabezales de una dosificadora o los días que le quedan a un rollo de fieltro.

Los dispositivos que tienen casilla dependen de lo que hayas conectado. Lo tienes en [Conectar tus equipos](/help/mobile-connections).

Puedes cambiar la etiqueta, el dispositivo y el tamaño.

## Qué muestra un widget de parámetro

Los widgets que dependen de un parámetro medido (Valor, Medidor, Gráfico y Estado) muestran siempre tres cosas:

- **El valor**, en grande
- **La antigüedad** (`now`, `1h`, `2d`), es decir, cuánto tiempo tiene la lectura, no cuándo se actualizó la pantalla
- **La fuente**, una pequeña insignia que indica de dónde viene el número

Las casillas de toma y de dispositivo muestran su propio estado, porque detrás de ellas no hay una sola lectura.

Toca cualquier widget para abrir su historial completo, todas las fuentes que lo informan y los umbrales que se aplican.

## Tamaños

Los widgets ocupan una o dos celdas de ancho y una o dos de alto. La excepción es la **tendencia**, que siempre ocupa al menos dos de ancho. En un panel de tres columnas, un medidor de dos de ancho llena dos tercios de la fila. Suele ser la mejor forma de mostrar tu parámetro más importante.
