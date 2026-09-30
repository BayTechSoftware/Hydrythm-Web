---
title: Controlar tus equipos
description: Abre la página de un dispositivo para ver su estado en directo y manejarlo, ya sean tomas, bombas, cabezales de dosificación o equipos de análisis.
section: Cora Mobile
reviewed: 2026-09-30
order: 11
group: Equipment
---

Cada equipo conectado tiene su propia página en Cora. Ahí ves su estado en directo y los controles que admite ese dispositivo. Ábrela desde la pestaña **Dispositivos**.

![Una página de dispositivo](img/mobile-device-detail.webp "Lecturas en vivo en la parte superior, y luego los controles que soporta ese dispositivo.")

Todas las páginas de dispositivo tienen el mismo orden. Arriba está la identificación, después una fila de lecturas en directo, luego el estado que informe el dispositivo y al final sus controles. Con la campana de la barra de título fijas umbrales de alerta para ese dispositivo. Más información en [Consumibles](/help/mobile-consumables).

:::warning Estos controles actúan sobre equipos en marcha
No hay vista previa ni forma de deshacer. Algunos controles te piden confirmación antes.
:::

## Qué pasa cuando envías una orden

Una orden no siempre sale bien. Cora no da nada por hecho y te dice cuál de estas cuatro cosas ha pasado:

| Resultado | Qué significa |
|---|---|
| **Confirmado** | El equipo aceptó el cambio e informó de su nuevo estado |
| **Sin confirmar** | La orden se envió, pero no llegó respuesta. **Quiere decir "no lo sabemos", no "ha funcionado".** Revisa el estado en el propio dispositivo |
| **Rechazado** | Algo la bloqueó (una regla de seguridad, un bloqueo o el propio equipo) o ningún dispositivo Cora la recogió a tiempo. Se canceló y no se ejecutó nada |
| **Sin cambios** | El equipo ya estaba en el estado que pediste |

Cada resultado queda registrado en [Actividad](/help/mobile-activity) junto con su causa.

## Neptune Apex

La página del Apex muestra tus sondas y tus tomas.

- **Las sondas** llegan a Cora como fuentes y puedes ponerlas en un panel.
- **Las tomas** cambian entre **Auto**, **Apagado** y **Encendido**. Con Auto, el control vuelve a la programación de tu Apex.
- **Los módulos instalados** (Trident, DŌS y otros) tienen su propia página.

## Trident

Muestra en qué punto está la prueba y cuánto reactivo y agua residual queda. Desde aquí también puedes iniciar una prueba.

En esta página puedes fijar un umbral de alerta para las pruebas que quedan. Así Cora te avisa antes de que se acabe el reactivo. Más información en [Consumibles](/help/mobile-consumables).

## DŌS

Un DŌS QD funciona igual que un DŌS, y todo lo que se explica aquí vale para los dos. Cuando un Cora Max lee tu Apex, los cabezales de dosificación aparecen en la página del DŌS. Nunca aparecen en la lista de tomas.

Cada cabezal muestra qué dosifica, su programa, cuánto ha dosificado hoy y cuánto queda en el recipiente. También muestra su **autonomía**, es decir, cuántos días te dura lo que queda al ritmo actual.

En cada cabezal puedes:

- **Pausar** y **Reanudar** su programa
- **Llenar**: indicarle a Cora que el recipiente vuelve a estar lleno, o fijar cuánto contiene
- **Dosificar ahora**: dar una dosis manual medida

:::note Los horarios se editan en Apex Fusion
Cora muestra el horario y lleva la cuenta de lo dosificado, pero no lo cambia. El horario, la tasa de dosis y el número de dosis se editan en la aplicación Apex Fusion. Aquí sí puedes pausar, llenar y dosificar a mano.
:::

:::note Mide un cabezal antes de dosificar a mano
Cora no dosifica a mano con un cabezal que no se ha medido. **Medir para dosificar** y **Volver a medir** están en el Cora Max que dosifica para el acuario. Cora hace funcionar el cabezal veinte segundos, tú mides cuánto ha salido y Cora calcula el caudal real. La medición sirve para todos los Cora Max y Cora Mobile. Mide cada cabezal una vez y repite la medición cuando cambies el tubo.
:::

:::warning Un DŌS sigue dosificando con el recipiente vacío
El equipo no tiene sensor de nivel y no se para solo. Fija una alerta de reposición en la página del cabezal para que Cora te avise antes de que el recipiente se vacíe.
:::

### Para qué se usa cada cabezal

