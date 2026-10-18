---
title: Controlar tus equipos
description: Abre la página de un dispositivo para ver su estado en directo y manejar tomas, bombas, cabezales de dosificación y analizadores, marca a marca.
section: Cora Mobile
reviewed: 2026-10-18
order: 13
group: Equipment
twin: max-device-control
---

Usa la página propia de un dispositivo para ver su estado en directo y cambiar lo que está haciendo. Ábrela desde **Dispositivos** → toca el dispositivo, o toca su tarjeta en el panel.

![La página de un ReefATO+ en Cora Mobile](img/mobile-device-detail.webp "El estado, las lecturas de hoy y el nivel del agua, y después fugas, rellenados y calibración de la sonda.")

Todas las páginas de dispositivo se organizan igual. El nombre y los datos están arriba, y después una fila de lecturas en directo, cualquier estado que informe el dispositivo y sus controles. La campana de la barra de título fija los umbrales de alerta de ese dispositivo, como se explica en [Consumibles](/help/mobile-consumables). Cómo añadir un dispositivo está en [Conectar tus equipos](/help/mobile-connections).

Ve directamente a tu equipo: [Neptune Apex](#neptune-apex) · [Trident](#trident) · [DŌS](#dos) · [Red Sea](#red-sea) · [ReefDose](#reefdose) · [ReefRun](#reefrun) · [ReefMat](#reefmat) · [ReefATO+](#reefato) · [Alertas de dosificadoras](#doser-alerts) · [Jecod](#jecod) · [AquaWiz](#aquawiz)

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

Cada cabezal de dosificación muestra qué dosifica, su horario, lo que ha dosificado hoy y cuánto queda en el recipiente. También muestra la **autonomía**, es decir, cuántos días durará eso al ritmo actual.

Si el DŌS deja de responder en el AquaBus, su página muestra **Fuera del bus** y una tarjeta **Necesita atención**. Los datos de la página son entonces los últimos que informó, no lo que está haciendo ahora. Revisa el cable AquaBus del módulo y el Apex.

Para cada cabezal puedes:

- **Pausar** y **Reanudar** su horario
- **Llenar**, para decirle a Cora que el recipiente vuelve a estar lleno o fijar cuánto tiene (**Volumen total** es el tamaño del recipiente, **Volumen restante** es lo que tiene ahora y **Lleno** iguala uno al otro)
- **Dosificar ahora**, para una dosis medida a mano

:::note Edita los horarios en Apex Fusion
Cora muestra el horario y sigue lo que se ha dosificado, pero no cambia el horario. El horario, el ritmo de dosificación y el número de dosis se editan en la app Apex Fusion. Pausar, llenar y dosificar a mano funcionan aquí.
:::

:::note Mide un cabezal antes de dosificar a mano
Cora no dosifica a mano con un cabezal hasta que el cabezal se haya medido. **Medir para dosificar** y **Volver a medir** están en el Cora Max que dosifica para el acuario. Cora hace funcionar el cabezal veinte segundos, tú mides lo que salió y Cora calcula el ritmo real del cabezal. Una medición vale para todos los Cora Max y Cora Mobile. Mide cada cabezal una vez, y otra vez después de cambiarle el tubo.
:::

:::warning Un DŌS sigue dosificando con el recipiente vacío
La unidad no tiene sensor de nivel y no se para sola. Fija una alerta de reposición para cada cabezal en **Alertas** en la página del DŌS, para que Cora te avise antes de que el recipiente se vacíe. Consulta [Alertas de dosificadoras](#doser-alerts).
:::

### Para qué se usa cada cabezal {#dos-head-use}

Dale a cada cabezal un **tipo de uso** para que Cora sepa qué hace y hable de él correctamente. Las opciones son **Suplemento**, **Cambio de agua: entrada de agua salada nueva**, **Cambio de agua: salida de agua vieja**, **Kalkwasser**, **Reactor de calcio**, **Alimento**, **Relleno** y **Otro**. Fíjalo en **Usado para** en los ajustes del cabezal.

Los dos tipos de uso de cambio de agua van en **parejas**. Pon en el **Cabezal emparejado** de un cabezal el cabezal que mueve el agua en sentido contrario, y Cora trata los dos como una pareja de cambio de agua.

Un recipiente puede tener hasta 1.000 L, en todos los tipos de uso. El propio Apex solo cuenta hasta 150 L, así que por encima de eso Cora sigue el recipiente a partir de lo que dosifica el cabezal. Introduce el **Volumen total** al configurarlo. Cora también restablece de vez en cuando el contador propio del Apex, y Actividad lo muestra como *Contador propio del Apex restablecido a 150 L*.

Cada cabezal tiene además un límite de **Dosis manual más grande**, para que una errata no convierta una dosis manual en algo mucho mayor de lo que querías. Las dosis manuales grandes solo están disponibles después de medir el ritmo del cabezal frente a una prueba real en el acuario, y después de activar **Dosis grandes** en los ajustes del cabezal. Viene desactivado. Actívalo solo después de haber visto la primera dosis grande en el acuario.

## Red Sea ReefBeat {#red-sea}

Cada unidad Red Sea tiene una página adaptada a lo que hace:

| Unidad | La página muestra | Puedes |
|---|---|---|
| [ReefDose](#reefdose) | Cada cabezal, su recipiente y lo que ha dosificado | Dosificar, cambiar la dosis diaria, editar el **Plan de dosificación** |
| [ReefRun](#reefrun) | La velocidad y el estado de las bombas de retorno y del skimmer | Cambiar la velocidad, encender o apagar una bomba |
| [ReefMat](#reefmat) | El rollo restante, en días y metros | Avanzar el fieltro, fijar los **Ajustes de ReefMat**, registrar un rollo nuevo |
| [ReefATO+](#reefato) | El nivel del depósito y la actividad de reposición | Fijar una alerta del depósito |



Cuando estás fuera de la red de la unidad, Cora Mobile envía las órdenes de Red Sea a través de un Cora Max del acuario. Si ningún Cora Max puede hacerlo, la página lo indica y no se envía nada.

## ReefDose {#reefdose}

![La página de una ReefDose 4 en Cora Mobile](img/mobile-reefdose.webp "El estado, los cabezales y el total de hoy, Usar la dosificadora para el consumo, y después cada cabezal de dosificación.")

Para cada cabezal puedes fijar la **Dosis por día** y lo **Restante en la botella**, hacer **Dosificar ahora** y **Activar horario**. Las alertas de reposición se fijan por cabezal con la campana, como se explica en [Alertas de dosificadoras](#doser-alerts).

La sección **Dosificación** muestra las **Próximas dosis**, lo que ha dosificado hoy cada cabezal (**Dosificado hoy hasta ahora**) y **Dosificado por cabezal** en los **Últimos 7 días** o en **Total**. Cora lo lee mientras un Cora Max o tu teléfono está en tu red doméstica.

### Editar un plan de dosificación {#reefdose-plan}

Toca el icono del calendario en la página de una ReefDose para abrir el **Plan de dosificación**.

Un plan es un total diario, repartido en hasta cuatro franjas horarias. Cada franja tiene una hora de inicio y de fin, cuántas dosis debe dar y una velocidad: **Susurro**, **Normal** o **Rápido**. Añade y quita franjas, y guarda. Cora te muestra lo que vas a enviar y te pide que confirmes antes de sustituir el plan completo del cabezal.

El editor lee primero el plan que ya está en la unidad, así que editas el plan real, no un formulario en blanco.

## ReefRun {#reefrun}

ReefRun controla bombas de retorno y de skimmer. No es una bomba de circulación. Puedes cambiar la velocidad de una bomba, encenderla o apagarla y ajustar los ajustes del skimmer.


## ReefMat {#reefmat}

La página de ReefMat muestra cuánto rollo queda, en días y metros. Toca **Avanzar ahora** para mover el fieltro a mano. Cora pregunta antes **¿Avanzar el tapete ahora?** También puedes fijar una alerta de reposición para el rollo.

Toca el engranaje para abrir los **Ajustes de ReefMat**:

- **Avance programado** activa un avance a una hora fija, aparte del sensor de avance automático que ya está en la página. Actívalo y fija cada cuánto, y cuánto mueve el fieltro cada avance.
- **Modelo de ReefMat** y **Posición del motor** (**Izquierda** o **Derecha**) le dicen a Cora qué unidad y qué orientación tienes.

Después de poner un rollo nuevo, díselo a Cora con **Nuevo rollo**: su grosor y, si lo sabes, su diámetro exterior. **Avanzar ahora** solo mueve el fieltro que ya tienes puesto.

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

## Alertas de dosificadoras {#doser-alerts}

Un DŌS y una ReefDose guardan sus alertas en su propia página. La pestaña **Reglas** del [Centro de alertas](/help/mobile-alerts) tiene una fila por dosificadora que la abre, y el botón **Abrir dosificadora** de una alerta de dosificadora también te trae aquí.

En la página de un DŌS, toca la tarjeta **Alertas** (o la campana de la barra de título). La hoja lista todos los cabezales, y para cada uno puedes fijar:

- *[cabezal] · días restantes*, por ejemplo *Yodo · días restantes*: recibes una alerta por debajo de esos días de suministro
- *[cabezal] · restante*: recibes una alerta cuando queda menos de esa cantidad en el recipiente
- **Espacio restante en el recipiente de residuos**, para un cabezal que saca agua vieja: recibes una alerta cuando el recipiente de residuos se está llenando
- **Alertas de dosis omitida**: un interruptor que te avisa cuando el cabezal se salta una dosis programada

Cada umbral tiene su propio interruptor, así que puedes desactivar uno y conservar su valor. Toca **Guardar** cuando termines.

En la página de una ReefDose, toca la campana de la barra de título. Cada cabezal tiene su propio umbral de días restantes y su interruptor.

Los valores predeterminados y otros consumibles están en [Consumibles](/help/mobile-consumables).

## Bombas Jecod / Jebao {#jecod}

La página de la bomba muestra el patrón de olas (modo) y la intensidad actuales, y puedes cambiar los dos. Su estado está en la fila del título, junto al nombre de la bomba. Un selector con **Igual todo el día** y **Horario** marca el que está en marcha con *· en marcha*, y la página se abre en él. Crear un horario diario, y copiarlo, guardarlo o compartirlo, se explica en [Programar equipos](/help/mobile-schedules).

Si la bomba forma parte de un grupo, la página muestra su papel, como **Lidera el grupo**, **Sigue: en sincronía** o **Sigue: alternando**.

### Pausa de alimentación {#jecod-feeding}

Empieza una pausa de alimentación desde **Alimentación** en la página de la bomba: toca **5**, **10**, **15** o **30** min. Algunas bombas terminan la pausa por sí mismas, y la página dice *La bomba termina esto por sí misma.*

:::warning Deja abierta la página de la bomba durante una pausa de alimentación
Algunas bombas no terminan una alimentación por sí mismas, y la página lo indica. En esas, y en cualquier bomba con horario, Cora Mobile devuelve el patrón de olas y el horario solo mientras la página de la bomba sigue abierta. Si sales de la página, la bomba se queda parada en modo alimentación, o fuera de su horario, hasta que la vuelvas a cambiar o toques **Horario**.
:::

Si tu hogar tiene un Cora Max, él termina la alimentación y devuelve la bomba a su programa cuando acaba el tiempo, incluso con Cora Mobile cerrado. La advertencia de arriba solo importa entonces cuando no hay un Cora Max.

Una bomba Bluetooth tiene que estar al alcance de tu teléfono para empezar una alimentación, y una bomba de red tiene que estar en tu red.

### Comprobaciones de fallos {#jecod-fault-checks}

**Comprobaciones de fallos** fija cada cuánto vuelve a leer Cora la bomba para poder avisarte de un fallo, como una bomba atascada o una que funciona en seco. Si lo pones en desactivado, esos avisos se detienen para esa bomba. Las comprobaciones de fallos necesitan un Cora Max en el acuario. Tu elección se guarda y las comprobaciones empiezan cuando se añade uno. **Usar esto para todas las bombas de este acuario** copia el ajuste a todas ellas.

## AquaWiz {#aquawiz}

La tarjeta de AquaWiz muestra tus lecturas de alcalinidad, y el pH si tu unidad lo informa. También muestra tu KH objetivo, la concentración de tu dosis y, en una unidad con dosificación configurada, su dosis máxima por hora y cuánto suplemento de alcalinidad queda en el recipiente. Estos datos vienen directamente de tus ajustes de AquaWiz, así que cámbialos en la app de AquaWiz. Cora no puede controlar un AquaWiz.

Debajo de las lecturas, la tarjeta dice cuándo se midió la última (por ejemplo *Medido 14:00*) y de dónde viene: **Cada hora desde tu Cora Max** o **Desde la nube de AquaWiz, cada 12 horas**. También muestra el **cambio de pH**. Al abrir la página se pide una lectura nueva, y **Leer ahora** la pide otra vez, como máximo cada 15 minutos. Si una lectura no ha cambiado, es normal: la unidad solo mide de vez en cuando.

Cuando un Cora Max lee la unidad cada hora, la tarjeta muestra también la bomba, la sonda de pH y el nivel del depósito de agua, y Cora te avisa cuando la bomba informa de un fallo, la sonda de pH ha fallado o está cerca del final de su vida, o el nivel del depósito de agua se queda bajo o alto más de una hora.

Si tu unidad sigue su recipiente, Cora te avisa cuando el suplemento se está acabando, a 100 mL por defecto. Cámbialo desde su regla en el [Centro de alertas](/help/mobile-alerts).


## Qué pasa después de cambiar algo {#what-happens-after-you-change-something}

Cada cambio queda registrado en [Actividad](/help/mobile-activity), con la superficie desde la que se hizo. Si un dispositivo no acepta un cambio, también queda registrado ahí.
