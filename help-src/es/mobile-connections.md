---
title: Conectar tus equipos
description: Cómo conectar a Cora equipos Neptune Apex, Red Sea ReefBeat, Jecod y AquaWiz.
section: Cora Mobile
reviewed: 2026-09-17
order: 10
group: Equipment
---

Cora funciona con los equipos que ya tienes. En esta página verás qué equipos son compatibles y qué necesita cada conexión.

Cada marca se conecta a su manera. Empieza desde el punto que corresponde a tu equipo:

| Marca | Empieza desde |
|---|---|
| Neptune Apex | El acuario. La conexión del Apex se guarda en su perfil |
| Red Sea ReefBeat | El acuario |
| Jecod / Jebao | **Dispositivos → Buscar una bomba en tu red**, o Bluetooth |
| AquaWiz | **Dispositivos → Agregar AquaWiz** |
| Maxspect *(beta)* | **Dispositivos → Buscar una bomba en tu red** |
| Cora Max | **Dispositivos → Agregar dispositivo** |

## Neptune Apex

Cora lee tu Apex por la red local. Lee las sondas, las tomas y los módulos de expansión que tengas instalados.

Necesitas la dirección de tu Apex en la red y sus datos de acceso.

Cada sonda que informa tu Apex aparece como una fuente que puedes poner en un panel. Las tomas aparecen como controles, y cada módulo de expansión instalado tiene su propia casilla de dispositivo.

:::note Tu Apex sigue con su propia programación
Cora lee tu Apex, lo muestra junto a todo lo demás y puede encender o apagar tomas cuando se lo pides. Tu programación sigue funcionando tal como la configuraste.
:::

## Red Sea ReefBeat

Cora se comunica con los equipos ReefBeat por la red local. Son compatibles **ReefDose**, **ReefATO+**, **ReefMat** y **ReefRun**.

El equipo tiene que estar ya configurado en ReefBeat. Cuando lo añadas, debe estar en la misma red que tu teléfono.

Cada equipo tiene su página de dispositivo y sus lecturas aparecen como fuentes. ReefDose informa de sus cabezales y recipientes. ReefATO+ informa de su depósito y de los rellenados. ReefMat informa de los días que le quedan y ReefRun, del estado de la bomba.

## Jecod / Jebao

Cora se conecta a las bombas Jecod y puede leerlas y controlarlas. Una bomba Jecod llega a Cora de una de estas dos formas, y de eso depende lo que puedes hacer con ella.

![Buscar una bomba](img/mobile-connections.webp "El escaneo explica qué necesita y por qué una bomba puede no aparecer en el primer barrido.")

Si la bomba se conecta por tu red, usa **Buscar una bomba en tu red**. La búsqueda encuentra las bombas que se anuncian en la red, así que no tienes que escribir ninguna dirección. Puedes leer y controlar una bomba de red siempre que esté encendida **y se pueda llegar a ella**. Para eso, tu teléfono tiene que estar en la misma red o un Cora Max de esa red tiene que hacer de enlace. Si estás fuera de casa y no hay ningún Cora Max allí, verás la bomba de red, pero no podrás controlarla.

:::note Es normal que una bomba no aparezca a la primera
Las bombas responden a una búsqueda y a la siguiente no. Si la tuya no sale en la lista, busca otra vez antes de pensar que no se puede llegar a ella.
:::

Si la búsqueda no encuentra nada, el resultado muestra las direcciones que revisó por Wi-Fi. Si tu bomba tiene otra dirección en la aplicación Jebao, tu teléfono está en otra red. Una red de invitados o de IoT, o una banda solo de 5 GHz, no ve estas bombas. En iPhone, Cora también necesita acceso a la red local para ver bombas en tu Wi-Fi. Si ese acceso está desactivado, la lista sale vacía y sin ningún error. Por eso el resultado te lo explica y te ofrece **Abrir Ajustes** para activarlo de nuevo. Puedes llegar al mismo sitio cuando quieras desde **Ajustes → Acceso a dispositivos**. Más información en [Ajustes](/help/mobile-settings).

