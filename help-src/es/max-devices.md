---
title: Dispositivos y estado de los dispositivos
description: Qué equipos ve Cora Max, qué dispositivo consulta cada acuario y qué revisar si deja de consultarlos.
section: Cora Max
reviewed: 2026-09-30
order: 7
group: Equipment
---

En **Ajustes → Dispositivos** ves los equipos que Cora Max tiene a la vista y cómo están.

## La lista de dispositivos

![La lista de dispositivos](img/max-devices.webp "Filtra por acuario. Cada dispositivo lleva una línea con lo que contiene.")

Cora Max ve los mismos equipos que tu teléfono, porque los dos leen la misma cuenta.

Con los filtros de arriba eliges **Todos los acuarios** o solo uno. Cada entrada tiene un punto de estado, una línea con lo que contiene el dispositivo (*21 tomas · 4 alimentaciones*, *19 pruebas restantes*) y el acuario al que pertenece.

Cora Max muestra y controla los dispositivos, pero cada dispositivo se añade, se asigna y se quita desde el teléfono. Sin ningún dispositivo todavía, esta pantalla dice **Agrega dispositivos en la app de Cora**. Más información sobre cómo añadir equipos en [Añadir, editar y eliminar dispositivos](/help/mobile-devices).

## Cora Max principal: qué pantalla habla con tus equipos

El **Cora Max principal** es el Cora Max (u otro dispositivo Cora) que lee el controlador y los demás equipos de un acuario para toda la cuenta. Basta con uno por acuario. Las demás pantallas muestran lo que lee ese.

Para verlo o cambiarlo, abre **Ajustes → [tu acuario] → Cora Max principal**. Tienes dos opciones:

- **Cualquiera activo (automático)**: todos los dispositivos Cora conectados que llegan a los equipos de este acuario se reparten el trabajo, y vale la última escritura. Usa esta opción salvo que tengas un motivo concreto para fijar un dispositivo.
- **Fijar un dispositivo**: solo ese dispositivo consulta los equipos. Si se queda sin conexión, nadie consulta los equipos de este acuario hasta que fijes otro o vuelvas a **Cualquiera activo (automático)**.

Esta elección se hace una sola vez por acuario, no en cada pantalla Cora. Puedes cambiarla desde cualquier Cora Max que muestre ese acuario o desde Cora Mobile. Más detalles en [Más de un dispositivo Cora](/help/mobile-multi-device).

:::note Cora Max principal y Cora Assistant son cosas distintas
El Cora Max principal decide qué dispositivo **lee tus equipos**. Otro ajuste, **Cora Assistant**, decide qué dispositivo **responde a "Hey Cora"**. Si en casa tienes más de un Cora Max, puedes elegir cada uno por separado. Consulta [Hablar con Cora](/help/max-voice).
:::

## Si un acuario deja de actualizarse

Si las lecturas de un acuario se paran mientras otro acuario de la misma pantalla sigue actualizándose, empieza por aquí:

1. **Ajustes → [ese acuario] → Cora Max principal**: comprueba que hay un dispositivo asignado y que está conectado.
2. Si un Cora Max secundario de este acuario muestra la etiqueta **Cora principal sin conexión** en la barra superior, el principal ha perdido la conexión. Qué significa cada etiqueta de estado lo explicamos en [La pantalla de inicio de Cora Max](/help/max-tour).
3. En **Ajustes → Ajustes de Cora Max → Red y actualizaciones → Sondeo de dispositivos** ves cada cuánto lee este Cora Max tus dispositivos. Aquí solo se puede consultar. El valor se cambia desde Cora Mobile.

Si sigue sin funcionar, consulta [Solución de problemas](/help/troubleshooting).

## Gestionar un Cora Max desde el teléfono

En el teléfono, abre el Cora Max desde la pestaña **Dispositivos**. Ahí ves su variante, la versión de firmware y cuándo se conectó por última vez. También puedes cambiarle el nombre o algunos ajustes sin ir hasta él.

![Ajustes de Cora Max desde el teléfono](img/max-from-phone.webp "Intervalo de sondeo, brillo, volumen, alertas en pantalla y temporizador de atenuación.")

Estos ajustes afectan **solo a esa pantalla** (su brillo, su volumen, los avisos de alerta en pantalla y el temporizador de atenuación), igual que si los cambiaras en la pared. Si desactivas las alertas en pantalla, el historial de alertas y las notificaciones push siguen igual.

Qué acuarios muestra un Cora Max y cuál es el Cora Max principal de cada acuario se decide para toda la cuenta. Puedes cambiarlo desde cualquiera de los dos dispositivos, como se explica arriba.

:::note El estado de los dispositivos, primero para consultar
En esta pantalla, la sección **Estado** de **Ajustes → Ajustes de Cora Max** muestra para cada acuario el estado del sondeo, la hora del último sondeo y la última escritura en la nube, sin cambiar nada. Míralo para saber qué está pasando antes de tocar ningún ajuste.
:::
