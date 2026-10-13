---
title: Controlar equipos desde Cora Max
description: Las páginas de dispositivo en Cora Max para Neptune Apex, Trident y DŌS, Red Sea ReefBeat, Jecod, AquaWiz y las marcas Beta, marca a marca.
section: Cora Max
reviewed: 2026-10-13
order: 6
group: Equipment
twin: mobile-device-control
---

Esta página explica qué puedes ver y hacer en la página de cada dispositivo en Cora Max, marca a marca. Cora Max llega a los mismos equipos que tu teléfono. Abre la página de un dispositivo desde el icono de dispositivos de la barra superior, desde **Ajustes → Dispositivos** o tocando la casilla de un dispositivo en el panel.

![La página de un Apex en Cora Max con sus botones de alimentación y sus tomas](img/max-device-control.webp "Feed A a D y Cancelar, y después las tomas, organizadas para una pantalla de pared.")

:::warning Estos controles actúan sobre equipos en funcionamiento
No hay vista previa ni deshacer. Una orden sale en cuanto tocas, pero enviarla no significa que esté hecha. Vuelve como **Confirmado**, **Sin confirmar**, **Rechazado** o **Sin cambios**, y puedes ver cuál en [Actividad](/help/max-activity).
:::

Los equipos se añaden, se asignan y se quitan en tu teléfono. Cora Max los muestra en cuanto tu cuenta los tiene. Consulta [Conectar tus equipos](/help/mobile-connections).

## Qué tiene página {#what-has-a-page}

| Dispositivo | Muestra |
|---|---|
| **Neptune Apex** | Sondas y tomas, y puedes cambiar cada toma |
| **Trident** | El estado de la prueba, los niveles de reactivo y de residuos, y un botón para empezar una prueba |
| **DŌS**, incluido el DŌS QD | La dosificación, el horario, la autonomía y el volumen del envase de cada cabezal (con pausa, llenado, dosificar ahora y una medición única de veinte segundos) |
| **Red Sea ReefBeat** | Lo que tenga la unidad: cabezales de dosificación, depósito, días de rollo, modo de las bombas, además de un editor completo del plan de ReefDose y del programa de ReefRun y los ajustes de ReefMat *(Beta)* |
| **Red Sea ReefControl**, **ReefControl Power**, **ReefWave**, **ReefLED** *(Beta)* | Las sondas de ReefControl. Los enchufes de ReefControl Power como tomas, encendidos o apagados, todavía sin modo automático. ReefWave y ReefLED, solo consulta |
| **Jecod** | El modo y la intensidad de la bomba, y su programa diario |
| **AquaWiz** | No tiene página propia. Aparece en **Dispositivos**, y sus lecturas van al panel |
| **Maxspect** *(Beta)* | El modo y la velocidad de **Gyre A** y **Gyre B**, **Salud de la bomba** (cuenta atrás de limpieza, corriente del cabezal A, cabezales instalados, firmware) y su horario, solo consulta |
| **GHL ProfiLux / Mitras** *(Beta)* | Sondas, tomas, dosificadoras, sensores de nivel y, en los modelos Director, resultados de pruebas de KH y de iones |
| **HYDROS** *(Beta)* | Lo que informe su clave de dispositivo: entradas y, con una clave de escritura, salidas, modos, cabezales de dosificación y órdenes del analizador |
| **Focustronic** *(Beta)* | Estado, última prueba, bombas y viales, además de **Medir ahora**, **Dosificar ahora** o **Probar ahora** según la unidad |
| **EcoTech** *(Beta)* | Luces Radion, bombas VorTech y dosificadoras Versa, cada una con su propia página. Las órdenes a VorTech y Versa todavía no se han probado en hardware real |
| **Inkbird** *(Beta)* | Lecturas del aire de la habitación, solo lectura |
| **Cámara** *(Beta)* | Una imagen de tu cámara, como casilla en el panel o en su propia página, con la vigilancia del skimmer en los planes de pago |

:::note Beta
**Beta.** Maxspect, GHL, HYDROS, Focustronic, EcoTech, Inkbird y las cámaras están en Beta y solo están abiertos a los usuarios Beta. Si no eres usuario Beta, no los verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html). Puede que algunas lecturas o controles todavía no funcionen.
:::

La mayoría de las páginas de dispositivo tienen un lápiz para cambiar el nombre del dispositivo. El nombre nuevo también aparece en tu teléfono. Más información en [Dispositivos y estado de los dispositivos](/help/max-devices).

## Neptune Apex {#neptune-apex}

La página del Apex lista tus sondas y tomas, con tus ciclos de alimentación arriba. Cada toma cambia entre **Auto**, **Apagado** y **Encendido**, y las tomas con candado te piden que confirmes. Cómo funcionan los tres estados y el modo alimentación se explica en [Tomas y controles](/help/max-controls).

