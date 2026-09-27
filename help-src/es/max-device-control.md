---
title: Controlar equipos desde Cora Max
description: Las páginas de dispositivo en la pantalla grande: sondas, tomas, cabezales de dosificación, analizadores y bombas.
section: Cora Max
reviewed: 2026-09-27
order: 6
group: Equipment
---

Cora Max llega a los mismos equipos que tu teléfono, con una página para cada dispositivo. Ábrelas desde **Ajustes → Dispositivos** o tocando la casilla de un dispositivo en el panel.

![Una página de Apex en Cora Max](img/max-device-control.webp "Los ciclos de alimentación y todas las tomas, colocados para una pantalla de pared.")

:::warning Estos controles actúan sobre equipos en marcha
No hay vista previa ni forma de deshacer. La orden sale en cuanto tocas, pero que se haya *enviado* no quiere decir que esté *hecha*. Vuelve como **Confirmado**, **Sin confirmar**, **Rechazado** o **Sin cambios**, y en [Actividad](/help/max-activity) ves cuál fue.
:::

## Qué dispositivos tienen página

| Dispositivo | Qué muestra |
|---|---|
| **Neptune Apex** | Sondas y tomas. Puedes cambiar cada toma |
| **Trident** | Estado de la prueba, niveles de reactivo y de residuos, y un botón para iniciar una prueba |
| **DŌS**, también el DŌS QD | Para cada cabezal, la dosificación, el programa, la autonomía y el volumen del envase (con pausar, rellenar, dosificar ahora y una medición única de veinte segundos) |
| **Red Sea ReefBeat** | Lo que tenga la unidad: cabezales de dosificación, depósito, días de rollo, modo de bomba |
| **Jecod** | Modo e intensidad de la bomba y su programa diario |
| **Maxspect** *(beta)* | Modo y velocidad de **Gyre A** y **Gyre B**, **Salud de la bomba** (cuenta atrás de limpieza, corriente del cabezal A, cabezales instalados, firmware) y su horario, solo para consulta |

Si una unidad Red Sea se detiene sola, su página te dice qué pasa y pone al lado el botón para arreglarlo: **Reanudar**, **Borrar emergencia**, **Sensor limpiado**, **Ya cargué un rollo nuevo** o, en un cabezal de dosificación, **Restablecer**.

## Cabezales DŌS

Antes de que Cora dosifique a mano con un cabezal DŌS, hay que medirlo una vez. **Medir para dosificar** hace funcionar el cabezal veinte segundos sobre un recipiente de medida, y tú anotas cuánto ha salido. Cora guarda una medición por cabezal y usa la más reciente, la haya hecho el Cora Max que sea. La página del cabezal indica dónde y cuándo se midió.

Después de una dosis manual, si el cabezal estaba en Apagado en Apex Fusion, se queda en Apagado. Los demás vuelven a Auto.

### Para qué usas cada cabezal

En la hoja de ajustes de cada cabezal puedes elegir un **tipo de uso**: **Suplemento**, **Cambio de agua: entrada de agua salada nueva**, **Cambio de agua: salida de agua vieja**, **Agua de kalk**, **Reactor de calcio**, **Alimento** o **Relleno**, u **Otro**. El tipo de uso cambia dos cosas:

- **El tamaño del envase que puede controlar.** Un cabezal de Suplemento controla hasta 20 litros. Con cualquier otro tipo de uso puede controlar un envase mucho mayor, de hasta 500 litros. Así, un cabezal que hace un cambio de agua o alimenta un reactor de calcio no se trata como una botellita de dosificación.
- **Si admite una dosis manual grande.** Los cabezales de Suplemento y Alimento mantienen el límite bajo y prudente de siempre. Con los demás tipos de uso puedes fijar tu propia **Dosis manual más grande**, hasta un máximo fijo de 10 litros, y tu propio **Límite diario para automatizaciones y el asistente**.

