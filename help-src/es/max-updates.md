---
title: Actualizaciones y recuperación
description: Cómo se actualiza Cora Max por sí solo, y qué pasa si una actualización sale mal.
section: Cora Max
reviewed: 2026-09-09
order: 14
group: Settings
---

## Actualizaciones automáticas

Cora Max se mantiene al día por sí solo. Las versiones nuevas se descargan en segundo plano y se instalan solas; se te informa de qué cambió.

No se necesita nada de tu parte para mantenerte al día.

## Comprobar la versión

![Ajustes del dispositivo](img/max-updates.webp "Actualización de firmware y salud del dispositivo, en la parte superior de los ajustes del dispositivo.")

**Ajustes → Cora Max → Firmware → Actualización de firmware** cubre la comprobación, la instalación, el canal de actualización y su calendario. **Salud y controles del dispositivo** está justo al lado, en el mismo grupo **Firmware**, y es donde viven los diagnósticos propios de la unidad: consulta principal, enlaces de dispositivos y el que responde por voz incluidos.

## Cuando hay una actualización disponible

Aparece un aviso que describe qué es nuevo, con dos opciones:

- **Actualizar ahora**: instala de inmediato y reinicia
- **Posponer 3 horas**: pregunta de nuevo más tarde

Si no haces nada, una actualización se instala sola durante la noche, aproximadamente entre las 3 y las 5 de la madrugada, para que la pantalla no se reinicie mientras la estás mirando.

:::note Las lecturas no se pierden durante una actualización
Los datos viven en tu cuenta, no en la pantalla. Una unidad que se reinicia vuelve con los mismos acuarios, paneles e historial.
:::

## Recuperación

Recuperación es un modo de mantenimiento para cuando una unidad no arranca con normalidad, o cuando necesitas reparar su configuración sin un ordenador portátil.

**Para entrar:** mantén **cinco dedos** en la parte superior derecha de la pantalla durante unos **diez segundos**, y luego introduce el **PIN de recuperación** de la unidad.

Ese PIN de seis cifras se mostró cuando se emparejó la unidad, y también está en los ajustes de ese dispositivo en Cora Mobile. No se muestra en el propio Cora Max, y ese es justamente el objetivo: la recuperación no debe estar al alcance de un invitado, ni de un niño que se apoye en la pantalla.

Desde recuperación puedes:

- Reparar la conexión de **Wi-Fi**
- **Volver a emparejar** la unidad con tu cuenta
- Forzar una **actualización de firmware**
- **Restablecer valores de fábrica** de la unidad

Una unidad que falla al arrancar varias veces seguidas también puede volver por sí sola a la versión anterior.

:::warning Una pantalla en recuperación no está controlando nada
Tu controlador sigue ejecutando su propia programación. Pero una [automatización](/help/mobile-automation) cuya acción tiene que llevarla a cabo **este Cora Max** no puede ejecutarse mientras esté en recuperación; la regla se activa y el paso no llega al hardware.
:::

## Si una unidad no vuelve a arrancar

Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con la versión que aparece en pantalla y lo que dice. No vuelvas a emparejar la unidad primero; el estado del emparejamiento suele ser útil para averiguar qué pasó.
