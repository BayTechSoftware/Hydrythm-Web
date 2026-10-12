---
title: Cámaras y vigilancia del skimmer
description: Añade a Cora una cámara Wyze, Tapo, Sonoff u otra RTSP, mírala en una casilla o a pantalla completa, y deja que la vigilancia del skimmer te avise antes de que se desborde el vaso.
section: Cora Mobile
reviewed: 2026-10-12
order: 35
group: Equipment
---

:::note Beta
**Beta.** Las cámaras están en Beta y solo están abiertas a los usuarios Beta. Si no eres usuario Beta, no las verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html).
:::

Añade una cámara para ver tu acuario desde Cora, en el teléfono y en Cora Max. Una cámara necesita un Cora Max en el acuario, así que la fila **Cámara** muestra **Requiere Cora Max** hasta que el acuario tiene uno.

## Añadir una cámara

1. Ve a **Dispositivos → Agregar dispositivo → Cámara** y luego a **Añadir una cámara**.
2. Elige el tipo: Wyze, Tapo, Sonoff u **Otra cámara (RTSP)**.
3. Sigue los pasos que muestra Cora para ese tipo. Te dicen qué activar antes en la app de la propia cámara.
4. Rellena el nombre, la dirección de la transmisión, el usuario, la contraseña y el acuario, y toca **Probar conexión**. Cuando la cámara responda, toca **Añadir cámara**.

Tu teléfono tiene que estar en el mismo Wi-Fi que la cámara mientras la añades. La dirección tiene que ser de tu red doméstica, y el usuario y la contraseña se escriben en sus propios campos, no en la dirección.

Se han probado cámaras Wyze, Tapo y Sonoff (Wyze Cam v4, Tapo C120 y Sonoff Cam S3W). Otras cámaras que ofrezcan RTSP también pueden funcionar.

| Cámara | Qué activar primero |
|---|---|
| Wyze | En la app de Wyze, abre la cámara y luego Ajustes, Ajustes avanzados, RTSP. Activa RTSP, elige un usuario y una contraseña y reinicia la cámara. La cámara necesita el firmware 4.52.17 o uno posterior. |
| Tapo | En la app de Tapo, abre Ajustes, Ajustes avanzados, Cuenta de la cámara y crea un usuario y una contraseña. No es tu cuenta de TP-Link. Una cámara Tapo solo puede tener activas a la vez dos de estas tres cosas: Tapo Care, la grabación en tarjeta SD y la transmisión a otras apps. |
| Sonoff | En eWeLink, activa RTSP en la cámara y configura su cuenta. Cora rellena por ti un ajuste predefinido de **Dirección Sonoff**. |
| Otra cámara (RTSP) | Activa RTSP u ONVIF en la app de la cámara, configura un acceso para la cámara e introduce la dirección de la transmisión que indica su manual. Deja el acceso vacío si tu cámara no tiene. |

## Cambiar una cámara

Abre la cámara y usa su menú: **Renombrar**, **Editar direcciones**, **Cambiar contraseña** o **Quitar cámara**. Al quitarla también se borra su contraseña guardada.

## Verla

Una cámara puede ser una casilla de tu panel, de hasta 3×2, y puedes abrirla en **Pantalla completa** y **Girar**.

En casa, con el teléfono en el Wi-Fi de la cámara, Cora reproduce **Vídeo en vivo** directamente desde la cámara. Fuera de casa, o cuando eliges **Instantáneas**, tu Cora Max toma imágenes fijas de la cámara y Cora las muestra casi en directo, actualizadas cada pocos segundos. Si Cora Max no envía imágenes, la casilla lo dice.

## Vigilancia del skimmer

:::note Beta
**Beta.** La vigilancia del skimmer está en Beta y solo está abierta a los usuarios Beta. Además necesita un plan de pago: **La vigilancia del skimmer forma parte de los planes de pago.** Para pedir acceso Beta, contacta con [soporte](/support.html).
:::

La vigilancia del skimmer observa el vaso del skimmer con una cámara y te avisa antes de que se desborde. Está en la página de la cámara, en la tarjeta **Vigilancia del skimmer**.

1. Apunta la cámara al vaso y activa **Vigilar el vaso**.
2. Toca **Marcar el vaso**. Arrastra el recuadro sobre el vaso y ajusta las esquinas: el borde inferior en el fondo del vaso y el superior justo debajo del borde, donde el vaso está lleno.
3. Vacía el vaso y toca **El vaso está vacío ahora**. Cora toma una imagen del vaso vacío para comparar. Tarda unos 10 segundos. Si mueves la cámara o el recuadro, repítelo.
4. Fija **Avisar al** con el nivel de llenado que debe avisarte. La tarjeta lo muestra como porcentaje.

Cora Max comprueba el vaso cada pocos minutos. La tarjeta muestra la última lectura y cuánto hace de ella. **Comprobar ahora** pide una comprobación al momento y tarda unos 10 segundos. **Últimas 24 horas** muestra cómo se fue llenando el vaso a lo largo del día.

Si la imagen es difícil de leer, la tarjeta lo dice, por ejemplo **Luz demasiado fuerte detrás del vaso**.

### Consejos para la cámara

**Consejos para la cámara**, en la tarjeta, te da los mismos consejos que aquí.

- Pon la visión nocturna de la cámara en Activada (siempre infrarrojo), no en Auto, para que cada imagen se vea igual de día y de noche.
- Pon el foco de la cámara en Manual y déjalo apagado. Las burbujas y el agua del sump cuentan como movimiento y lo encienden una y otra vez.
- Evita que luces fuertes den directamente a la cámara desde detrás del vaso.

## Qué pasa con las imágenes

En casa, el vídeo se reproduce directamente desde la cámara y no se graba. Fuera de casa, solo se guarda una imagen fija por cámara, y cada nueva sustituye a la anterior. La vigilancia del skimmer guarda la última imagen del vaso marcado, las lecturas de llenado de las últimas 24 horas (solo números) y una imagen pequeña del vaso vacío. Se borran cuando quitas la cámara, el acuario o tu cuenta. La [política de privacidad](/privacy-policy.html) tiene todo el detalle.
