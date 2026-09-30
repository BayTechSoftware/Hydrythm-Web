---
title: Alertas y umbrales
description: Fija el rango de cada parámetro, elige qué avisos recibes y entiende por qué saltó una alerta.
section: Cora Mobile
reviewed: 2026-09-30
order: 15
group: Alerts and automation
---

Cuando una lectura sale del rango que fijaste, Cora genera una alerta. Tú decides los rangos y también qué alertas llegan a tu teléfono.

El **Centro de alertas** se abre desde la fila de accesos directos, en la parte inferior del panel.

![El Centro de alertas](img/mobile-alerts.webp "Alertas activas, cada una con su gravedad, qué la activó, y cuándo.")

## El Centro de alertas

Tiene dos pestañas:

- **Activas**: las alertas que siguen abiertas, con un número que indica cuántas hay
- **Reglas**: los umbrales y las reglas de velocidad de cambio que las generan

En cada alerta activa ves el parámetro y el acuario, la lectura que la activó y una explicación sencilla. También ves una etiqueta con la gravedad, el tipo de regla (**Umbral** o **Tasa de cambio**) y la hora.

Cada una tiene dos botones:

- **Ver regla**: abre la regla que generó la alerta para que ajustes el rango
- **Explicar esta alerta**: le pide al asistente que la interprete con el historial de tu acuario

## Fijar un rango

Los parámetros que Cora puede valorar tienen un rango objetivo. Los valores iniciales salen del tipo y la antigüedad del acuario que indicaste al configurarlo, y suelen ser un buen punto de partida. Si un parámetro no tiene un rango útil, Cora no lo valora. Se queda en gris neutro y Cora no intenta adivinar.

Para cambiar un rango, **mantén pulsado el widget** del parámetro en el panel. Se abren directamente sus umbrales. Con un toque normal se abre la vista del parámetro. Vale la pena recordar el gesto de mantener pulsado.

Si el parámetro todavía no tiene regla, los campos muestran el valor predeterminado de Cora y una nota debajo te lo indica. Cambia cualquier valor para fijar el tuyo.

Para verlos todos juntos, toca **Alertas** en la fila de botones bajo el panel.

Puedes fijar:

- **Un rango**: un mínimo y un máximo, para parámetros como la alcalinidad o la temperatura
- **Un techo**: solo un máximo, para parámetros en los que un valor bajo no es problema, como el nitrato o el fosfato
- **Un suelo**: solo un mínimo

:::tip Usa el rango real de tu acuario
Los valores predeterminados son solo un punto de partida. Si tu acuario funciona bien con pocos nutrientes a 6 dKH, no está "mal" porque una tabla diga 8–9. Fija el rango con el que trabajas y Cora te avisará cuando *tú* te salgas de él.
:::

## Qué activa una alerta

Una alerta salta cuando una lectura cruza un umbral. Cora revisa cada lectura en cuanto llega, así que basta una sola lectura fuera de rango.

Mientras una alerta está activa, Cora no te avisa una y otra vez por lo mismo. Hay un tiempo de espera antes de que pueda volver a avisarte. Además, la alerta **se cierra sola** en cuanto una lectura vuelve al rango. No tienes que confirmar nada.

También puedes crear una regla de **tasa de cambio**. Esta regla vigila lo rápido que se mueve un parámetro, no el valor que tiene ahora. Úsala cuando importa más la velocidad del cambio que el número.

## Dónde aparecen las alertas

- **La campana**, arriba a la derecha en todas las pantallas, guarda tu historial. El número indica cuántas no has leído.
- **Las notificaciones push** llegan a tu teléfono si les das permiso.
- **El widget** del panel se pone ámbar o rojo.
- **Cora Max** muestra las mismas alertas en la pantalla grande.

## Cuando un equipo necesita atención

Algunas alertas tratan de un equipo y no de una lectura. Si un dispositivo como un Trident o una bomba Jecod informa de un fallo, Cora te envía una notificación con el nombre del acuario y del dispositivo, por ejemplo *"Acuario principal: la bomba de retorno necesita atención"*. La notificación también dice qué pasa, como un rotor atascado. Cuando el fallo se resuelve, llega otra que dice *"Acuario principal: la bomba de retorno vuelve a estar bien"*. Las dos pertenecen a **Fallas de equipos**, en **Ajustes → Notificaciones**.

Un gyre Maxspect (beta) puede generar la misma alerta. Pasa cuando un Cora Max de su red encuentra los dos cabezales al 0 % o el gyre no responde dos veces seguidas. Tómalo como un aviso y no como una protección. Cora Max lo comprueba de vez en cuando, no sin parar, y solo mientras está encendido y puede llegar al gyre.

