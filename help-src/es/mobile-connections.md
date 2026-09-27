---
title: Conectar tu equipo
description: Cómo conectar equipo Neptune Apex, Red Sea ReefBeat, Jecod y AquaWiz a Cora.
section: Cora Mobile
reviewed: 2026-09-17
order: 10
group: Equipment
---

Cora funciona con el equipo que ya tienes. Esta página cubre qué es compatible y qué necesita cada conexión.

Cada marca se conecta de la forma que le va mejor, así que empieza por el punto de entrada de tu equipo:

| Marca | Empieza desde |
|---|---|
| Neptune Apex | El acuario; su perfil guarda la conexión del Apex |
| Red Sea ReefBeat | El acuario |
| Jecod / Jebao | **Dispositivos → Buscar una bomba en tu red**, o Bluetooth |
| AquaWiz | **Dispositivos → Agregar AquaWiz** |
| Maxspect *(beta)* | **Dispositivos → Buscar una bomba en tu red** |
| Cora Max | **Dispositivos → Agregar dispositivo** |

## Neptune Apex

Cora lee tu Apex a través de tu red local: sondas, tomas y cualquier módulo de expansión que tengas instalado.

**Necesitarás:** la dirección de tu Apex en tu red, y su inicio de sesión.

**Qué obtienes:** cada sonda que informa tu Apex aparece como una fuente que puedes poner en un panel. Las tomas aparecen como controles. Los módulos de expansión instalados obtienen sus propias casillas de dispositivo.

:::note Tu Apex mantiene su propia programación
Cora lee tu Apex, lo muestra junto con todo lo demás, y puede cambiar el estado de las tomas cuando lo pides. Tu propia programación sigue ejecutándose exactamente como la configuraste.
:::

## Red Sea ReefBeat

Cora habla con el equipo ReefBeat en tu red local. Las unidades compatibles son **ReefDose**, **ReefATO+**, **ReefMat** y **ReefRun**.

**Necesitarás:** el equipo ya configurado en ReefBeat y en la misma red que tu teléfono cuando lo añadas.

**Qué obtienes:** una página de dispositivo por unidad, más las lecturas de cada unidad como fuentes. ReefDose informa de sus cabezales y envases; ReefATO+ informa de su depósito y sus rellenados; ReefMat informa de los días restantes; ReefRun informa del estado de la bomba.

## Jecod / Jebao

Cora se conecta a bombas Jecod, y puede leerlas y controlarlas. Las unidades Jecod llegan a Cora de una de dos formas, y cuál use la tuya decide qué es posible.

![Buscar una bomba](img/mobile-connections.webp "El escaneo explica qué necesita y por qué una bomba puede no aparecer en el primer barrido.")

**Por tu red.** Usa **Buscar una bomba en tu red**; encuentra unidades que se anuncian, así que no hay que introducir ninguna dirección. Una bomba de red se puede leer y controlar siempre que esté encendida **y sea accesible**: o bien tu teléfono está en la misma red, o bien un Cora Max de esa red retransmite por ti. Fuera de casa sin ningún Cora Max en el lugar, una bomba solo de red es visible pero no controlable.

:::note Una bomba a menudo se pierde en el primer barrido
Las bombas responden a un escaneo y se pierden en el siguiente. Si la tuya no aparece en la lista, vuelve a escanear en lugar de asumir que no es accesible.
:::

Si una búsqueda no encuentra nada, el resultado muestra las direcciones que revisó por Wi-Fi. Si tu bomba tiene una dirección distinta en la aplicación Jebao, tu teléfono está en otra red. Una red de invitados o de IoT, o una banda solo de 5 GHz, no verá estas bombas. En iPhone, Cora también necesita acceso a la Red local para ver bombas en tu Wi-Fi. Si está desactivado, la lista se queda vacía y no aparece ningún error, así que el resultado lo explica y ofrece **Abrir Ajustes** para volver a activarlo. **Ajustes → Acceso a dispositivos** abre el mismo lugar en cualquier momento; consulta [Ajustes](/help/mobile-settings).

