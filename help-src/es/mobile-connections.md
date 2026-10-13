---
title: Conectar tus equipos
description: Cómo conectar a Cora una unidad Neptune Apex, Red Sea ReefBeat, Jecod o AquaWiz y, en Beta, equipos Maxspect, GHL, HYDROS, Focustronic e Inkbird.
section: Cora Mobile
reviewed: 2026-10-13
order: 12
group: Equipment
---

Esta página explica cómo conectar a Cora cada marca de equipo y qué necesita cada conexión. Todas empiezan igual: **Dispositivos → Agregar dispositivo** y después eliges la marca.

![La lista Agregar dispositivo de un usuario Beta](img/mobile-add-device-beta.webp "La lista de marcas. Las marcas Beta llevan una etiqueta Beta.")

Las marcas marcadas como *(Beta)* solo están abiertas a los usuarios Beta. Consulta [Funciones Beta](/help/mobile-beta).

| Marca | Abre | Sin un Cora Max |
|---|---|---|
| Cora | Una búsqueda de un Cora Max nuevo, por Wi-Fi o Bluetooth | |
| Neptune Apex | Un escaneo de red o su dirección IP, y después a qué acuarios sirve | Solo local |
| Red Sea | Un escaneo de tu red, y después a qué acuario pertenece cada unidad | Solo local |
| Jecod / Jebao | Un escaneo de tu red, o Bluetooth | Solo local |
| AquaWiz | Tu inicio de sesión de AquaWiz | Funciona |
| Maxspect *(Beta)* | El mismo escaneo que Jecod | **Requiere Cora Max** |
| GHL *(Beta)* | Su dirección, su interfaz y, en un mini, su acceso | **Requiere Cora Max** |
| HYDROS *(Beta)* | Una clave de dispositivo de la app HYDROS | Funciona |
| Focustronic *(Beta)* | Tu inicio de sesión de Focustronic, y después a qué acuario pertenece cada dispositivo | Funciona |
| EcoTech *(Beta)* | Una búsqueda por Bluetooth de luces Radion, bombas VorTech y dosificadoras Versa. Consulta [Luces, bombas y dosificadoras EcoTech](/help/mobile-ecotech) | **Requiere Cora Max** |
| Inkbird *(Beta)* | Una búsqueda por Bluetooth de tu monitor de aire de habitación | **Requiere Cora Max** |
| Cámara *(Beta)* | Una cámara Wyze, Tapo, Sonoff u otra RTSP. Consulta [Cámaras y vigilancia del skimmer](/help/mobile-cameras) | **Requiere Cora Max** |

## Sin un Cora Max: solo local {#local-only}

Los equipos Neptune Apex, Red Sea y Jecod están en tu red doméstica (o en Bluetooth). Si no tienes ningún Cora Max (o ninguno en el acuario al que los añades), la pantalla de añadir de estas marcas dice *Sin Cora Max, esta integración solo funciona localmente en la app Mobile.* Eso significa que:

- Tu teléfono lee y controla el equipo mientras Cora Mobile está abierta en la misma red, o al alcance del Bluetooth.
- Fuera de casa ves las últimas lecturas que guardó tu teléfono, y no puedes controlarlo.

Un Cora Max en el acuario lee estos equipos a todas horas y transmite tus órdenes cuando estás fuera. AquaWiz, HYDROS y Focustronic se alcanzan a través del servicio propio del fabricante, así que funcionan desde cualquier sitio sin un Cora Max. Las filas marcadas con **Requiere Cora Max** aparecen en gris hasta que el acuario tiene uno. Más información en [Más de un dispositivo Cora](/help/mobile-multi-device).

## Neptune Apex {#neptune-apex}

Cora lee tu Apex por tu red local, incluidas las sondas, las tomas y los módulos de expansión que tengas instalados.

1. Ve a **Dispositivos → Agregar dispositivo → Neptune Apex**.
2. Toca **Buscar el APEX en la red** y elige tu Apex, o escribe su dirección en **O introduce la IP manualmente:**.
3. Rellena **Inicio de sesión del Apex (solo si configuraste uno en el Apex):**. Deja la contraseña en blanco si no has configurado ninguna.
4. Toca **Cargar parámetros del APEX** y marca los que quieras en **Parámetros a seguir**.
5. Fija la **Frecuencia de consulta**. No la dejes desactivada: con la consulta desactivada, nada lee el Apex y sus lecturas se quedan antiguas.
6. Toca **Continuar**, marca todos los acuarios en **¿A qué acuarios sirve este Apex?** y toca **Guardar**. Un Apex puede servir a más de un acuario.

