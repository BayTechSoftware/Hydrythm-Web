---
title: Conectar tus equipos
description: Cómo conectar a Cora equipos Neptune Apex, Red Sea ReefBeat, Jecod, AquaWiz, GHL y HYDROS.
section: Cora Mobile
reviewed: 2026-09-30
order: 10
group: Equipment
---

Cora funciona con los equipos que ya tienes. En esta página verás qué equipos son compatibles y qué necesita cada conexión.

Todas empiezan igual: **Dispositivos → Agregar dispositivo**, y luego eliges la marca. Cada una abre justo lo que necesita para encontrar tu equipo.

| Marca | Abre |
|---|---|
| Cora | Un escaneo para un Cora Max nuevo, por Wi-Fi o Bluetooth |
| Neptune Apex | Su dirección en tu red, el inicio de sesión y después a qué acuario pertenece |
| Red Sea | Un escaneo en tu red y después a qué acuario pertenece cada unidad |
| Jecod / Jebao | Un escaneo en tu red, o Bluetooth |
| Maxspect *(beta)* | El mismo escaneo que Jecod |
| GHL *(beta)* | Su dirección, la interfaz y, para una mini, su acceso |
| HYDROS *(beta)* | Una clave de dispositivo de la aplicación HYDROS |
| AquaWiz | Tu acceso de AquaWiz |

## Neptune Apex

Cora lee tu Apex por la red local. Lee las sondas, las tomas y los módulos de expansión que tengas instalados.

Añádelo desde **Dispositivos → Agregar dispositivo → Neptune Apex**. Necesitas su dirección en tu red y sus datos de acceso, y después eliges a qué acuario pertenece. Un Apex puede servir a más de un acuario.

Cada sonda que informa tu Apex aparece como una fuente que puedes poner en un panel. Las tomas aparecen como controles, y cada módulo de expansión instalado tiene su propia casilla de dispositivo.

:::note Tu Apex sigue con su propia programación
Cora lee tu Apex, lo muestra junto a todo lo demás y puede encender o apagar tomas cuando se lo pides. Tu programación sigue funcionando tal como la configuraste.
:::

## Red Sea ReefBeat

Cora se comunica con los equipos ReefBeat por la red local. Son compatibles **ReefDose**, **ReefATO+**, **ReefMat**, **ReefRun** y, en beta, **ReefControl**, **ReefControl Power**, **ReefWave** y **ReefLED**.

El equipo tiene que estar ya configurado en ReefBeat. Cuando lo añadas, debe estar en la misma red que tu teléfono. Añádelo desde **Dispositivos → Agregar dispositivo → Red Sea**, que escanea tu red y pregunta a qué acuario pertenece cada unidad. Una unidad Red Sea sirve a un acuario: elegir uno distinto la mueve ahí.

Cada equipo tiene su página de dispositivo y sus lecturas aparecen como fuentes. ReefDose informa de sus cabezales y recipientes. ReefATO+ informa de su depósito y de los rellenados. ReefMat informa de los días que le quedan y ReefRun, del estado de la bomba. ReefControl informa de sus sondas de la misma manera. ReefWave y ReefLED *(beta)* solo muestran su modo por ahora, únicamente para consultarlo.

## Jecod / Jebao

Cora se conecta a las bombas Jecod y puede leerlas y controlarlas. Añade una desde **Dispositivos → Agregar dispositivo → Jecod**. Una bomba Jecod llega a Cora de una de estas dos formas, y de eso depende lo que puedes hacer con ella.

![Buscar una bomba](img/mobile-connections.webp "El escaneo explica qué necesita y por qué una bomba puede no aparecer en el primer barrido.")

**Por tu red.** La búsqueda encuentra las bombas que se anuncian en la red, así que no tienes que escribir ninguna dirección. Puedes leer y controlar una bomba de red siempre que esté encendida **y se pueda llegar a ella**. Para eso, tu teléfono tiene que estar en la misma red o un Cora Max de esa red tiene que hacer de enlace. Si estás fuera de casa y no hay ningún Cora Max allí, verás la bomba de red, pero no podrás controlarla.

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

Cora lee la alcalinidad de un controlador de KH AquaWiz a través de tu cuenta de AquaWiz. Añádelo desde **Dispositivos → Agregar dispositivo → AquaWiz**.

Necesitas tu usuario y tu contraseña de AquaWiz. Cora inicia sesión por ti y guarda el acceso para poder seguir leyendo.

La alcalinidad aparece como fuente y se actualiza cada vez que tu controlador hace una titulación. Si tu equipo informa del pH, también puedes añadirlo.

La página del dispositivo también muestra tu KH objetivo, la concentración de tu dosis y, en un equipo con la dosificación configurada, su dosis máxima por hora y cuánto suplemento de alcalinidad queda en el recipiente. Estos datos vienen directamente de tus ajustes de AquaWiz. Cámbialos desde la aplicación AquaWiz. Si tu equipo controla su recipiente, Cora te avisa cuando el suplemento se está agotando, con un valor predeterminado de 100 mL.

