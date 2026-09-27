---
title: Cómo controlar tu equipo
description: Abre la propia página de un dispositivo para ver su estado en vivo y controlarlo: tomas, bombas, cabezales de dosificación y equipos de análisis.
section: Cora Mobile
reviewed: 2026-09-27
order: 11
group: Equipment
---

El equipo conectado tiene su propia página en Cora, que muestra el estado en vivo y ofrece los controles que soporta ese dispositivo. Abre una desde la pestaña **Dispositivos**.

![Una página de dispositivo](img/mobile-device-detail.webp "Lecturas en vivo en la parte superior, y luego los controles que soporta ese dispositivo.")

Cada página de dispositivo sigue la misma forma: identificación en la parte superior, una fila de lecturas en vivo, cualquier estado que reporte el dispositivo, y luego sus controles. La campana en la barra de título fija umbrales de alerta para ese dispositivo; consulta [Consumibles](/help/mobile-consumables).

:::warning Estos controles actúan sobre equipo en vivo
No hay vista previa ni deshacer. Algunos controles también te piden confirmar primero.
:::

## Qué pasa cuando envías una orden

Una orden no siempre tiene éxito, y Cora te dice cuál de cuatro cosas pasó en lugar de asumir:

| Resultado | Significa |
|---|---|
| **Confirmado** | El equipo reconoció el cambio y reportó su nuevo estado |
| **Sin confirmar** | La orden se envió, pero no llegó ninguna respuesta. **Esto significa "no lo sabemos", no "funcionó"**; revisa el propio estado del dispositivo |
| **Rechazado** | Algo la declinó (una regla de seguridad, un bloqueo, o el propio equipo), o ningún dispositivo Cora la recibió a tiempo, así que se canceló y no se ejecutó nada |
| **Sin cambios** | El equipo ya estaba en el estado que pediste |

Cada resultado se registra en [Actividad](/help/mobile-activity) con qué lo causó.

## Neptune Apex

La página del Apex lista tus sondas y tomas.

- **Las sondas** informan a Cora como fuentes y se pueden colocar en un panel.
- **Las tomas** cambian entre **Auto**, **Apagado** y **Encendido**. Auto devuelve el control a tu programación del Apex.
- **Los módulos instalados** (Trident, DŌS y otros) tienen cada uno su propia página.

## Trident

Muestra el estado actual de la prueba, los niveles restantes de reactivo y agua residual, y te permite iniciar una prueba.

Puedes fijar un umbral de alerta para las pruebas restantes desde esta página, así Cora te avisa antes de que se acabe el reactivo. Consulta [Consumibles](/help/mobile-consumables).

## DŌS

Un DŌS QD funciona exactamente igual que un DŌS, y todo lo de aquí se aplica a ambos. Cuando un Cora Max lee tu Apex, los cabezales de dosificación aparecen en la página del DŌS, nunca en la lista de tomas.

Cada cabezal de dosificación muestra qué está dosificando, su programa, qué ha dosificado hoy, cuánto queda en el envase y su **autonomía**: cuántos días durará eso al ritmo actual.

Por cabezal puedes:

- **Pausar** y **Reanudar** su programa
- **Llenar**: decirle a Cora que el envase está lleno de nuevo, o fijar el volumen que contiene
- **Dosificar ahora**: una dosis manual medida

:::note Los horarios se editan en Apex Fusion, no aquí
Cora muestra el horario y hace seguimiento de lo dosificado, pero no lo cambia. Editar el horario, la tasa de dosis o el número de dosis se hace en la aplicación Apex Fusion. Pausar, llenar y dosificar a mano son cosas que sí se soportan aquí.
:::

:::note Mide un cabezal antes de dosificarlo a mano
Cora no dosificará un cabezal a mano hasta que se haya medido. **Medir para dosificar** y **Volver a medir** están en el Cora Max que dosifica para el acuario: Cora ejecuta el cabezal durante veinte segundos, tú mides cuánto salió, y Cora calcula la tasa real del cabezal. Una medición sirve para todos los Cora Max y Cora Mobile, así que mide cada cabezal una vez, y de nuevo después de cambiar su tubo.
:::

:::warning Un DŌS sigue dosificando cuando su envase está vacío
La unidad no tiene sensor de nivel y no se detiene sola. Fija una alerta de reposición desde la página del cabezal para que Cora te avise antes de que el envase se seque.
:::

### Para qué se usa cada cabezal

Cada cabezal se fija en un **tipo de uso**, así Cora sabe qué hace y puede hablar de él correctamente: **Suplemento**, **Cambio de agua: entrada de agua salada nueva**, **Cambio de agua: salida de agua vieja**, **Agua de kalk**, **Reactor de calcio**, **Alimento**, **Relleno**, u **Otro**. Fija esto bajo **Usado para** en los ajustes del cabezal.

Los dos tipos de uso de cambio de agua están pensados para **emparejarse**: fija el **Cabezal emparejado** de un cabezal en el otro que mueve el agua en sentido contrario, y Cora los trata como un par de cambio de agua en lugar de dos cabezales sin relación.