## Un dispositivo ha dejado de informar

Si un Neptune Apex, un equipo Red Sea ReefBeat, un AquaWiz, una bomba Jecod o un gyre Maxspect deja de responder, Cora te avisa: *"[Dispositivo]: ha dejado de informar"*. Revisa su alimentación y su Wi-Fi, y comprueba que el Cora Max que lo lee esté encendido. La mayoría de los equipos reciben este aviso a los 30 minutos sin una actualización nueva. AquaWiz consulta con menos frecuencia, así que espera unas 3 horas. Recibes una segunda notificación en cuanto vuelve a informar.

Esto pertenece a **Fallas de equipos**, en **Ajustes → Notificaciones**, junto con las alertas de fallos anteriores.

## "Las lecturas de Red Sea han dejado de actualizarse"

Es posible que veas este aviso en la página de parámetros de un acuario:

> Las lecturas de Red Sea han dejado de actualizarse. Ningún dispositivo está leyendo los equipos Red Sea de este acuario: revisa el Cora Max principal en Ajustes o abre este acuario en un dispositivo conectado a la misma red Wi-Fi.

Quiere decir que ahora mismo ningún teléfono ni Cora Max consulta el equipo ReefBeat de ese acuario. Las lecturas que ves son antiguas, pero no tienen por qué estar mal. Toca el aviso para abrir **Cora Max principal**. Ahí elige un dispositivo que esté encendido o selecciona **Cualquiera activo (automático)**. Más información en [Más de un dispositivo Cora](/help/mobile-multi-device). Si el aviso no desaparece, consulta [Solución de problemas](/help/troubleshooting).

## Elegir qué te llega

**Ajustes → Notificaciones.** Aquí decides:

- Qué categorías de notificación pueden enviarte avisos push

Reef Buddy no tiene un interruptor propio. Te envía un resumen cuando hay algo que merece tu atención y no dice nada cuando no lo hay.

:::note Cora prefiere no molestar
El resumen diario es un solo aviso por acuario y día. Si ese día no hay nada que requiera tu atención, lo normal es que no llegue ningún mensaje para decirte que todo va bien. Si Cora te avisa, es que algo ha cambiado.
:::

## Tiempos de espera: cada cuánto puede avisarte la misma alerta

Cada regla tiene su propio **Tiempo de espera entre alertas**. Lo fijas al añadir o editar la regla, en la pestaña **Reglas** del Centro de alertas. El tiempo de espera no oculta la alerta. Solo limita cada cuánto te envía Cora un aviso push sobre ella. La lectura se sigue valorando, y la alerta sigue visible en el widget y en la campana todo el tiempo.

Puedes elegir 15 min, 30 min, 1 h, 2 h, 4 h, 8 h, 1 día, 3 días o **1 semana**.

Un tiempo corto va bien con lecturas que cambian rápido, como la temperatura. Uno largo, de hasta una semana, sirve para algo que va a seguir mal varios días mientras esperas una pieza. Por ejemplo, un Trident sin reactivo o un recipiente de dosificación vacío. Con un tiempo de espera corto, Cora te avisaría varias veces al día de un problema que ya conoces.

:::note Posponer una alerta activa se hace en Cora Max
Cora Mobile no tiene un botón para posponer una alerta activa. Ese botón está en la pantalla de Cora Max junto al acuario, y silencia la alerta durante el tiempo de espera que elegiste aquí. Desde el teléfono, para cambiar cada cuánto te avisa Cora de algo, ajusta el tiempo de espera de la regla.
:::

## Cerrar una alerta

Una alerta se cierra cuando la lectura vuelve al rango. No hay nada que descartar. La alerta describe el estado del acuario, no es una tarea pendiente.

:::note Una lectura suelta basta para generar una alerta
Una sola lectura fuera de rango genera una alerta, así que un pico de una sonda también la activa. Si una fuente no es fiable, recalíbrala o haz que el widget use otra fuente. No amplíes el umbral para evitarlo.
:::

Si el problema está en la lectura y no en el acuario (por ejemplo, una sonda sin calibrar), arregla la fuente. Si amplías un umbral para silenciar una sonda defectuosa, también te perderás el próximo problema real.

## Desactivar las alertas de un parámetro

Abre la regla en la pestaña **Reglas** del Centro de alertas y apaga su **interruptor de activación**. La regla y su rango se guardan, así que puedes volver a activarla sin crearla de nuevo.

:::warning Silencia un parámetro sin borrar su rango
Si eliminas un umbral, Cora puede seguir valorando esa lectura. Las bandas de referencia predeterminadas siguen dando color al valor y pueden seguir apareciendo en el resumen. Usa el interruptor de activación de la regla.
:::
