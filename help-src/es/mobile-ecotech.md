---
title: Luces, bombas y dosificadoras EcoTech
description: Vincula luces EcoTech Radion, bombas VorTech y dosificadoras Versa a Cora por Bluetooth, y mira qué puedes hacer con ellas.
section: Cora Mobile
reviewed: 2026-10-13
order: 18
group: Equipment
---

:::note Beta
**Beta.** EcoTech está en Beta y solo está abierto a los usuarios Beta. Si no eres usuario Beta, no lo verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html).
:::

Usa esta página para vincular luces EcoTech Radion, bombas VorTech y dosificadoras Versa a Cora y controlarlas. Empieza en **Dispositivos → Agregar dispositivo → EcoTech**. La misma fila también encuentra los dispositivos AquaIllumination, NYOS Quantum, Nero y Orbit que están en la misma red Bluetooth.

## Qué necesitas {#what-you-need}

- Un Cora Max en el acuario. Es quien hace la lectura y envía tus órdenes al equipo por Bluetooth. Sin uno, la fila **EcoTech** muestra **Requiere Cora Max** y se queda en gris.
- El Bluetooth del teléfono activado, con permiso de Bluetooth para Cora. Cora lo pide cuando buscas.
- Equipos encendidos y al alcance del Cora Max.

## Vincularlo {#linking-it}

1. Ve a **Dispositivos → Agregar dispositivo → EcoTech**.
2. Cora busca luces, bombas y dosificadoras cercanas. Las luces que ya están conectadas a la app Mobius de EcoTech pueden no aparecer.
3. Los equipos de la misma red Bluetooth se agrupan como un único **Acuario Mobius**. Toca **Vincular a…** y elige el acuario de Cora al que pertenece.
4. Ponle nombre al grupo cuando Cora te lo pida, y ya está vinculado.

Un dispositivo marcado como **Solo lectura** muestra sus lecturas, pero Cora todavía no puede controlarlo. El control de ese modelo llega después de probarlo.

Si la misma red Bluetooth también tiene luces de otro acuario, y los dos acuarios los leen Cora Max distintos, Cora indica **Lo lee un solo Cora Max**. En ese caso, un solo Cora Max lee toda la red para los dos acuarios.

Si no se encuentra nada, comprueba que el Bluetooth está activado y que el equipo está encendido, y toca **Buscar de nuevo**.

## Luces Radion {#radion}

![La página de una Radion en Cora Mobile](img/mobile-radion.webp "El estado, las luces de esta red (todas o una) y después la intensidad y cada canal de color.")

La página de la luz tiene un editor de horario y escenas rápidas (**Horario**, **Tormenta**, **Nubes**, **Colores**, **Alimentación**, **Apagado**). También puedes configurar la aclimatación, el ventilador, el ciclo lunar y el reloj.

En el editor de horario, **Vista previa del día** reproduce el día a gran velocidad para que lo veas sin esperar. **Detener vista previa** devuelve las luces a su estado. **Deshacer** y **Rehacer** recorren tus cambios, y **Partir de…** empieza un horario nuevo a partir de una copia de uno existente.

Cora lee las luces cada cierto tiempo. En **Ajustes de Radion**, dentro de **Lectura**, **Leer las luces cada** fija cada cuánto. Cuanto menos a menudo, más suave para las luces. Abrir la página y cada orden siguen leyendo las luces al instante.

**Ajustes de Radion** también tiene:

- **Ajustar reloj**, para poner en hora el reloj de la luz.
- **Aclimatación**, para corales nuevos: todo el horario sube poco a poco durante los días que elijas. Al activarla, vuelve a empezar desde el nivel más bajo.
- **Alertas**: **La luz deja de responder**, **Fallo: calor, ventilador o LED**, **Reloj desviado 5 min** y **Temperatura de los LED**. Activa las que quieras.

## Bombas VorTech {#vortech}

Una casilla VorTech muestra el modo y la velocidad de la bomba. Puedes cambiar el modo y la **Velocidad**, editar su horario y empezar una **Alimentación** de unos minutos. La alimentación ralentiza todas las VorTech del acuario, y vuelven a sus horarios cuando termina. Cada modo tiene una descripción corta al lado, desde un flujo constante hasta oleaje de cresta de arrecife, mareas y pulsos. Una bomba solo ofrece los modos que admite.

## Dosificadoras Versa {#versa}

La página de una Versa muestra su recipiente, sus dosis y sus límites. Puedes fijar el tamaño del recipiente, tocar **Marcar como rellenado**, hacer **Dosificar ahora**, **Pausar** la dosificación hasta medianoche y editar el horario. Cora guarda un historial de dosis de cada cabezal. La campana configura alertas de reposición por días restantes o por lo lleno que está el recipiente, como se explica en [Consumibles](/help/mobile-consumables).

:::warning Todavía no probado en hardware real
Las órdenes a las bombas VorTech y a las dosificadoras Versa todavía no se han probado en hardware real. La lectura funciona. Revisa el propio equipo las primeras veces que cambies algo, y cuéntanos qué ves desde [Informar de un problema](/help/mobile-support).
:::

## Alertas {#alerts}

Cora considera que un dispositivo EcoTech está en silencio tras tres lecturas perdidas, según su propio intervalo de lectura. Una red de solo luces se lee cada 30 minutos por defecto, así que eso tarda al menos 90 minutos. Consulta [Alertas y umbrales](/help/mobile-alerts). Las luces Radion también tienen sus propias alertas en **Ajustes de Radion**, descritas más arriba.

## En Cora Max {#on-cora-max}

El mismo equipo tiene sus propias páginas en la pantalla de pared. Más información en [Controlar equipos desde Cora Max](/help/max-device-control).
