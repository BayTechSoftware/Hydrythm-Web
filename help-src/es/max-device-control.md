---
title: Controlar equipos desde Cora Max
description: Páginas de dispositivo en la pantalla grande: sondas, tomas, cabezales de dosificación, equipos de análisis y bombas.
section: Cora Max
reviewed: 2026-09-27
order: 6
group: Equipment
---

Cora Max llega al mismo equipo que tu teléfono, con una página por dispositivo. Ábrelas desde **Ajustes → Dispositivos**, o tocando la casilla de un dispositivo en el panel.

![Una página de Apex en Cora Max](img/max-device-control.webp "Ciclos de alimentación y cada toma, organizados para una pantalla de pared.")

:::warning Estos controles actúan sobre equipo en vivo
No hay vista previa ni deshacer. Una orden sale en el momento en que tocas, pero *enviado* no es *hecho*: vuelve como **Confirmado**, **Sin confirmar**, **Rechazado** o **Sin cambios**, y [Actividad](/help/max-activity) es donde ves cuál fue.
:::

## Qué tiene una página

| Dispositivo | Muestra |
|---|---|
| **Neptune Apex** | Sondas y tomas, con cada toma conmutable |
| **Trident** | Estado de la prueba, niveles de reactivo y residuos, y la posibilidad de iniciar una prueba |
| **DŌS**, incluido el DŌS QD | La dosificación, el programa, la autonomía y el volumen del envase de cada cabezal (con pausar, rellenar, dosificar ahora y una medición única de veinte segundos) |
| **Red Sea ReefBeat** | Lo que sea la unidad: cabezales de dosificación, depósito, días de rodillo, modo de bomba |
| **Jecod** | Modo e intensidad de la bomba, y su programa diario |
| **Maxspect** *(beta)* | Modo y velocidad para **Gyre A** y **Gyre B**, **Salud de la bomba** (cuenta atrás de limpieza, corriente del cabezal A, cabezales instalados, firmware), y su horario, solo lectura |

Si una unidad Red Sea se detiene sola, su página indica qué está mal y pone la solución al lado: **Reanudar**, **Borrar emergencia**, **Sensor limpiado**, **Ya cargué un rollo nuevo**, o **Restablecer** para un cabezal de dosificación.

## Cabezales DŌS

Un cabezal DŌS tiene que medirse una vez antes de que Cora lo dosifique a mano. **Medir para dosificar** ejecuta el cabezal durante veinte segundos en un envase de medición, y tú introduces cuánto salió. Cora guarda una medición por cabezal y usa la más reciente, sea el Cora Max que la haya tomado; la página del cabezal muestra dónde y cuándo se midió.

Después de una dosis manual, un cabezal que habías puesto en Apagado en Apex Fusion se queda en Apagado. Cualquier otro cabezal vuelve a Auto.

### Para qué se usa un cabezal

Cada cabezal se puede fijar en un **tipo de uso**, desde su hoja de ajustes: **Suplemento**, **Cambio de agua: entrada de agua salada nueva**, **Cambio de agua: salida de agua vieja**, **Agua de kalk**, **Reactor de calcio**, **Alimento** o **Relleno**, u **Otro**. El tipo de uso cambia dos cosas:

- **Cuán grande puede ser el envase que hace seguimiento.** Un cabezal de Suplemento hace seguimiento hasta 20 litros; cualquier otro tipo de uso puede hacer seguimiento de un envase mucho mayor, hasta 500 litros, así que un cabezal que ejecuta un cambio de agua o un reactor de calcio no se trata como si fuera una botella de dosificación pequeña.
- **Si puede recibir una dosis grande a mano.** Los cabezales de Suplemento y Alimento mantienen el límite pequeño y cuidadoso actual. Cualquier otro tipo de uso puede tener su propio límite de **Dosis manual más grande**, hasta un techo fijo de 10 litros, y su propio **límite diario para automatizaciones y el asistente**.

