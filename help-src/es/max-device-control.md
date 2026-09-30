---
title: Controlar equipos desde Cora Max
description: Las páginas de dispositivo en la pantalla grande: sondas, tomas, cabezales de dosificación, analizadores y bombas.
section: Cora Max
reviewed: 2026-09-30
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
| **Red Sea ReefBeat** | Lo que tenga la unidad: cabezales de dosificación, depósito, días de rollo, modo de bomba, más el editor completo de plan ReefDose y programa ReefRun y los ajustes de ReefMat *(beta)* |
| **ReefControl**, **ReefControl Power**, **ReefWave**, **ReefLED** *(beta)* | Las sondas de ReefControl. Las tomas de ReefControl Power como tomas, encendido o apagado, todavía sin modo automático. ReefWave y ReefLED, solo para consultar |
| **Jecod** | Modo e intensidad de la bomba y su programa diario |
| **Maxspect** *(beta)* | Modo y velocidad de **Gyre A** y **Gyre B**, **Salud de la bomba** (cuenta atrás de limpieza, corriente del cabezal A, cabezales instalados, firmware) y su horario, solo para consulta |
| **GHL ProfiLux / Mitras** *(beta)* | Sondas, tomas, dosificadoras, sensores de nivel y, en los modelos Director, resultados de las pruebas de KH e iones |
| **HYDROS** *(beta)* | Lo que informe su clave de dispositivo: entradas, y con una clave de escritura, salidas, modos, cabezales de dosificación y órdenes de analizador |

Si una unidad Red Sea se detiene sola, su página te dice qué pasa y pone al lado el botón para arreglarlo: **Reanudar**, **Borrar emergencia**, **Sensor limpiado**, **Ya cargué un rollo nuevo** o, en un cabezal de dosificación, **Restablecer**.

Un plan de ReefDose, un programa de velocidad de ReefRun y el avance programado, el modelo, la posición y el Nuevo rollo de ReefMat funcionan aquí igual que en tu teléfono. [Conectar tus equipos](/help/mobile-connections) y [Controlar tus equipos](/help/mobile-device-control) tienen el detalle.

## Cabezales DŌS

Antes de que Cora dosifique a mano con un cabezal DŌS, hay que medirlo una vez. **Medir para dosificar** hace funcionar el cabezal veinte segundos sobre un recipiente de medida, y tú anotas cuánto ha salido. Cora guarda una medición por cabezal y usa la más reciente, la haya hecho el Cora Max que sea. La página del cabezal indica dónde y cuándo se midió.

Después de una dosis manual, si el cabezal estaba en Apagado en Apex Fusion, se queda en Apagado. Los demás vuelven a Auto.

### Para qué usas cada cabezal

En la hoja de ajustes de cada cabezal puedes elegir un **tipo de uso**: **Suplemento**, **Cambio de agua: entrada de agua salada nueva**, **Cambio de agua: salida de agua vieja**, **Agua de kalk**, **Reactor de calcio**, **Alimento** o **Relleno**, u **Otro**. El tipo de uso cambia dos cosas:

- **El tamaño del envase que puede controlar.** Un cabezal de Suplemento controla hasta 20 litros. Con cualquier otro tipo de uso puede controlar un envase mucho mayor, de hasta 500 litros. Así, un cabezal que hace un cambio de agua o alimenta un reactor de calcio no se trata como una botellita de dosificación.
- **Si admite una dosis manual grande.** Los cabezales de Suplemento y Alimento mantienen el límite bajo y prudente de siempre. Con los demás tipos de uso puedes fijar tu propia **Dosis manual más grande**, hasta un máximo fijo de 10 litros, y tu propio **Límite diario para automatizaciones y el asistente**. Una dosis manual grande también necesita **Dosis grandes (Beta)** activado en los ajustes del cabezal, desactivado por defecto: actívalo solo después de haber observado cómo se ejecuta la primera dosis grande junto al acuario.