También puedes llegar a las tomas desde el cajón **Tomas y alimentación** de la parte de abajo del panel. Lista las tomas activadas para este panel (o todas, si no has elegido ninguna).

Un Apex grande con varios módulos muestra todas sus tomas y sondas. Los cabezales DŌS nunca aparecen en la lista de tomas, así que no puedes encender uno ahí y dejarlo funcionando. Dosifica desde la página del propio cabezal.

### Trident {#trident}

La página del Trident muestra el estado de la prueba y los niveles de reactivo y de residuos. Desde aquí puedes empezar una prueba, y fijar una alerta de reposición con **Configuración de alertas**.

## Cabezales DŌS {#dos-heads}

Tienes que medir un cabezal DŌS una vez antes de que Cora dosifique con él a mano. **Medir para dosificar** hace funcionar el cabezal veinte segundos dentro de un recipiente medidor, y tú introduces cuánto salió. Cora guarda una medición por cabezal y usa la más reciente, la haya tomado el Cora Max que sea. La página del cabezal muestra dónde y cuándo se midió.

Después de una dosis manual, un cabezal que tenías en Off en Apex Fusion se queda en Off. Cualquier otro cabezal vuelve a Auto.

Un DŌS no tiene sensor de nivel y sigue dosificando con el envase vacío. Fija una alerta de reposición con **Configuración de alertas** en la página del DŌS. Más información en [Alertas de dosificadores](/help/mobile-device-control#doser-alerts).

### Para qué se usa un cabezal {#what-a-head-is-used-for}

En la hoja de ajustes de un cabezal puedes fijar su **tipo de uso**. Las opciones son **Suplemento**, **Cambio de agua: entrada de agua salada nueva**, **Cambio de agua: salida de agua vieja**, **Agua de kalk**, **Reactor de calcio**, **Alimento** o **Relleno**, y **Otro**. El tipo de uso cambia dos cosas.

- El tamaño del envase que puede seguir. Todos los tipos de uso pueden seguir un envase de hasta 1.000 litros. Por encima del contador propio del Apex de 150 litros, Cora sigue el volumen por su cuenta, y restablece el contador del Apex cada 100 litros.
- Si puede dar una dosis grande a mano. Los cabezales de Suplemento y Alimento mantienen el tope actual, pequeño y prudente. Todos los demás tipos de uso pueden tener su propio límite de **Dosis manual más grande**, hasta un tope máximo de 10 litros, y su propio **Límite diario para automatizaciones y el asistente**. Una dosis manual grande también necesita **Dosis grandes (Beta)** activado en los ajustes del cabezal, que viene desactivado. Actívalo solo después de haber visto la primera dosis grande en el acuario.

Puedes vincular una pareja de cambio de agua (entrada de agua salada nueva, salida de agua vieja) como **Cabezal emparejado** y fijar una cantidad en **Aviso de balance por encima de**. Si los totales del día de los dos cabezales se separan más que eso, Cora te avisa. Una pareja desequilibrada suele significar que uno de los lados no bombea como debería.

### Si se interrumpe una dosis grande {#if-a-large-dose-is-interrupted}

Una dosis grande cambia durante un rato lo que hace el cabezal en el Apex, y después vuelve a poner su horario normal. Si la conexión se corta a medias, Cora Max muestra un aviso en la página de ese cabezal: *"Una dosis grande en [cabezal] no terminó correctamente. Cora sigue intentando restaurar su programa; revísalo en Apex Fusion."*

Revisa tú el cabezal en Apex Fusion, y después toca **Ya revisé el cabezal en Fusion** para quitar el aviso. Hazlo solo cuando hayas confirmado que está funcionando el horario propio del cabezal, no el programa de dosificación de Cora.

Si el aviso no desaparece, o vuelve una y otra vez, echa un vistazo a [Solución de problemas](/help/troubleshooting).

## Red Sea ReefBeat {#red-sea}

Cada unidad Red Sea tiene una página adaptada a lo que hace: los cabezales y envases de ReefDose, el depósito de ReefATO+, los días de rollo de ReefMat y las velocidades de las bombas ReefRun. Las alertas de suministro de los cabezales ReefDose, el depósito de ReefATO+ y el rollo de ReefMat se fijan con **Configuración de alertas** en la página de la unidad.

Si una unidad Red Sea se detiene sola, su página te dice qué pasa y pone la solución justo al lado. Es **Reanudar**, **Borrar emergencia**, **Sensor limpiado**, **Ya cargué un rollo nuevo** o **Restablecer** para un cabezal de dosificación.

Un plan de ReefDose, un programa de velocidad de ReefRun y el avance programado, el modelo, la posición y el rollo nuevo de ReefMat funcionan aquí igual que en tu teléfono. [Controlar tus equipos](/help/mobile-device-control) tiene los detalles.

ReefControl, ReefControl Power, ReefWave y ReefLED llevan *(Beta)* en su nombre pero están abiertos a todos. ReefControl muestra sus sondas. Los enchufes de ReefControl Power aparecen como tomas, solo encendidos o apagados. ReefWave y ReefLED son solo de consulta, de momento.

## Jecod {#jecod}

La página de Jecod muestra el modo y la intensidad de la bomba, y puedes cambiar los dos.

Puedes escribir programas diarios de bombas Jecod en la pantalla de pared igual que en tu teléfono. El editor es el mismo, con un gráfico del día, una lista de periodos y una fila de acciones. Más información en [Programar equipos](/help/mobile-schedules).

## AquaWiz {#aquawiz}

Un AquaWiz KH Controller no tiene página propia en Cora Max. Aparece en **Dispositivos**, donde puedes cambiarle el nombre, y sus lecturas salen en el panel como cualquier otra fuente. Configúralo y gestiónalo en tu teléfono, consulta [Conectar tus equipos](/help/mobile-connections).

## Maxspect {#maxspect}

:::note Beta
**Beta.** Maxspect está en Beta y solo está abierto a los usuarios Beta. Si no eres usuario Beta, no lo verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html). Puede que algunas lecturas o controles todavía no funcionen.
:::

