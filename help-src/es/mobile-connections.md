---
title: Conectar tus equipos
description: Cómo conectar a Cora una unidad Neptune Apex, Red Sea ReefBeat, Jecod o AquaWiz.
section: Cora Mobile
reviewed: 2026-10-18
order: 12
group: Equipment
---

Esta página explica cómo conectar a Cora cada marca de equipo y qué necesita cada conexión. Todas empiezan igual: **Dispositivos → Agregar dispositivo** y después eliges la marca.

![La lista de marcas de Agregar dispositivo](img/mobile-add-device-brands.webp "La lista de marcas.")


| Marca | Abre | Sin un Cora Max |
|---|---|---|
| Cora | Una búsqueda de un Cora Max nuevo, por Wi-Fi o Bluetooth | |
| Neptune Apex | Un escaneo de red o su dirección IP, y después a qué acuarios sirve | Solo local |
| Red Sea | Un escaneo de tu red, y después a qué acuario pertenece cada unidad | Solo local |
| Jecod / Jebao | Un escaneo de tu red, o Bluetooth | Solo local |
| AquaWiz | Tu inicio de sesión de AquaWiz | Funciona |

## Sin un Cora Max: solo local {#local-only}

Los equipos Neptune Apex, Red Sea y Jecod están en tu red doméstica (o en Bluetooth). Si no tienes ningún Cora Max (o ninguno en el acuario al que los añades), la pantalla de añadir de estas marcas dice *Sin Cora Max, esta integración solo funciona localmente en la app Mobile.* Eso significa que:

- Tu teléfono lee y controla el equipo mientras Cora Mobile está abierta en la misma red, o al alcance del Bluetooth.
- Fuera de casa ves las últimas lecturas que guardó tu teléfono, y no puedes controlarlo.

Un Cora Max en el acuario lee estos equipos a todas horas y transmite tus órdenes cuando estás fuera. AquaWiz se alcanza a través del servicio propio del fabricante, así que funciona desde cualquier sitio sin un Cora Max. Más información en [Más de un dispositivo Cora](/help/mobile-multi-device).

## Neptune Apex {#neptune-apex}

Cora lee tu Apex por tu red local, incluidas las sondas, las tomas y los módulos de expansión que tengas instalados.

1. Ve a **Dispositivos → Agregar dispositivo → Neptune Apex**.
2. Toca **Buscar el APEX en la red** y elige tu Apex, o escribe su dirección en **O introduce la IP manualmente:**.
3. Rellena **Inicio de sesión del Apex (solo si configuraste uno en el Apex):**. Deja la contraseña en blanco si no has configurado ninguna.
4. Toca **Cargar parámetros del APEX** y marca los que quieras en **Parámetros a seguir**.
5. Fija la **Frecuencia de consulta**. No la dejes desactivada: con la consulta desactivada, nada lee el Apex y sus lecturas se quedan antiguas.
6. Toca **Continuar**, marca todos los acuarios en **¿A qué acuarios sirve este Apex?** y toca **Guardar**. Un Apex puede servir a más de un acuario.

Si el escaneo no encuentra nada, comprueba que tu teléfono está en el mismo Wi-Fi que el Apex, o escribe tú la dirección IP.