Un par de cambio de agua (entrada de agua salada nueva, salida de agua vieja) se puede vincular como **Cabezal emparejado**, con una cantidad de **Aviso de balance por encima de**: si los totales del día de los dos cabezales se separan más de esa cantidad, Cora te avisa, ya que un par desequilibrado suele significar que un lado no está bombeando como se espera.

### Si una dosis grande se interrumpe

Una dosis grande cambia temporalmente lo que está haciendo el cabezal en el Apex, y luego devuelve su programa normal después. Si la conexión se corta a mitad de camino, Cora Max muestra un aviso en la página de ese cabezal: *"Una dosis grande en [cabezal] no terminó correctamente. Cora sigue intentando devolver su programa; revísalo en Apex Fusion."*

Revisa el cabezal en Apex Fusion tú mismo, y luego toca **Ya revisé el cabezal en Fusion** para cerrar el aviso. Haz esto solo después de confirmar que el propio horario del cabezal, no el programa de dosificación de Cora, es lo que realmente se está ejecutando.

**Si no funciona:** si el aviso no se cierra, o sigue volviendo, consulta [Solución de problemas](/help/troubleshooting).

## Horarios

Los programas diarios de bombas Jecod se pueden crear en la pared igual que en el teléfono. El editor es el mismo: un gráfico del día, una lista de periodos y una fila de acciones. Consulta [Programar equipos](/help/mobile-schedules).

El horario de un gyre Maxspect *(beta)* se puede consultar aquí pero no guardar. Fíjalo en la aplicación Maxspect.

## Tomas

Las tomas también son accesibles desde el cajón **Tomas y alimentación** en la parte inferior del panel, que lista en un solo lugar las tomas habilitadas para este panel (todas, si no se ha elegido ninguna). Consulta [Tomas y controles](/help/max-controls).

Los cabezales DŌS nunca aparecen en la lista de tomas, así que un cabezal no se puede encender ahí y dejar en marcha; dosifica desde su propia página. Un Apex grande con varios módulos muestra todas sus tomas y sondas.

## Consumibles

Los umbrales de reposición (reactivo, envases, depósitos) se fijan desde la propia página del dispositivo aquí, exactamente igual que en el teléfono. Consulta [Consumibles](/help/mobile-consumables).

## Registrar y calcular junto al acuario

Dos cosas suelen ser más prácticas en la pared que en un teléfono:

- **Registrar parámetros**: introduce resultados de pruebas en el teclado en pantalla, desde el menú del acuario
- **Calculadora de dosis**: calcula una corrección usando el volumen del acuario y las concentraciones de tus productos, desde la página de un parámetro. Usa el mismo volumen y las mismas concentraciones de producto que el teléfono, así que una dosis calculada aquí coincide con una calculada allí. Consulta [Dosificación](/help/mobile-dosing).

## En un segundo Cora Max

Cuando más de un Cora Max muestra un acuario, uno de ellos lee el equipo de ese acuario; las páginas de dispositivo lo llaman el Cora Max del acuario. Los demás igualmente abren las páginas de dispositivo (una píldora de estado que dice **Nube** significa que esta pantalla es uno de ellos). Muestran lo que el Cora Max del acuario leyó por última vez, y cuánto hace, y pasan cada orden a través de Cora Cloud a ese Cora Max para que la lleve a cabo.

Algunas cosas se quedan con el Cora Max del acuario:

- **Medir para dosificar** y **Volver a medir** aparecen solo ahí. Una vez medido un cabezal, **Dosificar ahora** funciona desde cualquier Cora Max.
- Un horario Jecod solo se puede cambiar desde otro Cora Max si el Cora Max del acuario ha leído la bomba en la última hora, y nunca para una bomba que solo habla por Bluetooth. Un **Aplicar a la bomba** desde ahí envía como máximo 12 cambios, así que envía una edición mayor en partes.

## Qué se cambió, y con qué

Cada acción se registra con su causa. Consulta [Actividad y línea de tiempo](/help/mobile-activity).
