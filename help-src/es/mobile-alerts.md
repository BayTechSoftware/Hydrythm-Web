---
title: Alertas y umbrales
description: Fija el rango de cada parámetro, elige de qué te avisan y entiende por qué se activó una alerta.
section: Cora Mobile
reviewed: 2026-09-27
order: 15
group: Alerts and automation
---

Una alerta se genera cuando una lectura sale del rango que fijaste para ella. Tú fijas los rangos, y tú controlas qué alertas llegan a tu teléfono.

Abre el **Centro de alertas** desde la fila de accesos directos en la parte inferior del panel.

![El Centro de alertas](img/mobile-alerts.webp "Alertas activas, cada una con su gravedad, qué la activó, y cuándo.")

## El Centro de alertas

Dos pestañas:

- **Activas**: alertas generadas en este momento, con una insignia de recuento
- **Reglas**: los umbrales y las reglas de velocidad de cambio que las producen

Cada alerta activa muestra el parámetro y el acuario, la lectura que la activó, una explicación sencilla, un chip de gravedad, el tipo de regla que se activó (**Umbral** o **Tasa de cambio**), y la hora en que se activó.

Dos acciones en cada una:

- **Ver regla**: abre la regla que la generó, para que puedas ajustar el rango
- **Explicar esta alerta**: le pide al Asistente que la interprete frente al historial de tu acuario

## Fijar un rango

Los parámetros que Cora puede calificar tienen un rango objetivo, y los valores predeterminados vienen del tipo y la antigüedad de tu acuario cuando lo configuraste, normalmente un punto de partida razonable. Un parámetro sin rango utilizable no se califica en absoluto: se queda en gris neutro en lugar de adivinarse.

Para cambiar uno: **mantén pulsado su widget** en el panel, lo que abre directamente los umbrales de ese parámetro. Un toque simple abre en cambio la vista del parámetro; los dos gestos van a lugares distintos, y mantener pulsado es el atajo que vale la pena recordar.

Si el parámetro todavía no tiene regla, los campos empiezan con el valor predeterminado de Cora, y una nota debajo lo indica. Cambia cualquier valor para fijar el tuyo.

Para verlos todos juntos, usa **Alertas** en la fila de botones bajo el panel.

Puedes fijar:

- **Un rango**: un mínimo y un máximo, para cosas como alcalinidad o temperatura
- **Un techo**: solo un máximo, para cosas donde un valor bajo está bien, como nitrato o fosfato
- **Un suelo**: solo un mínimo

:::tip Fija el rango en el que realmente funciona tu acuario
Los valores predeterminados son un punto de partida, no un veredicto. Un acuario que funciona bajo en nutrientes a 6 dKH no está "mal" porque un gráfico diga 8-9. Fija el rango en el que realmente funcionas, y Cora te avisará cuando *tú* te desvíes.
:::

## Qué activa una alerta

Una alerta se activa cuando una lectura cruza un umbral. Cora revisa cada lectura al llegar, así que una sola lectura fuera de tu rango basta para generar una.

Una vez que una alerta está activa, no seguirá avisándote repetidamente sobre lo mismo; hay un tiempo de espera antes de que pueda activarse de nuevo. Y **se cierra sola** en el momento en que una lectura vuelve a estar dentro del rango; no hay nada que reconocer.

También puedes fijar una regla de **tasa de cambio**, que observa la velocidad a la que se mueve un parámetro en lugar de dónde está en este momento. Es la que hay que usar para cosas donde la velocidad del cambio importa más que el número.

## Dónde aparecen las alertas

- **La campana**, arriba a la derecha de cada pantalla, guarda tu historial. El número es cuántas no has leído.
- **Las notificaciones push** llegan a tu teléfono cuando las permites.
- **El widget** se pone ámbar o rojo en el panel.
- **Cora Max** muestra las mismas alertas en la pantalla grande.

## Cuando un equipo necesita atención

Algunas alertas son sobre equipo en lugar de una lectura. Cuando un dispositivo como un Trident o una bomba Jecod informa de un fallo, Cora envía una notificación que nombra el acuario y el dispositivo, por ejemplo *"Acuario principal: la bomba de retorno necesita atención"*, e indica qué está mal, como un rotor atascado. Cuando el fallo se resuelve, sigue una segunda: *"Acuario principal: la bomba de retorno vuelve a estar bien"*. Ambas entran en **Fallas de equipos** en **Ajustes → Notificaciones**.

