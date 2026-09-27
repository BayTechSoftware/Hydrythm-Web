---
title: Programar equipos
description: Crea un programa diario para una bomba Jecod y cópialo entre bombas, y consulta el programa de un gyre Maxspect (beta).
section: Cora Mobile
reviewed: 2026-09-17
order: 12
group: Equipment
---

Las bombas y los gyres pueden ejecutar un **programa diario**: un conjunto de periodos, cada uno con su propia intensidad, que se repite cada día. Cora puede crear estos directamente para bombas Jecod. El programa de un gyre Maxspect *(beta)* solo se puede consultar aquí: se fija en la aplicación Maxspect.

Abre el dispositivo desde la pestaña **Dispositivos**.

![El horario de una bomba](img/mobile-schedules.webp "El gráfico del día de 0 a 24 horas, con cada periodo listado debajo.")

## Igual todo el día, u Horario

Una bomba funciona en uno de dos modos, elegido en la parte superior de su página:

- **Igual todo el día**: una intensidad, constante
- **Horario**: un programa diario con periodos

Tu elección se envía a la bomba, a través del Cora Max del acuario cuando tu teléfono no está en la red de la bomba. Una bomba Bluetooth tiene que estar al alcance: hasta entonces, elegir aquí solo cambia lo que estás viendo.

## El editor de horarios

Cada pantalla de horario tiene las mismas tres partes:

**El gráfico del día**: el día completo de 0 a 24 horas, con cada periodo dibujado como un bloque cuya altura es su intensidad. Es la forma más rápida de ver si un programa hace lo que crees.

**La lista de periodos**: cada periodo debajo del gráfico, con sus horas, su modo y su intensidad: *Aleatorio, 00:00-03:00, Frec 50%, 40%*. Añade, edita y elimina periodos aquí.

**Añadir y cambiar periodos**: **Agregar al programa** añade un periodo. Abre un periodo para cambiarlo y toca **Guardar**, o **Eliminar** para quitarlo; se te pide confirmar antes de que se vaya.

Un gyre Maxspect *(beta)* tiene dos cabezales, mostrados como Gyre A y Gyre B, así que su gráfico del día tiene dos pistas, una para cada uno, y sus planes se listan bajo **GYRE A** y **GYRE B**. El horario de un gyre es solo de lectura: su fila de acción dice **Solo lectura**, y el horario se fija en la aplicación Maxspect.

:::warning Un horario se escribe en el dispositivo
Guardar envía el programa al equipo, que luego lo ejecuta con su propio reloj. Sigue funcionando tanto si Cora es accesible como si no.
:::

## Copiar un programa entre bombas

Si usas varias bombas que deberían comportarse igual, crea un programa y cópialo.

Abre la bomba cuyo programa quieres, luego **Copiar horario a…**, y elige la bomba a la que copiarlo.

## Conservar y compartir un horario

Un horario con el que estés satisfecho no tiene que crearse de nuevo:

- **Guardar horario como…** lo guarda con un nombre, y **Horarios guardados…** lo aplica de nuevo más tarde.
- **Compartir este horario** lo convierte en un código corto, y **Pegar un código de horario…** aplica uno que alguien te envió. Esto es una función de Cora Mobile; el código lleva el horario, no acceso a tu cuenta.

## Fuera de la red de la bomba

Cuando tu teléfono no está en la red de la bomba, Cora Mobile funciona a través del Cora Max del acuario, con límites:

- **Igual todo el día** y **Horario** cambian el modo de la bomba a través de ese Cora Max.
- Un periodo que añadas o cambies pasa por él solo si ha llegado a la bomba en la última hora. Si no, el horario lo indica y no se puede cambiar desde donde estás.
- **Copiar horario a…**, **Guardar horario como…**, **Horarios guardados…**, **Compartir este horario** y **Pegar un código de horario…** necesitan que tu teléfono esté en la red de la bomba. Hasta entonces aparecen en gris, y el menú indica por qué.

Una bomba Bluetooth solo se puede alcanzar desde un teléfono cercano: ponte al alcance para cambiar su estado, cambiar su horario o usar cualquiera de esos elementos.

## Aplicar un programa

A una bomba también se le puede dar un programa preparado en un solo paso, en lugar de crear los periodos a mano.

## Comprobar que se aplicó

Después de guardar, la página del dispositivo muestra el programa que la unidad está ejecutando realmente. Si los dos no coinciden, la escritura no llegó; comprueba que el dispositivo es accesible e inténtalo de nuevo.
