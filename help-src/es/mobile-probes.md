---
title: Asignación de parámetros y sondas
description: Elige qué sonda da cada lectura, dile a Cora qué mide cada sonda y registra la calibración y la limpieza de las sondas.
section: Cora Mobile
reviewed: 2026-10-13
order: 15
group: Equipment
---

Usa **Asignación de parámetros** para decirle a Cora qué mide cada sonda y, cuando dos sondas informan de lo mismo, en cuál confiar. Ve a **Ajustes**, abre el acuario y toca **Asignación de parámetros**.

Está entre **Editar acuario** y **Umbrales de alerta**. El lápiz de la parte superior del panel abre **Editar acuario**, que no la tiene. También puedes llegar desde las páginas de dispositivo de Neptune Apex.

La pantalla tiene un campo de búsqueda (**Buscar parámetros**) y dos pestañas, **Asignación** y **Fuentes**. La búsqueda mira los nombres de parámetros, los nombres de sondas, los dispositivos y las marcas. El mismo campo de búsqueda está en todos los selectores de parámetros.

## Sondas: decirle a Cora qué es cada una {#mapping}

![La pestaña Asignación](img/mobile-probe-mapping.webp "Cada sonda, agrupada por el dispositivo del que procede, con el parámetro al que está asignada.")

La pestaña **Asignación** se abre primero. Lista todas las sondas que Cora conoce, agrupadas por el dispositivo del que proceden, con su lectura actual. Cora reconoce sola los nombres estándar de las sondas, y cada fila indica con qué la ha emparejado. Normalmente solo tienes que corregir las pocas que no ha sabido identificar.

Cada fila te da tres opciones.

- **Un parámetro de Cora** es lo que mide esa sonda.
- **Personalizado…** es para una sonda sin parámetro estándar en Cora. Escribe un nombre corto en mayúsculas en **Parámetro personalizado (token en MAYÚSCULAS)**, y Cora la sigue con ese nombre.
- **Ignorar** es para las sondas que no quieres registrar en absoluto.

Una sonda ignorada o sin asignar no sale en ningún panel y no genera alertas.

Una asignación empieza a funcionar con las siguientes lecturas. Corregirla aquí no reescribe el historial. Solo cambia lo que se guarda desde ese momento. Toca **Guardar** para aplicar los cambios.

:::warning Cora no ve una sonda sin asignar
Si un parámetro no muestra lecturas pero la sonda funciona, revisa primero su asignación.
:::

## De dónde viene cada lectura {#sources}

![La pestaña Fuentes](img/mobile-probes.webp "Cada lectura, la sonda que la alimenta y si está en Automático o Elegido por ti.")

La pestaña **Fuentes** lista cada parámetro que Cora sigue para este acuario, como el pH o la temperatura, y muestra qué sonda lo está alimentando ahora.

Toca una lectura para ver todas las sondas que informan de ella, entre todos los controladores que has conectado. Cada una muestra su marca, el nombre que le da a la sonda su propio controlador y su valor en directo. Elige una para fijarla, o elige **Automático (gana la lectura más reciente)** para que Cora use la sonda que haya informado más recientemente. Las demás se quedan en el historial.

Una etiqueta junto a cada lectura indica cuál está en efecto: **Automático**, o **Elegido por ti** una vez que has fijado una sonda. Tu elección se aplica a esa lectura en todo el acuario, no a un solo widget.

Si una sonda fijada deja de informar, Cora muestra cuándo se supo de ella por última vez y ofrece **Volver a Automático**, para que una sonda muerta no deje una lectura bloqueada.

Toca **Renombrar** para darle a una lectura su propio nombre. Es independiente del nombre que le des a la propia sonda. Es lo que aparece en tu panel, en las alertas y en Reef Buddy.

El perfil del acuario también tiene una sección **Fuentes de parámetros** (está oculta mientras creas un acuario nuevo). Configura lo mismo de forma más resumida. Usa Asignación de parámetros cuando quieras ver todas las sondas de todos los controladores en un solo sitio.

:::note Un sensor de fugas no se puede reasignar aquí
La alarma de un sensor de fugas depende de su propio nombre, así que queda fuera de este selector. Funciona igual que siempre.
:::

## Varias sondas para un mismo parámetro {#multiple-probes}

Si tienes dos sondas de temperatura, ya sea en el mismo controlador o en dos distintos, asigna las dos. Cora las guarda como fuentes distintas, y la pestaña **Fuentes** es donde eliges cuál da la lectura, o la dejas en Automático. Puedes compararlas en [la vista del parámetro](/help/mobile-metric-detail).

Cuando dos fuentes informan del mismo parámetro, gana la medición más reciente. Un valor en pantalla solo lo reemplaza una lectura con una hora de medición posterior, venga del dispositivo que venga. Una lectura más antigua, o un dispositivo que reenvía una antigua, va al historial y no sobrescribe el valor actual. Si fijaste una fuente en la pestaña **Fuentes**, Cora sigue esa fuente.

## Registrar el cuidado de las sondas {#recording-probe-care}

Las sondas se descalibran. Cuando calibres, limpies o cambies una sonda, díselo a Cora, para que no confunda el salto de la lectura con un cambio real en el acuario.

1. Toca el widget del parámetro en el panel, por ejemplo pH, temperatura, salinidad u ORP.
2. Toca **Registrar cuidado de sonda** (el icono del sensor) en la barra superior.
3. Elige lo que hiciste: **Calibrada**, **Limpiada**, **Reemplazada**, **Reposicionada** o **Comparada con una referencia**. Puedes añadir una **Lectura de referencia** y una nota.
4. Toca **Registrar cuidado de sonda**.

La vista del parámetro muestra entonces cuánto hace que se calibró esa sonda. El cuidado de las sondas también funciona bien como [tarea de mantenimiento](/help/mobile-maintenance) periódica.

:::note Las fechas de calibración explican las diferencias
Cuando una sonda y un kit de pruebas no coinciden, mira cuándo calibraste la sonda por última vez. Casi siempre esa es la respuesta.
:::
