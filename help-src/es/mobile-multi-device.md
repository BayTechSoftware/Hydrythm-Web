---
title: Más de un dispositivo Cora
description: Elige qué dispositivo responde por voz y cuál consulta cada acuario.
section: Cora Mobile
reviewed: 2026-09-27
order: 29
group: Account
---

Un hogar puede tener más de un Cora Max. Dos ajustes deciden qué hace cada uno, para que no dupliquen el trabajo del otro, y hay una tercera cosa que vale la pena saber: qué se comparte entre ellos y qué no.

## Qué se comparte, y qué no

| Se comparte en todos los dispositivos | Pertenece a una sola pantalla |
|---|---|
| Acuarios, lecturas e historial | Su diseño de panel |
| Dispositivos y sus ajustes | Wi-Fi, brillo, audio |
| Diario, fauna, mantenimiento | Palabra de activación y bloqueo infantil |
| Alertas, umbrales, automatizaciones | Qué acuarios muestra esa pantalla |
| Planes y uso | |

Cambiar un umbral en un dispositivo lo cambia en todas partes. Reorganizar un panel no lo hace; cada pantalla mantiene su propio diseño, y el teléfono y Cora Max nunca comparten uno.

## Cora Assistant: dispositivo que responde

**Ajustes → Cora Assistant → Dispositivo que responde** elige qué **dispositivo Cora** responde cuando le hablas a la sala. Solo uno responde, sin importar cuántos puedan oírte; fíjalo en la unidad más cercana al lugar donde sueles estar.

Esto es una elección distinta de Cora Max principal más abajo: el dispositivo que responde decide qué dispositivo responde a tu voz, y Cora Max principal decide qué dispositivo consulta el equipo de un acuario. Un hogar con dos tabletas puede querer fijar cada uno de forma distinta.

![El selector del que responde por voz](img/mobile-voice-responder.webp "Cada dispositivo muestra qué escucha, y si está en línea.")

Cada dispositivo de la lista muestra la frase de activación que escucha, junto con si está en línea. **No son todas la misma.** Una frase de activación se entrena en el propio dispositivo, así que distintos modelos Cora pueden escuchar frases distintas. Lee la frase en la propia fila del dispositivo en lugar de suponer que el hogar comparte una.

:::note Tu teléfono no está en este selector
El teléfono no escucha una frase de activación. Inicias una conversación en él tocando, lo cual siempre funciona y no se ve afectado por este ajuste. El selector lista solo el hardware Cora con capacidad de voz.
:::

## Cora Max principal

El equipo de tu red lo lee un Cora Max. Cuando más de uno podría leer el mismo controlador, de lo contrario lo consultarían en paralelo.

**Cora Max principal** es una elección por acuario de qué dispositivo lee el controlador de ese acuario. En Cora Mobile, abre el acuario y toca **Cora Max principal**.

| Ajuste | Comportamiento |
|---|---|
| Un dispositivo con nombre | Se convierte en el único dispositivo Cora que consulta el controlador, y se mantiene como principal incluso mientras está sin conexión: otros dispositivos Cora no toman el relevo. Cora Mobile consulta solo mientras está sin conexión. |
| **Cualquiera activo (automático)** | La aplicación y cualquier dispositivo Cora en línea comparten el trabajo (gana la última escritura), así que si uno se queda sin conexión otro continúa. Adecuado para un hogar con un solo dispositivo, y la opción predeterminada más segura cuando no estás seguro de qué dispositivo debería encargarse. |

Mientras un dispositivo que nombraste está sin conexión, una orden que tiene que pasar por él no se ejecuta: Cora te dice que el acuario está configurado para usar ese dispositivo, que está sin conexión, y que no se ejecutó nada, para que puedas intentarlo de nuevo cuando vuelva. Si va a estar sin conexión un tiempo, elige otro dispositivo o **Cualquiera activo (automático)**.

:::note Fija un principal cuando dos dispositivos vigilan un acuario
Nombrar un principal reduce la carga sobre el controlador y elimina lecturas duplicadas de la misma fuente.
:::

:::note Esto es un ajuste de toda la cuenta, por acuario, no por dispositivo
Cora Max principal pertenece al acuario, no al teléfono o la tableta que estás mirando. Cambiarlo desde cualquier dispositivo lo cambia para todo el hogar.
:::

## Qué funciona fuera de casa

Tu teléfono no habla con tu equipo directamente cuando estás fuera del Wi-Fi de tu propio acuario. En su lugar, una orden viaja a Cora Cloud, que la pasa a un Cora Max que está junto al acuario; ese Cora Max es el que realmente llega al equipo.

Esto significa:

- **Las lecturas y el historial** siempre están disponibles, estés donde estés, porque ya están guardados en Cora Cloud.
- **Controlar equipos** (cambiar el estado de una toma, iniciar una alimentación, dosificar un cabezal, pausar una bomba) también funciona fuera de casa, siempre que un Cora Max junto al acuario esté en línea y pueda alcanzar ese equipo. Si ninguno lo está, la orden no se puede entregar.
- **Los propios ajustes nativos de un dispositivo** (a diferencia de sus lecturas) a veces necesitan un teléfono en la *misma* red que el propio dispositivo, no solo un Cora Max junto al acuario. Cuando eso aplica, la página lo indica.

Dos mensajes te dicen que la orden no simplemente tuvo éxito:

- **"No se envió nada"**: la orden nunca salió de tu teléfono, o ningún Cora Max junto al acuario pudo recibirla. No se ejecutó nada. Esto es lo que verás si el Cora Max principal del acuario está sin conexión y ningún otro dispositivo de ese acuario puede intervenir.
- **"Puede que ya se haya ejecutado"**: la orden se envió, pero ningún Cora Max respondió a tiempo para confirmarla. Cora realmente no sabe si se ejecutó. Revisa el propio estado del equipo antes de intentarlo de nuevo, para no enviarla dos veces.

Si cualquiera de los dos mensajes sigue apareciendo, comprueba que un Cora Max junto al acuario esté en línea, o fija **Cora Max principal** en **Cualquiera activo (automático)** para que cualquier dispositivo en línea pueda recibir la orden. Consulta [Cómo controlar tu equipo](/help/mobile-device-control) para conocer todos los resultados que puede tener una orden.

## Dónde se muestra el estado de cada dispositivo

Cora Max informa de su propio estado de consulta y voz en **Ajustes → Cora Max → Firmware → Salud y controles del dispositivo**. Consulta [Dispositivos y estado de los dispositivos](/help/max-devices).
