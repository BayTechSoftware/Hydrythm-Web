---
title: Programar equipos
description: Crea un programa diario para una bomba Jecod en el editor, cópialo desde otras bombas o a ellas, guárdalo y compártelo, y comprueba que la bomba lo ha recibido.
section: Cora Mobile
reviewed: 2026-11-03
order: 14
group: Equipment
---

Usa esta página para darle a una bomba Jecod un **programa diario**: un conjunto de periodos, cada uno con su intensidad, que se repite todos los días. Ábrela desde **Dispositivos** → toca la bomba.

Las luces y bombas de otras marcas tienen sus horarios en sus propias páginas: ReefDose de Red Sea en [Controlar tus equipos](/help/mobile-device-control#red-sea).

![La página de una bomba Jecod en Cora Mobile con Horario elegido](img/mobile-schedules.webp "Horario elegido arriba, la pausa de alimentación y después el gráfico del día.")

## Manual, u Horario {#same-all-day-or-schedule}

Una bomba funciona en uno de dos modos. Elige uno con el selector de su página. El que está en marcha lleva *· en marcha*, y la página se abre en él:

- **Manual**, con una sola intensidad constante
- **Horario**, con un horario diario dividido en periodos

Cora envía tu elección directamente a la bomba cuando tu teléfono está en su red. Si no lo está, se envía a través del Cora Max del acuario. Una bomba Bluetooth tiene que estar a tu alcance. Mientras no lo esté, lo que elijas aquí solo cambia lo que ves en pantalla.

Una pausa de alimentación saca la bomba de su horario durante un rato, y en tu teléfono el horario solo vuelve mientras la página de la bomba sigue abierta. Consulta [Pausa de alimentación](/help/mobile-device-control#jecod-feeding).

## El editor de horarios

Todas las pantallas de horario tienen las mismas tres partes.

El **gráfico del día** muestra el día entero, de 0 a 24 horas. Cada periodo es un bloque y su altura es la intensidad. Es la forma más rápida de comprobar que el programa hace lo que crees.

La **lista de periodos**, debajo del gráfico, muestra cada periodo con su horario, su modo y su intensidad, por ejemplo *Aleatorio, 00:00–03:00, Frec 50%, 40%*. Aquí añades, editas y quitas periodos.

Todo cambio en un horario pasa por el editor. **Editar** lo abre con el día de la bomba, y también tocar un periodo o **Agregar al horario** en la página de la bomba: el editor se abre con ese periodo, o uno nuevo, listo para cambiar. En el editor, cambia un periodo y toca **Guardar**, o quítalo con **Eliminar tramo**. **Deshacer** vuelve un paso atrás. El menú ⋮ tiene **Guardar horario como…**, **Horarios guardados…** y **Copiar de…**.

No se envía nada a la bomba hasta que tocas **Guardar en la bomba**. Cora escribe entonces todo el día de una vez. Si no puede, el editor dice por qué y conserva tus cambios. Si cierras el editor antes de guardar, Cora pregunta primero *¿Descartar estos cambios?*


:::warning Guardar en la bomba escribe el horario en el propio equipo
Al tocar **Guardar en la bomba**, el programa se envía al equipo, que lo sigue con su propio reloj. Sigue funcionando aunque Cora no pueda conectarse con él.
:::

## Copiar un programa a otras bombas {#copying-a-program-between-pumps}

Si tienes varias bombas que deben funcionar igual, crea un programa y cópialo. Puedes copiar en los dos sentidos, y no se envía nada hasta que tocas **Guardar en la bomba**.

- **Copiar de…** (en el menú ⋮ del horario y en el del editor) toma el horario de otra bomba de circulación de cualquiera de tus acuarios. Cada periodo recibe el modo más parecido que tenga esta bomba, las velocidades se ajustan a lo que puede dar, y **Qué cambia en esta bomba** muestra cada cambio. **Cargar en el editor** pone la copia en el editor de esta bomba, donde puedes ajustarla y luego tocar **Guardar en la bomba**. Una bomba cuyo horario Cora aún no ha leído aparece en gris, con el motivo.
- **Copiar horario a…** pasa el día de esta bomba a otras bombas de cualquiera de tus acuarios, cada una listada como *Acuario · Bomba*. Marca las bombas y toca **Revisar**. Todavía no se envía nada. **Revisar copias** muestra cada bomba con su estado, **Sin guardar**, **Guardado en la bomba** o **Error** con el motivo, y cuántos cambios recibe. **Abrir editor** abre el editor propio de esa bomba con el día copiado, con su propio **Guardar en la bomba**, que lo envía solo a esa bomba. Si un guardado falla, el borrador se conserva para que puedas intentarlo de nuevo. Si sales con bombas sin guardar, Cora pregunta primero *¿Descartar las copias sin guardar?*

## Guardar y compartir un horario

No tienes que volver a crear un horario que ya te funciona:

- **Guardar horario como…** lo guarda con un nombre, y con **Horarios guardados…** lo recuperas más tarde: **Cargar en el editor** lo abre en el editor, y **Guardar en la bomba** lo envía.
- **Compartir este horario** lo convierte en un código corto, y **Pegar un código de horario…** carga en el editor uno que te hayan enviado, y no se envía nada hasta que tocas **Guardar en la bomba**. Es una función de Cora Mobile. El código contiene el horario, no da acceso a tu cuenta.

## Lejos de la red de la bomba

Cuando tu teléfono no está en la red de la bomba, Cora Mobile trabaja a través del Cora Max del acuario, con algunos límites:

- **Manual** y **Horario** cambian el modo de la bomba a través de ese Cora Max.
- Un horario que guardes en la bomba solo pasa por el Cora Max si este ha conectado con la bomba en la última hora. Si no, el horario te lo indica y no puedes cambiarlo desde donde estás.
- **Copiar horario a…**, **Guardar horario como…**, **Horarios guardados…**, **Compartir este horario** y **Pegar un código de horario…** necesitan que tu teléfono esté en la red de la bomba. Mientras tanto aparecen en gris y el menú te explica por qué.

Sin un Cora Max en el acuario, solo puedes cambiar una bomba mientras tu teléfono está en su red. Más información en [Conectar tus equipos](/help/mobile-connections#local-only).

A una bomba Bluetooth solo se llega desde un teléfono que esté cerca. Acércate para cambiarle el modo, cambiar su horario o usar cualquiera de esas opciones.

## Aplicar un programa

Puedes darle a una bomba un horario guardado en un solo paso, sin volver a crear los periodos. Abre la bomba, toca **Más** arriba y elige **Horarios guardados…**. La lista incluye todos los horarios guardados en este acuario, también los que creaste en otra bomba. Elige uno y toca **Cargar en el editor**. Revísalo en el editor y luego toca **Guardar en la bomba**. Sustituye el día completo de la bomba.

## Comprobar que se ha aplicado

Después de guardar, la página del dispositivo muestra el programa que el equipo está siguiendo de verdad. Si no coincide con el tuyo, el cambio no llegó. Comprueba que el dispositivo está conectado y vuelve a intentarlo.
