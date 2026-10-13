---
title: Alertas en Cora Max
description: Qué hacer cuando aparece una alerta en Cora Max, cómo posponerla o descartarla, cambiar los umbrales de alerta en la pantalla de pared y configurar el sonido de alerta.
section: Cora Max
reviewed: 2026-10-13
order: 8
group: Alerts and automation
twin: mobile-alerts
---

Esta página explica qué hace Cora Max cuando algo necesita tu atención, y qué puedes cambiar en la pantalla de pared. Cómo funcionan los rangos, las reglas y las notificaciones del teléfono se explica en [Alertas y umbrales](/help/mobile-alerts).

## Cuando aparece una alerta

Cuando una lectura sale de rango, un dispositivo informa de un fallo, se omite una dosis o se acaba un suministro, Cora Max muestra la alerta en el centro de la pantalla. Debajo hay tres botones.

1. **Responder por voz** empieza una conversación con Cora sobre esta alerta, para que no tengas que tocar nada más. Más información en [Hablar con Cora](/help/max-voice).
2. **Posponer** silencia la alerta en este Cora Max durante un tiempo. El botón muestra cuánto, por ejemplo **Posponer 1 h**. Es el tiempo de espera fijado para esta alerta en los ajustes de alertas de Cora Mobile, y puede llegar a 1 semana (útil para algo como un nivel bajo de reactivo que no va a cambiar en días).
3. **Descartar** cierra la alerta ahora. Se queda en silencio en esta pantalla hasta que el problema desaparece. Si vuelve más tarde, recibirás una alerta nueva.

Cuando la alerta trata de un dosificador, como un cabezal DŌS o ReefDose con poco líquido o una dosis omitida, la tarjeta también tiene un botón **Abrir DŌS** o **Abrir ReefDose** (**Abrir Versa** para una EcoTech Versa). Te lleva a la página de ese dosificador, donde se configuran sus alertas.

Si Posponer o Descartar muestran un error, inténtalo una vez más. Si sigue fallando, consulta [Una alerta no desaparece](/help/troubleshooting#an-alert-is-not-clearing).

:::note Posponer solo afecta a este Cora Max
Mientras una alerta está pospuesta o descartada, este Cora Max deja de mostrarla, de hacerla sonar y de decirla en voz alta, y desaparece de la barra superior. Tu teléfono sigue recibiendo sus notificaciones, otras pantallas Cora Max siguen mostrando la alerta, sigue en **Historial de notificaciones** y tus ajustes de alertas no cambian.
:::

## Alertas en la barra superior

Cada alerta activa también aparece como una pequeña etiqueta en la barra superior, lo bastante grande para verla desde el otro lado de la habitación. Si hay más de las que caben, verás **+2** (o las que sean).

- Toca una etiqueta para volver a traer esa alerta al centro de la pantalla.
- Toca **+2** para abrir **Alarmas activas**, la lista de todo lo que está activo. Toca una de la lista para abrirla.

## La bandeja de notificaciones

**Ajustes → Ajustes de Cora Max → Historial de notificaciones** es la bandeja de toda tu cuenta. Guarda cada resumen, alarma y aviso de la cuenta de tu sistema, incluidos los que no generó esta pantalla y todo lo que se le pasó a tu teléfono. Cuando una lectura sale de rango y vuelve, ves las dos cosas.

## Editar umbrales {#editing-thresholds}

![Los ajustes de un acuario en Cora Max, con Umbrales de alerta, Unidades y Cora Max principal](img/max-tank-settings.webp "Umbrales de alerta y Unidades primero, y después el Cora Max principal de este acuario.")

Toca el nombre del acuario en la barra superior y elige **Umbrales de alerta**, o ve a **Ajustes → [tu acuario] → Umbrales de alerta**. Los dos abren los mismos rangos que ves en tu teléfono, y un cambio que hagas aquí se aplica en todas partes.

También puedes cambiar un umbral manteniendo pulsado su widget en el panel, o por voz: *"Hey Cora, pon la alerta de pH entre 7,9 y 8,4."* Cora te dice el cambio y espera a que des el visto bueno.

Cada parámetro de la lista tiene su propio interruptor. Una alerta que has desactivado dice **Alerta desactivada**. Cora conserva su rango, pero no valora esa lectura mientras está desactivada. El widget se queda en gris neutro y nunca genera una alerta. Si un parámetro todavía no tiene alerta, dice **Sin alerta configurada**, y **Añadir alerta** crea una con el rango que se muestra.

![La lista Umbrales de alerta en Cora Max](img/max-alerts.webp "Cada lectura tiene su propio interruptor. Una lectura sin alerta muestra Sin alerta configurada y un botón Añadir alerta.")

La hoja del umbral tiene el mismo interruptor arriba, junto a **Alerta activada** o **Alerta desactivada**. Si guardas un rango nuevo en una alerta desactivada, Cora pregunta **¿Activar esta alerta?** Toca **Activar** para activarla con los valores nuevos, o **Dejar desactivada** para guardarlos y dejarla desactivada.

## Alertas de dispositivos y suministros {#doser-alerts}

Los equipos con algo que se acaba tienen un botón **Configuración de alertas** en su página de Cora Max. Son el Trident (reactivos y residuos), los cabezales DŌS, las Red Sea ReefDose, ReefATO+ y ReefMat, y las EcoTech Radion, VorTech y Versa. Elige el nivel del que quieres enterarte, y recibes una notificación cuando se pasa. En un cabezal DŌS, **Alertas de dosis omitida** también te avisa cuando el cabezal se salta sus dosis programadas.

Lo que significa cada alerta de dosificador está en [Alertas de dosificadores](/help/mobile-device-control#doser-alerts).

:::note Beta
**Beta.** EcoTech está en Beta y solo está abierto a los usuarios Beta. Si no eres usuario Beta, no lo verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html).
:::

## Sonido de alerta, alertas habladas y encender la pantalla

Estos ajustes son solo de esta pantalla. Están en **Ajustes → Ajustes de Cora Max**.

- **Sonido de alerta** (en **SONIDO Y VOZ**) reproduce un tono cuando llega una alerta nueva. Su control deslizante fija el volumen.
- **Alertas habladas** (en **SONIDO Y VOZ**) hace que Cora diga la alerta en voz alta.
- **Encender pantalla con alarma** (en **PANTALLA**) ilumina una pantalla atenuada cuando llega una alerta. Las alertas críticas siempre la encienden.

Para que un Cora Max deje de mostrar alertas en su pantalla, abre Cora Mobile, ve a **Dispositivos →** tu Cora Max y desactiva **Alertas**. El historial de notificaciones y las notificaciones de tu teléfono no cambian.

:::note Una sola alerta para toda la cuenta
Cada dispositivo no genera su propia copia de una alerta. Cora Max, tu teléfono y cualquier otra pantalla muestran la misma, y desaparece en todos cuando la lectura vuelve al rango.
:::
