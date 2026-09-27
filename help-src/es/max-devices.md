---
title: Dispositivos y estado de los dispositivos
description: Qué puede ver Cora Max, qué dispositivo consulta cada acuario, y qué revisar cuando la consulta se detiene.
section: Cora Max
reviewed: 2026-09-27
order: 7
group: Equipment
---

**Ajustes → Dispositivos** lista el equipo que Cora Max puede ver e informa de cómo le va.

## La lista de dispositivos

![La lista de dispositivos](img/max-devices.webp "Filtra por acuario, y luego cada dispositivo con un resumen de una línea de lo que contiene.")

Cora Max ve el mismo equipo que tu teléfono, porque ambos leen la misma cuenta.

Los chips de filtro en la parte superior reducen la lista a **Todos los acuarios** o a uno solo. Cada entrada lleva un punto de estado, un resumen de una línea de lo que contiene el dispositivo (*21 tomas · 4 alimentaciones*, *19 pruebas restantes*) y el acuario al que pertenece.

Añadir y configurar equipo es más fácil en el teléfono; consulta [Añadir, editar y eliminar dispositivos](/help/mobile-devices).

## Cora Max principal: qué tableta habla con tu equipo

**Cora Max principal** es la tableta (u otro dispositivo Cora) que lee el controlador y el resto del equipo de un acuario para toda la cuenta. Solo un dispositivo necesita hacer esto por acuario; el resto de pantallas simplemente muestran lo que él lee.

Abre **Ajustes → [tu acuario] → Cora Max principal** para verlo o cambiarlo. Hay dos tipos de elección:

- **Cualquiera activo (automático)**: todos los dispositivos Cora en línea que puedan llegar al equipo de este acuario comparten el trabajo, y gana la escritura más reciente. Este es el ajuste que hay que usar salvo que tengas una razón concreta para fijar un dispositivo.
- **Fijar un dispositivo**: solo ese dispositivo consulta el equipo. Si el dispositivo fijado se queda sin conexión, nada consulta el equipo de este acuario hasta que fijes otro distinto, o vuelvas a Cualquiera activo (automático).

Esta elección se hace una vez, por acuario, no una vez por cada pantalla Cora. Cámbiala desde cualquier Cora Max que muestre ese acuario, o desde Cora Mobile; consulta [Más de un dispositivo Cora](/help/mobile-multi-device).

:::note Cora Max principal no es lo mismo que Cora Assistant
Cora Max principal decide qué dispositivo **lee tu equipo**. Un ajuste distinto, **Cora Assistant**, decide qué dispositivo **responde a "Hey Cora"**. Un hogar con más de un Cora Max puede fijar estos dos de forma independiente. Consulta [Hablar con Cora](/help/max-voice).
:::

## Si las lecturas de un acuario se detienen

Si las lecturas de un acuario se detienen mientras otro acuario en la misma pantalla sigue actualizándose, empieza por:

1. **Ajustes → [ese acuario] → Cora Max principal**: confirma que hay un dispositivo realmente asignado, y que está en línea.
2. Si un Cora Max secundario para este acuario muestra la píldora **Cora principal sin conexión** en su barra superior, el principal ha perdido su conexión; consulta [La pantalla de inicio de Cora Max](/help/max-tour) para saber qué significa la píldora de estado.
3. **Ajustes → Ajustes de Cora Max → Red y actualizaciones → Sondeo de dispositivos** muestra con qué frecuencia esta unidad lee tus dispositivos; este valor es de solo lectura aquí y se fija desde Cora Mobile.

**Si no funciona:** consulta [Solución de problemas](/help/troubleshooting).

## Gestionar un Cora Max desde tu teléfono

Abre la unidad desde la pestaña **Dispositivos** de tu teléfono para ver su variante, la versión de firmware y cuándo se vio por última vez, y para renombrarla o cambiar algunos de sus ajustes sin acercarte a ella.

![Ajustes de Cora Max desde el teléfono](img/max-from-phone.webp "Intervalo de sondeo, brillo, volumen, alertas en pantalla y temporizador de atenuación.")

Los ajustes que se muestran así describen **solo esta pantalla** (su brillo, volumen, avisos de alerta en pantalla y temporizador de atenuación), igual que si los cambiaras en la pared. Desactivar las alertas en pantalla no afecta al historial de alertas ni a las notificaciones push.

Qué acuarios muestra un Cora Max, y cuál es su Cora Max principal para cada acuario, son decisiones de toda la cuenta; cámbialas desde cualquiera de los dos dispositivos, como se describe arriba.

:::note El estado de los dispositivos es de solo lectura primero
La sección **Estado** de **Ajustes → Ajustes de Cora Max** en esta pantalla informa del estado de sondeo, la última hora de sondeo y la última escritura en la nube para cada acuario, sin cambiar nada. Úsala para establecer qué está pasando antes de modificar un ajuste.
:::
