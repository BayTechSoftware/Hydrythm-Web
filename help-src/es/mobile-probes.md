---
title: Asignación de parámetros
description: Consulta qué sonda controla cada lectura entre todos tus controladores, y registra la calibración y la limpieza.
section: Cora Mobile
reviewed: 2026-10-12
order: 13
group: Equipment
---

Si tienes más de un controlador, o dos sondas que miden lo mismo, Cora necesita saber en cuál de las lecturas confiar. **Asignación de parámetros** es donde resuelves eso, y donde le dices a Cora qué es cada sonda desde el principio.

Ve a **Ajustes**, abre el acuario y elige **Asignación de parámetros**. Está entre **Editar acuario** y **Umbrales de alerta**. El lápiz de la parte superior del panel abre **Editar acuario**, que no la tiene. También puedes llegar desde las páginas de dispositivo de Neptune Apex y GHL (Beta). GHL solo está abierto a los usuarios Beta. Consulta [Funciones Beta](/help/mobile-beta).

La pantalla tiene un campo de búsqueda (**Buscar parámetros**) y dos pestañas, **Asignación** y **Fuentes**. La búsqueda mira los nombres de parámetros, los nombres de sondas, los dispositivos y las marcas. El mismo campo de búsqueda está en todos los selectores de parámetros.

## De dónde viene cada lectura

Esta es la pestaña **Fuentes**.

![De dónde viene cada lectura](img/mobile-probes.webp "Cada parámetro, qué sonda lo controla, y un botón Elegir para cambiarlo.")

Esta sección lista cada parámetro que Cora sigue para este acuario, como el pH o la temperatura, y muestra qué sonda lo está alimentando en este momento.

Toca una lectura para ver todas las sondas que la informan, entre todos los controladores que has conectado. Cada una muestra su marca, el nombre que le da su propio controlador y su valor en directo. Elige una para fijarla, o elige **Automático (gana la lectura más reciente)** para que Cora use la que haya informado más recientemente. Las demás se quedan en el historial.

Una etiqueta junto a cada lectura indica cuál está en efecto: **Automático**, o **Elegida por ti** una vez que has fijado una sonda.

Si una sonda fijada deja de informar, Cora muestra cuándo se supo de ella por última vez y ofrece **Volver a Automático**, para que una sonda muerta no deje una lectura bloqueada.

Toca **Cambiar nombre** para darle a una lectura su propio nombre de pantalla. Es independiente del nombre que le des a la sonda en sí. Es lo que aparece en tu panel, en las alertas y en Reef Buddy.

:::note Un sensor de fugas no se puede reasignar aquí
La alarma de un sensor de fugas depende de su propio nombre, así que queda fuera de este selector. Funciona igual que siempre.
:::

## Sondas: decirle a Cora qué es cada una

La pestaña **Asignación** se abre primero. Lista todas las sondas que Cora conoce, agrupadas por el dispositivo que las informa, con su lectura actual. Cora reconoce sola los nombres estándar de las sondas, y cada fila indica con qué ha emparejado cada una. Normalmente solo tienes que corregir las que no ha sabido identificar.

Cada fila te da tres opciones.

- **Un parámetro de Cora**: lo que mide esa sonda.
- **Personalizado**: para una sonda sin parámetro estándar en Cora. Le pones un identificador corto en mayúsculas y Cora la sigue con ese nombre.
- **Ignorar**: para las sondas que no quieres registrar.

Una sonda ignorada o sin asignar no sale en ningún panel y no genera alertas.

Los cambios se aplican a partir de las siguientes lecturas. El historial no se reescribe, solo cambia lo que se guarda desde ese momento. Toca **Guardar** para aplicarlos.

:::warning Cora no ve una sonda sin asignar
Si un parámetro no muestra lecturas pero la sonda funciona, revisa primero su asignación.
:::

## Varias sondas para un mismo parámetro

Si tienes dos sondas de temperatura, ya sea en el mismo controlador o en dos distintos, asigna las dos. Cora las guarda como fuentes distintas, y la pestaña **Fuentes** es donde eliges cuál controla la lectura, o la dejas en Automático. Puedes compararlas en [la vista del parámetro](/help/mobile-metric-detail).

Cuando dos fuentes informan el mismo parámetro, gana la medición más reciente. Un valor en pantalla solo lo reemplaza una lectura con una hora de medición posterior, venga del dispositivo que venga. Una lectura más antigua, o un dispositivo que reenvía una antigua, va al historial y no sobrescribe el valor actual. Si fijaste una fuente, Cora sigue esa fuente.

## Registrar el cuidado de las sondas

Con el tiempo, las sondas se descalibran. Cora puede guardar cuándo calibraste o limpiaste cada una por última vez. Así sabrás si un cambio es real o si la sonda necesita atención.

Registra la calibración o la limpieza desde la ficha de la sonda. También puedes crear una [tarea de mantenimiento](/help/mobile-maintenance) recurrente para ello.

:::note La calibración explica muchas diferencias
Si una sonda y un kit de pruebas no coinciden, lo primero que conviene mirar es cuándo calibraste la sonda por última vez.
:::