Los dos cabezales de un cambio de agua (entrada de agua salada nueva y salida de agua vieja) se pueden unir como **Cabezal emparejado**, con un valor de **Aviso de balance por encima de**. Si los totales del día de los dos cabezales se separan más de esa cantidad, Cora te avisa. Cuando una pareja se desequilibra, lo normal es que uno de los dos no esté bombeando como debe.

### Si se corta una dosis grande

Durante una dosis grande, Cora cambia por un rato lo que hace el cabezal en el Apex y después le devuelve su programa normal. Si la conexión se corta a mitad, Cora Max muestra un aviso en la página de ese cabezal: *"Una dosis grande en [cabezal] no terminó correctamente. Cora sigue intentando devolver su programa; revísalo en Apex Fusion."*

Revisa tú el cabezal en Apex Fusion y luego toca **Ya revisé el cabezal en Fusion** para quitar el aviso. Hazlo solo cuando hayas comprobado que lo que está funcionando es el horario propio del cabezal y no el programa de dosificación de Cora.

Si el aviso no se quita o vuelve a salir, consulta [Solución de problemas](/help/troubleshooting).

## GHL ProfiLux y Mitras

:::note GHL está en beta
Seguimos probando y desarrollando el soporte para GHL. Algunas lecturas o controles pueden no funcionar todavía, y lo que ves aquí puede cambiar con las actualizaciones.
:::

Conecta un controlador GHL desde **Ajustes → [tu acuario] → Controlador GHL (Beta)**. Escribe su dirección IP en tu red y toca **Detectar**. Cora prueba primero la API oficial del controlador y después sus otras interfaces, y te dice cuál encontró.

Si no responde nada y el controlador es un ProfiLux mini, Cora ofrece una alternativa: escribe su usuario y contraseña, y Cora lee sus sondas, tomas, dosificadoras y sensores de nivel. Con **Permitir el control desde Cora (Beta)** activado, un mini también puede cambiar sus tomas, igual que cualquier otro controlador GHL. Todo lo demás, como las consignas y la pausa de alimentación, necesita un ProfiLux 3, 4 o Mitras.

Los controles quedan desactivados hasta que activas **Permitir el control desde Cora (Beta)** en la página del dispositivo. Está desactivado por defecto. Una vez activado, una toma se puede poner en **Siempre encendido**, **Siempre apagado** o **Volver a automatico**, y una consigna, como la de temperatura o pH, muestra su rango permitido y rechaza un valor fuera de él. Los dos tipos de cambio se guardan en el propio controlador y siguen ahí aunque Cora pierda después el contacto con él. Un cambio que parezca afectar a un calentador o a una bomba de retorno te pide confirmar dos veces.

Si el recipiente de una dosificadora se está agotando, Cora te avisa igual que con otros consumibles. El valor predeterminado es el 20 % lleno, y puedes cambiarlo desde la regla de la dosificadora en el [Centro de alertas](/help/mobile-alerts).

Si el controlador no acepta un cambio, probablemente su API de GHL está desactivada. GHL la desactiva después de cada actualización de firmware; vuelve a activarla desde **System → GHL API** en GHL Control Center o GHL Connect. [Solución de problemas](/help/troubleshooting) tiene el resto.

## HYDROS

:::note HYDROS está en beta
Seguimos probando y desarrollando el soporte para HYDROS. Algunas lecturas o controles pueden no funcionar todavía, y lo que ves aquí puede cambiar con las actualizaciones.
:::

HYDROS es la única integración que llega a su controlador a través de la nube, así que funciona incluso cuando Cora Max está en una red distinta a la del controlador. Conéctalo desde **Ajustes → [tu acuario] → HYDROS (Beta)**.

En la aplicación HYDROS, crea una clave de dispositivo para el proveedor **cora-iq**, eligiendo **Read** solo para lecturas o **Write** para controlarlo también. Pega la clave, toca **Validar**, elige el acuario y luego **Guardar**. Se importan los últimos 33 días de su historial en cuanto queda conectado.

Leerlo y controlarlo funciona igual que en tu teléfono; consulta [Controlar tus equipos](/help/mobile-device-control) para las salidas, los modos, los cabezales de dosificación y las órdenes de analizador, y para los límites de dosis por cabezal.

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