La página de Maxspect muestra el modo y la velocidad de **Gyre A** y **Gyre B** y su **Salud de la bomba**. Aquí puedes ver el horario de un gyre, pero no guardarlo. Configúralo en la app de Maxspect.

## GHL ProfiLux y Mitras {#ghl}

:::note Beta
**Beta.** GHL está en Beta y solo está abierto a los usuarios Beta. Si no eres usuario Beta, no lo verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html). Puede que algunas lecturas o controles todavía no funcionen.
:::

Conecta un controlador GHL desde tu teléfono: **Dispositivos → Agregar dispositivo → GHL**. [Conectar tus equipos](/help/mobile-connections) tiene los pasos. Cora Max lo muestra y lo controla en cuanto un Cora Max de su red lo ha leído, pero la configuración se hace en el teléfono.

Un ProfiLux mini lee sus sondas, tomas, dosificadoras y sensores de nivel. Con **Permitir el control desde Cora (Beta)** activado, un mini también puede encender y apagar sus tomas, igual que cualquier otro controlador GHL. Todo lo demás, como los valores de consigna y la pausa de alimentación, necesita un ProfiLux 3, 4 o Mitras.

Los controles siguen desactivados hasta que activas **Permitir el control desde Cora (Beta)** en la página del dispositivo. Viene desactivado. Cuando está activado, una toma se puede poner en **Siempre encendido**, **Siempre apagado** o **Volver a automático**, y un valor de consigna como la temperatura o el pH muestra su rango permitido y rechaza un valor fuera de él. Los dos tipos de cambio se guardan en el propio controlador y se quedan ahí aunque Cora pierda después el contacto con él. Un cambio que parece afectar a un calentador o a una bomba de retorno te pide que confirmes dos veces.

Si el envase de una dosificadora se está acabando, Cora te avisa igual que con otros consumibles. El valor predeterminado es el 20 % de llenado, y puedes cambiarlo desde la regla de la dosificadora en el [Centro de alertas](/help/mobile-alerts).

Si el controlador no acepta un cambio, probablemente su API de GHL está desactivada. GHL la desactiva después de cada actualización de firmware. Vuelve a activarla desde **System → GHL API** en GHL Control Center o GHL Connect. [Solución de problemas](/help/troubleshooting) tiene el resto.

## HYDROS {#hydros}

:::note Beta
**Beta.** HYDROS está en Beta y solo está abierto a los usuarios Beta. Si no eres usuario Beta, no lo verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html). Puede que algunas lecturas o controles todavía no funcionen.
:::

HYDROS llega a su controlador a través de la nube de HYDROS, así que funciona aunque Cora Max esté en otra red que el controlador. Solo se configura desde tu teléfono: **Dispositivos → Agregar dispositivo → HYDROS**. [Conectar tus equipos](/help/mobile-connections) tiene los pasos.

Leerlo y controlarlo funciona igual que en tu teléfono. Consulta [Controlar tus equipos](/help/mobile-device-control) para las salidas, los modos, los cabezales de dosificación y las órdenes del analizador, y para los límites de dosis por cabezal.

## Focustronic {#focustronic}

