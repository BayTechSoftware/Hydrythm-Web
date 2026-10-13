---
title: Cámaras y vigilancia del skimmer
description: Añade a Cora una cámara Wyze, Tapo, Sonoff u otra RTSP, mira tu acuario en una casilla o a pantalla completa y deja que la vigilancia del skimmer te avise antes de que el vaso se desborde.
section: Cora Mobile
reviewed: 2026-10-13
order: 17
group: Equipment
---

:::note Beta
**Beta.** Las cámaras están en Beta y solo están abiertas a los usuarios Beta. Si no eres usuario Beta, no las verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html). Más información en [Funciones Beta](/help/mobile-beta).
:::

Añade una cámara para ver tu acuario desde Cora, en el teléfono y en Cora Max, y para que la vigilancia del skimmer controle el vaso del skimmer. Empieza en **Dispositivos → Agregar dispositivo → Cámara**. Una cámara necesita un Cora Max en el acuario, así que la fila **Cámara** muestra **Requiere Cora Max** hasta que el acuario tiene uno.

## Añadir una cámara {#adding-a-camera}

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

## Cambiar una cámara {#changing-a-camera}

Abre la cámara y usa su menú: **Renombrar**, **Editar direcciones**, **Cambiar contraseña** o **Quitar cámara**. Al quitarla también se borra su contraseña guardada.

## Verla {#watching-it}

![La página de una cámara](img/mobile-camera.webp "La página de la cámara, con la imagen arriba y la tarjeta de vigilancia del skimmer debajo.")

Una cámara puede ser una casilla de tu panel, de hasta 3×2. Consulta [Editar tu panel](/help/mobile-dashboard-editing). Ábrela para tener **Pantalla completa** y **Girar**.

En casa, con el teléfono en el Wi-Fi de la cámara, Cora reproduce **Vídeo en vivo** directamente desde la cámara. Fuera de casa, o cuando eliges **Instantáneas**, tu Cora Max toma imágenes fijas de la cámara y Cora las muestra casi en directo, actualizadas cada pocos segundos. Si Cora Max no envía imágenes, la casilla lo dice.

## Vigilancia del skimmer {#skimmer-watch}

:::note Beta
**Beta.** La vigilancia del skimmer está en Beta y solo está abierta a los usuarios Beta. Además necesita un plan de pago. Sin él, la tarjeta dice **La vigilancia del skimmer forma parte de los planes de pago.** y ofrece **Ver planes**. Para pedir acceso Beta, contacta con [soporte](/support.html).
:::

La vigilancia del skimmer observa el vaso colector del skimmer con una cámara y te avisa antes de que se desborde. Está en la página de la cámara, en la tarjeta **Vigilancia del skimmer**.

![Marcar el vaso](img/mobile-camera-mark-cup.webp "Arrastra el recuadro sobre el vaso: el borde inferior en el fondo del vaso y el superior justo debajo del borde.")

1. Apunta la cámara al vaso y activa **Vigilar el vaso**.
2. Toca **Marcar el vaso**. Arrastra el recuadro sobre el vaso y ajusta las esquinas: el borde inferior en el fondo del vaso y el superior justo debajo del borde, donde el vaso está lleno. Más adelante el botón dice **Mover el recuadro del vaso**.
3. Vacía el vaso y toca **El vaso está vacío ahora**. Cora toma una imagen del vaso vacío para comparar. Tarda unos 10 segundos. Si mueves la cámara o el recuadro, repítelo.
4. Arrastra el control **Avisar al** hasta el nivel de llenado que debe avisarte. Deja algo de margen, porque Cora comprueba cada 15 minutos.

![La tarjeta de vigilancia del skimmer en la página de una cámara](img/mobile-skimmer-watch.webp "El vaso está vacío ahora, la última lectura, las últimas 24 horas, Comprobar ahora y los consejos para la cámara.")

Cora Max comprueba el vaso cada 15 minutos. La tarjeta muestra la última lectura y cuánto hace de ella, y la casilla de la cámara en tu panel también muestra el nivel del vaso. **Comprobar ahora** comprueba el vaso en ese momento y tarda unos 10 segundos. **Últimas 24 horas** muestra cómo se fue llenando el vaso a lo largo del día.

Cuando el vaso llega a tu nivel de **Avisar al**, recibes una notificación. Se envía dentro de **Fallas de equipos**, así que mantén esa categoría activada en [Notificaciones](/help/mobile-notifications). Cuando hayas vaciado el vaso, la alerta vuelve a estar lista para saltar.

### Si la lectura parece incorrecta {#skimmer-watch-problems}

| La tarjeta dice | Qué hacer |
|---|---|
| **Luz demasiado fuerte detrás del vaso** | Apaga o mueve la luz que hay detrás del vaso. Mira los consejos para la cámara más abajo |
| **No estoy seguro (poca confianza)** | La imagen era difícil de leer. Revisa los consejos para la cámara y toca **Comprobar ahora** |
| **Marca primero el vaso** | Toca **Marcar el vaso** y dibuja el recuadro |
| **Sin calibrar: vacía el vaso y toca El vaso está vacío ahora** | Vacía el vaso y toca **El vaso está vacío ahora** |
| **Recuadro movido: calibra de nuevo** | Moviste el recuadro. Vacía el vaso y vuelve a tocar **El vaso está vacío ahora** |
| **Cora Max no pudo obtener imagen de la cámara.** | Comprueba que la cámara está encendida y que el Cora Max del acuario está en línea |
| **La última comprobación falló.** | Toca **Comprobar ahora**. Si sigue fallando, consulta [Solución de problemas](/help/troubleshooting) |
| **Aún no hay lectura. Cora Max comprueba cada 15 minutos.** | Espera a la primera comprobación, o toca **Comprobar ahora** |

### Consejos para la cámara {#camera-tips}

**Consejos para la cámara**, en la tarjeta, te da los mismos consejos que aquí.

- Pon la visión nocturna de la cámara en Activada (siempre infrarrojo), no en Auto, para que cada imagen se vea igual de día y de noche.
- Pon el foco de la cámara en Manual y déjalo apagado. Las burbujas y el agua del sump cuentan como movimiento y lo encienden una y otra vez.
- Evita que luces fuertes den directamente a la cámara desde detrás del vaso.

### En Cora Max {#skimmer-watch-on-cora-max}

![Casillas de cámara en Cora Max, una con el nivel del vaso del skimmer](img/max-skimmer-watch.webp "En Cora Max, la casilla de la cámara muestra el nivel del vaso y su antigüedad.")

En Cora Max, la casilla de la cámara y la cámara a pantalla completa muestran **Vaso** con el nivel de llenado y la antigüedad de la lectura. La etiqueta se pone ámbar cuando el vaso está a 10 puntos de tu nivel de alerta y roja cuando lo alcanza. En la cámara a pantalla completa, el botón **Aviso al** abre **Aviso del vaso del skimmer**, donde también puedes cambiar el nivel. Mientras se hace una comprobación, la imagen en directo puede pausarse unos segundos. Más información en [Controlar equipos desde Cora Max](/help/max-device-control).

## Qué pasa con las imágenes {#pictures}

En casa, el vídeo se reproduce directamente desde la cámara y no se graba. Fuera de casa, solo se guarda una imagen fija por cámara, y cada nueva sustituye a la anterior. La vigilancia del skimmer guarda la última imagen del vaso marcado, las lecturas de llenado de las últimas 24 horas (solo números) y una imagen pequeña del vaso vacío. Se borran cuando quitas la cámara o eliminas tu cuenta. La [política de privacidad](/privacy-policy.html) tiene todo el detalle.
