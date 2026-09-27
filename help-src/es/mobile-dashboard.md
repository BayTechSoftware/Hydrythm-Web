---
title: Leer tu panel
description: Cómo leer el panel de Cora: widgets, antigüedad de las lecturas, fuentes y significado de los colores.
section: Cora Mobile
reviewed: 2026-09-09
order: 5
group: Your dashboard
---

El panel es una cuadrícula de **widgets**. Cada uno muestra un dato de un acuario, y tú decides qué widgets pones. Más información en **[Editar tu panel](/help/mobile-dashboard-editing)**.

![Un panel de Cora Mobile](img/mobile-dashboard.webp "Medidores, números, tendencias y controles en una sola pantalla.")

## La cabecera del acuario

Arriba del todo, en cada panel, tienes:

- **El nombre del acuario**, con un pequeño icono al lado. Ese icono es para **cambiar el nombre** y nada más
- **Alimentar**: detiene el caudal y el skimmer durante la alimentación y luego lo deja todo como estaba
- **Reef Buddy**: abre el resumen de esta mañana
- **Compartir**: envía una captura del panel
- **El lápiz de la derecha**: abre [el perfil del acuario](/help/mobile-tank-profile)

:::note Tres botones parecidos que hacen cosas distintas
El icono junto al nombre cambia el nombre del acuario. El lápiz de la derecha abre el **perfil** del acuario. Para editar el panel en sí, usa **Editar panel**, que está al *final* del panel, debajo de los widgets.
:::

Si tienes más de un acuario, desliza hacia los lados para pasar de uno a otro.

## La tarjeta de Reef Buddy

Debajo de la cabecera hay una tarjeta con el último resumen. Muestra un titular, las puntuaciones de **Estabilidad** y **Datos** y el número de análisis. Tócala para abrir el resumen completo o ciérrala con **×**. Con el siguiente resumen aparece una tarjeta nueva.

## Cómo leer un widget de parámetro

Los widgets de un **parámetro medido** muestran siempre tres cosas en el mismo sitio. Las casillas de dispositivos y controles (una toma, una unidad de dosificación, una bomba) muestran su estado, porque no dependen de una sola lectura.

**El valor** es la lectura, en grande y en el centro.

**La antigüedad** aparece debajo o al lado: `now`, `1h`, `2d`. Indica cuánto hace que se tomó la lectura, no cuándo se actualizó la pantalla. Si un número lleva dos días sin cambiar, verás `2d`, y eso también te dice algo.

**La insignia de fuente** es la pequeña marca junto a la antigüedad. Indica de dónde viene el número: una sonda, un controlador, un resultado de laboratorio o tu propio kit de pruebas. Toca cualquier widget para ver la fuente con detalle y su historial reciente.

:::note La antigüedad importa
Una lectura de alcalinidad perfecta de hace cuatro días no es tu alcalinidad de hoy. Por eso cada valor lleva su antigüedad al lado, para que lo veas de un vistazo.
:::

## Colores

Cora usa pocos colores, y cada uno significa siempre lo mismo:

| Color | Significado |
|---|---|
| Verde | Bien dentro del rango de este parámetro |
| Ámbar | Cerca de un límite. **Normalmente aún dentro del rango**, en su último 10 % |
| Rojo | Fuera del límite. Conviene hacer algo |
| Gris | Sin valoración. No hay lectura reciente o no hay un rango con el que comparar |

:::note Ámbar suele querer decir "bien, pero cambiando"
El ámbar es un *margen de aviso*. Una lectura que está dentro de su rango, pero en el último 10 %, se marca en ámbar. Así ves que el valor se está desviando cuando todavía tienes tiempo de reaccionar, antes de que sea un problema.

Hay dos detalles más.

**Un rango que fijas tú es un límite firme.** Si la lectura lo pasa, el widget se pone directamente en rojo, sin margen ámbar, porque esa línea la has puesto tú. Un rango **que propone Cora** es una referencia más flexible. Durante el primer 10 % fuera del límite se muestra en ámbar, y a partir de ahí en rojo.

**Un límite de un solo lado** (un máximo para un contaminante o un mínimo para un nutriente) solo se valora por su extremo superior. Por eso el cobre a cero sale en verde y no en ámbar por estar cerca del mínimo de la escala.
:::

Un widget con borde ámbar o rojo necesita tu atención. El borde rodea todo el widget, así que lo ves aunque estés desplazándote.

## Debajo de los widgets

![El final del panel](img/mobile-dashboard-foot.webp "Editar panel, Registrar parámetros y accesos directos a las cuatro áreas de registro.")

Al final del panel tienes:

- **Editar panel**: abre el [editor del panel](/help/mobile-dashboard-editing)
- **Registrar parámetros**: para anotar a mano las lecturas de tus kits de pruebas
- **Diario · Alertas · Mantenimiento · Fauna**: accesos directos a esas secciones de este acuario

Encima hay una línea que indica cuándo se actualizó el panel por última vez y de qué fuentes tomó los datos.

## Ver más detalle

Toca cualquier widget para abrir su detalle. Verás todo el historial en un gráfico, cada fuente que ha enviado ese dato y los umbrales que se aplican ahora. Desde ahí puedes anotar una lectura a mano, cambiar el rango o ver datos más antiguos.

## Si un widget no muestra ningún valor

Un widget muestra un valor en cuanto recibe uno. Si está vacío, suele ser por una de estas razones:

- El dispositivo está desconectado. Revisa la pestaña **Dispositivos**
- El parámetro todavía no tiene fuente. Regístralo a mano o conecta un equipo que lo mida
- Nunca se ha enviado ni registrado ese parámetro, así que aún no hay nada guardado

Una lectura antigua no desaparece aunque el gráfico abarque menos tiempo que su antigüedad. Se queda en el widget con su antigüedad, así sabes que es un dato viejo y no que falta.

Para cualquier otro problema, consulta **[Solución de problemas](/help/troubleshooting)**.