:::warning Un solo acceso compartido
AquaWiz da un solo acceso por cuenta. El que guarda Cora es el mismo que usa su aplicación. Si cambias tu contraseña de AquaWiz, Cora se desconectará. Después, vuelve a conectarlo desde la fila del dispositivo. Para quitarle a Cora el acceso del todo, elimina el dispositivo en Cora y cambia tu contraseña de AquaWiz.
:::

## Maxspect

:::note Maxspect está en beta
Seguimos probando y desarrollando el soporte para el gyre Maxspect. Algunos controles pueden estar limitados y lo que ves aquí puede cambiar con las actualizaciones. Si algo no funciona como se describe, avísanos desde [Obtener ayuda](/help/mobile-support).
:::

Cora se conecta a las bombas Maxspect Gyre y puede leerlas y controlarlas. Añade una desde **Dispositivos → Agregar dispositivo → Maxspect**, el mismo escaneo que usa Jecod.

Para añadirlo, el gyre y tu teléfono tienen que estar en la misma red.

Verás el patrón de olas y la velocidad de **Gyre A** y **Gyre B**, el horario del gyre (solo para consultarlo, se configura en la aplicación Maxspect) y la **Salud de la bomba**. También verás si está en marcha y cuándo se leyó por última vez. Más información en [Controlar tus equipos](/help/mobile-device-control).

:::note Cómo se comunica Cora Mobile con un gyre
Si un Cora Max atiende el acuario, Cora Mobile trabaja a través de ese Cora Max, también cuando estás fuera de casa. **Cambiar ajustes** parte entonces de la última lectura de ese Cora Max. Si no, tu teléfono habla con el gyre directamente y tiene que estar en la red del gyre. En ese caso, al abrir la página del gyre se lee el equipo. Si la página muestra una lectura guardada más antigua, **Cambiar ajustes** no aparece hasta que tocas actualizar.
:::

## GHL ProfiLux y Mitras

:::note GHL está en beta
Seguimos probando y desarrollando el soporte para GHL. Algunas lecturas o controles pueden no funcionar todavía, y lo que ves aquí puede cambiar con las actualizaciones. Si algo no funciona como se describe, avísanos desde [Obtener ayuda](/help/mobile-support).
:::

Cora lee un controlador GHL ProfiLux o Mitras: sondas, tomas, dosificadoras, sensores de nivel y, en los modelos Director, los resultados de las pruebas de KH e iones.

Añádelo desde **Dispositivos → Agregar dispositivo → GHL**. Tu teléfono no puede escanearlo, así que tienes que introducir su dirección y elegir tú la interfaz: **Official API**, **HTTP** o **ProfiLux mini** (que además necesita su acceso). Después eliges a qué acuario pertenece. Un controlador GHL puede servir a más de un acuario.

Un controlador GHL no habla directamente con tu teléfono. Muestra **Esperando a Cora Max** hasta que un Cora Max de su red lo ha leído, y a partir de ahí sus lecturas y controles aparecen en todas partes.

La API de GHL tiene que estar activada para que Cora llegue al controlador. GHL la desactiva después de cada actualización de firmware, así que conviene revisarlo primero si no aparece nada. [Solución de problemas](/help/troubleshooting) explica qué hacer.

## HYDROS

:::note HYDROS está en beta
Seguimos probando y desarrollando el soporte para HYDROS. Algunas lecturas o controles pueden no funcionar todavía, y lo que ves aquí puede cambiar con las actualizaciones. Si algo no funciona como se describe, avísanos desde [Obtener ayuda](/help/mobile-support).
:::

HYDROS es la única integración que no necesita que tu Cora y tu controlador estén en la misma red. Cora llega a él a través de la propia nube de HYDROS, así que sigue funcionando fuera de casa, e incluso con Cora cerrado.

Para conectarlo, abre la aplicación HYDROS y crea una **clave de dispositivo** para el proveedor **cora-iq**. Elige **Read** si solo quieres sus lecturas, o **Write** si además quieres controlarlo desde Cora. Después ve a **Dispositivos → Agregar dispositivo → HYDROS** y pega la clave.

Una vez enlazado, Cora importa los últimos 33 días de su historial y luego sigue leyendo desde ahí en adelante. [Controlar tus equipos](/help/mobile-device-control) explica qué puedes leer y, con una clave Write, controlar.

## Registrar a mano

Algunos parámetros salen de un kit de pruebas y no de un equipo. Para anotar un resultado, baja hasta el final del panel y toca **Registrar parámetros**.

Las lecturas que registras a mano cuentan igual que las demás. Aparecen en los widgets, llevan su propia fuente y antigüedad y llegan a Reef Buddy. Además, Cora las usa como referencia para comparar tus sondas cuando te dice que dos fuentes no coinciden.

## Si una conexión deja de funcionar

La fila del dispositivo te indica qué tipo de problema hay. Revisa la tabla de [Añadir, editar y eliminar dispositivos](/help/mobile-devices). Si tu caso no aparece ahí, consulta [Solución de problemas](/help/troubleshooting).
