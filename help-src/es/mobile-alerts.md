---
title: Alertas y umbrales
description: Fija el rango saludable de cada lectura, elige cada cuánto puede avisarte una alerta y descubre por qué un dispositivo "dejó de informar".
section: Cora Mobile
reviewed: 2026-10-17
order: 22
group: Alerts and automation
twin: max-alerts
---

Recibes una alerta cuando una lectura sale del rango que fijaste para ella. Esta página explica cómo fijar esos rangos, qué pasa cuando salta una alerta y cuánto espera Cora antes de decir que un dispositivo ha dejado de informar.

Para abrir el **Centro de alertas**, toca **Alertas** en la fila de botones que hay debajo del panel. También está en Ajustes → tu acuario → **Umbrales de alerta**.

![La pestaña Activas del Centro de alertas en Cora Mobile](img/mobile-alerts.webp "Las alertas activas, cada una con su gravedad, qué la activó y cuándo, además de Ver regla y Explicar esta alerta.")

## El Centro de alertas {#alert-center}

Tiene dos pestañas. **Activas** lista las alertas que están saltando ahora mismo, con un contador. **Reglas** guarda las reglas que las generan.

Cada alerta activa muestra el parámetro y el acuario, la lectura que la provocó, una breve explicación, una etiqueta de gravedad, el tipo de regla que saltó (**Umbral** o **Tasa de cambio**) y cuándo saltó. Tiene dos botones:

- **Ver regla** abre la regla que hay detrás, para que puedas ajustar el rango. En una alerta de dosificadora, como un cabezal DŌS o ReefDose con poco líquido o una dosis omitida, este botón es **Abrir dosificadora**. Abre la página de esa dosificadora con sus alertas.
- **Explicar esta alerta** abre Cora Assistant con una pregunta sobre la alerta lista para enviar. Revísala, cámbiala si quieres y envíala.

## La pestaña Reglas {#rules}

![La pestaña Reglas](img/mobile-alert-rules.webp "Las reglas agrupadas por parámetro, cada una con su propio interruptor.")

Las reglas se agrupan por parámetro. Cada regla tiene su propio interruptor en su fila, así que puedes desactivar una sin abrirla. Una fila también muestra **Activada ahora** mientras su alerta está activa, o cuándo saltó por última vez (o **Nunca se ha activado**).

