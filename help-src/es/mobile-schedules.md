---
title: Programar equipos
description: Crea un programa diario para una bomba Jecod, cópialo a otras bombas y consulta el programa de un gyre Maxspect (beta).
section: Cora Mobile
reviewed: 2026-09-17
order: 12
group: Equipment
---

Las bombas y los gyres pueden seguir un **programa diario**. Es un conjunto de periodos, cada uno con su intensidad, que se repite todos los días. En las bombas Jecod puedes crear el programa directamente desde Cora. El programa de un gyre Maxspect *(beta)* aquí solo se puede ver. Se configura en la aplicación de Maxspect.

Abre el dispositivo desde la pestaña **Dispositivos**.

![El horario de una bomba](img/mobile-schedules.webp "El gráfico del día de 0 a 24 horas, con los periodos en una lista debajo.")

## Igual todo el día, u Horario

En la parte superior de la página de la bomba eliges uno de estos dos modos:

- **Igual todo el día**, con una sola intensidad constante
- **Horario**, con un programa diario dividido en periodos

Tu elección se envía a la bomba. Si tu teléfono no está en la red de la bomba, se envía a través del Cora Max del acuario. Una bomba Bluetooth tiene que estar a tu alcance. Mientras no lo esté, lo que elijas aquí solo cambia lo que ves en pantalla.

## El editor de horarios

Todas las pantallas de horario tienen las mismas tres partes.

El **gráfico del día** muestra el día entero, de 0 a 24 horas. Cada periodo es un bloque y su altura es la intensidad. Es la forma más rápida de comprobar que el programa hace lo que crees.

La **lista de periodos**, debajo del gráfico, muestra cada periodo con su horario, su modo y su intensidad, por ejemplo *Aleatorio, 00:00–03:00, Frec 50%, 40%*. Aquí añades, editas y quitas periodos.

Con **Agregar al programa** añades un periodo. Para cambiar uno, ábrelo y toca **Guardar**. Para quitarlo, toca **Eliminar**. Antes de borrarlo se te pide que lo confirmes.

Un gyre Maxspect *(beta)* tiene dos cabezales, que aparecen como Gyre A y Gyre B. Por eso su gráfico del día tiene dos pistas, una por cabezal, y sus planes salen en **GYRE A** y **GYRE B**. El horario de un gyre solo se puede ver. En su fila de acciones pone **Solo lectura**, y el horario se configura en la aplicación de Maxspect.

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

A una bomba Bluetooth solo se llega desde un teléfono que esté cerca. Acércate para cambiarle el modo, cambiar su horario o usar cualquiera de esas opciones.

## Aplicar un programa preparado

También puedes darle a una bomba un programa ya preparado en un solo paso, sin crear los periodos a mano.

## Comprobar que se ha aplicado

Después de guardar, la página del dispositivo muestra el programa que el equipo está siguiendo de verdad. Si no coincide con el tuyo, el cambio no llegó. Comprueba que el dispositivo está conectado y vuelve a intentarlo.
