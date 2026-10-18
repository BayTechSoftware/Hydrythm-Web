---
title: La pantalla de inicio de Cora Max
description: Qué significan la barra superior, la etiqueta de estado, las etiquetas de alerta, el menú del acuario y el panel en Cora Max, y cómo cambiar de acuario y abrir Tomas y alimentación.
section: Cora Max
reviewed: 2026-10-13
order: 2
group: Getting started
twin: mobile-tour
---

Esta página explica lo que ves en Cora Max. Muestra un acuario cada vez, con las lecturas en directo llenando la pantalla para que puedas leerlas desde el otro lado de la habitación.

![La pantalla de inicio de Cora Max con los medidores, valores, gráficos y tarjetas de dispositivos de un acuario bajo la barra superior](img/max-home.webp "El panel de un acuario llena la pantalla, con la barra superior encima.")

## La barra superior {#the-top-bar}

![La barra superior de Cora Max](img/max-topbar.webp "La barra superior, numerada de izquierda a derecha según la lista de abajo.")

De izquierda a derecha:

1. **El icono de cuadrícula** abre [el Cuarto de los Acuarios](/help/max-reef-room), la vista general de todos los acuarios que muestra esta pantalla.
2. **El nombre del acuario**, con una pequeña flecha. Tócalo para abrir el **menú del acuario**, que tiene todas las pantallas del acuario que estás mirando. La lista completa está más abajo.
3. **Las etiquetas de alerta** muestran lo que necesita atención ahora mismo: lecturas fuera de rango, fallos de dispositivos, dosis omitidas o suministros bajos. Toca una etiqueta para volver a traer esa alerta al centro de la pantalla. Si hay más de las que caben, verás **+2** (o las que sean). Tócalo para ver todas las alarmas activas.
4. **El reloj**. Puedes ocultarlo con **Mostrar reloj** en **Ajustes → Ajustes de Cora Max**.
5. **La etiqueta de estado** muestra lo que está haciendo esta pantalla ahora mismo. Verde significa que todo va bien, azul que está ocupada, ámbar que hay que echar un vistazo y rojo que hay un fallo. Todos los estados aparecen más abajo.
6. **Batería y Wi-Fi**.
7. **El icono de dispositivos** abre **Dispositivos**, filtrado por este acuario. Un acuario sin dispositivos no lo muestra.
8. **El icono de Reef Buddy** abre el resumen de hoy. Un punto significa que todavía no lo has leído.
9. **El icono de Cora Assistant** empieza una conversación de voz.
10. **El engranaje** abre los ajustes.

:::warning Cora Assistant empieza a escuchar al momento
Tocar el icono de Cora Assistant empieza una sesión de voz en directo. Si querías los ajustes, son el engranaje de la derecha del todo.
:::

### Qué significa la etiqueta de estado {#what-the-status-pill-means}

| Etiqueta | Significado |
|---|---|
| **En línea** | Esta pantalla está recogiendo tus lecturas, y están al día |
| **Nube** | Otro Cora está recogiendo las lecturas de este acuario y esta pantalla las está mostrando. Están tan al día como con **En línea**. Si tienes más de un Cora, el que no las está recogiendo muestra esto |
| **Sondeando Apex**, **Voz activa** | Ocupada con algo ahora mismo (azul) |
| **Sondeo desactivado** | La recogida está desactivada para este acuario. Puedes volver a activarla en Cora Mobile |
| **Actualizando** | La recogida está en pausa mientras se instala una actualización |
| **Desactualizado** | Han dejado de llegar lecturas. La pantalla muestra las últimas que recibió |
| **Reintento de Apex 12s** | Tu Apex no respondió. Cora Max lo vuelve a intentar cuando termina la cuenta atrás |
| **Falló la sincronización con la nube** | Tu Apex respondió, pero sus lecturas no se pudieron guardar en Cora Cloud, así que el panel se queda atrás. Cora Max sigue intentándolo |
| **Guardado en la nube rechazado** | Cora Cloud se niega a guardar algunos datos de esta pantalla. No pasa nada con tu acuario ni con Cora Max, y no hay que cambiar nada en esta pantalla. La solución es una actualización de Cora Cloud. Abre **Ajustes → Ajustes de Cora Max** y baja hasta la sección **Estado**, donde la línea **Guardado en la nube** dice qué datos están afectados. Después [contacta con soporte](/support.html) |
| **Sin conexión** | No hay conexión. La pantalla muestra los últimos datos que recibió |
| **Sin conexión, reintentando en 45s** | Tu red funciona, pero lleva más de 30 segundos sin poder llegar a Cora Cloud. Cora Max se vuelve a conectar sola, y la cuenta atrás muestra cuándo lo intenta de nuevo |
| **Cora principal sin conexión** | Esta pantalla es un segundo Cora Max para este acuario, y el **Cora Max principal** (el fijado para leer los equipos de este acuario) se ha desconectado. Esta pantalla sigue mostrando los últimos datos que tiene hasta que el principal vuelva o elijas otro Cora Max principal. Más información en [Más de un dispositivo Cora](/help/mobile-multi-device) |
| **Contraseña de Apex** | Tu Apex rechazó la contraseña guardada. Echa un vistazo a [Solución de problemas](/help/troubleshooting) |