A cada cabezal se le asigna un **tipo de uso**. Así Cora sabe qué hace y puede hablar de él con precisión. Los tipos son **Suplemento**, **Cambio de agua: entrada de agua salada nueva**, **Cambio de agua: salida de agua vieja**, **Agua de kalk**, **Reactor de calcio**, **Alimento**, **Relleno** y **Otro**. Elige el tipo en **Usado para**, dentro de los ajustes del cabezal.

Los dos tipos de cambio de agua van **en pareja**. En el **Cabezal emparejado** de un cabezal, elige el otro, el que mueve el agua en sentido contrario. Cora los tratará como una pareja de cambio de agua y no como dos cabezales sueltos.

Cada cabezal tiene además un límite de **Dosis manual más grande**. Sirve para que un error al escribir una dosis manual no acabe en una dosis mucho mayor de lo previsto. Las dosis manuales grandes solo se pueden usar cuando el caudal del cabezal se ha medido con una prueba real en el acuario.

## Red Sea ReefBeat

Cada equipo tiene una página adaptada a lo que es:

| Equipo | La página muestra | Puedes |
|---|---|---|
| **ReefDose** | Cada cabezal, su recipiente y cuánto ha dosificado | En cada cabezal: **Dosis por día**, **Restante en la botella**, **Dosificar ahora** y **Activar horario**. Fijar alertas de reposición por cabezal |
| **ReefATO+** | Nivel del depósito y actividad de rellenado | Fijar una alerta del depósito |
| **ReefMat** | Rollo que queda, en días y metros | Avanzar el rollo y fijar una alerta de reposición |
| **ReefRun** | Velocidad y estado de la bomba de retorno y de la del skimmer | Cambiar la velocidad, encender o apagar una bomba y cambiar los ajustes del skimmer |

**ReefRun controla la bomba de retorno y la del skimmer.** No es una bomba de circulación.

Un equipo puede pararse por su cuenta. Por ejemplo, una bomba ReefRun se para cuando se llena el vaso del skimmer. Si pasa, su página te dice por qué y te ofrece la solución:

| Equipo | La página dice | Toca |
|---|---|---|
| ReefRun | Qué bomba se paró y por qué, por ejemplo *Vaso lleno. Vacíalo y reanuda.* | **Reanudar** |
| ReefRun o ReefMat | **Parada de emergencia** | **Borrar emergencia** |
| ReefMat | **Tapete atascado**, **Error de instalación** o **Error de configuración** | **Reanudar** |
| ReefMat | *Carga un rollo nuevo, luego confírmalo en la aplicación de Red Sea.* | **Ya cargué un rollo nuevo** |
| ReefMat | **El sensor necesita limpieza** | **Sensor limpiado** |
| ReefDose | **Fallo del cabezal**, con el nombre del cabezal | **Restablecer** |
| ReefATO+ | **Borrar fallo** | **Reanudar** |

Algunas de estas acciones te piden confirmación. Si no estás en la red del equipo, Cora Mobile las envía a través de un Cora Max del acuario. Si ningún Cora Max puede hacerlo, la página te lo indica y no se envía nada.

## Bombas Jecod

La página de la bomba muestra su modo y su intensidad actuales, y puedes cambiar los dos.

También puedes:

- **Copiar horario a…**: pasar el horario de esta bomba a otra
- **Guardar horario como…** y **Horarios guardados…**: guardar un horario y volver a aplicarlo más adelante
- **Compartir este horario** y **Pegar un código de horario…**: llevar un horario de un sistema a otro con un código corto

## Maxspect

:::note Maxspect está en beta
Seguimos probando y desarrollando el soporte para el gyre Maxspect. Algunos controles pueden estar limitados y lo que ves aquí puede cambiar con las actualizaciones. Si algo no funciona como se describe, avísanos desde [Obtener ayuda](/help/mobile-support).
:::

La página del gyre muestra si está en marcha, el patrón de olas y la velocidad de **Gyre A** y **Gyre B**, y cuándo se leyeron por última vez. Desde ella puedes:

- Encender o apagar el gyre con el interruptor que hay junto a su estado. Cora te pide confirmación antes. Al apagarlo se paran los dos gyres y el horario no cambia.
- Tocar **Cambiar ajustes** para elegir el patrón de olas y la velocidad de bomba de cada gyre, y si los dos gyres van vinculados. Si el patrón tiene duración, también la eliges aquí. Cora te enseña lo que va a cambiar y te pide confirmación antes de aplicarlo. El modo alterno se configura en la aplicación Maxspect. Un gyre que lo usa conserva sus rampas y tiempos de pausa.
- Tocar **Configurar programa** cuando no se puede leer el programa guardado en el gyre. Configura los dos gyres para que el gyre pueda volver a arrancar.
- Consultar el programa del día en la tarjeta **Horario**. Solo sirve para verlo. El horario se configura en la aplicación Maxspect.
- Revisar la **Salud de la bomba**. Ahí ves cuándo toca la próxima limpieza (la propia bomba lleva la cuenta atrás), la corriente que consume el cabezal A, qué cabezales están instalados y el firmware. Toca **Leer** para obtener los datos.

