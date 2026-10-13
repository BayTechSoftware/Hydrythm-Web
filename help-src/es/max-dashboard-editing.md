---
title: Editar el panel de Cora Max
description: Añade, mueve y quita casillas en el panel de Cora Max, elige una cuadrícula, usa plantillas o Diseñar con IA y guarda diseños para reutilizarlos en cualquier Cora Max.
section: Cora Max
reviewed: 2026-10-13
order: 4
group: Your dashboard
twin: mobile-dashboard-editing
---

Esta página explica cómo colocar las casillas de un panel de Cora Max. Usa una **cuadrícula fija**: la pantalla no se desplaza, así que todas las casillas tienen que caber en una sola pantalla. Es la principal diferencia con el panel del teléfono.

Abre el editor desde el **menú del acuario**: toca el nombre del acuario en la barra superior y después **Diseño del panel**. También está en **Ajustes → [tu acuario] → Diseño del panel**.

![El editor del panel en Cora Max](img/max-dashboard-editor.webp "Los tamaños de cuadrícula arriba y después las casillas. Es una pantalla de diseño, así que cada casilla muestra su tipo y su fuente en lugar de una lectura. No se guarda nada hasta que pulsas Guardar.")

:::tip También puedes editarlo desde tu teléfono
En Cora Mobile, abre la pestaña **Dispositivos**, toca tu Cora Max y después toca **Diseño del panel** en la tarjeta del acuario. Es más rápido que colocar casillas a mano en una pantalla de pared, y el resultado aparece en Cora Max en cuanto guardas.
:::

## Elegir una cuadrícula {#choosing-a-grid}

Elige primero el tamaño de la cuadrícula. Cambiarlo después mueve todas las casillas.

| Cuadrícula | Casillas | Cómo se ve |
|---|---|---|
| 2×2, 3×2, 3×3 | 4–9 | Grande. Fácil de leer desde el otro lado de la habitación. |
| 4×4, 5×3, 6×4 | 16–24 | La opción habitual para un sistema completo. |
| 6×5, 8×4, 8×5 | 30–40 | Densa. Todo un cuarto de acuarios en una pantalla. |
| 9×5, 10×5 | 45–50 | Muy densa. Mejor en las pantallas más grandes. |
| **Auto** | hasta 32 | Cora elige una forma que encaje con las casillas que hayas añadido. |

Una cuadrícula fija admite tantas casillas como celdas tiene, hasta 50 en 10×5. **Auto** tiene su propio límite de 32 casillas. Por encima de eso, el texto queda demasiado pequeño para leerlo a distancia.

:::note ¿No lo tienes claro? Empieza con Auto
Añade las casillas que quieras y deja la cuadrícula en **Auto**. Cora elige una forma que encaje. Si te gusta, después puedes cambiar a esa forma fija.
:::

:::warning Cambiar la cuadrícula solo quita casillas cuando no caben
Cuando cambias la cuadrícula, Cora no descarta casillas según su posición. Las casillas que siguen teniendo una celda válida se quedan donde están, y el resto se vuelven a colocar, en orden. Solo pierdes casillas cuando la cuadrícula nueva tiene **menos celdas que casillas tienes**, y Cora te dice cuántas se han quitado. Pasar de 10×5 (50 celdas) a 3×3 (9) quita la mayoría.
:::

## Añadir y colocar casillas {#adding-and-arranging}

1. Toca una celda vacía (muestra un **+**) para abrir **Añadir widget**.
2. En **TIPO**, elige el tipo de casilla, y después qué muestra (una lectura, una toma, un dispositivo o una escena).
3. En **TAMAÑO**, elige lo grande que es. Una casilla puede ocupar una o dos celdas de ancho y una o dos de alto. Un Gráfico también tiene un **RANGO DE TIEMPO**. Una casilla de dosificadora tiene **Mostrar lo restante como**, en **Días** o **Mililitros (mL)**.
4. Toca **Agregar**.

Los gestos aparecen arriba en el editor: **toca un mosaico para editar**, **mantén pulsado para mover** y **✕ para eliminar**. **Vaciar todo** vacía la cuadrícula para que empieces de nuevo.

Los dieciséis tipos de casilla son Valor, Medidor, Gráfico, Estado, Toma, Escena, ReefBeat, Módulo del Apex, Jecod, Maxspect *(Beta)*, GHL *(Beta)*, HYDROS *(Beta)*, Radion *(Beta)*, VorTech *(Beta)*, Versa *(Beta)* y Cámara *(Beta)*. Los encontrarás en la [Referencia de widgets](/help/mobile-widgets). La casilla **Escena** solo existe en Cora Max. Ejecuta una [escena](/help/max-automation) con un toque.