**Por Bluetooth.** Algunas bombas solo son accesibles desde un teléfono cerca de ellas. La página de la bomba lo indica, y muestra los últimos ajustes que consiguió leer junto con su antigüedad.

Cora necesita el permiso de Bluetooth para esto. Concédelo antes de añadir una bomba Bluetooth: sin permiso la bomba no se puede detectar en absoluto, más allá de tardar más en aparecer.

**Qué obtienes:** estado en vivo, modo e intensidad, pausa de alimentación y un programa diario. Consulta [Programar equipos](/help/mobile-schedules).

:::warning Una bomba Bluetooth solo es accesible cuando estás cerca de ella
Su página muestra los últimos ajustes que leyó Cora y cuánto hace. Cambiar cualquier cosa, incluido iniciar una pausa de alimentación, necesita la bomba al alcance. Ponte cerca de ella y vuelve a abrir la página.
:::

## Controlador de KH AquaWiz

Cora lee la alcalinidad de un controlador de KH AquaWiz a través de tu cuenta AquaWiz.

**Necesitarás:** tu nombre de usuario y contraseña de AquaWiz. Cora inicia sesión en tu nombre y guarda el inicio de sesión para poder seguir leyendo.

**Qué obtienes:** la alcalinidad como fuente, actualizada tan a menudo como tu controlador titula. El pH está disponible como opción si tu unidad lo informa.

:::warning Un inicio de sesión, compartido
AquaWiz emite un solo inicio de sesión por cuenta, así que el que guarda Cora es el mismo que usa su propia aplicación. Cambiar tu contraseña de AquaWiz desconectará a Cora; reconéctalo después desde la fila del dispositivo. Para revocar el acceso de Cora por completo, elimina el dispositivo en Cora y cambia tu contraseña de AquaWiz.
:::

## Maxspect

:::note El soporte de Maxspect está en beta
El soporte del gyre Maxspect todavía se está probando y desarrollando, así que algunos controles pueden ser limitados, y lo que ves aquí puede cambiar entre actualizaciones. Si algo no funciona como se describe, dínoslo desde [Obtener ayuda](/help/mobile-support).
:::

Cora se conecta a bombas Maxspect Gyre y puede leerlas y controlarlas.

**Necesitarás:** al añadirla, el gyre y tu teléfono en la misma red. Usa **Dispositivos → Buscar una bomba en tu red**.

**Qué obtienes:** patrón de olas y velocidad para **Gyre A** y **Gyre B**, el horario del gyre para consultar (se fija en la aplicación Maxspect), **Salud de la bomba**, y si está en marcha, con cuándo se leyó por última vez. Consulta [Cómo controlar tu equipo](/help/mobile-device-control).

:::note Cómo llega Cora Mobile a un gyre
Cuando un Cora Max atiende al acuario, Cora Mobile funciona a través de ese Cora Max, incluso cuando estás fuera de casa, y **Cambiar ajustes** parte de la última lectura de ese Cora Max. En otro caso, tu teléfono habla directamente con el gyre y debe estar en la red del gyre. Abrir la página del gyre lo lee entonces; si la página muestra en cambio una lectura guardada más antigua, **Cambiar ajustes** se mantiene oculto hasta que tocas actualizar.
:::

## Registrar a mano

Algunos parámetros vienen de un kit de pruebas en lugar de un equipo. Para introducir un resultado, desplázate hasta el final del panel y toca **Registrar parámetros**.

Las lecturas registradas a mano son de primera clase: aparecen en los widgets, llevan su propia fuente y antigüedad, alimentan a Reef Buddy, y son con lo que Cora compara tus sondas cuando te dice que dos fuentes no coinciden.

## Si una conexión deja de funcionar

La fila del dispositivo te indica de qué tipo de problema se trata. Consulta la tabla en **[Añadir, editar y eliminar dispositivos](/help/mobile-devices)**, y **[Solución de problemas](/help/troubleshooting)** para cualquier cosa que no cubra.