:::note Cómo funciona la cuenta atrás de reintento
Cora Max intenta volver a conectarse a un ritmo constante. Espera unos 15 segundos después del primer corte, luego otros 15 segundos, luego 30 segundos dos veces y después una vez por minuto hasta que lo consigue. Nunca se rinde. **Sin conexión, reintentando en 45s** es normal.
:::

## El panel {#the-dashboard}

El resto de la pantalla es el panel, una cuadrícula fija que mantiene visibles todos los widgets. No se desplaza.

Los widgets funcionan igual que en tu teléfono, pero lo bastante grandes para leerlos desde unos pasos atrás. Lo que muestra cada forma está en la [Referencia de widgets](/help/mobile-widgets). Para cambiar lo que hay en el panel, consulta [Editar el panel de Cora Max](/help/max-dashboard-editing).

Cada widget con un parámetro medido muestra su **antigüedad** y su **fuente**, igual que en tu teléfono. Un número con `2d` al lado tiene dos días. Las tarjetas de dispositivos y controles muestran su propio estado.

### Cuando la pantalla está atenuada {#when-the-screen-is-dimmed}

Cuando pasa el tiempo de **Atenuar después de** sin que nadie la toque, la pantalla se atenúa. Tu primer toque solo la despierta, así que no puede pulsar un control por accidente. Vuelve a tocar para usar la pantalla.

## El menú del acuario {#the-tank-menu}

![El menú del acuario abierto sobre el panel, con Registrar parámetros, Diario, Reef Buddy y las demás pantallas del acuario](img/max-menu.webp "El menú del acuario, abierto desde el nombre del acuario en la barra superior.")

Toca el nombre del acuario para abrir el menú del acuario que hay en pantalla.

| Elemento | Abre |
|---|---|
| **Registrar parámetros** | Escribe lecturas de kits de pruebas con el teclado en pantalla |
| **Diario** | [El diario](/help/max-records) de este acuario |
| **Reef Buddy** | El último [resumen](/help/max-intelligence) |
| **Informes de salud** | Evaluaciones de salud |
| **Mantenimiento** | La [lista de tareas](/help/max-records) |
| **Informes ICP** | Los [resultados de laboratorio](/help/max-intelligence) subidos |
| **Historial de parámetros** | Elige cualquier parámetro que tenga datos y abre su [gráfico](/help/max-intelligence) |
| **Umbrales de alerta** | El [rango saludable](/help/max-alerts) de cada parámetro de este acuario |
| **Fauna** | El inventario de este acuario, solo de consulta en esta pantalla |
| **Actividad** | [Cada toma, alimentación y dosis](/help/max-activity), y lo que pasó |
| **Diseño del panel** | [Coloca los widgets de esta pantalla](/help/max-dashboard-editing) |
| **Unidades** | Las unidades de visualización de las lecturas de este acuario |
| **Ajustes del acuario** | La pantalla completa de ajustes de este acuario |

## Cambiar de acuario {#switching-tanks}

Toca el **icono de cuadrícula** de la izquierda del todo en la barra superior para ir a [el Cuarto de los Acuarios](/help/max-reef-room), y después abre el acuario que quieras. También puedes deslizar a los lados en el panel. Cada acuario tiene su propio diseño de panel, así que toda la pantalla cambia al pasar de uno a otro.

## El cajón Tomas y alimentación {#the-outlets-feed-drawer}

En un acuario con un Neptune Apex, una pequeña etiqueta **Tomas y alimentación** está en la parte de abajo del panel. Tócala, o desliza hacia arriba en cualquier parte del panel, para abrir **Controles**.

- **ALIMENTACIÓN** empieza uno de los ciclos de alimentación de tu Apex con **A**, **B**, **C** o **D**. **Cancelar** lo termina antes.
- Las **tomas** se pueden cambiar cada una entre Auto, Apagado y Encendido.

Lista las tomas y los ciclos de alimentación que elegiste para este panel, o todos si no elegiste ninguno. Más información en [Tomas y controles](/help/max-controls).

:::warning Este cajón controla equipos reales
Una orden sale en cuanto tocas, pero enviarla no significa que esté hecha. Vuelve como Confirmado, Sin confirmar, Rechazado o Sin cambios, y puedes ver cuál en [Actividad](/help/max-activity). El modo alimentación es la forma segura de detener el caudal para alimentar, porque lo vuelve a poner todo como estaba por sí solo. Un Apagado manual se queda apagado hasta que lo vuelvas a cambiar.
:::

## Si algo no parece estar bien {#if-something-looks-out-of-place}

Si las lecturas parecen antiguas, o la etiqueta de estado está en ámbar o en rojo, empieza por [Solución de problemas](/help/troubleshooting).