Cada cabezal también tiene un techo de **Dosis manual más grande**, para evitar que una dosis manual mal escrita sea mucho mayor de lo previsto. Las dosis manuales grandes solo están disponibles una vez que la tasa del cabezal se ha medido frente a una prueba real en el acuario.

## Red Sea ReefBeat

Cada unidad tiene una página adecuada a lo que es:

| Unidad | La página muestra | Puedes |
|---|---|---|
| **ReefDose** | Cada cabezal, su envase y qué ha dosificado | Por cabezal: **Dosis por día**, **Restante en la botella**, **Dosificar ahora** y **Activar horario**. Fijar alertas de reposición por cabezal |
| **ReefATO+** | Nivel del depósito y actividad de relleno | Fijar una alerta de depósito |
| **ReefMat** | Rollo restante, en días y metros | Avanzar el rollo, fijar una alerta de reposición |
| **ReefRun** | Velocidad y estado de la bomba de retorno y del skimmer | Cambiar la velocidad, cambiar el estado de una bomba, ajustar los ajustes del skimmer |

**ReefRun es un controlador de bomba de retorno y skimmer**, no una bomba de olas.

Una unidad puede detenerse sola, por ejemplo una bomba ReefRun cuando se llena el vaso del skimmer. Cuando eso pasa, su página indica por qué y ofrece la solución:

| Unidad | La página dice | Toca |
|---|---|---|
| ReefRun | Qué bomba se detuvo y por qué, por ejemplo *Vaso lleno. Vacíalo, luego reanuda.* | **Reanudar** |
| ReefRun o ReefMat | **Parada de emergencia** | **Borrar emergencia** |
| ReefMat | **Tapete atascado**, **Error de instalación** o **Error de configuración** | **Reanudar** |
| ReefMat | *Carga un rollo nuevo, luego confírmalo en la aplicación de Red Sea.* | **Ya cargué un rollo nuevo** |
| ReefMat | **El sensor necesita limpieza** | **Sensor limpiado** |
| ReefDose | **Fallo del cabezal**, con el nombre del cabezal | **Restablecer** |
| ReefATO+ | **Borrar fallo** | **Reanudar** |

Algunas de estas te piden confirmar primero. Fuera de la red de la unidad, Cora Mobile las envía a través de un Cora Max del acuario; si ningún Cora Max puede hacerlo, la página lo indica y no se envía nada.

## Bombas Jecod

La página de la bomba muestra su modo e intensidad actuales, y te permite cambiar ambos.

También puedes:

- **Copiar horario a…**: poner el horario de esta bomba en otra
- **Guardar horario como…** y **Horarios guardados…**: guardar un horario y volver a aplicarlo más tarde
- **Compartir este horario** y **Pegar un código de horario…**: mover un horario entre sistemas como un código corto

## Maxspect

:::note El soporte de Maxspect está en beta
El soporte del gyre Maxspect todavía se está probando y desarrollando, así que algunos controles pueden ser limitados, y lo que ves aquí puede cambiar entre actualizaciones. Si algo no funciona como se describe, dínoslo desde [Obtener ayuda](/help/mobile-support).
:::

La página del gyre muestra si el gyre está en marcha, el patrón de olas y la velocidad de **Gyre A** y **Gyre B**, y cuándo se leyó por última vez. Desde ella puedes:

- Cambiar el estado del gyre con el interruptor junto a su estado. Cora te pide confirmar primero. Apagarlo detiene ambos gyres y deja el horario como está.
- Tocar **Cambiar ajustes** para fijar el patrón de olas y la velocidad de bomba de cada gyre (y la duración, para un patrón que tenga una), y si los dos gyres están vinculados. Cora lista qué va a cambiar y te pide confirmar antes de aplicarlo. La alternancia se fija en la aplicación Maxspect: un gyre que la ejecuta mantiene sus rampas y tiempos de espera.
- Tocar **Configurar programa** en su lugar cuando el programa guardado en el gyre no se pueda leer. Fija ambos gyres para que el gyre pueda volver a empezar.
- Ver el programa diario del gyre en la tarjeta **Horario**. Es solo de lectura: fija el horario en la aplicación Maxspect.
- Revisar **Salud de la bomba**: cuándo necesita limpieza la bomba la próxima vez (la propia bomba hace la cuenta atrás), la corriente que consume el cabezal A, qué cabezales están instalados, y el firmware. Toca **Leer** para obtenerlo.

:::note Cómo llega Cora Mobile a un gyre
Cuando un Cora Max atiende al acuario, Cora Mobile funciona a través de ese Cora Max, incluso cuando estás fuera de casa, y **Cambiar ajustes** parte de la última lectura de ese Cora Max. En otro caso, tu teléfono habla directamente con el gyre y debe estar en la red del gyre. Abrir la página entonces lee el gyre; si la página muestra en cambio una lectura guardada más antigua, **Cambiar ajustes** se mantiene oculto hasta que tocas actualizar.
:::

## Qué pasa después de cambiar algo

Cada cambio se registra en [Actividad](/help/mobile-activity) con la superficie que lo solicitó. Si un dispositivo no acepta un cambio, el fallo también se registra ahí.