Una vez conectado, cada sonda que informa tu Apex pasa a ser una fuente que puedes poner en un panel. Las tomas aparecen como controles, y cada módulo de expansión instalado tiene su propia tarjeta de dispositivo. Tu propia programación del Apex sigue funcionando exactamente como la configuraste. Lo que puedes controlar está en [Controlar tus equipos](/help/mobile-device-control#neptune-apex).

## Red Sea ReefBeat {#red-sea-reefbeat}

Cora se comunica con los equipos ReefBeat por tu red local. Es compatible con **ReefDose**, **ReefATO+**, **ReefMat** y **ReefRun**.

1. Configura primero la unidad en la app ReefBeat de Red Sea, y comprueba que está en la misma red que tu teléfono.
2. Ve a **Dispositivos → Agregar dispositivo → Red Sea**. Cora escanea tu red.
3. Elige a qué acuario pertenece cada unidad.

Una unidad Red Sea sirve a un solo acuario. Elegir otro la mueve ahí.

Cada unidad tiene su propia página de dispositivo, y sus lecturas pasan a ser fuentes. ReefDose informa de sus cabezales y recipientes, ReefATO+ de su depósito y sus rellenados, ReefMat de los días que le quedan y ReefRun del estado de sus bombas. Lo que permite hacer cada página está en [Controlar tus equipos](/help/mobile-device-control#red-sea).

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

Con cualquiera de las dos conexiones tienes el estado en directo, el modo y la intensidad, una pausa de alimentación y un horario diario. En algunas bombas, una pausa de alimentación iniciada desde tu teléfono necesita que la página de la bomba siga abierta. Los detalles están en [Controlar tus equipos](/help/mobile-device-control#jecod), y [Programar equipos](/help/mobile-schedules) explica el programa diario.

## AquaWiz KH Controller {#aquawiz-kh-controller}

Cora lee la alcalinidad de un controlador de KH AquaWiz a través de la nube de AquaWiz, así que funciona fuera de casa y no necesita un Cora Max. Un Cora Max añade lecturas cada hora: mira [Cómo lee Cora tu AquaWiz](#how-cora-reads-aquawiz).

1. Ve a **Dispositivos → Agregar dispositivo → AquaWiz**.
2. Inicia sesión con la cuenta de AquaWiz que usas en la app de AquaWiz y toca **Conectar**.
3. Elige el acuario, revisa **Leer también su pH** (empieza activado en una unidad que informa del pH) y toca **Vincular a Cora**.

Inicias sesión una sola vez, para que Cora encuentre tus controladores. Después, Cora guarda solo tu nombre de usuario de AquaWiz: ni contraseña ni token de inicio de sesión. No hay nada que renovar, así que Cora nunca te pide volver a iniciar sesión y ya no existe el interruptor **Mantenerse conectado automáticamente**. Si AquaWiz informa más tarde de que ese usuario ya no es propietario del controlador, su tarjeta se pone naranja y te dice que lo vincules de nuevo: abre **Agregar AquaWiz** e inicia sesión otra vez.

Tienes la alcalinidad como fuente, y también el pH si tu unidad lo informa y **Leer también su pH** está activado. Tu primera lectura llega en cuanto la vinculas, junto con las últimas 6 horas de historial. Después, el servicio Cora de AquaWiz envía una lectura cada 12 horas, que es el límite de AquaWiz, así que una lectura de ahí puede tener hasta medio día. Un Cora Max en el acuario también puede leer el controlador él mismo cada hora cuando llega hasta él. Abre la página del dispositivo para ver cuándo se midió cada lectura y de dónde viene, y toca **Leer ahora** para una nueva (como máximo cada 15 minutos). Lo que muestra la tarjeta de AquaWiz, y sus alertas, están en [Controlar tus equipos](/help/mobile-device-control#aquawiz).

Para mover el controlador a otro acuario, abre su página en **Dispositivos** y toca **Cambiar** en **Acuarios**. No tienes que volver a iniciar sesión en AquaWiz.

:::note Cora guarda solo tu nombre de usuario
Cora usa tu contraseña una sola vez, mientras vinculas, y no la guarda. Cambiar tu contraseña de AquaWiz no desconecta a Cora. Desvincular detiene la lectura del controlador y Cora olvida tu nombre de usuario; no cierra tu sesión en la app de AquaWiz. Tus lecturas existentes se conservan.
:::

### Cómo lee Cora tu AquaWiz {#how-cora-reads-aquawiz}

Cora llega a un AquaWiz por hasta tres vías, que trabajan juntas.

| Vía | Qué le da a Cora | Con qué frecuencia |
| --- | --- | --- |
| Tu inicio de sesión de AquaWiz | Se usa una sola vez, al vincular, para encontrar tus controladores. Después, Cora guarda solo tu nombre de usuario. | Una vez |
| El servicio Cora de AquaWiz | La última lectura de KH y pH, las últimas 6 horas de historial y los ajustes del controlador (KH objetivo, intensidad de dosificación, suplemento restante, estado de bomba y sonda de pH, firmware). | Al vincular, después cada 12 horas (el límite de AquaWiz) y cuando abres la página del dispositivo o tocas **Leer ahora** (como máximo cada 15 minutos) |
| Un Cora Max en el acuario | Lee el controlador directamente por su propio Wi-Fi y suma avisos del nivel de la caja de agua. | Cada hora |

Sin un Cora Max, las lecturas llegan cada 12 horas, que es el límite de AquaWiz, así que una lectura puede tener hasta medio día. **¿Quieres lecturas cada hora? Añade un Cora Max a tu acuario.** [Conoce Cora Max](https://coraiq.tech/es/#max) y [configúralo](/help/max-setup). Necesita el controlador al alcance del Wi-Fi de Cora Max y un firmware del controlador con acceso local. Los detalles están en [Lectura cada hora desde Cora Max](/help/max-device-control#aquawiz-hourly).

La tarjeta del dispositivo muestra de dónde viene cada lectura: **Cada hora desde tu Cora Max** o **Desde la nube de AquaWiz, cada 12 horas**.

Cora guarda todo el historial por horas de tu controlador. Al vincular, rellena hasta 30 días atrás, así que tus gráficas no empiezan vacías.


## Registrar a mano {#logging-by-hand}

Algunos parámetros salen de un kit de pruebas, no de un equipo. Para introducir un resultado, baja hasta el final del panel y toca **Registrar parámetros**.

Las lecturas que registras a mano cuentan igual que las demás. Aparecen en los widgets con su propia fuente y antigüedad, y alimentan a Reef Buddy. Cora también compara tus sondas con ellas cuando te avisa de que dos fuentes no coinciden.

## Si una conexión deja de funcionar {#if-a-connection-stops-working}

La fila del dispositivo te dice qué tipo de problema es. Búscalo en la tabla de [Añadir, editar y eliminar dispositivos](/help/mobile-devices#health). Para cualquier cosa que no cubra, consulta [Solución de problemas](/help/troubleshooting).