:::note Beta
**Beta.** Maxspect, GHL, HYDROS, EcoTech (Radion, VorTech, Versa) y las cámaras están en Beta y solo están abiertos a los usuarios Beta. Si no eres usuario Beta, no los verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html). Sus casillas solo aparecen cuando tienes el dispositivo. Más información en [Funciones Beta](/help/mobile-beta).
:::

## Tomas y alimentación {#outlets-feed}

**Tomas y alimentación** en el editor elige qué tomas y ciclos de alimentación aparecen en **Controles**, el cajón que abres deslizando hacia arriba desde la parte de abajo del panel. No añade casillas. Si no eliges ninguno, Controles los lista todos. Para poner una toma en la propia cuadrícula, añade una casilla **Toma**. Más información en [Tomas y controles](/help/max-controls).

## Plantillas {#templates}

**Plantillas** está arriba en el editor, junto a **Mis paneles** y **Diseñar con IA**. Está disponible en todos los planes y nunca usa IA, así que también funciona sin el uso compartido de datos con la IA.

Abre **Plantillas de panel**, unos cuantos diseños ya hechos a partir de lo que este acuario informa y tiene vinculado:

- **Resumen**: pocas casillas grandes, con los parámetros principales como medidores y tus dispositivos principales
- **Equipo**: primero una casilla por dispositivo, y después las tomas y los parámetros principales
- **Parámetros**: primero los gráficos y las lecturas, y al final los dispositivos y las tomas
- **Cámara**: una vista grande en directo arriba a la izquierda con los parámetros principales al lado. Solo aparece cuando el acuario tiene una cámara. Las cámaras están en Beta y solo están abiertas a los usuarios Beta.

Cada una muestra una vista previa y cuántas casillas tiene y en qué cuadrícula. Toca **Usar este**. Cora pregunta antes **¿Sustituir tu panel?** Toca **Guardar antes el actual como preajuste** si quieres conservar el diseño que tienes, o **Sustituir**. No se guarda nada hasta que pulsas **Guardar**.

## Diseñar con IA {#design-with-ai}

El editor tiene un botón **Diseñar con IA**. Funciona con un plan de pago y durante la prueba gratuita. Cora propone un diseño completo a partir de lo que este acuario informa y tiene vinculado, y muestra cuántas casillas tiene y en qué cuadrícula. Toca **Usar este** para ponerlo en el editor, o **Intentar de nuevo** para ver otro. Puedes hacer 5 diseños por acuario al día.

Un diseño con IA sustituye lo que hay ahora en este panel. No se guarda nada hasta que pulsas **Guardar**, y antes puedes conservar tu diseño actual guardándolo en **Mis paneles**. En el plan gratuito, **Diseñar con IA** te lleva a los planes. También necesita que el uso compartido de datos con la IA esté activado en Cora Mobile. Más información en [Preguntar a Cora](/help/mobile-assistant).

## Diseñar para leer a distancia {#designing-for-distance}

Una pantalla de pared se lee desde más lejos que un teléfono, y normalmente de un vistazo.

- Pon tus parámetros clave de dos por dos. La alcalinidad, la temperatura y el pH son cosas que querrás leer sin acercarte.
- Pon los controles en los bordes. Las casillas de tomas son las que vas a tocar, y en los laterales es más fácil acertar.
- Agrupa las casillas por tema. Pon junto todo lo de la dosificación y todo lo del caudal, porque una pared se recorre por zonas.
- Deja pequeños los oligoelementos. Ellos y otros números que cambian despacio son de consulta, así que basta con una casilla de valor de uno por uno.

## Guardar y reutilizar diseños {#saving-layouts}

Nada de lo que hagas en el editor se aplica hasta que pulsas **Guardar**. Si sales con cambios sin guardar, Cora pregunta antes **¿Descartar cambios?**

**Mis paneles** guarda los diseños a los que quieres volver. Se guardan en tu cuenta, no en esta pantalla, así que cualquier Cora Max de tu cuenta puede cargarlos, para otro acuario o para una pantalla de sustitución.

- **Guardar este diseño** guarda lo que hay en el editor. Puedes guardar hasta 30.
- **Cargar** pone un diseño guardado en el editor. Los diseños guardados desde tu teléfono llevan la marca **Teléfono**.
- Antes de cargar, Cora te dice cuántas casillas van a pasar. Lo que no puede pasar, como una lectura que este acuario no informa o un dispositivo que no está en este acuario, aparece en **Se quedan fuera:** con el motivo.

Por ejemplo, puedes tener un diseño denso para el día a día y otro de casillas grandes para cuando trabajas en el acuario.

## Varios acuarios {#multiple-tanks}

Cada acuario tiene su propio diseño. Cambia a ese acuario y abre **Diseño del panel** desde su menú del acuario, o usa **Ajustes → [ese acuario] → Diseño del panel**.
