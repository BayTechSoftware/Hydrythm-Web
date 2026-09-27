---
title: Actualizaciones y recuperación
description: Cómo se actualiza Cora Max solo y qué pasa si una actualización sale mal.
section: Cora Max
reviewed: 2026-09-09
order: 14
group: Settings
---

## Actualizaciones automáticas

Cora Max se actualiza solo. Las versiones nuevas se descargan en segundo plano y se instalan sin que hagas nada. Después te cuenta qué ha cambiado.

No tienes que hacer nada para estar al día.

## Ver la versión

![Ajustes del dispositivo](img/max-updates.webp "Actualización de firmware, en la sección Red y actualizaciones de los Ajustes de Cora Max.")

En **Ajustes → Ajustes de Cora Max → Actualización de firmware** (en la sección **Red y actualizaciones**) puedes buscar e instalar actualizaciones y elegir el canal y el horario. Más abajo en la misma pantalla, la sección **Estado** muestra, para cada acuario, el estado del sondeo, el último sondeo y la última escritura en la nube.

## Cuando hay una actualización

Aparece un aviso con las novedades y dos opciones:

- **Actualizar ahora**: la instala al momento y reinicia
- **Posponer 3 horas**: te lo vuelve a preguntar más tarde

Si no haces nada, la actualización se instala sola por la noche, más o menos entre las 3 y las 5 de la madrugada, para que la pantalla no se reinicie mientras la miras.

:::note Una actualización no borra tus lecturas
Los datos están en tu cuenta, no en la pantalla. Después de reiniciarse, Cora Max vuelve con los mismos acuarios, paneles e historial.
:::

## Recuperación

Recuperación es un modo de mantenimiento para cuando Cora Max no arranca con normalidad o tienes que arreglar su configuración sin un portátil.

Para entrar, mantén **cinco dedos** en la esquina superior derecha de la pantalla unos **diez segundos** y luego escribe el **PIN de recuperación**.

Ese PIN de seis cifras apareció al emparejar el Cora Max y también está en los ajustes de ese dispositivo en Cora Mobile. En el propio Cora Max no se muestra. Así, ni una visita ni un niño apoyado en la pantalla pueden entrar en recuperación.

Desde recuperación puedes:

- Arreglar la conexión **Wi-Fi**
- **Volver a emparejar** el Cora Max con tu cuenta
- Forzar una **actualización de firmware**
- **Restablecer valores de fábrica**

Si Cora Max falla al arrancar varias veces seguidas, también puede volver solo a la versión anterior.

:::warning En recuperación, la pantalla no controla nada
Tu controlador sigue con su propia programación. Pero una [automatización](/help/mobile-automation) cuya acción tiene que hacer **este Cora Max** no se ejecuta mientras está en recuperación. La regla se activa, pero el paso no llega al equipo.
:::

## Si no vuelve a arrancar

Escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con la versión que aparece en pantalla y lo que dice el mensaje. No lo vuelvas a emparejar antes, porque el estado del emparejamiento suele ayudar a averiguar qué ha pasado.