Si el escaneo no encuentra nada, comprueba que tu teléfono está en el mismo Wi-Fi que el Apex, o escribe tú la dirección IP.

Una vez conectado, cada sonda que informa tu Apex pasa a ser una fuente que puedes poner en un panel. Las tomas aparecen como controles, y cada módulo de expansión instalado tiene su propia casilla de dispositivo. Tu propia programación del Apex sigue funcionando exactamente como la configuraste. Lo que puedes controlar está en [Controlar tus equipos](/help/mobile-device-control#neptune-apex).

## Red Sea ReefBeat {#red-sea-reefbeat}

Cora se comunica con los equipos ReefBeat por tu red local. Es compatible con **ReefDose**, **ReefATO+**, **ReefMat** y **ReefRun**, además de **ReefControl**, **ReefControl Power**, **ReefWave** y **ReefLED**, que llevan *(Beta)* en su nombre pero están abiertos a todos.

1. Configura primero la unidad en la app ReefBeat de Red Sea, y comprueba que está en la misma red que tu teléfono.
2. Ve a **Dispositivos → Agregar dispositivo → Red Sea**. Cora escanea tu red.
3. Elige a qué acuario pertenece cada unidad.

Una unidad Red Sea sirve a un solo acuario. Elegir otro la mueve ahí.

Cada unidad tiene su propia página de dispositivo, y sus lecturas pasan a ser fuentes. ReefDose informa de sus cabezales y envases, ReefATO+ de su depósito y sus rellenados, ReefMat de los días que le quedan y ReefRun del estado de sus bombas. ReefControl informa de sus sondas de la misma forma. ReefWave y ReefLED solo muestran su modo, de momento. Lo que permite hacer cada página está en [Controlar tus equipos](/help/mobile-device-control#red-sea).

## Jecod / Jebao {#jecod}

Cora se conecta a las bombas Jecod y puede leerlas y controlarlas. Añade una desde **Dispositivos → Agregar dispositivo → Jecod**. Una bomba Jecod llega a Cora de una de dos formas, y eso decide qué puedes hacer con ella.

![La pantalla Añadir una bomba en Cora Mobile, todavía sin bombas encontradas](img/mobile-connections.webp "Aún no se ve ninguna: la búsqueda explica qué necesita y por qué una bomba puede perderse un barrido.")

**Por tu red.** La búsqueda encuentra las bombas que se anuncian en la red, así que no tienes que escribir ninguna dirección. Puedes leer y manejar una bomba de red siempre que esté encendida y se pueda llegar a ella. Eso significa que tu teléfono está en la misma red, o que un Cora Max de esa red transmite tus órdenes. Si estás fuera de casa y no hay ningún Cora Max allí, puedes ver una bomba de red pero no controlarla.

:::note Una bomba a menudo se pierde el primer escaneo
Las bombas responden a un escaneo y se pierden el siguiente. Si la tuya no aparece, vuelve a buscar antes de decidir que no se puede llegar a ella.
:::

Si una búsqueda no encuentra nada, el resultado muestra las direcciones que revisó por Wi-Fi. Si la app de Jebao muestra otra dirección para tu bomba, tu teléfono está en otra red. Una red de invitados o de IoT, o una banda solo de 5 GHz, no ve estas bombas. En iPhone, Cora también necesita acceso a la Red local para ver las bombas de tu Wi-Fi. Sin él, la lista se queda vacía y no aparece ningún error, así que el resultado lo explica y ofrece **Abrir Ajustes** para volver a activarlo. También puedes llegar ahí en cualquier momento desde **Ajustes → Acceso a dispositivos**, descrito en [Ajustes de Cora Mobile](/help/mobile-settings).

**Por Bluetooth.** A algunas bombas solo se puede llegar desde un teléfono que esté cerca. La página de la bomba lo indica, y muestra los últimos ajustes que leyó y su antigüedad. Cora necesita permiso de Bluetooth para esto. Concédelo antes de añadir una bomba Bluetooth, o Cora no podrá encontrar la bomba.

:::warning Tienes que estar cerca de una bomba Bluetooth
Su página muestra los últimos ajustes que leyó Cora y hace cuánto. Cambiar cualquier cosa, incluso empezar una pausa de alimentación, necesita la bomba al alcance. Acércate y vuelve a abrir la página.
:::

Con cualquiera de las dos conexiones tienes el estado en directo, el modo y la intensidad, una pausa de alimentación y un programa diario. En algunas bombas, una pausa de alimentación iniciada desde tu teléfono necesita que la página de la bomba siga abierta. Los detalles están en [Controlar tus equipos](/help/mobile-device-control#jecod), y [Programar equipos](/help/mobile-schedules) explica el programa diario.

## AquaWiz KH Controller {#aquawiz-kh-controller}

Cora lee la alcalinidad de un controlador de KH AquaWiz a través de tu cuenta de AquaWiz, así que funciona fuera de casa y no necesita un Cora Max.

1. Ve a **Dispositivos → Agregar dispositivo → AquaWiz**.
2. Escribe tu usuario y tu contraseña de AquaWiz y toca **Conectar**.
3. Elige el acuario, activa **Leer también su pH** si lo quieres y toca **Vincular a Cora**.

Con **Mantenerse conectado automáticamente** activado, Cora guarda tu contraseña de AquaWiz y renueva la conexión por su cuenta. Desactivado, Cora guarda solo un token de inicio de sesión, que AquaWiz hace caducar más o menos cada 30 días, y te envía una notificación cuando toca volver a iniciar sesión.

Tienes la alcalinidad como fuente, actualizada tan a menudo como titula tu controlador, y también el pH si lo activaste y tu unidad lo informa. Lo que muestra la tarjeta de AquaWiz, y su alerta de suplemento, están en [Controlar tus equipos](/help/mobile-device-control#aquawiz).

:::warning Cora comparte tu inicio de sesión de AquaWiz
AquaWiz da a cada cuenta un solo inicio de sesión, así que Cora usa el mismo que la app de AquaWiz. Si cambias tu contraseña de AquaWiz, Cora se desconecta. Vuelve a conectarlo después desde la fila del dispositivo. Para quitarle a Cora el acceso por completo, quita el dispositivo en Cora y cambia tu contraseña de AquaWiz.
:::

## Maxspect {#maxspect}

:::note Beta
**Beta.** Maxspect está en Beta y solo está abierto a los usuarios Beta. Si no eres usuario Beta, no lo verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html). Algunos controles pueden estar limitados, y lo que ves aquí puede cambiar entre actualizaciones. Si algo no funciona como se describe, cuéntanoslo desde [Informar de un problema](/help/mobile-support).
:::

Cora se conecta a las bombas Gyre de Maxspect y puede leerlas y manejarlas. Añade una desde **Dispositivos → Agregar dispositivo → Maxspect**, el mismo escaneo que usa Jecod. Necesita un Cora Max en el acuario. Sin uno, la fila muestra **Requiere Cora Max**.

Cuando añades un gyre, tiene que estar en la misma red que tu teléfono. Después, Cora Mobile llega a él a través del Cora Max del acuario, incluso cuando estás fuera. El patrón de olas, la velocidad, el horario y **Salud de la bomba** están en [Controlar tus equipos](/help/mobile-device-control#maxspect).

## GHL ProfiLux y Mitras {#ghl-profilux-and-mitras}

:::note Beta
**Beta.** GHL está en Beta y solo está abierto a los usuarios Beta. Si no eres usuario Beta, no lo verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html). Puede que algunas lecturas o controles todavía no funcionen. Si algo no funciona como se describe, cuéntanoslo desde [Informar de un problema](/help/mobile-support).
:::

Cora lee un controlador GHL ProfiLux o Mitras: sondas, tomas, dosificadoras, sensores de nivel y, en los modelos Director, los resultados de las pruebas de KH y de iones.

1. Ve a **Dispositivos → Agregar dispositivo → GHL**. Necesita un Cora Max en el acuario, y muestra **Requiere Cora Max** si no hay ninguno.
2. Tu teléfono no puede buscarlo, así que escribe su dirección y elige tú la interfaz: **API oficial**, **HTTP** o **ProfiLux mini** (que además necesita su acceso).
3. Elige a qué acuario pertenece. Un controlador GHL puede servir a más de un acuario.

Un controlador GHL no habla directamente con tu teléfono. Muestra **Esperando a Cora Max** hasta que un Cora Max de su red lo ha leído, y después sus lecturas y controles aparecen en todas partes.

La API de GHL tiene que estar activada para que Cora pueda llegar al controlador. GHL la desactiva después de cada actualización de firmware, así que revisa esto primero si no aparece nada. [Solución de problemas](/help/troubleshooting) explica qué hacer. Los controles están en [Controlar tus equipos](/help/mobile-device-control#ghl).

## HYDROS {#hydros}

:::note Beta
**Beta.** HYDROS está en Beta y solo está abierto a los usuarios Beta. Si no eres usuario Beta, no lo verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html). Puede que algunas lecturas o controles todavía no funcionen. Si algo no funciona como se describe, cuéntanoslo desde [Informar de un problema](/help/mobile-support).
:::

HYDROS no necesita que tu teléfono y tu controlador estén en la misma red, ni un Cora Max. Cora llega a él a través de la nube de HYDROS, así que sigue funcionando fuera de casa, e incluso con Cora Mobile cerrada.

1. En la app HYDROS, crea una **clave de dispositivo** para el proveedor **cora-iq**. Elige **Read** si solo quieres sus lecturas, o **Write** si también quieres controlarlo desde Cora.
2. En Cora Mobile, ve a **Dispositivos → Agregar dispositivo → HYDROS**. La pantalla se llama **Añadir HYDROS (Beta)**.
3. Pega la clave en **Clave de dispositivo HYDROS**, toca **Comprobar clave**, elige el acuario y toca **Vincular**.

Una vez vinculado, Cora importa los últimos 33 días de su historial y después sigue leyendo a partir de ahí. [Controlar tus equipos](/help/mobile-device-control#hydros) explica qué puedes leer y, con una clave de escritura, controlar.

## Focustronic {#focustronic}

:::note Beta
**Beta.** Focustronic está en Beta y solo está abierto a los usuarios Beta. Si no eres usuario Beta, no lo verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html).
:::

Cora lee los dispositivos Focustronic Alkatronic, Dosetronic y Mastertronic a través de tu cuenta de Focustronic, así que funciona fuera de casa y no necesita un Cora Max.

1. Ve a **Dispositivos → Agregar dispositivo → Focustronic** e inicia sesión con la misma cuenta que usas en la app de Focustronic.
2. Elige a qué acuario pertenece cada dispositivo y toca **Vincular a Cora**.

**Mantener la sesión** deja que Cora guarde tu contraseña de Focustronic, cifrada, y vuelva a iniciar sesión por su cuenta. Si lo desactivas, Cora guarda solo un inicio de sesión temporal y te envía una notificación cuando tengas que volver a iniciar sesión. Si Focustronic rechaza el inicio de sesión, abre **Añadir Focustronic** y vuelve a iniciar sesión.

Lo que muestra cada dispositivo, y **Medir ahora**, **Dosificar ahora** y **Probar ahora**, están en [Controlar tus equipos](/help/mobile-device-control#focustronic).

## Monitor de aire de habitación Inkbird {#inkbird-room-air-monitor}

:::note Beta
**Beta.** Inkbird está en Beta y solo está abierto a los usuarios Beta. Si no eres usuario Beta, no lo verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html).
:::

Cora lee un monitor de aire de habitación Inkbird IAM-T1 o IAM-T2. Un Cora Max del acuario lo lee por Bluetooth, y Cora nunca escribe nada en el monitor. La fila muestra **Requiere Cora Max** hasta que el acuario tiene uno.

1. Ve a **Dispositivos → Agregar dispositivo → Inkbird**. Cora busca monitores cercanos. El Bluetooth tiene que estar activado, con permiso para Cora.
2. Elige el tuyo y toca **Vincular a un acuario**. Si no aparece ninguno, acércate y toca **Buscar de nuevo**.

La página del monitor muestra su última lectura. **Intervalo de muestreo** fija cada cuánto lo lee un Cora Max. Hasta que un Cora Max lo ha leído, la página dice **Esperando a Cora Max**. Si se queda en silencio, muestra **Sin datos** y Cora te avisa. Las lecturas de la habitación también alimentan a [Reef Buddy](/help/mobile-reef-buddy). Para dejar de usarlo, toca **Desvincular**. Cora Max deja de leerlo y el historial se conserva.

## Registrar a mano {#logging-by-hand}

Algunos parámetros salen de un kit de pruebas, no de un equipo. Para introducir un resultado, baja hasta el final del panel y toca **Registrar parámetros**.

Las lecturas que registras a mano cuentan igual que las demás. Aparecen en los widgets con su propia fuente y antigüedad, y alimentan a Reef Buddy. Cora también compara tus sondas con ellas cuando te avisa de que dos fuentes no coinciden.

## Si una conexión deja de funcionar {#if-a-connection-stops-working}

La fila del dispositivo te dice qué tipo de problema es. Búscalo en la tabla de [Añadir, editar y eliminar dispositivos](/help/mobile-devices#health). Para cualquier cosa que no cubra, consulta [Solución de problemas](/help/troubleshooting).
