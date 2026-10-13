---
title: Actualizaciones y recuperación
description: Cómo se actualiza solo Cora Max, la ventana de instalación y el canal de actualización, cómo ver la versión, el PIN de recuperación y qué hacer si Cora Max no arranca o muestra un código de soporte.
section: Cora Max
reviewed: 2026-10-13
order: 15
group: Settings and account
---

Cora Max se mantiene al día solo. Esta página explica cuándo se instalan las actualizaciones, cómo ver tu versión y cómo volver a poner en marcha Cora Max si no arranca con normalidad.

## Actualizaciones automáticas

Las versiones nuevas se descargan en segundo plano en cuanto salen. Se instalan dentro de la **Ventana de instalación**, de 3 a 5 de la madrugada si no la cambias, para que la pantalla no se reinicie mientras la estás mirando. Cuando una versión trae notas de la versión, Cora Max las muestra.

No tienes que hacer nada para estar al día.

## Ver la versión y los ajustes de actualización {#checking-the-version-and-update-settings}

![Red y actualizaciones en Cora Max](img/max-updates.webp "Actualización de firmware, en la sección RED Y ACTUALIZACIONES de Ajustes de Cora Max.")

Tu versión está en la tarjeta de arriba de **Ajustes → Ajustes de Cora Max** (*Cora Max · firmware 0.28.170*), y en **AYUDA Y ACERCA DE → Acerca de**.

**Ajustes → Ajustes de Cora Max → Actualización de firmware** (en **RED Y ACTUALIZACIONES**) muestra la versión que tienes y si hay una actualización esperando. Toca **Buscar actualizaciones** para mirar ahora, o **Descargar e instalar** cuando haya una.

En **Ajustes de actualización**, en la misma pantalla:

- **Ventana de instalación** fija las horas en que se pueden instalar las actualizaciones, con una hora de **Inicio** y de **Fin**, en la hora local de esta pantalla. La zona horaria se fija en Cora Mobile, en **Dispositivos →** tu Cora Max **→ Zona horaria**.
- **Canal de actualización** es **Estable** o **Beta**. Déjalo en **Estable** salvo que el soporte te pida cambiarlo. Un Cora Max en **Beta** no recibe las versiones estables.

Para ver si esta pantalla está leyendo tus dispositivos y guardando en Cora Cloud, vuelve a **Ajustes de Cora Max** y baja hasta **ESTADO**. Muestra el **Estado de sondeo**, el **Último sondeo**, la **Última escritura en la nube** y el **Guardado en la nube** de cada acuario.

## Cuando hay una actualización disponible

Un aviso te cuenta las novedades y te da dos opciones.

- **Actualizar ahora** la instala al momento y reinicia. Tarda más o menos un minuto. Mantén Cora Max enchufado.
- **Posponer 24 horas** oculta el aviso y te vuelve a preguntar un día después.

Mientras una actualización está esperando, aparece un pequeño punto en el icono de **Ajustes** de la barra superior y en la fila **Actualización de firmware**. El punto se mantiene aunque la pospongas, así que sigues viendo que hay una actualización. Desaparece mientras se instala la actualización.

Si no haces nada, la actualización se instala sola en la **Ventana de instalación**.

También puedes empezarla desde tu teléfono: en Cora Mobile, abre **Dispositivos →** tu Cora Max y toca **Actualizar a v…**.

:::note No pierdes lecturas durante una actualización
Tus datos están en tu cuenta. Cuando Cora Max se reinicia, vuelve con los mismos acuarios, paneles e historial.
:::

## Recuperación {#recovery}

La recuperación es un modo de mantenimiento para cuando Cora Max no arranca con normalidad, o cuando necesitas arreglar su configuración sin un ordenador.

1. Mantén **cinco dedos** en la esquina superior derecha de la pantalla durante **diez segundos**.
2. Se abre el cuadro **PIN de recuperación**. Escribe el PIN de 6 dígitos y toca **Entrar**.

Viste el PIN cuando emparejaste Cora Max. También lo encontrarás en Cora Mobile, en **Dispositivos →** tu Cora Max **→ PIN de recuperación**. El propio Cora Max nunca lo muestra, así que una visita o un niño que se apoye en la pantalla no puede entrar en la recuperación.

Si escribes mal el PIN tres veces, la recuperación se bloquea 30 segundos, y más tiempo con cada intento fallido posterior. **Demasiados intentos** te dice cuánto esperar. Si Cora Max nunca ha estado en línea desde que lo emparejaste, todavía no tiene PIN y muestra **La recuperación no está disponible**. Conéctalo antes al Wi-Fi.

Desde **Recuperación** puedes:

- **Repetir configuración de Wi-Fi**: elegir una red Wi-Fi y una contraseña nuevas
- **Volver a emparejar este dispositivo**: borrar el emparejamiento y configurarlo de nuevo con Cora Mobile
- **Forzar comprobación de OTA**: buscar actualizaciones ahora
- **Restablecer valores de fábrica**: quitar el emparejamiento y todos los ajustes de la pantalla

Los datos del acuario ya guardados en Cora Cloud se conservan en todos los casos.

Si Cora Max no consigue arrancar varias veces seguidas, también puede volver por sí solo a la versión anterior.

:::note El mismo gesto desbloquea el bloqueo infantil
Si el [Bloqueo infantil](/help/max-settings#child-lock) está activado, mantener cinco dedos en la esquina también desbloquea la pantalla. Toca **Cancelar** en el cuadro **PIN de recuperación** si solo querías desbloquearla.
:::

:::warning Una pantalla en recuperación no controla nada
Tu controlador sigue con su propia programación. Pero un paso de una [automatización](/help/mobile-automation) que tiene que ejecutar **este Cora Max** no puede ejecutarse mientras está en recuperación. La regla se activa, pero el paso nunca llega al equipo.
:::

## Si Cora Max muestra "Cora Max tuvo un problema"

Esta pantalla significa que algo falló mientras Cora Max arrancaba o funcionaba. Muestra un **Código de soporte** (empieza por *CXB-*).

1. Apunta el código de soporte.
2. Espera. Cora Max se reinicia solo en unos 10 minutos. Para reiniciarlo ahora, mantén cinco dedos en la esquina superior derecha durante 10 segundos.
3. Si sigue pasando, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el código de soporte.

## Si una unidad no se reinicia

Escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con la versión que aparece en pantalla y el mensaje que muestra. No la vuelvas a emparejar antes. El estado del emparejamiento suele ayudar a saber qué pasó.
