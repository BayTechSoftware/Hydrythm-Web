---
title: Controlar tus equipos
description: Abre la página de un dispositivo para ver su estado en directo y manejar tomas, bombas, cabezales de dosificación y analizadores, marca a marca.
section: Cora Mobile
reviewed: 2026-10-13
order: 13
group: Equipment
twin: max-device-control
---

Usa la página propia de un dispositivo para ver su estado en directo y cambiar lo que está haciendo. Ábrela desde **Dispositivos** → toca el dispositivo, o toca su casilla en el panel.

![La página de un ReefATO+ en Cora Mobile](img/mobile-device-detail.webp "El estado, las lecturas de hoy y el nivel del agua, y después fugas, rellenados y calibración de la sonda.")

Todas las páginas de dispositivo se organizan igual. El nombre y los datos están arriba, y después una fila de lecturas en directo, cualquier estado que informe el dispositivo y sus controles. La campana de la barra de título fija los umbrales de alerta de ese dispositivo, como se explica en [Consumibles](/help/mobile-consumables). Cómo añadir un dispositivo está en [Conectar tus equipos](/help/mobile-connections).

Ve directamente a tu equipo: [Neptune Apex](#neptune-apex) · [Trident](#trident) · [DŌS](#dos) · [Red Sea](#red-sea) · [ReefDose](#reefdose) · [ReefRun](#reefrun) · [ReefMat](#reefmat) · [ReefATO+](#reefato) · [Alertas de dosificadores](#doser-alerts) · [Jecod](#jecod) · [AquaWiz](#aquawiz) · [Maxspect](#maxspect) · [GHL](#ghl) · [HYDROS](#hydros) · [Focustronic](#focustronic) · [EcoTech, Inkbird y cámaras](#ecotech-inkbird-cameras)

:::warning Estos controles actúan sobre equipos en funcionamiento
No hay vista previa ni deshacer. Algunos controles te piden que confirmes primero.
:::

## Qué pasa cuando envías una orden {#what-happens-when-you-send-a-command}

Una orden no siempre llega. Cora te dice cuál de estas cuatro cosas ha pasado:

| Resultado | Significa |
|---|---|
| **Confirmado** | El equipo aceptó el cambio e informó de su nuevo estado |
| **Sin confirmar** | La orden salió, pero no llegó respuesta. **Significa "no lo sabemos". No significa que funcionara.** Revisa el estado del propio dispositivo |
| **Rechazado** | Algo la denegó (una regla de seguridad, un bloqueo o el propio equipo), o ningún dispositivo Cora la recogió a tiempo. Se canceló y no se ejecutó nada |
| **Sin cambios** | El equipo ya estaba como lo pediste |

Cada resultado queda registrado en [Actividad](/help/mobile-activity), junto con lo que lo provocó.

Sin un Cora Max en el acuario, los equipos Neptune Apex, Red Sea y Jecod solo funcionan en local: tu teléfono tiene que estar en la misma red (o al alcance del Bluetooth) para enviar una orden. Con un Cora Max en el acuario, Cora Mobile la envía a través de ese Cora Max, incluso cuando estás fuera de casa.

## Neptune Apex {#neptune-apex}

![La página de un Apex en Cora Mobile, con su estado, sus módulos Trident y DŌS, Asignación de parámetros y el acuario al que sirve](img/mobile-apex.webp "La página del Apex: Estado, Módulos, Asignación de parámetros y Acuarios.")

La página del Apex muestra el estado del controlador, y después **Módulos**, **Asignación de parámetros** y **Acuarios**.

- **Módulos** lista cada Trident y DŌS instalado. Toca uno para abrir su propia página.
- **Asignación de parámetros** es donde eliges qué alimenta cada sonda. Las sondas llegan a Cora como fuentes, y puedes ponerlas en un panel. Consulta [Asignación de parámetros y sondas](/help/mobile-probes).
- **Acuarios** muestra a qué acuarios sirve el Apex. Toca **Cambiar** para editarlos.
- Las **tomas** se cambian entre **Auto**, **Apagado** y **Encendido** desde un widget **Toma** del panel. Auto devuelve el control a la programación de tu Apex. Consulta [Referencia de widgets](/help/mobile-widgets#outlet).

Tu Apex sigue con su propia programación. Cora solo cambia una toma cuando se lo pides.

## Trident {#trident}

La página del Trident muestra el estado actual de la prueba y los niveles de reactivo y de agua residual. Desde aquí puedes empezar una prueba.

También puedes fijar una alerta para las pruebas restantes y para la botella de residuos, para que Cora te avise antes de que se acabe el reactivo o se llene la botella. Consulta [Consumibles](/help/mobile-consumables).

## DŌS {#dos}

![La página de un DŌS que dice que el DŌS no responde en el AquaBus, con su última autonomía, la dosis de hoy y el plan diario, y después la fila Alertas](img/mobile-dos.webp "Un DŌS que está fuera del AquaBus: la página muestra sus últimos datos conocidos, una tarjeta Necesita atención y la fila Alertas.")

Un DŌS QD funciona exactamente igual que un DŌS, y todo lo de aquí se aplica a los dos. Cuando un Cora Max lee tu Apex, los cabezales de dosificación aparecen en la página del DŌS. Nunca aparecen en la lista de tomas.

Cada cabezal de dosificación muestra qué dosifica, su horario, lo que ha dosificado hoy y cuánto queda en el envase. También muestra la **autonomía**, es decir, cuántos días durará eso al ritmo actual.

Si el DŌS deja de responder en el AquaBus, su página muestra **Fuera del bus** y una tarjeta **Necesita atención**. Los datos de la página son entonces los últimos que informó, no lo que está haciendo ahora. Revisa el cable AquaBus del módulo y el Apex.

Para cada cabezal puedes:

- **Pausar** y **Reanudar** su horario
- **Llenar**, para decirle a Cora que el envase vuelve a estar lleno o fijar cuánto tiene (**Volumen total** es el tamaño del envase, **Volumen restante** es lo que tiene ahora y **Lleno** iguala uno al otro)
- **Dosificar ahora**, para una dosis medida a mano

:::note Edita los horarios en Apex Fusion
Cora muestra el horario y sigue lo que se ha dosificado, pero no cambia el horario. El horario, el ritmo de dosificación y el número de dosis se editan en la app Apex Fusion. Pausar, llenar y dosificar a mano funcionan aquí.
:::

:::note Mide un cabezal antes de dosificar a mano
Cora no dosifica a mano con un cabezal hasta que el cabezal se haya medido. **Medir para dosificar** y **Volver a medir** están en el Cora Max que dosifica para el acuario. Cora hace funcionar el cabezal veinte segundos, tú mides lo que salió y Cora calcula el ritmo real del cabezal. Una medición vale para todos los Cora Max y Cora Mobile. Mide cada cabezal una vez, y otra vez después de cambiarle el tubo.
:::

:::warning Un DŌS sigue dosificando con el envase vacío
La unidad no tiene sensor de nivel y no se para sola. Fija una alerta de reposición para cada cabezal en **Alertas** en la página del DŌS, para que Cora te avise antes de que el envase se vacíe. Consulta [Alertas de dosificadores](#doser-alerts).
:::

### Para qué se usa cada cabezal {#dos-head-use}

Dale a cada cabezal un **tipo de uso** para que Cora sepa qué hace y hable de él correctamente. Las opciones son **Suplemento**, **Cambio de agua: entrada de agua salada nueva**, **Cambio de agua: salida de agua vieja**, **Kalkwasser**, **Reactor de calcio**, **Alimento**, **Relleno** y **Otro**. Fíjalo en **Usado para** en los ajustes del cabezal.

Los dos tipos de uso de cambio de agua van en **parejas**. Pon en el **Cabezal emparejado** de un cabezal el cabezal que mueve el agua en sentido contrario, y Cora trata los dos como una pareja de cambio de agua.

Un envase puede tener hasta 1.000 L, en todos los tipos de uso. El propio Apex solo cuenta hasta 150 L, así que por encima de eso Cora sigue el envase a partir de lo que dosifica el cabezal. Introduce el **Volumen total** al configurarlo. Cora también restablece de vez en cuando el contador propio del Apex, y Actividad lo muestra como *Contador propio del Apex restablecido a 150 L*.

Cada cabezal tiene además un límite de **Dosis manual más grande**, para que una errata no convierta una dosis manual en algo mucho mayor de lo que querías. Las dosis manuales grandes solo están disponibles después de medir el ritmo del cabezal frente a una prueba real en el acuario, y después de activar **Dosis grandes (Beta)** en los ajustes del cabezal. Viene desactivado. Actívalo solo después de haber visto la primera dosis grande en el acuario.

## Red Sea ReefBeat {#red-sea}

Cada unidad Red Sea tiene una página adaptada a lo que hace:

| Unidad | La página muestra | Puedes |
|---|---|---|
| [ReefDose](#reefdose) | Cada cabezal, su envase y lo que ha dosificado | Dosificar, cambiar la dosis diaria, editar el **Plan de dosificación (Beta)** |
| [ReefRun](#reefrun) | La velocidad y el estado de las bombas de retorno y del skimmer | Cambiar la velocidad, encender o apagar una bomba, editar el **Programa de la bomba (Beta)** |
| [ReefMat](#reefmat) | El rollo restante, en días y metros | Avanzar el fieltro, fijar los **Ajustes de ReefMat (Beta)**, registrar un rollo nuevo |
| [ReefATO+](#reefato) | El nivel del depósito y la actividad de reposición | Fijar una alerta del depósito |
| **ReefControl** *(Beta)* | Sus sondas de temperatura, pH, salinidad y ORP | Ver sus lecturas |
| **ReefWave**, **ReefLED** *(Beta)* | Su modo actual | Solo consulta, de momento |

ReefControl, ReefControl Power, ReefWave y ReefLED llevan *(Beta)* en su nombre pero están abiertos a todos. Consulta [Funciones Beta](/help/mobile-beta).

Los enchufes de **ReefControl Power** *(Beta)* aparecen como tomas, que se manejan con el mismo control que una toma del Apex, solo encendido o apagado. De momento no tienen modo automático.

Cuando estás fuera de la red de la unidad, Cora Mobile envía las órdenes de Red Sea a través de un Cora Max del acuario. Si ningún Cora Max puede hacerlo, la página lo indica y no se envía nada.

## ReefDose {#reefdose}

![La página de una ReefDose 4 en Cora Mobile](img/mobile-reefdose.webp "El estado, los cabezales y el total de hoy, Usar el dosificador para el consumo, y después cada cabezal de dosificación.")

Para cada cabezal puedes fijar la **Dosis por día** y lo **Restante en la botella**, hacer **Dosificar ahora** y **Activar horario**. Las alertas de reposición se fijan por cabezal con la campana, como se explica en [Alertas de dosificadores](#doser-alerts).

La sección **Dosificación** muestra las **Próximas dosis**, lo que ha dosificado hoy cada cabezal (**Dosificado hoy hasta ahora**) y **Dosificado por cabezal** en los **Últimos 7 días** o en **Total**. Cora lo lee mientras un Cora Max o tu teléfono está en tu red doméstica.

### Editar un plan de dosificación *(Beta)* {#reefdose-plan}

Toca el icono del calendario en la página de una ReefDose para abrir el **Plan de dosificación (Beta)**.

Un plan es un total diario, repartido en hasta cuatro franjas horarias. Cada franja tiene una hora de inicio y de fin, cuántas dosis debe dar y una velocidad: **Susurro**, **Normal** o **Rápido**. Añade y quita franjas, y guarda. Cora te muestra lo que vas a enviar y te pide que confirmes antes de sustituir el plan completo del cabezal.

El editor lee primero el plan que ya está en la unidad, así que editas el plan real, no un formulario en blanco.

## ReefRun {#reefrun}

ReefRun controla bombas de retorno y de skimmer. No es una bomba de olas. Puedes cambiar la velocidad de una bomba, encenderla o apagarla y ajustar los ajustes del skimmer.

Toca el icono del calendario para abrir el **Programa de la bomba (Beta)**. Un programa tiene hasta seis tramos en un puerto de bomba. Cada tramo tiene una hora de inicio y una velocidad, y puede añadir un pulso corto. La velocidad es 0 o a partir del 5 %. Como el plan de ReefDose, lee primero el programa de la unidad, y **Guardar** te pide que confirmes antes de sustituir el programa completo de la bomba.

## ReefMat {#reefmat}

La página de ReefMat muestra cuánto rollo queda, en días y metros. Toca **Avanzar ahora** para mover el fieltro a mano. Cora pregunta antes **¿Avanzar el tapete ahora?** También puedes fijar una alerta de reposición para el rollo.

Toca el engranaje para abrir los **Ajustes de ReefMat (Beta)**:

- **Avance programado** activa un avance a una hora fija, aparte del sensor de avance automático que ya está en la página. Actívalo y fija cada cuánto, y cuánto mueve el fieltro cada avance.
- **Modelo de ReefMat** y **Posición del motor** (**Izquierda** o **Derecha**) le dicen a Cora qué unidad y qué orientación tienes.

Después de poner un rollo nuevo, díselo a Cora con **Nuevo rollo (Beta)**: su grosor y, si lo sabes, su diámetro exterior. **Avanzar ahora** solo mueve el fieltro que ya tienes puesto.

## ReefATO+ {#reefato}

La página de ReefATO+ muestra el nivel del depósito y las reposiciones recientes. Fija una alerta del depósito con la campana. Cora calcula cuántos días le quedan al depósito según el uso reciente de la reposición, y también puedes preguntárselo al Asistente.

## Cuando una unidad Red Sea se detiene sola {#red-sea-stops}

Una unidad puede detenerse sola. Una bomba ReefRun lo hace cuando se llena el vaso del skimmer, por ejemplo. Cuando pasa, la página dice por qué y ofrece la solución:

| Unidad | La página dice | Toca |
|---|---|---|
| ReefRun | Qué bomba se detuvo y por qué, por ejemplo *Vaso lleno. Vacíalo y reanuda.* | **Reanudar** |
| ReefRun o ReefMat | **Parada de emergencia** | **Borrar emergencia** |
| ReefMat | **Tapete atascado**, **Error de instalación** o **Error de configuración** | **Reanudar** |
| ReefMat | *Carga un rollo nuevo, luego confírmalo en la aplicación de Red Sea.* | **Ya cargué un rollo nuevo** |
| ReefMat | **El sensor necesita limpieza** | **Sensor limpiado** |
| ReefDose | **Fallo del cabezal**, con el nombre del cabezal | **Restablecer** |
| ReefATO+ | **Borrar fallo** | **Reanudar** |

Algunas te piden que confirmes primero. Fuera de la red de la unidad pasan por un Cora Max del acuario, como se explica en [Red Sea ReefBeat](#red-sea).

## Alertas de dosificadores {#doser-alerts}

Un DŌS y una ReefDose guardan sus alertas en su propia página. La pestaña **Reglas** del [Centro de alertas](/help/mobile-alerts) tiene una fila por dosificador que la abre, y el botón **Abrir dosificador** de una alerta de dosificador también te trae aquí.

En la página de un DŌS, toca la tarjeta **Alertas** (o la campana de la barra de título). La hoja lista todos los cabezales, y para cada uno puedes fijar:

- *[cabezal] · días restantes*, por ejemplo *Yodo · días restantes*: recibes una alerta por debajo de esos días de suministro
- *[cabezal] · restante*: recibes una alerta cuando queda menos de esa cantidad en el envase
- **Espacio restante en el contenedor de residuos**, para un cabezal que saca agua vieja: recibes una alerta cuando el contenedor de residuos se está llenando
- **Alertas de dosis omitida**: un interruptor que te avisa cuando el cabezal se salta una dosis programada

Cada umbral tiene su propio interruptor, así que puedes desactivar uno y conservar su valor. Toca **Guardar** cuando termines.

En la página de una ReefDose, toca la campana de la barra de título. Cada cabezal tiene su propio umbral de días restantes y su interruptor.

Los valores predeterminados y otros consumibles están en [Consumibles](/help/mobile-consumables).

## Bombas Jecod / Jebao {#jecod}

La página de la bomba muestra el patrón de olas (modo) y la intensidad actuales, y puedes cambiar los dos. Elige **Igual todo el día** u **Horario** arriba. Crear un programa diario, y copiarlo, guardarlo o compartirlo, se explica en [Programar equipos](/help/mobile-schedules).

Si la bomba forma parte de un grupo, la página muestra su papel, como **Lidera el grupo**, **Sigue: en sincronía** o **Sigue: alternando**.

### Pausa de alimentación {#jecod-feeding}

Empieza una pausa de alimentación desde la sección **Alimentación** de la página de la bomba. Algunas bombas terminan la pausa por sí mismas, y la página dice *La bomba termina esto por sí misma.*

:::warning Deja abierta la página de la bomba durante una pausa de alimentación
Algunas bombas no terminan una alimentación por sí mismas, y la página lo indica. En esas, y en cualquier bomba con horario, Cora Mobile devuelve el patrón de olas y el horario solo mientras la página de la bomba sigue abierta. Si sales de la página, la bomba se queda parada en modo alimentación, o fuera de su horario, hasta que la vuelvas a cambiar o toques **Horario**.
:::

Una bomba Bluetooth tiene que estar al alcance de tu teléfono para empezar una alimentación, y una bomba de red tiene que estar en tu red.

### Comprobaciones de fallos {#jecod-fault-checks}

**Comprobaciones de fallos** fija cada cuánto vuelve a leer Cora la bomba para poder avisarte de un fallo, como una bomba atascada o una que funciona en seco. Si lo pones en desactivado, esos avisos se detienen para esa bomba. Las comprobaciones de fallos necesitan un Cora Max en el acuario. Tu elección se guarda y las comprobaciones empiezan cuando se añade uno. **Usar esto para todas las bombas de este acuario** copia el ajuste a todas ellas.

## AquaWiz {#aquawiz}

La tarjeta de AquaWiz muestra tus lecturas de alcalinidad, y el pH si tu unidad lo informa. También muestra tu KH objetivo, la concentración de tu dosis y, en una unidad con dosificación configurada, su dosis máxima por hora y cuánto suplemento de alcalinidad queda en el envase. Estos datos vienen directamente de tus ajustes de AquaWiz, así que cámbialos en la app de AquaWiz. Cora no puede controlar un AquaWiz.

Si tu unidad sigue su envase, Cora te avisa cuando el suplemento se está acabando, a 100 mL por defecto. Cámbialo desde su regla en el [Centro de alertas](/help/mobile-alerts).

## Maxspect {#maxspect}

:::note Beta
**Beta.** Maxspect está en Beta y solo está abierto a los usuarios Beta. Si no eres usuario Beta, no lo verás en **Agregar dispositivo**. Para pedir acceso Beta, [contacta con soporte](/support.html). Algunos controles pueden estar limitados, y lo que ves aquí puede cambiar entre actualizaciones. Si algo no funciona como se describe, cuéntanoslo desde [Informar de un problema](/help/mobile-support). Más información en [Funciones Beta](/help/mobile-beta).
:::

La página del gyre muestra si el gyre está en marcha, el patrón de olas y la velocidad de **Gyre A** y **Gyre B**, y cuándo se leyeron por última vez. Desde aquí puedes:

- Encender o apagar el gyre con el interruptor que hay junto a su estado. Cora te pide que confirmes primero. Apagarlo detiene los dos gyres y deja el horario como está.
- Tocar **Cambiar ajustes** para fijar el patrón de olas y la velocidad de la bomba de cada gyre, además de la duración en los patrones que la tienen, y si los dos gyres están vinculados. Cora lista lo que va a cambiar y te pide que confirmes. El modo alterno se configura en la app de Maxspect, y un gyre que lo usa conserva sus rampas y tiempos de espera.
- Tocar **Configurar programa** si no se puede leer el programa guardado en el gyre. Configura los dos gyres para que el gyre pueda volver a arrancar.
- Ver el programa diario del gyre en la tarjeta **Horario**. Aquí solo puedes verlo. El horario se configura en la app de Maxspect.
- Revisar **Salud de la bomba**. Muestra cuándo necesita limpieza la bomba (la propia bomba lleva la cuenta atrás), la corriente que consume el cabezal A, qué cabezales están instalados y el firmware. Toca **Leer** para obtenerlo.

:::note Cómo llega Cora Mobile a un gyre
Si un Cora Max sirve al acuario, Cora Mobile pasa por ese Cora Max, incluso cuando estás fuera de casa. **Cambiar ajustes** parte entonces de la última lectura de ese Cora Max. Si no, tu teléfono habla directamente con el gyre y tiene que estar en la red del gyre. Abrir la página lee el gyre. Si la página muestra una lectura guardada más antigua, **Cambiar ajustes** sigue oculto hasta que tocas actualizar.
:::

## GHL ProfiLux y Mitras {#ghl}

:::note Beta
**Beta.** GHL está en Beta y solo está abierto a los usuarios Beta. Si no eres usuario Beta, no lo verás en **Agregar dispositivo**. Para pedir acceso Beta, [contacta con soporte](/support.html). Puede que algunas lecturas o controles todavía no funcionen, y lo que ves aquí puede cambiar entre actualizaciones. Si algo no funciona como se describe, cuéntanoslo desde [Informar de un problema](/help/mobile-support). Más información en [Funciones Beta](/help/mobile-beta).
:::

La página del controlador muestra sus sondas, tomas, dosificadoras y sensores de nivel y, en los modelos Director, sus resultados de pruebas de KH y de iones.

Los controles siguen desactivados hasta que activas **Permitir el control desde Cora (Beta)** en la página del dispositivo. Viene desactivado, y al activarlo Cora puede enviar a ese controlador órdenes de pausa de alimentación, mantenimiento, cambio de agua, tormenta, iluminación, valores de consigna y tomas. Una vez que puedes añadir el dispositivo, este interruptor no necesita ningún acceso extra.

Cuando está activado:

- Una toma se puede poner en **Siempre encendido**, **Siempre apagado** o **Volver a automático** para devolverla a la programación propia del controlador.
- Un valor de consigna, como la temperatura o el pH, muestra su rango permitido y rechaza un valor fuera de él.

:::warning Un cambio de toma o de consigna se guarda en el propio controlador
No se guarda solo en Cora. Poner una toma en Siempre encendido o Siempre apagado anula la programación propia del controlador para esa toma hasta que elijas Volver a automático.
:::

Si una toma o un valor de consigna parece pertenecer a un calentador o a una bomba de retorno, Cora te pide que confirmes dos veces antes de enviarlo.

Si el envase de una dosificadora se está acabando, Cora te avisa igual que con otros consumibles. El valor predeterminado es el 20 % de llenado, y puedes cambiarlo desde la regla de la dosificadora en el [Centro de alertas](/help/mobile-alerts).

:::note ProfiLux mini
Un mini solo puede encender y apagar sus tomas. Todo lo demás de aquí, como los valores de consigna y la pausa de alimentación, necesita un ProfiLux 3, 4 o Mitras.
:::

Si el controlador rechaza el cambio, comprueba que su API de GHL está activada con acceso completo. GHL la desactiva después de cada actualización de firmware. [Solución de problemas](/help/troubleshooting) tiene los pasos.

## HYDROS {#hydros}

:::note Beta
**Beta.** HYDROS está en Beta y solo está abierto a los usuarios Beta. Si no eres usuario Beta, no lo verás en **Agregar dispositivo**. Para pedir acceso Beta, [contacta con soporte](/support.html). Puede que algunas lecturas o controles todavía no funcionen, y lo que ves aquí puede cambiar entre actualizaciones. Si algo no funciona como se describe, cuéntanoslo desde [Informar de un problema](/help/mobile-support). Más información en [Funciones Beta](/help/mobile-beta).
:::

Lo que ves aquí depende de la clave con la que lo vinculaste. Una clave **Read** solo te da sus entradas. Una clave **Write** añade salidas, modos, dosificación y órdenes del analizador, además de un aviso en la página que te recuerda qué tipo de clave usas.

Con una clave de escritura, los controles también siguen desactivados hasta que activas **Permitir el control desde Cora (Beta)** en la página del dispositivo. Viene desactivado.

Cuando está activado, la página puede mostrar:

- **Salidas**, como un interruptor para una salida de encendido y apagado, un control deslizante para un nivel como una bomba o una luz, o un botón para un indicador. Una salida anulada muestra **Anulado** con un botón **Volver a la programación** para devolverla a su propio programa.
- **Modos**, como Alimentación o Cambio de agua, como una fila de opciones. Al tocar uno se te pide que confirmes.
- **Cabezales de dosificación**, cada uno con un botón **Dosificar** y una entrada **Ajustes del cabezal** donde fijas sus propios límites: una dosis manual máxima y un tope diario. Pedir más que el límite de un cabezal, o más de lo que le queda de su tope diario, se rechaza con los números en el mensaje.
- **Órdenes del analizador**, para un iV o un Maven conectado, que se ejecutan con un botón y se confirman primero.

Si el controlador lleva un rato sin informar, la página lo indica y las lecturas pueden estar desactualizadas. Una orden enviada mientras parece desconectado no se envía, y la página también te lo dice.

## Focustronic {#focustronic}

:::note Beta
**Beta.** Focustronic está en Beta y solo está abierto a los usuarios Beta. Si no eres usuario Beta, no lo verás en **Agregar dispositivo**. Para pedir acceso Beta, [contacta con soporte](/support.html). Más información en [Funciones Beta](/help/mobile-beta).
:::

Cada dispositivo muestra su estado, su firmware, su última prueba y, en un Alkatronic, la alcalinidad y el pH que midió. También ves las bombas con lo que queda en cada una, los parámetros, los viales y cualquier aviso de reactivo o de tampón. Cora pide lecturas nuevas a Focustronic cada 30 minutos.

En **Controles** puedes hacer **Medir ahora**, **Dosificar ahora** con una bomba (hasta 500 mL de una vez) y, en un Mastertronic, **Probar ahora**. Cada uno te pide que confirmes primero. Cora nunca reintenta una dosis, así que si el resultado dice que es desconocido, revisa el dispositivo. Las órdenes pasan por los servidores de Focustronic, que Cora no controla, y solo están disponibles mientras el dispositivo está en línea.

## EcoTech, Inkbird y cámaras {#ecotech-inkbird-cameras}

:::note Beta
**Beta.** EcoTech, Inkbird y las cámaras están en Beta y solo están abiertos a los usuarios Beta. Si no eres usuario Beta, no los verás en **Agregar dispositivo**. Para pedir acceso Beta, [contacta con soporte](/support.html).
:::

Tienen sus propias páginas:

- Luces EcoTech Radion, bombas VorTech y dosificadoras Versa: [Luces, bombas y dosificadoras EcoTech](/help/mobile-ecotech)
- Los monitores de aire de habitación Inkbird solo informan de lecturas, así que no hay nada que controlar: [Conectar tus equipos](/help/mobile-connections#inkbird-room-air-monitor)
- Cámaras y vigilancia del skimmer: [Cámaras y vigilancia del skimmer](/help/mobile-cameras)

## Qué pasa después de cambiar algo {#what-happens-after-you-change-something}

Cada cambio queda registrado en [Actividad](/help/mobile-activity), con la superficie desde la que se hizo. Si un dispositivo no acepta un cambio, también queda registrado ahí.