Las reglas de un cabezal de dosificación llevan el nombre del cabezal y lo que vigilan, por ejemplo *Yodo · días restantes* o *Yodo · restante*. Una dosis omitida aparece como *Yodo · dosis omitida*. Cada DŌS y cada ReefDose tiene aquí una fila propia, y las alertas de sus cabezales no se listan una a una. Toca la fila para abrir la página de esa dosificadora. Consulta [Alertas de dosificadoras](/help/mobile-device-control#doser-alerts).

Al final:

- **Agregar reglas recomendadas** añade las reglas recomendadas de Cora que falten. Se salta los parámetros que ya tienen una regla. En un acuario sin ninguna regla, este botón dice **Agregar reglas predeterminadas**.
- **Agregar regla personalizada** crea una regla tuya. Elige el parámetro y el **Tipo de regla**, **Umbral** o **Tasa de cambio**. El botón **Agregar regla** de abajo a la derecha hace lo mismo.

### Editar una regla {#editing-a-rule}

Toca la fila de una regla para abrirla. Encontrarás:

- **Mínimo de alerta** y **Máximo de alerta**, el propio rango. Deja uno vacío para un máximo o un mínimo.
- **Recomendado**, que vuelve a poner el rango sugerido por Cora.
- **Rango del medidor (pantalla Cora)**, con **Mínimo del medidor** y **Máximo del medidor**. Solo fijan la escala del medidor en Cora Max. Nunca generan una alerta.
- **Tiempo de espera entre alertas**, explicado [más abajo](#cooldowns).
- **Activada**, y un botón para eliminar.

Una regla de fallo de dispositivo, como un Trident sin reactivo, no tiene rango. Solo eliges su tiempo de espera.

## Fijar un rango {#setting-a-range}

Los parámetros que Cora puede valorar tienen un rango objetivo. Los valores predeterminados salen del tipo y la edad de tu acuario cuando lo configuras, y son un punto de partida sensato. Si un parámetro no tiene un rango útil, Cora no lo valora, y su widget se queda en gris neutro.

La forma más rápida de cambiar un rango es mantener pulsado el widget del parámetro en el panel. Se abren sus umbrales. Un toque normal abre la vista del parámetro.

![La hoja de umbral del pH en Cora Mobile](img/mobile-threshold-sheet.webp "Mínimo y máximo de alerta, el rango del medidor para Cora Max y el tiempo de espera entre alertas.")

Si el parámetro todavía no tiene regla, los campos empiezan con el valor predeterminado de Cora y una nota debajo lo indica. Cambia cualquier valor para fijar el tuyo.

Puedes fijar:

- un rango, con un mínimo y un máximo, para cosas como la alcalinidad o la temperatura
- un máximo, solo con el valor alto, para cosas en las que estar bajo está bien, como el nitrato o el fosfato
- un mínimo, solo con el valor bajo

:::tip Fija el rango en el que de verdad funciona tu acuario
Los valores predeterminados son solo un punto de partida. Un acuario con pocos nutrientes que funciona a 6 dKH no está "mal" porque una tabla diga 8–9. Fija el rango con el que trabajas, y Cora te avisa cuando *tú* te desvías.
:::

## Qué hace saltar una alerta {#what-triggers-an-alert}

Una alerta salta cuando una lectura cruza un umbral. Cora revisa cada lectura en cuanto llega, así que basta con una lectura fuera de tu rango.

Una regla de tasa de cambio vigila lo rápido que se mueve un parámetro en lugar de dónde está. Úsala cuando la velocidad de un cambio importa más que el número.

Cuando una alerta está activa, no te sigue avisando de lo mismo. El [tiempo de espera](#cooldowns) de la regla decide cuándo puede volver a avisarte.

## Dónde aparecen las alertas

- La campana, arriba a la derecha en las pestañas principales, guarda tu historial. El número indica cuántas no has leído. Más información en [Notificaciones](/help/mobile-notifications).
- Una notificación push llega a tu teléfono si esa categoría está activada.
- El widget del panel se pone ámbar o rojo.
- Cora Max muestra las mismas alertas en su pantalla.

## Cuando un equipo necesita atención {#equipment-faults}

Algunas alertas tratan de un equipo, no de una lectura. Cuando un dispositivo como un Trident o una bomba Jecod informa de un fallo, Cora envía una notificación con el nombre del acuario y del dispositivo, por ejemplo *"Acuario principal: la bomba de retorno necesita atención"*. También dice qué pasa, como un rotor atascado. Cuando el fallo se resuelve, recibes una segunda: *"Acuario principal: la bomba de retorno vuelve a estar bien"*. Las dos pertenecen a **Fallas de equipos** en **Ajustes → Notificaciones**.


## Un dispositivo ha dejado de informar {#stopped-reporting}

Cuando un dispositivo conectado se queda en silencio, Cora envía *"[Dispositivo]: ha dejado de informar"*. No significa que el dispositivo esté averiado, solo que Cora lleva un rato sin saber de él. Recibes una segunda notificación, *"[Dispositivo]: vuelve a informar"*, cuando vuelve.

Cuánto espera Cora depende del dispositivo:

| Dispositivo | Cora espera |
|---|---|
| Neptune Apex | Unos 30 minutos sin actualizaciones |
| Red Sea ReefBeat | Unos 30 minutos |
| AquaWiz | Unas 25 horas, porque AquaWiz solo deja que Cora lea su nube cada 12 horas |
| Bombas Jecod | Tres lecturas perdidas seguidas, según el intervalo de lectura de la bomba (90 minutos con el predeterminado de 30) |
| Enchufe Zigbee | No ha vuelto 30 minutos después de reiniciar el hub. Ponle nombre con **Renombrar** para que el aviso la nombre |

Qué revisar depende de cómo lee Cora el dispositivo.

- Apex, ReefBeat y Jecod los lee un Cora Max por Wi-Fi. Revisa la alimentación eléctrica y el Wi-Fi del dispositivo, y que el Cora Max que lo lee esté encendido y en línea.
- AquaWiz se lee a través de tu cuenta con el fabricante. Revisa la conexión de la cuenta en la página del dispositivo en Cora Mobile.


Estas notificaciones pertenecen a **Fallos de equipos** en **Ajustes → Notificaciones**.


Un acuario Red Sea también puede mostrar un aviso, *"Las lecturas de Red Sea han dejado de actualizarse"*, cuando ningún teléfono ni Cora Max está leyendo sus equipos ReefBeat. Tócalo para elegir un **Cora Max principal**. La solución completa está en [Solución de problemas](/help/troubleshooting#red-sea-readings-have-stopped-updating).

## Elegir qué te llega {#choosing-what-reaches-you}

En **Ajustes → Notificaciones** eliges qué categorías pueden enviarte una notificación push. Consulta [Notificaciones](/help/mobile-notifications), que también explica cómo [tener noches tranquilas](/help/mobile-notifications#quiet-at-night).

Reef Buddy no tiene interruptor propio. Su hora es la fila **Hora del resumen**, justo debajo de Notificaciones en Ajustes. En el plan gratuito no hay notificación del resumen.

:::note Cora no dice nada si nada ha cambiado
El resumen diario es una notificación por acuario al día. Un día en que nada te necesita, normalmente no dice nada en lugar de contarte que todo va bien. Si Cora te avisa, es que algo ha cambiado.
:::

## Tiempos de espera: cada cuánto puede avisarte la misma alerta {#cooldowns}

Cada regla tiene su propio **Tiempo de espera entre alertas**. Lo fijas al añadir o editar la regla. Una regla que nunca tuvo uno usa 1 h.

El tiempo de espera no oculta la alerta. Solo limita cada cuánto te avisa Cora de ella. La lectura se sigue valorando, y la alerta se queda en el widget y en la campana todo el tiempo.

Puedes elegir 15 min, 30 min, 1 h, 2 h, 4 h, 8 h, 1 día, 3 días o 1 semana.

Un tiempo de espera corto va bien para una lectura que cambia rápido, como la temperatura. Uno largo, de hasta una semana, va bien para algo que sigue mal durante días mientras esperas una pieza, como un Trident sin reactivo o un recipiente de dosificación vacío.

:::note Posponer está en Cora Max
Cora Mobile no tiene un botón para posponer una alerta activa. Posponer está en la pantalla de Cora Max junto al acuario, y silencia la alerta durante el tiempo de espera que elegiste aquí. En tu teléfono, el tiempo de espera de cada regla es la forma de cambiar cada cuánto te enteras de algo.
:::

## Cuando una alerta se resuelve {#clearing-an-alert}

Una alerta se resuelve sola cuando la lectura vuelve al rango. No hay nada que descartar. Recibes una notificación cuando pasa, por ejemplo *"Acuario principal: alcalinidad recuperada"*. Si el problema vuelve más tarde, recibes una alerta nueva.

:::note Los picos cortos también generan alertas
Una sola lectura fuera de rango basta para generar una alerta, así que una sonda que da un pico hará saltar una. Si una fuente no es fiable, recalíbrala o haz que el widget siga otra fuente. No amplíes el umbral.
:::

A veces la lectura está mal y el acuario está bien, por ejemplo cuando hay que calibrar una sonda. En ese caso, arregla la fuente. Si amplías un umbral para silenciar una sonda defectuosa, también te perderás el siguiente problema real.

## Desactivar una alerta {#turning-an-alert-off}

Desactiva el interruptor de la fila de la regla en la pestaña **Reglas**. Cora conserva la regla y su rango, así que puedes volver a activarla sin configurarla otra vez.

Mientras una regla está desactivada, Cora no valora esa lectura. Su widget se queda en gris neutro y nunca genera una alerta.

:::warning Desactiva un parámetro sin borrar su rango
Eliminar una regla no siempre impide que Cora valore esa lectura. Las bandas de referencia predeterminadas siguen dando color al valor y pueden seguir influyendo en el resumen. Usa el interruptor de la regla.
:::
