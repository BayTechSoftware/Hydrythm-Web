---
title: Referencia de widgets
description: Cada tipo de widget en Cora (valor, medidor, gráfico, estado, toma y las casillas de dispositivo) y cuándo usar cada uno.
section: Cora Mobile
reviewed: 2026-09-17
order: 7
group: Your dashboard
---

Un widget es una casilla en tu panel que muestra una sola cosa. Esta página cubre cada tipo y qué puedes configurar.

Añádelos y ordénalos en **[el editor de panel](/help/mobile-dashboard-editing)**; toca un widget ahí para abrir sus ajustes.

![Configurar un widget](img/mobile-widget-config.webp "Tipo, parámetro, y luego ancho y alto.")

## Los nueve tipos

| Tipo | Muestra |
|---|---|
| **Valor** | La lectura actual, su unidad, antigüedad y fuente |
| **Medidor** | Un arco con tu rango marcado en bandas y una marca en el valor |
| **Gráfico** | Una tendencia en una ventana que elijas |
| **Estado** | Un estado como texto: en marcha, inactivo, cerrado |
| **Toma** | Un control de tres posiciones: Auto, Apagado, Encendido |
| **ReefBeat** | Una unidad Red Sea, con su propio resumen |
| **Módulo Apex** | Un módulo Apex instalado, como un Trident o un DŌS |
| **Jecod** | Una bomba Jecod, con su modo e intensidad |
| **Maxspect** *(beta)* | Un gyre, con ambos motores |

Los últimos cuatro son casillas de **dispositivo**: están vinculadas a un equipo en lugar de a un parámetro, y cada una muestra lo que esa unidad reporte.

## Tamaño

**Ancho** y **Alto** son cada uno **1×** o **2×**. Un gráfico nunca tiene un ancho de una sola celda.

## Valor

El número simple. Lectura actual, su unidad, cuán antigua es y de dónde viene.

Úsalo para parámetros que revisas numéricamente en lugar de por tendencia: calcio, magnesio, nitrato.

**Ajustes:** etiqueta, fuente, tamaño.

## Medidor

Un arco con tu rango objetivo marcado en bandas y una marca en el valor actual. El color de la marca te dice dónde estás: dentro de la banda, desviándose, o fuera.

Úsalo para los parámetros que gestionas activamente: alcalinidad, pH, salinidad, temperatura.

**Ajustes:** etiqueta, fuente, rango (heredado de los objetivos de tu acuario a menos que lo anules aquí), tamaño.

:::note Usa medidores de dos columnas o más
En una sola columna el arco es demasiado pequeño para leerlo de un vistazo; usa un widget de **valor** en su lugar si el espacio es limitado.
:::

## Gráfico

Una minigráfica en una ventana que elijas, con el máximo y el mínimo marcados y el valor actual destacado.

Para un parámetro que pruebas (con Trident o con un kit de pruebas), la línea une tus pruebas reales. Si la ventana solo contiene una prueba, la línea entra desde la prueba anterior a ella, y no se marca ni máximo ni mínimo. Sin ninguna prueba en la ventana, o sin nada anterior con qué unir una sola prueba, la casilla muestra **Recopilando…** en lugar de una línea.

Úsalo para cualquier cosa que se mueva: pH a lo largo del día, temperatura durante una ola de calor, alcalinidad entre dosis.

**Ajustes:** etiqueta, fuente, **ventana de tiempo** (1 hora, 6 horas, 24 horas, 7 días, 30 días, 1 año), tamaño.

Una tendencia siempre tiene **al menos dos celdas de ancho**; una minigráfica apretada en una sola celda no te dice nada, así que el editor no va a crear una así.

:::note Elige la ventana según el ritmo
El pH oscila en un ciclo diario, así que 24 horas te muestra la forma. La alcalinidad se mueve durante días, así que 7 o 30 te dicen más de lo que 24 dirá nunca.
:::

## Estado

Texto en lugar de un número, para cosas que son un estado. En marcha, inactivo, abierto, cerrado, alimentando.

**Ajustes:** etiqueta, fuente, tamaño.

## Toma

Un interruptor de tres posiciones para una toma: **Auto**, **Apagado**, **Encendido**.

- **Auto** devuelve la toma a lo que normalmente la gestiona: un horario, una regla, o el controlador al que pertenece.
- **Apagado** y **Encendido** son anulaciones manuales que se quedan hasta que las cambies de vuelta.

**Ajustes:** etiqueta, qué toma, tamaño.

:::warning Una anulación manual no caduca
Apagado significa apagado hasta que lo vuelvas a poner en Auto. Si apagas una bomba de retorno para trabajar en el acuario, vuelve a ponerla en Auto cuando termines; Cora no lo hará por ti.
:::

## ReefBeat

Una casilla para todo un equipo, mostrando su propio resumen en lugar de un solo parámetro: el estado y el depósito de un ATO, los cabezales de una unidad de dosificación, los días restantes de un rodillo de estera.

Qué dispositivos ofrecen una casilla depende de lo que tengas conectado. Consulta **[Conectar tu equipo](/help/mobile-connections)**.

**Ajustes:** etiqueta, qué dispositivo, tamaño.

## Qué muestra un widget de parámetro

En un widget respaldado por un parámetro medido (Valor, Medidor, Gráfico y Estado), siempre hay tres cosas presentes. Las casillas de Toma y de dispositivo muestran su propio estado en su lugar, porque no hay una sola lectura detrás de ellas:

- **El valor**, en grande
- **La antigüedad** (`now`, `1h`, `2d`): cuán antigua es la lectura, no cuándo se actualizó la pantalla por última vez
- **La fuente**: una pequeña insignia que indica de dónde vino el número

Toca cualquier widget para abrir su historial completo, cada fuente que lo reporta y los umbrales en vigor.

## Tamaños

Los widgets tienen uno o dos celdas de ancho y una o dos de alto, excepto una **tendencia**, que siempre tiene al menos dos de ancho. En un panel de tres columnas, un medidor de dos de ancho ocupa dos tercios de la fila, que suele ser la forma adecuada para tu parámetro más importante.