Los dos cabezales de un cambio de agua (entrada de agua salada nueva y salida de agua vieja) se pueden unir como **Cabezal emparejado**, con un valor de **Aviso de balance por encima de**. Si los totales del día de los dos cabezales se separan más de esa cantidad, Cora te avisa. Cuando una pareja se desequilibra, lo normal es que uno de los dos no esté bombeando como debe.

### Si se corta una dosis grande

Durante una dosis grande, Cora cambia por un rato lo que hace el cabezal en el Apex y después le devuelve su programa normal. Si la conexión se corta a mitad, Cora Max muestra un aviso en la página de ese cabezal: *"Una dosis grande en [cabezal] no terminó correctamente. Cora sigue intentando devolver su programa; revísalo en Apex Fusion."*

Revisa tú el cabezal en Apex Fusion y luego toca **Ya revisé el cabezal en Fusion** para quitar el aviso. Hazlo solo cuando hayas comprobado que lo que está funcionando es el horario propio del cabezal y no el programa de dosificación de Cora.

Si el aviso no se quita o vuelve a salir, consulta [Solución de problemas](/help/troubleshooting).

## Horarios

Los programas diarios de las bombas Jecod se pueden crear en la pantalla de pared igual que en el teléfono. El editor es el mismo: un gráfico del día, una lista de periodos y una fila de acciones. Lo tienes explicado en [Programar equipos](/help/mobile-schedules).

El horario de un gyre Maxspect *(beta)* se puede ver aquí, pero no guardar. Configúralo en la app de Maxspect.

## Tomas

Las tomas también están en el cajón **Tomas y alimentación**, en la parte inferior del panel. Ahí ves juntas las tomas activadas para este panel (o todas, si no has elegido ninguna). Consulta [Tomas y controles](/help/max-controls).

Los cabezales DŌS nunca aparecen en la lista de tomas, así que no se pueden encender desde ahí y quedarse en marcha. Para dosificar, usa la página del cabezal. Un Apex grande con varios módulos muestra todas sus tomas y sondas.

## Consumibles

Los umbrales de reposición (reactivo, envases, depósitos) se ajustan aquí desde la página de cada dispositivo, igual que en el teléfono. Consulta [Consumibles](/help/mobile-consumables).

## Anotar y calcular junto al acuario

Hay dos cosas que suelen ser más cómodas en la pantalla de pared que en el teléfono:

- **Registrar parámetros**: anota los resultados de tus pruebas con el teclado en pantalla, desde el menú del acuario
- **Calculadora de dosis**: calcula una corrección con el volumen del acuario y la concentración de tus productos, desde la página de un parámetro. Usa el mismo volumen y las mismas concentraciones que el teléfono, así que la dosis que calcules aquí coincide con la de allí. Más información en [Dosificación](/help/mobile-dosing).

## En un segundo Cora Max

Cuando un acuario aparece en más de un Cora Max, solo uno de ellos lee los equipos de ese acuario. Las páginas de dispositivo lo llaman el Cora Max del acuario. Los demás también pueden abrir las páginas de dispositivo (si ves una etiqueta de estado que dice **Nube**, esta pantalla es una de ellas). Muestran lo último que leyó el Cora Max del acuario y hace cuánto, y envían cada orden a través de Cora Cloud a ese Cora Max para que la ejecute.

Algunas cosas solo se pueden hacer en el Cora Max del acuario:

- **Medir para dosificar** y **Volver a medir** solo aparecen allí. Cuando un cabezal ya está medido, **Dosificar ahora** funciona desde cualquier Cora Max.
- Desde otro Cora Max solo puedes cambiar un horario Jecod si el Cora Max del acuario ha leído la bomba en la última hora, y nunca si la bomba solo se comunica por Bluetooth. Cada **Aplicar a la bomba** desde ahí envía como mucho 12 cambios, así que divide los cambios grandes en varias partes.

## Qué cambió y por qué

Cada acción queda registrada con su causa. Puedes verlo en [Actividad y línea de tiempo](/help/mobile-activity).