:::note Cómo se comunica Cora Mobile con un gyre
Si un Cora Max atiende el acuario, Cora Mobile trabaja a través de ese Cora Max, también cuando estás fuera de casa. **Cambiar ajustes** parte entonces de la última lectura de ese Cora Max. Si no, tu teléfono habla con el gyre directamente y tiene que estar en la red del gyre. En ese caso, al abrir la página se lee el gyre. Si la página muestra una lectura guardada más antigua, **Cambiar ajustes** no aparece hasta que tocas actualizar.
:::

## GHL ProfiLux y Mitras

:::note GHL está en beta
Seguimos probando y desarrollando el soporte para GHL. Algunas lecturas o controles pueden no funcionar todavía, y lo que ves aquí puede cambiar con las actualizaciones. Si algo no funciona como se describe, avísanos desde [Obtener ayuda](/help/mobile-support).
:::

La página del controlador muestra sus sondas, tomas, dosificadoras y sensores de nivel, y en los modelos Director, sus resultados de las pruebas de KH e iones.

Los controles quedan desactivados hasta que activas **Permitir el control desde Cora (Beta)** en la página del dispositivo. Está desactivado por defecto, y al activarlo Cora puede enviar a ese controlador órdenes de pausa de alimentación, mantenimiento, cambio de agua, tormenta, iluminación, consignas y tomas.

Una vez activado:

- Una toma se puede poner en **Siempre encendido**, **Siempre apagado** o **Volver a automático** para devolverla a la programación propia del controlador.
- Una consigna, como la de temperatura o pH, muestra su rango permitido y rechaza un valor fuera de él.

:::warning Un cambio de toma o de consigna se guarda en el controlador
No se guarda solo en Cora. Poner una toma en Siempre encendido o Siempre apagado anula la programación propia del controlador para esa toma hasta que eliges Volver a automático.
:::

Si una toma o una consigna parece pertenecer a un calentador o a una bomba de retorno, Cora te pide confirmar dos veces antes de enviarla.

Si el controlador rechaza el cambio, revisa que su API de GHL esté activada con acceso completo. GHL la desactiva después de cada actualización de firmware. [Solución de problemas](/help/troubleshooting) tiene los pasos.

## HYDROS

:::note HYDROS está en beta
Seguimos probando y desarrollando el soporte para HYDROS. Algunas lecturas o controles pueden no funcionar todavía, y lo que ves aquí puede cambiar con las actualizaciones. Si algo no funciona como se describe, avísanos desde [Obtener ayuda](/help/mobile-support).
:::

Lo que ves aquí depende de la clave con la que lo enlazaste. Una clave **Read** te da solo sus entradas. Una clave **Write** añade salidas, modos, dosificación y órdenes de analizador, además de un aviso en la página que te recuerda qué tipo de clave tienes.

Con una clave Write, los controles también quedan desactivados hasta que activas **Permitir el control desde Cora (Beta)** en la página del dispositivo. Está desactivado por defecto.

Una vez activado, la página puede mostrar:

- **Salidas**, como un interruptor para una salida de encendido/apagado, un deslizador para un nivel como una bomba o una luz, o un botón para una bandera. Una salida anulada muestra **Anulado** con un botón **Volver a la programación** para devolverla a su propio programa.
- **Modos**, como Alimentación o Cambio de agua, como una fila de opciones. Tocar una te pide confirmación.
- **Cabezales de dosificación**, cada uno con un botón **Dosificar** y una entrada **Ajustes del cabezal** donde fijas sus propios límites: una dosis manual máxima y un tope diario. Pedir más del límite de un cabezal, o más de lo que le queda de su propio tope diario, se rechaza con las cifras en el mensaje.
- **Órdenes de analizador**, para un iV o un Maven conectado, se ejecutan desde un botón y se confirman antes.

Si el controlador lleva un rato sin reportar, la página lo indica y las lecturas pueden estar desactualizadas. Una orden enviada mientras parece desconectado no se envía en absoluto, y la página también te lo dice.

## Qué pasa después de cambiar algo

Cada cambio queda registrado en [Actividad](/help/mobile-activity) junto con la superficie que lo pidió. Si un dispositivo no acepta un cambio, el fallo también queda registrado ahí.