:::note Beta
**Beta.** Focustronic está en Beta y solo está abierto a los usuarios Beta. Si no eres usuario Beta, no lo verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html). Puede que algunas lecturas o controles todavía no funcionen.
:::

La página de Focustronic muestra el estado de la unidad, su última prueba y sus bombas y viales. En **Controles**:

- Un Alkatronic tiene **Medir ahora**.
- Un Dosetronic tiene **Dosificar ahora** para cada bomba. Escribe la cantidad, hasta 500 mL de una vez, toca **Revisar** y confirma. Una dosis no se puede deshacer, y Cora nunca la reintenta.
- Un Mastertronic tiene un perfil de prueba para elegir y **Probar ahora**.

Estas órdenes pasan por los servidores de Focustronic, que Cora no controla. Configura la unidad en tu teléfono, consulta [Conectar tus equipos](/help/mobile-connections).

## EcoTech, Inkbird y cámaras {#ecotech-inkbird-and-cameras}

:::note Beta
**Beta.** EcoTech, Inkbird y las cámaras están en Beta y solo están abiertos a los usuarios Beta. Si no eres usuario Beta, no los verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html).
:::

Se vinculan desde tu teléfono, y un Cora Max del acuario hace la lectura.

### EcoTech {#ecotech}

Las luces Radion, las bombas VorTech y las dosificadoras Versa tienen cada una su propia página, con un botón **Configuración de alertas** para sus suministros. [Luces, bombas y dosificadoras EcoTech](/help/mobile-ecotech) tiene los detalles.

### Inkbird {#inkbird}

Un monitor de aire de habitación Inkbird muestra sus lecturas y nada más.

### Cámaras y vigilancia del skimmer {#cameras}

Para mostrar una cámara en la pared, añade una casilla **Cámara** en el [editor del panel](/help/max-dashboard-editing). Toca la casilla para abrir la cámara a pantalla completa. Sus botones desaparecen a los pocos segundos, y un toque los hace volver.

Con la vigilancia del skimmer activada (planes de pago), la casilla de la cámara y la vista a pantalla completa muestran el nivel del vaso y su antigüedad, por ejemplo *Vaso 42 % · hace 5 min*. Se pone ámbar a 10 puntos de tu nivel de alerta y roja al alcanzarlo. En la cámara a pantalla completa, **Aviso al 80 %** (o tu nivel) abre **Aviso del vaso del skimmer**, donde fijas el nivel. Recibes una notificación cuando el vaso lo alcanza.

Cómo configurar una cámara y la vigilancia del skimmer se explica en [Cámaras y vigilancia del skimmer](/help/mobile-cameras).

## Consumibles {#consumables}

Los umbrales de reposición (reactivo, envases, depósitos) se fijan aquí en la propia página del dispositivo, igual que en tu teléfono. Más información en [Consumibles](/help/mobile-consumables).

## Anotar y calcular junto al acuario {#logging-and-calculating-at-the-tank}

Hay dos cosas que a menudo son más fáciles en la pantalla de pared que en un teléfono.

- **Registrar parámetros** te deja escribir resultados de pruebas con el teclado en pantalla. Está en el menú del acuario.
- **Calculadora de dosis** calcula una corrección a partir del volumen del acuario y la concentración de tus productos. Ábrela desde la página de un parámetro. Usa el mismo volumen y las mismas concentraciones que tu teléfono, así que una dosis calculada aquí coincide con una calculada allí. Más información en [Dosificación](/help/mobile-dosing).

## En un segundo Cora Max {#on-a-second-cora-max}

Cuando más de un Cora Max muestra un acuario, uno de ellos lee los equipos de ese acuario. Las páginas de dispositivo lo llaman el Cora Max del acuario. Los demás también pueden abrir las páginas de dispositivo, y una etiqueta de estado que dice **Nube** significa que estás en uno de ellos. Muestran lo que leyó por última vez el Cora Max del acuario y hace cuánto. Cada orden pasa por Cora Cloud hasta el Cora Max del acuario, que la ejecuta.

Algunas cosas solo funcionan en el Cora Max del acuario.

- **Medir para dosificar** y **Volver a medir** solo aparecen ahí. Cuando un cabezal está medido, **Dosificar ahora** funciona desde cualquier Cora Max.
- Puedes cambiar un horario de Jecod desde otro Cora Max solo si el Cora Max del acuario ha leído la bomba en la última hora, y nunca en una bomba que solo se comunica por Bluetooth. Un **Aplicar a la bomba** desde ahí envía como mucho 12 cambios, así que envía una edición más grande por partes.

## Qué se cambió, y qué lo cambió {#what-was-changed-and-by-what}

Cada acción queda registrada junto con lo que la provocó. Más información en [Actividad en Cora Max](/help/max-activity).
