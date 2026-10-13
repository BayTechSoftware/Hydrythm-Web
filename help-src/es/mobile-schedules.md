---
title: Programar equipos
description: Crea un programa diario para una bomba Jecod, cópialo a otras bombas y consulta el programa de un gyre Maxspect (Beta).
section: Cora Mobile
reviewed: 2026-10-13
order: 14
group: Equipment
---

Usa esta página para darle a una bomba Jecod un **programa diario**: un conjunto de periodos, cada uno con su intensidad, que se repite todos los días. Ábrela desde **Dispositivos** → toca la bomba.

También puedes ver el horario de un gyre Maxspect *(Beta)* de la misma forma, pero se configura en la aplicación de Maxspect. Maxspect solo está abierto a los usuarios Beta. Consulta [Funciones Beta](/help/mobile-beta). Las luces y bombas de otras marcas tienen sus horarios en sus propias páginas: [EcoTech](/help/mobile-ecotech) *(Beta)*, y ReefRun y ReefDose de Red Sea en [Controlar tus equipos](/help/mobile-device-control#red-sea).

![La página de una bomba Jecod en Cora Mobile con Horario elegido](img/mobile-schedules.webp "Horario elegido arriba, la pausa de alimentación y después el gráfico del día.")

## Igual todo el día, u Horario {#same-all-day-or-schedule}

En la parte superior de la página de la bomba eliges uno de estos dos modos:

- **Igual todo el día**, con una sola intensidad constante
- **Horario**, con un programa diario dividido en periodos

Cora envía tu elección directamente a la bomba cuando tu teléfono está en su red. Si no lo está, se envía a través del Cora Max del acuario. Una bomba Bluetooth tiene que estar a tu alcance. Mientras no lo esté, lo que elijas aquí solo cambia lo que ves en pantalla.

Una pausa de alimentación saca la bomba de su horario durante un rato, y en tu teléfono el horario solo vuelve mientras la página de la bomba sigue abierta. Consulta [Pausa de alimentación](/help/mobile-device-control#jecod-feeding).

## El editor de horarios

Todas las pantallas de horario tienen las mismas tres partes.

El **gráfico del día** muestra el día entero, de 0 a 24 horas. Cada periodo es un bloque y su altura es la intensidad. Es la forma más rápida de comprobar que el programa hace lo que crees.

La **lista de periodos**, debajo del gráfico, muestra cada periodo con su horario, su modo y su intensidad, por ejemplo *Aleatorio, 00:00–03:00, Frec 50%, 40%*. Aquí añades, editas y quitas periodos.

Con **Agregar al programa** añades un periodo. Para cambiar uno, ábrelo y toca **Guardar**. Para quitarlo, toca **Eliminar**. Antes de borrarlo se te pide que lo confirmes.

Un gyre Maxspect *(Beta)* tiene dos cabezales, que aparecen como Gyre A y Gyre B. Por eso su gráfico del día tiene dos pistas, una por cabezal, y sus planes salen en **GYRE A** y **GYRE B**. El horario de un gyre solo se puede ver. En su fila de acciones pone **Solo lectura**, y el horario se configura en la aplicación de Maxspect.

:::warning El horario se guarda en el propio equipo
Al guardar, el programa se envía al equipo, que lo sigue con su propio reloj. Sigue funcionando aunque Cora no pueda conectarse con él.
:::

## Copiar un programa a otras bombas

Si tienes varias bombas que deben funcionar igual, crea un programa y cópialo.

Abre la bomba que tiene el programa, toca **Copiar horario a…** y elige la bomba de destino.

## Guardar y compartir un horario

No tienes que volver a crear un horario que ya te funciona:

- **Guardar horario como…** lo guarda con un nombre, y con **Horarios guardados…** lo vuelves a aplicar cuando quieras.
- **Compartir este horario** lo convierte en un código corto, y **Pegar un código de horario…** aplica uno que te hayan enviado. Es una función de Cora Mobile. El código contiene el horario, no da acceso a tu cuenta.

## Lejos de la red de la bomba

Cuando tu teléfono no está en la red de la bomba, Cora Mobile trabaja a través del Cora Max del acuario, con algunos límites:

- **Igual todo el día** y **Horario** cambian el modo de la bomba a través de ese Cora Max.
- Un periodo que añadas o cambies solo pasa por el Cora Max si este ha conectado con la bomba en la última hora. Si no, el horario te lo indica y no puedes cambiarlo desde donde estás.
- **Copiar horario a…**, **Guardar horario como…**, **Horarios guardados…**, **Compartir este horario** y **Pegar un código de horario…** necesitan que tu teléfono esté en la red de la bomba. Mientras tanto aparecen en gris y el menú te explica por qué.

Sin un Cora Max en el acuario, solo puedes cambiar una bomba mientras tu teléfono está en su red. Más información en [Conectar tus equipos](/help/mobile-connections#local-only).

A una bomba Bluetooth solo se llega desde un teléfono que esté cerca. Acércate para cambiarle el modo, cambiar su horario o usar cualquiera de esas opciones.

## Aplicar un programa

Puedes darle a una bomba un horario guardado en un solo paso, sin volver a crear los periodos. Abre la bomba, toca **Más** arriba y elige **Horarios guardados…**. La lista incluye todos los horarios guardados en este acuario, también los que creaste en otra bomba. Elige uno y toca **Aplicar**. Sustituye el día completo de la bomba.

## Comprobar que se ha aplicado

Después de guardar, la página del dispositivo muestra el programa que el equipo está siguiendo de verdad. Si no coincide con el tuyo, el cambio no llegó. Comprueba que el dispositivo está conectado y vuelve a intentarlo.
