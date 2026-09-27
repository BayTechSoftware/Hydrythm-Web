---
title: Sondas
description: Asigna las sondas de tu controlador a los parámetros de Cora, y registra calibración y limpieza.
section: Cora Mobile
reviewed: 2026-09-09
order: 13
group: Equipment
---

Un controlador informa de sus sondas con sus propios nombres. La asignación de sondas le indica a Cora cuál es tu sonda de pH, cuál es de temperatura, y así.

## Asignar sondas

Abre tu **perfil del acuario** (el lápiz en la parte superior del panel), despliega la sección de tu controlador y elige **Asignación de sondas**.

![Asignación de sondas](img/mobile-probes.webp "Cada sonda que informa tu controlador, su lectura en vivo y qué hace Cora con ella.")

Cada sonda que informa tu controlador aparece en la lista con su lectura actual. Cora detecta automáticamente los nombres estándar, y la fila muestra con cuál la ha emparejado, así que aquí normalmente solo hay que corregir las que no pudo ubicar, en lugar de asignarlas todas a mano.

Cada fila ofrece tres opciones:

- **Un parámetro de Cora**: la magnitud que mide esa sonda.
- **Personalizado**: para una sonda para la que Cora no tiene un parámetro estándar. Le das un identificador corto en mayúsculas, y se hace seguimiento con ese nombre.
- **Ignorar**: para sondas que no quieres que se registren en absoluto.

Una sonda ignorada o sin asignar no aparecerá en un panel y no alimentará alertas.

Las asignaciones surten efecto la próxima vez que se registren lecturas, así que una corrección aquí no reescribe el historial; cambia lo que se guarda a partir de ese momento. Pulsa **Guardar** para aplicarlas.

:::warning Una sonda sin asignar es invisible para Cora
Si un parámetro no muestra lecturas aunque la sonda funcione, revisa primero la asignación antes que ninguna otra cosa.
:::

## Varias sondas para un mismo parámetro

Un sistema con dos sondas de temperatura puede asignar ambas. Cora las mantiene como fuentes distintas; el ajuste de fuente del widget decide a cuál sigue una casilla, y [la vista del parámetro](/help/mobile-metric-detail) te permite compararlas.

## Registrar el cuidado de las sondas

Las sondas se desvían. Cora puede hacer seguimiento de cuándo se calibró o limpió cada una por última vez, para que puedas distinguir un cambio real de una sonda que necesita atención.

Registra la calibración o la limpieza desde la ficha de la sonda. También funciona bien como una [tarea de mantenimiento](/help/mobile-maintenance) recurrente.

:::note El historial de calibración explica las discrepancias
Cuando una sonda y un kit de pruebas no coinciden, la fecha en que se calibró la sonda por última vez suele ser lo primero que vale la pena revisar.
:::
