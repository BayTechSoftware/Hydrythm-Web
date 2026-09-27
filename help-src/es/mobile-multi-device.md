---
title: Más de un dispositivo Cora
description: Elige qué dispositivo responde a tu voz y cuál consulta cada acuario.
section: Cora Mobile
reviewed: 2026-09-27
order: 29
group: Account
---

Un hogar puede tener más de un Cora Max. Con dos ajustes decides qué hace cada uno, para que no repitan el mismo trabajo. También conviene saber qué comparten y qué no.

## Qué se comparte y qué no

| Se comparte en todos los dispositivos | Es propio de cada pantalla |
|---|---|
| Acuarios, lecturas e historial | El diseño de su panel |
| Dispositivos y sus ajustes | Wi-Fi, brillo, audio |
| Diario, fauna, mantenimiento | Palabra de activación y bloqueo infantil |
| Alertas, umbrales, automatizaciones | Qué acuarios muestra esa pantalla |
| Planes y uso | |

Si cambias un umbral en un dispositivo, cambia en todos. Si reorganizas un panel, no. Cada pantalla tiene su propio diseño, y el teléfono y Cora Max nunca comparten el mismo.

## Cora Assistant: dispositivo que responde

En **Ajustes → Cora Assistant → Dispositivo que responde** eliges qué **dispositivo Cora** te contesta cuando hablas en voz alta en la habitación. Aunque te oigan varios, solo responde uno. Elige el que tengas más cerca del sitio donde sueles estar.

Este ajuste es distinto de Cora Max principal, que se explica más abajo. El dispositivo que responde es el que contesta a tu voz. Cora Max principal es el que consulta el equipo de un acuario. En un hogar con dos Cora Max puede interesarte configurarlos de forma diferente.

![El selector del dispositivo que responde](img/mobile-voice-responder.webp "Cada dispositivo muestra qué frase escucha y si está en línea.")

Cada dispositivo de la lista muestra la frase de activación que escucha y si está en línea. **No todos usan la misma frase.** La frase de activación va entrenada en el propio dispositivo, así que cada modelo Cora puede escuchar una distinta. Mira la frase en la fila de cada dispositivo y no des por hecho que todo el hogar usa la misma.

:::note Tu teléfono no aparece en esta lista
El teléfono no escucha ninguna frase de activación. En él empiezas una conversación tocando la pantalla, y eso funciona siempre, sin depender de este ajuste. La lista solo muestra equipos Cora con voz.
:::

## Cora Max principal

El equipo de tu red lo lee un Cora Max. Si varios pueden leer el mismo controlador, sin este ajuste lo consultarían todos a la vez.

**Cora Max principal** se elige para cada acuario e indica qué dispositivo lee su controlador. En Cora Mobile, abre el acuario y toca **Cora Max principal**.

| Ajuste | Qué pasa |
|---|---|
| Un dispositivo concreto | Pasa a ser el único dispositivo Cora que consulta el controlador. Sigue siendo el principal aunque esté desconectado, y los demás dispositivos Cora no lo sustituyen. Cora Mobile solo consulta el controlador mientras ese dispositivo está desconectado. |
| **Cualquiera activo (automático)** | Cora Mobile y todos los dispositivos Cora en línea se reparten el trabajo (vale la última escritura). Si uno se desconecta, otro sigue. Es lo adecuado en un hogar con un solo dispositivo, y la opción más segura si no sabes cuál debería encargarse. |

Si el dispositivo que elegiste está desconectado, las órdenes que tienen que pasar por él no se ejecutan. Cora te avisa de que el acuario usa ese dispositivo, de que está desconectado y de que no se ha ejecutado nada. Así puedes volver a intentarlo cuando se conecte. Si va a estar desconectado un tiempo, elige otro dispositivo o **Cualquiera activo (automático)**.

:::note Elige un principal si dos dispositivos vigilan el mismo acuario
Con un principal, el controlador recibe menos consultas y desaparecen las lecturas repetidas de la misma fuente.
:::

:::note Este ajuste es de cada acuario, para toda la cuenta
Cora Max principal pertenece al acuario, no al teléfono ni al Cora Max que tienes delante. Si lo cambias desde cualquier dispositivo, cambia para todo el hogar.
:::

## Qué funciona fuera de casa

Cuando no estás conectado al Wi-Fi de tu acuario, el teléfono no habla directamente con tu equipo. La orden va a Cora Cloud, que se la pasa a un Cora Max que está junto al acuario. Ese Cora Max es el que llega al equipo.

Esto quiere decir que:

- **Las lecturas y el historial** están siempre disponibles, estés donde estés, porque ya están guardados en Cora Cloud.
- **Controlar equipos** (encender o apagar una toma, empezar una alimentación, dosificar con un cabezal, pausar una bomba) también funciona fuera de casa, si hay un Cora Max en línea junto al acuario que llegue a ese equipo. Si no lo hay, la orden no puede llegar.
- **Los ajustes propios de un dispositivo** (no sus lecturas) a veces necesitan un teléfono en la *misma* red que el dispositivo. No basta con un Cora Max junto al acuario. Cuando pasa esto, la página lo indica.

Hay dos mensajes que te avisan de que la orden no ha salido del todo bien:

- **"No se envió nada"**: la orden no salió de tu teléfono o ningún Cora Max junto al acuario pudo recibirla. No se ejecutó nada. Es lo que verás si el Cora Max principal del acuario está desconectado y ningún otro dispositivo de ese acuario puede sustituirlo.
- **"Puede que ya se haya ejecutado"**: la orden se envió, pero ningún Cora Max respondió a tiempo para confirmarla. Cora no sabe si se ejecutó. Revisa el estado del equipo antes de volver a intentarlo, para no enviarla dos veces.

Si alguno de estos mensajes aparece una y otra vez, comprueba que haya un Cora Max en línea junto al acuario. También puedes poner **Cora Max principal** en **Cualquiera activo (automático)** para que cualquier dispositivo en línea pueda recibir la orden. Todos los resultados posibles de una orden están en [Controlar tus equipos](/help/mobile-device-control).

## Dónde se ve el estado de cada dispositivo

Cora Max muestra el estado de consulta de cada acuario en **Ajustes → Ajustes de Cora Max → Estado**. Más información en [Dispositivos y estado de los dispositivos](/help/max-devices).
