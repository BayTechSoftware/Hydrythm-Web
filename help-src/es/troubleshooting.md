---
title: Solución de problemas
description: Arregla una lectura desactualizada, un dispositivo que se ha desconectado, una orden que no llegó, un Cora Max que no se empareja o una alerta que no desaparece.
section: Help
reviewed: 2026-10-18
order: 1
---

Busca la familia a la que pertenece tu problema, y después el mensaje o el síntoma que ves. Los títulos entre comillas son las palabras exactas que te muestra Cora.

- [Lecturas y widgets](#readings-and-widgets)
- [Un dispositivo ha dejado de informar o no se puede contactar](#device-not-reporting)
- [Una orden no llegó](#command-did-not-go-through)
- [Cora Max](#cora-max)
- [Alertas, notificaciones y el resumen diario](#alerts-and-notifications)
- [Cora Assistant y la voz](#cora-assistant-and-voice)
- [Resultados de laboratorio e informes de salud](#lab-results-and-health-reports)
- [Idioma, unidades e inicio de sesión](#language-units-and-signing-in)


## Lecturas y widgets {#readings-and-widgets}

### Un widget no muestra ningún valor {#a-widget-shows-no-value}

Revisa esto en orden.

1. Mira la antigüedad de los widgets de al lado. Si también son todos antiguos, es la conexión, no el parámetro.
2. Abre la pestaña **Dispositivos**. Si no se puede contactar con un dispositivo, su fila tiene un punto rojo o lo dice.
3. Comprueba en qué acuario está el dispositivo. Un dispositivo que informa al acuario equivocado parece exactamente uno que no informa. Abre el dispositivo y comprueba su acuario.
4. Comprueba que algo lo mide. Nada informa del fosfato salvo que tengas un equipo que lo mida o lo anotes a mano.

### Un widget está en gris {#a-widget-is-grey}

Gris significa que Cora no está valorando esa lectura. Hay tres motivos habituales.

1. Su alerta está desactivada. Vuelve a activarla en la pestaña **Reglas** del Centro de alertas.
2. No tiene un rango con el que valorarla. Mantén pulsado el widget y fija un rango.
3. La lectura es demasiado antigua. Mira la antigüedad en el widget, y después anota una lectura nueva o revisa el dispositivo.

Lo que significa cada color está en [Leer tu panel](/help/mobile-dashboard#colours).

### Una lectura está desactualizada {#a-reading-is-stale}

La antigüedad del widget es correcta. No ha llegado nada nuevo.

- Los parámetros que se anotan a mano se quedan antiguos cuando nadie ha anotado una lectura. Anota una.
- Las lecturas de los equipos se quedan antiguas cuando el dispositivo deja de informar. Revisa su fila en **Dispositivos**.
- Algunos equipos solo informan de vez en cuando. Un titulador que mide cada hora normalmente muestra `1h`. Es normal.

### Dos fuentes no coinciden {#two-sources-disagree}

No hay nada roto. Cuando tu sonda y tu kit de pruebas no coinciden, eso te dice algo real de tu sistema.

Normalmente hay que calibrar la sonda. A veces el kit de pruebas es viejo. Calibra la sonda, vuelve a medir con reactivo nuevo y compara las dos en las mismas condiciones. Si una lectura estaba claramente mal, puedes excluirla. Consulta [Ver un parámetro a fondo](/help/mobile-metric-detail).

Un [resultado de ICP](/help/mobile-icp-health) te da un tercer número para comparar, pero por sí solo no zanja la cuestión. Los laboratorios difieren entre sí, y la forma de manipular y enviar una muestra cambia el resultado.

### Un widget muestra unidades equivocadas {#a-widget-shows-the-wrong-units}

Son las unidades de visualización del acuario. Tus datos están bien, y los valores se guardan igual se muestren como se muestren.

1. Abre **Ajustes**, abre ese acuario y elige **Unidades**.
2. Cámbialas ahí. Todos los teléfonos y Cora Max que muestran ese acuario se actualizan.

### Un medidor o un umbral se ve distinto después de cambiar las unidades {#a-gauge-or-threshold-looks-different-after-changing-display-}

Es lo esperado. Los medidores, las tarjetas y el historial se vuelven a dibujar en la unidad que elegiste. Los valores que hay debajo no han cambiado.

### Mi panel se ve mal después de editarlo {#my-dashboard-looks-wrong-after-editing}

Tus lecturas, tu historial y tu diario se guardan aparte del diseño, así que no has perdido nada.

- **En tu teléfono**, el editor no tiene deshacer ni diseños guardados. Abre **Editar panel** y vuelve a colocar los widgets. Más información en [Editar tu panel](/help/mobile-dashboard-editing).
- **En Cora Max**, carga un diseño guardado: abre **Diseño del panel**, toca **Mis paneles** y elige uno. Si no has guardado ninguno, vuelve a crear el diseño y toca **Guardar este diseño**, para que la próxima vez sea un solo toque. Más información en [Editar el panel de Cora Max](/help/max-dashboard-editing#saving-layouts).

### Saber por qué ha cambiado algo {#establishing-why-something-changed}

**Ajustes → Actividad** lista cada cambio de toma, alimentación y dosis, y lo que lo pidió: Cora Mobile, un Cora Max, la voz, el Asistente, una automatización o tu cuenta. Más información en [Actividad y línea de tiempo](/help/mobile-activity).

## Un dispositivo ha dejado de informar o no se puede contactar {#device-not-reporting}

### "[Dispositivo]: ha dejado de informar" {#device-stopped-reporting}

Cora envía esto cuando un dispositivo se queda en silencio. No significa que el dispositivo esté averiado, solo que Cora lleva un rato sin saber de él. Cuánto espera Cora con cada marca está en [Alertas y umbrales](/help/mobile-alerts#stopped-reporting).

1. Revisa la alimentación eléctrica del dispositivo, y su Wi-Fi o el alcance del Bluetooth.
2. Comprueba que el Cora Max que lo lee está encendido y en línea. Sin un Cora Max, tu teléfono lee un dispositivo Neptune Apex, Red Sea o Jecod solo mientras Cora Mobile está abierta en el mismo Wi-Fi.
3. Espera a la siguiente lectura. Recibirás una segunda notificación cuando vuelva a informar.


### "El dispositivo está fuera de línea. Mostrando el último estado conocido." {#device-is-offline-showing-last-known-state}

El dispositivo ha dejado de informar, y Cora muestra los últimos valores que tenía. No son actuales.

1. Revisa la propia conexión de red del dispositivo.
2. No tomes los valores como en directo hasta que la fila deje de decir que está fuera de línea.

### No se puede contactar con un dispositivo {#a-device-cannot-be-reached}

Normalmente es la red.

1. ¿El equipo está encendido y funciona en su propia app?
2. ¿Está en la misma red en la que lo añadiste?
3. ¿Ha cambiado algo en tu router (equipo nuevo, nombre de red nuevo, aislamiento de la red de invitados)?

Un equipo de tu red local tiene que ser accesible en esa red. Un equipo que se conecta a través de una cuenta del fabricante no, pero esa cuenta tiene que seguir siendo válida. Si la dirección del dispositivo cambió, ábrelo en la pestaña **Dispositivos** y toca **Editar conexión** en **Conexión**.

### Un dispositivo dice que se rechazó el inicio de sesión {#a-device-says-the-sign-in-was-refused}

El fabricante rechazó el inicio de sesión guardado. Casi siempre es porque cambiaste tu contraseña con él. Abre la fila del dispositivo y vuelve a iniciar sesión.

### "Las lecturas de Red Sea han dejado de actualizarse" {#red-sea-readings-have-stopped-updating}

Ahora mismo nada de este acuario está leyendo tus equipos Red Sea, así que las lecturas de la pantalla no se están actualizando.

1. Abre **Ajustes**, abre el acuario y después **Cora Max principal**. Comprueba que hay un Cora Max fijado, o que está elegido **Cualquiera activo (automático)**.
2. Si no tienes Cora Max, abre el acuario en Cora Mobile mientras tu teléfono está en el mismo Wi-Fi que los equipos Red Sea.
3. Comprueba que los equipos Red Sea están encendidos y en línea en su propia app.

### Algunos ajustes de ReefBeat aparecen en gris o no aparecen {#some-reefbeat-settings-are-greyed-out-or-missing}

Es normal. Los ajustes propios de un dispositivo Red Sea solo se abren cuando tu teléfono está en la misma red que el dispositivo. Fuera de esa red solo ves lecturas.

1. Conéctate al Wi-Fi del acuario para cambiar esos ajustes.
2. Las lecturas y el historial siguen funcionando cuando estás fuera.


## Una orden no llegó {#command-did-not-go-through}

Cada orden termina como **Confirmado**, **Sin confirmar**, **Rechazado** o **Sin cambios**. Lo que significa cada uno está en [Controlar tus equipos](/help/mobile-device-control).

### "No se pudo contactar a esta bomba: no se envió nada" {#could-not-reach-this-pump-nothing-was-sent}

Una orden a tu bomba Jecod o Jebao nunca salió de Cora. En tu teléfono el mensaje dice *"No se pudo contactar a esta bomba. Debe estar en la misma red Wi-Fi que tu teléfono."* Normalmente la bomba está apagada o no está en su red.

1. Comprueba que la bomba está encendida.
2. Comprueba que está en la misma red en la que la añadiste, y que tu teléfono o tu Cora Max también están en esa red.
3. Toca **Reintentar**.

### "No se pudo contactar a esta bomba por Bluetooth. Acércate a ella e intenta de nuevo." {#could-not-reach-this-pump-over-bluetooth-stand-near-it-and-t}

Tu teléfono está fuera del alcance de una bomba Jecod que solo usa Bluetooth. Acércate a la bomba y toca **Reintentar**.


### "No se pudo contactar al Apex: nada cambió" / "no se dosificó nada" {#could-not-reach-the-apex-nothing-changed-nothing-was-dosed}

Un Neptune Apex, un Trident o un cabezal DŌS no respondió a una orden o a una petición de dosis.

1. Abre la propia app del Apex y comprueba que está en línea.
2. Revisa la conexión de red del teléfono o del Cora Max que estás usando. Cambiar un cabezal DŌS desde tu teléfono necesita que el teléfono esté en la misma red que el Apex.
3. Toca **Reintentar**.

### "No se pudo enviar …: este Cora Max no tiene los datos de Apex" {#this-could-not-be-sent-no-device-on-this-tank-can-send-it}

Cora Max muestra esto cuando no tiene forma de llegar a tu Apex y ningún otro dispositivo del acuario puede enviar la orden por él. El mensaje dice que añadas los datos del Apex en Ajustes, pero ahora se configuran en tu teléfono.

1. En tu teléfono, abre **Dispositivos**, luego tu Apex, y comprueba su dirección y su inicio de sesión en **Conexión**. Corrígelos con **Editar conexión**.
2. O haz que un Cora Max que funcione sea el **Cora Max principal** de este acuario: **Ajustes**, abre el acuario y después **Cora Max principal**.

### La alimentación no empieza desde el teléfono {#feed-does-not-start}

En tu teléfono, **Alimentar** solo aparece en un acuario con un Neptune Apex, y empieza uno de los ciclos de alimentación programados en el Apex.

- *"Ningún Cora de este acuario puede contactar al Apex, y no estás en su red."* Conéctate al Wi-Fi del Apex, o empareja un Cora Max con el acuario.
- *"El Apex no respondió, pero puede que ya esté alimentando."* Revisa el controlador antes de volver a intentarlo.

### Una dosis se detuvo a medias y apareció una alerta de "restauración" {#a-dose-stopped-partway-through-and-a-restore-alert-appeared}

El cabezal DŌS perdió el contacto durante la dosis. Cora te lo dice para no tener que suponer que entró la dosis completa.

1. Abre la alerta y comprueba cuánto se dosificó antes de que se detuviera.
2. Usa esa cantidad para decidir si reanudas o ajustas la dosis.

## Cora Max {#cora-max}

### Mi Cora Max está desconectado {#my-cora-max-is-offline}

En tu teléfono, su fila de la pestaña **Dispositivos** tiene un punto rojo. Mientras está desconectado, los equipos que lee dejan de actualizarse, puedes recibir alertas de "ha dejado de informar" de esos equipos, y las órdenes enviadas desde fuera pueden volver como *"No se envió nada"*.

1. Comprueba que Cora Max tiene corriente y que la pantalla está encendida.
2. En Cora Max, revisa **Ajustes → Ajustes de Cora Max → Wi-Fi**, y que tu router funciona.
3. Si hay otro Cora Max en el acuario, pon **Cora Max principal** en **Cualquiera activo (automático)** para que pueda tomar el relevo. Consulta [Más de un dispositivo Cora](/help/mobile-multi-device#primary-cora-max).
4. Si no arranca bien, consulta [Actualizaciones y recuperación](/help/max-updates).

:::tip Entérate la próxima vez
En Cora Mobile, abre **Ajustes → Automatizaciones** y crea una regla con el disparador **Cuando un dispositivo se desconecta**, elige tu Cora Max y añade la acción **Notificarme**. Más información en [Automatizaciones y escenas](/help/mobile-automation).
:::

### No se puede emparejar un Cora Max {#pairing-a-cora-max-fails}

Cora Mobile encuentra un Cora Max nuevo por Bluetooth, y después le da tu Wi-Fi. Antes de empezar, ten al menos un acuario en Cora Mobile, el Bluetooth activado y tu teléfono cerca de la pantalla. Si el emparejamiento se detiene a medias, Cora Mobile te dice por qué, con **Cancelar** y **Reintentar** debajo.

- *"El Bluetooth está desactivado. Actívalo y vuelve a tocar Buscar."* Activa el Bluetooth y vuelve a buscar.
- *"El permiso de Bluetooth está desactivado para Cora. Actívalo en Ajustes y vuelve a tocar Buscar."* Permite el Bluetooth para Cora en los ajustes de tu teléfono. **Ajustes → Acceso a dispositivos** en Cora Mobile te lleva ahí.
- *"No se encontraron dispositivos de configuración Cora cercanos por Bluetooth."* Ponte al lado de Cora Max, comprueba que muestra su pantalla de configuración y vuelve a buscar.
- **No se encontraron acuarios**: crea primero un acuario en Cora Mobile y después empareja.
- *"Tu teléfono no pudo comunicarse con el Cora Max en tu red Wi-Fi."* Pon tu teléfono y Cora Max en la misma red Wi-Fi. En iPhone, comprueba también que Cora tiene acceso a la Red local (**Ajustes → Acceso a dispositivos**). Después toca **Reintentar**.
- *"El Cora Max no aceptó esta sesión de emparejamiento."* Reintentar no servirá. Cierra la pantalla y empieza de nuevo desde **Dispositivos → Agregar dispositivo → Cora**.

Con cualquier otro mensaje, toca **Reintentar**. Toda la configuración está en [Configurar Cora Max](/help/max-setup).

### Cora Max muestra datos antiguos {#cora-max-shows-old-data}

Mira la etiqueta de estado de la barra superior. **En línea** y **Nube** están bien los dos. Si tienes más de un Cora Max, el que no está recogiendo los datos muestra **Nube**, y sus lecturas están igual de al día. **Desactualizado** o **Sin conexión** significa que Cora Max ha perdido su fuente y muestra los últimos datos que recibió.

- Revisa el Wi-Fi en **Ajustes → Ajustes de Cora Max → Wi-Fi**.
- Comprueba que tu propia red funciona.
- Si la etiqueta dice **En línea** o **Nube** y los datos siguen siendo antiguos, el problema está antes de Cora Max. Revisa el mismo acuario en tu teléfono.

### Cora Max muestra "Contraseña de Apex" {#cora-max-shows-apex-password}

Tu Apex rechazó el inicio de sesión que tiene guardado Cora, normalmente porque se cambió la contraseña del Apex. En tu teléfono, abre **Dispositivos**, luego tu Apex, y toca **Editar conexión** en **Conexión** para escribir la nueva.

### Cora Max muestra "Guardado en la nube rechazado" {#cora-max-shows-cloud-save-refused}

Cora Cloud se niega a guardar algunos datos de esta pantalla. No pasa nada con tu acuario ni con Cora Max, y no hay que cambiar nada en la pantalla. La solución es una actualización de Cora Cloud.

1. Abre **Ajustes → Ajustes de Cora Max** y baja hasta **ESTADO**. La línea **Guardado en la nube** dice qué datos se están rechazando, por ejemplo las lecturas o las tomas de un dispositivo.
2. [Contacta con soporte](/support.html) y dinos lo que dice esa línea.

Mientras tanto, tus lecturas se siguen mostrando en Cora Max. Simplemente no se guardan en tu cuenta hasta que llegue la solución.

### Un segundo Cora Max muestra "Cora principal sin conexión" {#a-secondary-cora-max-shows-main-cora-offline}

El Cora Max principal de este acuario se ha desconectado. Esta pantalla muestra los últimos datos que recibió, así que no son en directo.

1. Revisa la alimentación eléctrica y el Wi-Fi del Cora Max principal.
2. Espera a que se vuelva a conectar, o cambia el **Cora Max principal** a un dispositivo que esté en línea.

### Cora Max no se vuelve a conectar enseguida después de un corte del Wi-Fi {#cora-max-wont-reconnect-right-away-after-a-wi-fi-outage}

Después de perder la conexión, Cora Max espera un poco más antes de cada reintento para no saturar tu red. La espera llega a más o menos un minuto.

1. Dale más o menos un minuto después de que vuelva tu red.
2. Si sigue sin conectarse, revisa **Ajustes → Ajustes de Cora Max → Wi-Fi**.

### Cambiar el nombre de un Cora Max en el teléfono no cambia lo que muestra {#renaming-a-cora-max-on-the-phone-doesnt-change-what-the-tabl}

El nombre que pones en tu teléfono es la etiqueta de la cuenta para ese dispositivo. El nombre que Cora Max muestra en su propia pantalla de emparejamiento puede ser otro.

1. Comprueba qué nombre estás mirando: el de la lista de dispositivos de tu teléfono o el de la pantalla de emparejamiento de Cora Max.
2. Para cambiar la etiqueta de la cuenta, cámbiale el nombre desde la lista de dispositivos de tu teléfono.

### No encuentro dónde desactivar la palabra de activación {#i-cant-find-where-to-turn-off-the-wake-word-on-cora-max}

Los controles de la palabra de activación están con los ajustes de sonido, no con los de Cora Assistant.

1. En Cora Max, ve a **Ajustes → Ajustes de Cora Max** y busca **Palabra de activación** en **SONIDO Y VOZ**.
2. Desactívala. Todavía puedes tocar el icono de **Cora Assistant** para empezar a hablar.

Más información en [Hablar con Cora](/help/max-voice).

### El bloqueo infantil no deja entrar a nadie en Ajustes {#child-lock-wont-let-anyone-into-settings}

Es lo que hace el bloqueo infantil. Cuando pasa un tiempo fijado sin que nadie toque la pantalla, impide que nadie maneje equipos desde ella, tocándola o por voz. Las lecturas se siguen actualizando, y todavía puedes hacerle preguntas a Cora. Para desbloquearlo:

1. Pulsa **Subir volumen** o **Bajar volumen** tres veces en menos de dos segundos, o
2. Mantén cinco dedos en la esquina superior derecha de la pantalla durante diez segundos.

Más información en [Ajustes de Cora Max](/help/max-settings#child-lock).

### Una escena creada en el teléfono no se puede editar en Cora Max {#a-scene-made-on-the-phone-doesnt-show-up-as-editable-on-cora}

Solo las versiones más recientes de Cora Max pueden editar escenas en la pantalla. Las versiones antiguas siguen ejecutando las escenas que creaste en tu teléfono, pero no pueden editarlas.

1. Actualiza Cora Max ([Actualizaciones y recuperación](/help/max-updates)), o
2. Sigue editando esa escena en tu teléfono. Se ejecuta en Cora Max igualmente.

## Alertas, notificaciones y el resumen diario {#alerts-and-notifications}

### Una alerta no desaparece {#an-alert-is-not-clearing}

Una alerta desaparece cuando la lectura vuelve al rango. Si no desaparece, hay tres motivos probables.

- La lectura está realmente fuera de rango. Mira el historial del widget.
- El rango no encaja con tu acuario. Consulta [Alertas y umbrales](/help/mobile-alerts).
- La fuente está mal. Una sonda que necesita calibración informa de un número que de verdad está fuera de rango. Arregla la sonda y deja el rango como está.

### Una alerta no deja de avisar después de atenderla {#an-alert-wont-stop-notifying-even-after-ive-acknowledged-it}

**Posponer** y **Descartar** en Cora Max solo silencian ese Cora Max. Tu teléfono sigue recibiendo notificaciones mientras la lectura esté fuera de rango.

1. Para enterarte con menos frecuencia, abre la regla de la alerta en Cora Mobile y fija un **Tiempo de espera entre alertas** más largo (hasta 1 semana).
2. Si el rango no encaja con tu acuario, cambia el propio rango.

### No me llegan las notificaciones {#im-not-getting-notifications}

1. En **Ajustes → Notificaciones**, comprueba que la categoría puede enviar notificaciones.
2. Revisa el permiso de notificaciones de tu teléfono para Cora.
3. El resumen diario no dice nada los días en que no cambia nada. Si ha dejado de llegar por completo, mira la siguiente entrada.

Más información en [Notificaciones](/help/mobile-notifications).

### Mi resumen diario ha dejado de llegar {#my-daily-briefing-stopped}

- Tu prueba gratuita ha terminado. Reef Buddy forma parte de los planes de pago. Después de la prueba de 30 días, una cuenta gratuita deja de recibir el resumen diario. Consulta [Planes y suscripciones](/help/mobile-plans).
- Tu plan no cubre el acuario. Cada plan cubre un número fijo de acuarios, contados en el orden de **Ajustes → Reordenar acuarios**. Sube un acuario para incluirlo.
- Hoy no ha cambiado nada. El resumen no dice nada en un día tranquilo.

Más información en [Reef Buddy](/help/mobile-reef-buddy).

### Siguen llegando alertas de un acuario que quité {#alerts-from-a-removed-tank}

Un acuario eliminado se conserva por su historial, pero no envía alertas ni recordatorios y sus automatizaciones se detienen. Si aún recibes alguna:

1. Abre **Ajustes → Acuarios eliminados**. Si el acuario no aparece, no se ha eliminado.
2. Actualiza Cora Mobile y tu Cora Max a la última versión.
3. ¿Siguen llegando alertas? Escribe al soporte con el texto de la alerta y la hora a la que llegó. Consulta [Informar de un problema](/help/mobile-support).

Más información en [Gestionar tus acuarios](/help/mobile-tanks).


## Cora Assistant y la voz {#cora-assistant-and-voice}

### Cora Assistant responde sobre el acuario equivocado {#cora-assistant-answers-about-the-wrong-tank}

No elegiste un acuario antes de preguntar, o está elegido el que no es. Elige el acuario al que te refieres y vuelve a preguntar. Más información en [Preguntar a Cora](/help/mobile-assistant).

### Cora Assistant se niega a responder, o vuelve a mostrar una pantalla de consentimiento {#cora-assistant-refuses-to-answer-or-shows-a-consent-screen-a}

**Permitir que el Cora Assistant use los datos guardados del acuario** está desactivado, así que no tiene nada con lo que responder. Toca **Aceptar y continuar** en la pantalla de consentimiento, o activa el interruptor en **Ajustes → Cora Assistant**.

### Cora Max dice "La voz necesita tu autorización" {#voice-needs-your-ok}

La voz en Cora Max usa la misma elección de uso compartido de datos que Cora Assistant en tu teléfono. En Cora Mobile, abre **Ajustes → Cora Assistant** y activa **Permitir que el Cora Assistant use los datos guardados del acuario**, y vuelve a intentarlo. Más información en [Hablar con Cora](/help/max-voice).

## Resultados de laboratorio e informes de salud {#lab-results-and-health-reports}

### Un resultado de ICP de un laboratorio o enviado por correo nunca apareció {#a-lab-or-emailed-icp-result-never-showed-up}

Un resultado solo se adjunta cuando tiene un acuario, a veces Cora también tiene que reconocer al remitente, y Cora necesita tu autorización para leerlo.

1. Si ves *"Cora Assistant necesita tu autorización para leerlo."*, abre **Ajustes → Cora Assistant** y activa **Permitir que el Cora Assistant use los datos guardados del acuario**. El resultado entra en cuanto aceptas.
2. Revisa la indicación que muestra Cora la primera vez que le envías un resultado.
3. Cuando Cora lo pregunte, confirma a qué acuario pertenece el resultado.
4. Si ya has enviado un resultado antes, envía este desde la misma dirección de correo.

Más información en [ICP e informes de salud](/help/mobile-icp-health).

### Mi archivo de ICP no se sube {#my-icp-file-wont-upload}

Cora lee el informe PDF que te envía tu laboratorio. Las fotos y las capturas de pantalla no se pueden leer. Descarga antes el PDF de tu laboratorio y vuelve a tocar **Subir ICP**.

### La pantalla se queda en negro después de un informe de salud o de subir un ICP {#black-screen-after-a-report}

Esto podía pasar en Cora Mobile 1.2 y anteriores, y Cora Mobile 1.3 lo soluciona: actualiza Cora Mobile desde App Store o Google Play. Si te pasa antes de actualizar, cierra Cora Mobile y vuelve a abrirla. El informe se guardó, y lo encontrarás en **Inteligencia**.

## Idioma, unidades e inicio de sesión {#language-units-and-signing-in}

### De repente todo está en el idioma equivocado {#everything-is-suddenly-in-the-wrong-language}

Alguien cambió el idioma de la cuenta en uno de tus dispositivos. Es un único ajuste para toda la cuenta.

1. Abre **Ajustes → Idioma** en Cora Mobile o en Cora Max.
2. Vuelve a ponerlo como estaba. El cambio se aplica en todas partes.

### Una alerta o un informe antiguo está en otro idioma después del cambio {#an-old-alert-or-report-is-still-in-a-different-language-afte}

Es lo esperado. Cora no vuelve a traducir nada que ya haya escrito. Las alertas, los informes y los resúmenes nuevos usan el idioma nuevo.

### "No se pudo contactar con Cora. Comprueba tu Wi-Fi o tus datos móviles, y vuelve a intentarlo." {#could-not-reach-cora-check-your-wi-fi-or-mobile-data-then-tr}

Tu teléfono no puede llegar a Cora Cloud para iniciar sesión. Tiene que ver con la conexión de tu teléfono, no con los equipos de tu acuario.

1. Comprueba que tu teléfono tiene Wi-Fi o datos móviles que funcionan.
2. Prueba con otra red si tienes una.
3. Toca **Reintentar**.

Otros problemas de inicio de sesión están en [Inicio de sesión y recuperación de la cuenta](/help/mobile-account).

## ¿Sigues atascado? {#still-stuck}

Escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**, o infórmanos desde Cora Mobile como se explica en [Informar de un problema](/help/mobile-support). Dinos qué acuario, qué dispositivo, qué pantalla y qué esperabas ver.