Algunas bombas van por Bluetooth y solo responden a un teléfono que esté cerca. La página de la bomba te lo indica y muestra los últimos ajustes que pudo leer y su antigüedad.

Para esto, Cora necesita permiso de Bluetooth. Concédelo antes de añadir una bomba Bluetooth. Sin ese permiso, Cora no puede encontrar la bomba.

Con una bomba Jecod tienes el estado en directo, el modo y la intensidad, la pausa de alimentación y un programa diario. Más información en [Programar equipos](/help/mobile-schedules).

:::warning Solo llegas a una bomba Bluetooth si estás cerca
Su página muestra los últimos ajustes que leyó Cora y cuándo los leyó. Para cambiar cualquier cosa, también para iniciar una pausa de alimentación, la bomba tiene que estar a tu alcance. Acércate a ella y vuelve a abrir la página.
:::

## Controlador de KH AquaWiz

Cora lee la alcalinidad de un controlador de KH AquaWiz a través de tu cuenta de AquaWiz.

Necesitas tu usuario y tu contraseña de AquaWiz. Cora inicia sesión por ti y guarda el acceso para poder seguir leyendo.

La alcalinidad aparece como fuente y se actualiza cada vez que tu controlador hace una titulación. Si tu equipo informa del pH, también puedes añadirlo.

:::warning Un solo acceso compartido
AquaWiz da un solo acceso por cuenta. El que guarda Cora es el mismo que usa su aplicación. Si cambias tu contraseña de AquaWiz, Cora se desconectará. Después, vuelve a conectarlo desde la fila del dispositivo. Para quitarle a Cora el acceso del todo, elimina el dispositivo en Cora y cambia tu contraseña de AquaWiz.
:::

## Maxspect

:::note Maxspect está en beta
Seguimos probando y desarrollando el soporte para el gyre Maxspect. Algunos controles pueden estar limitados y lo que ves aquí puede cambiar con las actualizaciones. Si algo no funciona como se describe, avísanos desde [Obtener ayuda](/help/mobile-support).
:::

Cora se conecta a las bombas Maxspect Gyre y puede leerlas y controlarlas.

Para añadirlo, el gyre y tu teléfono tienen que estar en la misma red. Usa **Dispositivos → Buscar una bomba en tu red**.

Verás el patrón de olas y la velocidad de **Gyre A** y **Gyre B**, el horario del gyre (solo para consultarlo, se configura en la aplicación Maxspect) y la **Salud de la bomba**. También verás si está en marcha y cuándo se leyó por última vez. Más información en [Controlar tus equipos](/help/mobile-device-control).

:::note Cómo se comunica Cora Mobile con un gyre
Si un Cora Max atiende el acuario, Cora Mobile trabaja a través de ese Cora Max, también cuando estás fuera de casa. **Cambiar ajustes** parte entonces de la última lectura de ese Cora Max. Si no, tu teléfono habla con el gyre directamente y tiene que estar en la red del gyre. En ese caso, al abrir la página del gyre se lee el equipo. Si la página muestra una lectura guardada más antigua, **Cambiar ajustes** no aparece hasta que tocas actualizar.
:::

## Registrar a mano

Algunos parámetros salen de un kit de pruebas y no de un equipo. Para anotar un resultado, baja hasta el final del panel y toca **Registrar parámetros**.

Las lecturas que registras a mano cuentan igual que las demás. Aparecen en los widgets, llevan su propia fuente y antigüedad y llegan a Reef Buddy. Además, Cora las usa como referencia para comparar tus sondas cuando te dice que dos fuentes no coinciden.

## Si una conexión deja de funcionar

La fila del dispositivo te indica qué tipo de problema hay. Revisa la tabla de [Añadir, editar y eliminar dispositivos](/help/mobile-devices). Si tu caso no aparece ahí, consulta [Solución de problemas](/help/troubleshooting).