Un gyre Maxspect (beta) puede generar la misma alerta cuando un Cora Max en su red encuentra los dos cabezales fijados en 0%, o no obtiene respuesta del gyre dos veces seguidas. Trata esto como una advertencia, no como una salvaguarda: el Cora Max comprueba de vez en cuando en lugar de continuamente, y solo mientras está en marcha y puede alcanzar el gyre.

## "Las lecturas de Red Sea han dejado de actualizarse"

Puede que veas este aviso en la página de parámetros de un acuario:

> Las lecturas de Red Sea han dejado de actualizarse. Ningún dispositivo está leyendo los equipos Red Sea de este acuario: revisa el Cora Max principal en Ajustes o abre este acuario en un dispositivo conectado a la misma red Wi-Fi.

Significa que ningún teléfono ni Cora Max está consultando en este momento el equipo ReefBeat de ese acuario, así que las lecturas mostradas son antiguas, no necesariamente incorrectas. Toca el aviso para abrir **Cora Max principal** y elige un dispositivo que esté activo, o fíjalo en **Cualquiera activo (automático)**. Consulta [Más de un dispositivo Cora](/help/mobile-multi-device). Si no se resuelve, consulta [Solución de problemas](/help/troubleshooting).

## Elegir qué te llega

**Ajustes → Notificaciones.** Puedes controlar:

- Cuál de las categorías de notificación puede enviarse

Reef Buddy no tiene un interruptor propio: envía un resumen cuando hay algo que merece la pena atender y se mantiene en silencio cuando no lo hay.

:::note Cora está hecho para mantenerse en silencio
El resumen diario es un aviso por acuario al día, y en un día en que nada necesita tu atención normalmente se mantiene en silencio en lugar de decirte que todo va bien. Si Cora está avisando, algo cambió.
:::

## Tiempos de espera: con qué frecuencia puede avisarte la misma alerta

Cada regla tiene su propio **Tiempo de espera entre alertas**, fijado al añadir o editar la regla (en la pestaña **Reglas** del Centro de alertas). El tiempo de espera no oculta la propia alerta: solo limita con qué frecuencia Cora te envía un aviso sobre ella. La lectura sigue calificada y la alerta sigue visible en el widget y en la campana todo el tiempo.

Puedes elegir entre: 15 min, 30 min, 1 h, 2 h, 4 h, 8 h, 1 día, 3 días, o **1 semana**.

Un tiempo de espera corto conviene a una lectura que cambia rápido, como la temperatura. Uno largo, hasta una semana, conviene a algo que se mantiene mal durante días mientras esperas una pieza, como un Trident sin reactivo o un envase de dosificación vacío: sin un tiempo de espera largo, Cora avisaría varias veces al día sobre el mismo problema conocido.

:::note Posponer una alerta activa vive en Cora Max
Cora Mobile no tiene un botón de Posponer propio en una alerta activa; ese control está en la pantalla de Cora Max del acuario, y silencia la misma alerta durante el tiempo de espera que elegiste aquí. Desde el teléfono, la forma de cambiar con qué frecuencia te avisan de algo es este tiempo de espera por regla, no un aplazamiento por alerta.
:::

## Cerrar una alerta

Una alerta se cierra cuando la lectura vuelve a estar en rango. No hay nada que descartar; es una afirmación sobre el acuario, no una tarea.

:::note Las lecturas puntuales generan alertas
Una sola lectura fuera de rango basta para generar una alerta, así que una sonda que se dispara activará una. Si una fuente no es fiable, recalíbrala o apunta el widget a otra fuente en lugar de ampliar el umbral.
:::

Si una lectura está mal en lugar de que el acuario esté mal (una sonda que necesita calibrarse, por ejemplo), arregla la fuente. Ampliar un umbral para silenciar una sonda defectuosa también oculta el próximo problema real.

## Desactivar alertas para un parámetro

Abre la regla en la pestaña **Reglas** del Centro de alertas y desactiva su **interruptor de activación**. La regla y su rango se conservan, así que puedes volver a activarla sin crearla de nuevo.

:::warning Silencia un parámetro sin eliminar su rango
Eliminar un umbral no necesariamente detiene toda evaluación de esa lectura; las bandas de referencia predeterminadas siguen coloreando el valor y pueden seguir alimentando el resumen. Usa el interruptor de activación de la regla.
:::
