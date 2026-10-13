---
title: Leer tu panel
description: Cómo leer el panel de Cora, desde los widgets, la antigüedad de las lecturas y las fuentes hasta lo que significan los colores y las tarjetas que aparecen y desaparecen.
section: Cora Mobile
reviewed: 2026-10-13
order: 6
group: Your dashboard
---

El panel es una cuadrícula de **widgets** de un acuario. Cada widget muestra una cosa. Tú decides qué va en él, como se explica en [Editar tu panel](/help/mobile-dashboard-editing).

![Un panel de Cora Mobile](img/mobile-dashboard.webp "La cabecera del acuario y la tarjeta de Reef Buddy, y después medidores, valores, gráficos y casillas de dispositivos.")

## La cabecera del acuario {#the-tank-header}

Cada panel empieza con:

- El nombre del acuario, con un pequeño icono al lado. Toca el nombre para cambiar el nombre del acuario. No hace nada más.
- **Alimentar**, solo en un acuario con un Neptune Apex. Abre el **Modo de alimentación** con los ciclos **Feed A** a **Feed D** de tu Apex. Tu Apex decide qué se pausa y cuándo vuelve, según lo configuraste allí. Mientras un ciclo está en marcha, el botón muestra cuál, por ejemplo **Feed A**. Tócalo y elige **Cancelar alimentación** para terminarlo antes. Fuera de casa, un Cora Max del acuario envía la orden por ti.
- El icono del periódico, que abre el último resumen de **Reef Buddy**.
- El icono de compartir, que crea una instantánea del acuario. Consulta [Compartir tu acuario](/help/mobile-sharing).
- La regla, que abre **Unidades** para este acuario. Consulta [El perfil de tu acuario](/help/mobile-tank-profile#units).
- El lápiz de la derecha, que abre [el perfil del acuario](/help/mobile-tank-profile).

:::note Tres controles que se parecen
El nombre del acuario cambia el nombre del acuario. El lápiz de la derecha abre el **perfil** del acuario. Para editar el propio panel, toca **Editar panel** justo debajo de los widgets.
:::

Si tienes más de un acuario, desliza hacia los lados para pasar de uno a otro. Consulta [Gestionar tus acuarios](/help/mobile-tanks).

## La tarjeta de Reef Buddy {#the-reef-buddy-card}

Encima de los widgets, una tarjeta resume el último resumen. Muestra el titular, una puntuación sobre 100 cuando Cora tiene datos suficientes, la fecha del resumen y cuántos análisis y lecturas que se desvían hay. Tócala para abrir el resumen completo, o ciérrala con **×**. Con el siguiente resumen aparece una tarjeta nueva. Más información en [Reef Buddy](/help/mobile-reef-buddy).

## Cómo leer un widget de parámetro {#how-to-read-a-parameter-widget}

Un widget de un **parámetro medido** siempre muestra las mismas tres cosas en el mismo sitio. Las casillas de dispositivos y controles, como una toma, una unidad de dosificación o una bomba, muestran su propio estado, porque no hay una sola lectura detrás.

El valor es la propia lectura, en grande y en el centro.

La antigüedad aparece debajo o al lado, como `now`, `1h` o `2d`. Indica cuánto hace que la fuente confirmó ese valor por última vez, no cuándo se actualizó la pantalla. En una sonda, es cuándo se comunicó su dispositivo por última vez, así que una lectura estable de una sonda que funciona sigue reciente aunque el número no cambie. En un resultado de kit de pruebas o de ICP, es cuándo hiciste la prueba. Una antigüedad que no para de crecer en una sonda significa que su dispositivo ha dejado de informar.

La insignia de fuente es la pequeña marca junto a la antigüedad. Indica de dónde viene el número: una sonda, un controlador, un resultado de laboratorio o tú con un kit de pruebas. Toca el widget para ver la fuente escrita, con su historial reciente.

:::note Por qué importa la antigüedad
Una lectura de alcalinidad perfecta de hace cuatro días no es tu alcalinidad de hoy. Cada valor muestra su antigüedad para que veas la diferencia enseguida.
:::

## Colores {#colours}

Cora usa pocos colores, y cada uno significa siempre lo mismo:

| Color | Significado |
|---|---|
| Verde | Bien dentro del rango de este parámetro |
| Ámbar | Cerca de un límite. **Normalmente aún dentro del rango**, en su última décima parte |
| Rojo | Fuera del límite, y conviene hacer algo |
| Gris | Sin valoración. No hay lectura reciente, o no hay un rango útil con el que valorarla |

:::note Ámbar suele querer decir "bien por ahora, pero desviándose"
El ámbar es un margen. Una lectura que está dentro de su rango, pero en su último 10 %, se pone en ámbar, para que veas la desviación cuando todavía hay tiempo de actuar.

Hay dos matices.

**Un rango que fijas tú es un límite firme.** Si lo cruzas, el widget pasa directamente a rojo, sin margen ámbar. Un rango **que propone Cora** es más flexible. Al cruzarlo se muestra en ámbar durante el primer 10 % fuera del límite, y en rojo a partir de ahí.

**Un límite de un solo lado**, como un máximo para un contaminante o un mínimo para un nutriente, solo se valora por su extremo superior. Así que el cobre a cero sale en verde y no se pone en ámbar por estar cerca del fondo de la escala.
:::

Un widget con borde ámbar o rojo necesita atención. El borde rodea todo el widget, así que lo verás mientras te desplazas.

Para cambiar un rango, mantén pulsado el widget. Más información en [Alertas y umbrales](/help/mobile-alerts).

## Tarjetas que aparecen y desaparecen {#cards-that-come-and-go}

Algunas tarjetas solo aparecen cuando hay algo que decir. La mayoría están entre la cabecera y los widgets.

| Tarjeta | Cuándo aparece | Qué tocar |
|---|---|---|
| **¿Estás empezando un acuario nuevo?** | En un acuario sin ninguna lectura. Cuando empiezas, pasa a ser **Continuar el ciclado** | La tarjeta, para empezar el ciclado guiado. Consulta [Itinerarios guiados](/help/mobile-journeys) |
| **Parámetros del acuario** con *Aún no hay lecturas* | El acuario todavía no tiene lecturas | **Configurar acuario** |
| *No se pudo acceder a tus lecturas: mostrando lo que hay en caché.* | Cora no puede cargar las últimas lecturas, a menudo por falta de conexión | **Reintentar** |
| **Un resultado de laboratorio de {lab} te está esperando.** | Un laboratorio envió un resultado y Cora necesita saber de qué acuario es | **Elegir acuario**. Consulta [ICP e informes de salud](/help/mobile-icp-health) |
| Aviso del perfil (**Desbloquea perspectivas más inteligentes**) | El perfil del acuario está completo en menos de un 80 % | La tarjeta, para seguir con el perfil |
| **Prueba de Cora Pro: quedan 9 días** | Los últimos días de tu prueba gratuita | La tarjeta, o **Mantener Pro**. Consulta [Planes y suscripciones](/help/mobile-plans) |
| **Reef Buddy** | Hay un resumen listo | La tarjeta |
| **¿Cómo alimentas normalmente?** | No has configurado una rutina de alimentación | **Configurar rutina** |
| *Las lecturas de Red Sea han dejado de actualizarse.* | Nada está leyendo los equipos Red Sea de este acuario | Consulta [Alertas y umbrales](/help/mobile-alerts) |
| **Cámaras** (Beta) | El acuario tiene una cámara, debajo de los widgets. Las cámaras solo están abiertas a los usuarios Beta | **Ver en vivo** |
| **Registra tu primera prueba de agua** | Sin lecturas y sin equipos vinculados, debajo de los widgets | La tarjeta. Consulta [Configurar Cora Mobile](/help/mobile-setup#the-first-test-card) |

## Debajo de los widgets {#below-the-widgets}

![El final del panel en Cora Mobile](img/mobile-dashboard-foot.webp "Editar panel, los botones Registrar parámetros, Historial de parámetros y Alimentación, y accesos directos a las cuatro áreas de registro.")

De arriba abajo encontrarás:

- Una línea que dice cuándo se actualizó el panel por última vez y qué fuentes usó, con **Editar panel** al lado. Abre el [editor del panel](/help/mobile-dashboard-editing).
- La tarjeta **Registra tu primera prueba de agua**, en un acuario sin lecturas y sin equipos vinculados.
- **Registrar parámetros**, para anotar a mano las lecturas de tus kits de pruebas.
- **Historial de parámetros**, para abrir el historial de cualquier parámetro que tenga datos, aunque no tenga widget. Consulta [Ver un parámetro a fondo](/help/mobile-metric-detail).
- **Alimentación**, para anotar una comida que se sale de tu rutina. Consulta [El diario](/help/mobile-journal).
- **Diario · Alertas · Mantenimiento · Fauna**, accesos directos a esas áreas de este acuario.

## Tocar y mantener pulsado {#tapping-through}

Toca cualquier widget de parámetro para abrir su detalle. Verás todo el historial en un gráfico, cada fuente que lo ha informado y tu banda de alerta. Desde ahí puedes comparar fuentes, excluir una lectura errónea o registrar el cuidado de una sonda. Consulta [Ver un parámetro a fondo](/help/mobile-metric-detail).

**Mantén pulsado** un widget de parámetro para fijar su rango de alerta directamente desde el panel.

## Si un widget no muestra ningún valor {#if-a-widget-has-no-value}

Un widget muestra un valor en cuanto recibe uno. Si está vacío, suele ser por una de estas razones:

- El dispositivo está desconectado. Revisa la pestaña **Dispositivos**.
- El parámetro todavía no tiene fuente. Regístralo a mano o conecta un equipo que lo informe.
- Nunca se ha informado ni registrado nada de ese parámetro.

Una lectura antigua no desaparece solo porque sea más antigua que la ventana del gráfico. Se queda en el widget con su antigüedad, así que un valor viejo parece viejo y no parece que falte.

Para cualquier otra cosa, consulta [Solución de problemas](/help/troubleshooting#a-widget-shows-no-value).
