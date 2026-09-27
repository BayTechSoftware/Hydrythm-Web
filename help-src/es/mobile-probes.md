---
title: Sondas
description: Asigna las sondas de tu controlador a los parámetros de Cora y registra la calibración y la limpieza.
section: Cora Mobile
reviewed: 2026-09-09
order: 13
group: Equipment
---

Cada controlador llama a sus sondas con sus propios nombres. Con la asignación de sondas le dices a Cora cuál es la de pH, cuál la de temperatura, etc.

## Asignar sondas

Abre el **perfil del acuario** (el lápiz de la parte superior del panel), despliega la sección de tu controlador y elige **Asignación de sondas**.

![Asignación de sondas](img/mobile-probes.webp "Cada sonda de tu controlador, su lectura en vivo y qué hace Cora con ella.")

La lista muestra cada sonda de tu controlador con su lectura actual. Cora reconoce sola los nombres estándar, y cada fila indica con qué parámetro la ha emparejado. Normalmente solo tienes que corregir las que no ha sabido identificar.

En cada fila tienes tres opciones:

- **Un parámetro de Cora**: lo que mide esa sonda.
- **Personalizado**: para una sonda sin parámetro estándar en Cora. Le pones un identificador corto en mayúsculas y Cora la sigue con ese nombre.
- **Ignorar**: para las sondas que no quieres registrar.

Una sonda ignorada o sin asignar no sale en ningún panel y no genera alertas.

Los cambios se aplican a partir de las siguientes lecturas. El historial no se reescribe, solo cambia lo que se guarda desde ese momento. Toca **Guardar** para aplicarlos.

:::warning Cora no ve una sonda sin asignar
Si un parámetro no muestra lecturas pero la sonda funciona, revisa primero la asignación.
:::

## Varias sondas para un mismo parámetro

Si tienes dos sondas de temperatura, puedes asignar las dos. Cora las guarda como fuentes distintas. El ajuste de fuente del widget decide qué sonda muestra cada casilla, y en [la vista del parámetro](/help/mobile-metric-detail) puedes compararlas.

## Registrar el cuidado de las sondas

Con el tiempo, las sondas se descalibran. Cora puede guardar cuándo calibraste o limpiaste cada una por última vez. Así sabrás si un cambio es real o si la sonda necesita atención.

Registra la calibración o la limpieza desde la ficha de la sonda. También puedes crear una [tarea de mantenimiento](/help/mobile-maintenance) recurrente para ello.

:::note La calibración explica muchas diferencias
Si una sonda y un kit de pruebas no coinciden, lo primero que conviene mirar es cuándo calibraste la sonda por última vez.
:::
