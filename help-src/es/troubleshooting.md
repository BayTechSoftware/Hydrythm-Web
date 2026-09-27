---
title: Solución de problemas
description: Las lecturas se detuvieron, un dispositivo quedó sin conexión, las alertas no se cierran, o algo se ve mal. Empieza aquí.
section: Help
reviewed: 2026-09-27
order: 1
---

Empieza por el síntoma.

## Un widget no muestra valor

Repasa esta lista en orden:

1. **Revisa la antigüedad de los widgets cercanos.** Si todo está desactualizado, el problema es la conexión, no el parámetro.
2. **Abre la pestaña Dispositivos.** Un dispositivo al que no se puede llegar lo indica en su fila.
3. **Revisa la asignación del acuario.** Un dispositivo que informa al acuario equivocado se ve exactamente igual que uno que no informa. Abre el dispositivo y confirma su acuario.
4. **Comprueba que la fuente existe.** Nada informa fosfato a menos que tengas equipo que lo mida o lo registres a mano.

## Una lectura está desactualizada

La insignia de antigüedad te está diciendo la verdad: no ha llegado nada nuevo.

- **Los parámetros registrados a mano** se desactualizan cuando no se ha introducido ninguna lectura. Registra una.
- **Las lecturas de equipo** desactualizadas significan que el dispositivo dejó de informar; revisa su fila en **Dispositivos**.
- **Algún equipo está pensado para ser lento.** Un titulador que mide cada hora normalmente se leerá `1h`. Eso no es un fallo.

## No se puede llegar a un dispositivo

Normalmente es la red.

1. ¿Está el equipo encendido y funcionando en su propia aplicación?
2. ¿Está en la misma red en la que se añadió?
3. ¿Ha cambiado tu router (hardware nuevo, nombre de red nuevo, aislamiento de red de invitados)?

El equipo que se conecta por tu red local necesita ser accesible en esa red. El equipo que se conecta a través de una cuenta del fabricante no necesita eso, pero necesita que esa cuenta siga siendo válida.

## Un dispositivo dice que se rechazó el inicio de sesión

El fabricante rechazó el inicio de sesión guardado. Casi siempre porque cambiaste tu contraseña con ellos.

Abre la fila del dispositivo e inicia sesión de nuevo.

## El emparejamiento de un Cora Max falla

Si añadir un Cora Max se detiene a mitad de camino, Cora Mobile te dice qué paso falló y por qué, con **Cancelar** y **Reintentar** debajo.

- *"Tu teléfono no pudo comunicarse con el Cora Max en tu red Wi-Fi."* Pon tu teléfono y el Cora Max en la misma red Wi-Fi. En iPhone, comprueba también que Cora tenga acceso a la Red local: **Ajustes → Acceso a dispositivos** te lleva ahí (consulta [Ajustes](/help/mobile-settings)). Luego toca **Reintentar**.
- *"El Cora Max no aceptó esta sesión de emparejamiento."* Reintentar no ayudará. Cierra la pantalla y vuelve a empezar desde **Dispositivos → Agregar dispositivo**.

Para cualquier otro mensaje, toca **Reintentar**.

## Cora Max muestra datos antiguos

Revisa la píldora de estado en la barra superior. **En línea** y **Nube** son ambas saludables: con más de un Cora, la pantalla que no está recopilando muestra **Nube**, y sus lecturas son igual de actuales. **Desactualizado** o **Sin conexión** significa que la pantalla perdió su fuente y está mostrando los últimos datos que recibió (comportamiento correcto, pero no actual).

- Revisa el Wi-Fi en **Ajustes → Cora Max → Red**
- Comprueba que la propia red esté activa
- Si la píldora dice **En línea** o **Nube** y los datos siguen siendo antiguos, el problema está más arriba: revisa el mismo acuario en tu teléfono

## Una alerta no se cierra

Una alerta se cierra cuando la lectura vuelve al rango. Si no se cierra:

- **La lectura está realmente fuera de rango.** Mira el historial del widget.
- **El umbral está mal para tu acuario.** Consulta [Alertas y umbrales](/help/mobile-alerts).
- **La fuente está mal.** Una sonda que necesita calibrarse informa un número que realmente está fuera de rango. Arregla la sonda en lugar del umbral.

## Dos fuentes no coinciden

Esto es Cora funcionando, no Cora fallando. Cuando tu sonda y tu kit de pruebas no coinciden, eso es un hecho real sobre tu sistema.

Un resultado de ICP es una tercera opinión útil aquí, pero no resuelve la discusión: los laboratorios difieren entre sí, y la manipulación y el transporte de una muestra mueven el resultado. Que dos pruebas coincidan vale mucho más que una sola.

Normalmente la sonda necesita calibrarse; a veces el kit de pruebas está caducado. Calibra la sonda, repite la prueba con reactivo fresco, y compara las dos en las mismas condiciones. Un [resultado de ICP](/help/mobile-icp-health) añade un tercer dato a esa comparación.

## No me llegan notificaciones

1. **Ajustes → Notificaciones**: comprueba que esa categoría tenga permiso para enviarse
2. Revisa los propios permisos de notificación de tu teléfono para Cora
3. Recuerda que el resumen diario es deliberadamente silencioso los días en que nada cambió

## Averiguar por qué algo cambió

**Ajustes → Actividad** lista cada cambio de toma, alimentación, dosis y cambio de enchufe, con qué lo pidió: Cora Mobile, una pantalla Cora, la voz, el Assistant, una regla de automatización, un botón inteligente o tu cuenta.

## Mi panel se ve mal después de editarlo

Carga un diseño guardado: **Mis paneles**, y elige uno.

Si no has guardado ninguno, reconstruye el diseño y luego guárdalo como uno. A partir de ese momento, volver a él es un solo toque.

De cualquier forma, las lecturas, el historial y las entradas del diario se guardan por separado del diseño, así que nada detrás del panel se pierde.

## "Las lecturas de Red Sea han dejado de actualizarse"

**Qué significa:** Ningún dispositivo en la red de este acuario está consultando en este momento tu equipo Red Sea, así que las lecturas en pantalla no se han actualizado.

**Qué hacer:**
1. Abre **Ajustes → Cora Max principal** y comprueba que hay un Cora Max fijado (o que está elegido **Cualquiera activo (automático)**).
2. Abre el acuario en un dispositivo que esté en la misma Wi-Fi que el equipo Red Sea.
3. Confirma que el equipo Red Sea está encendido y en línea en su propia aplicación.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## "No se pudo contactar a esta bomba: no se envió nada"

**Qué significa:** Una orden para una bomba Jecod o Jebao nunca salió de la aplicación, normalmente porque la bomba está apagada o fuera de su red.

**Qué hacer:**
1. Comprueba que la bomba está encendida.
2. Comprueba que está en la misma red en la que se añadió.
3. Toca **Reintentar**.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## "No se pudo contactar a esta bomba por Bluetooth. Acércate a ella e intenta de nuevo."

**Qué significa:** Un dispositivo Jecod solo por Bluetooth está fuera del alcance de tu teléfono.

**Qué hacer:**
1. Acércate a la bomba.
2. Toca **Reintentar**.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## "No se pudo contactar con ese Gyre. No se inició ninguna alimentación."

**Qué significa:** Un gyre Maxspect (integración beta) no respondió cuando Cora intentó iniciar el modo alimentación en él.

**Qué hacer:**
1. Comprueba que el gyre está encendido y en su red.
2. Toca **Reintentar**.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## "No se pudo contactar con ese Gyre. Su programa no cambió."

**Qué significa:** Un envío de horario a un gyre Maxspect (integración beta) no logró llegar a él.

**Qué hacer:**
1. Comprueba que tu teléfono o Cora Max está en la red del gyre.
2. Toca **Reintentar** desde la pantalla de horario.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## "No se pudo contactar al Apex: nada cambió" / "no se dosificó nada"

**Qué significa:** Un Neptune Apex, Trident o cabezal DŌS no respondió a una orden o solicitud de dosis.

**Qué hacer:**
1. Abre la propia aplicación del Apex y confirma que está en línea.
2. Revisa la conectividad de red en el dispositivo que estás usando.
3. Toca **Reintentar**.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## "Esto no se pudo enviar: ningún dispositivo de este acuario puede enviarlo"

**Qué significa:** Ningún dispositivo Cora de este acuario tiene los datos de conexión del Apex necesarios para llevar a cabo la orden, o el que los tiene está sin conexión.

**Qué hacer:**
1. Añade los datos del Apex en **Ajustes** en un dispositivo que esté en línea en ese momento, o
2. Fija un Cora Max distinto que funcione como **Cora Max principal** de este acuario.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## Un Cora Max secundario muestra "Cora principal sin conexión"

**Qué significa:** La tableta principal de este acuario se ha quedado sin conexión, así que esta pantalla secundaria muestra los últimos datos que recibió en lugar de datos en vivo.

**Qué hacer:**
1. Comprueba la alimentación y el Wi-Fi de la tableta principal.
2. Espera a que se reconecte, o cambia el **Cora Max principal** a un dispositivo que esté en línea en ese momento.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## "El dispositivo está sin conexión. Mostrando el último estado conocido."

**Qué significa:** Manejo normal de desconexión: el dispositivo dejó de informar, y Cora muestra los últimos valores que tenía en lugar de simular que son actuales.

**Qué hacer:**
1. Revisa la propia conexión de red del dispositivo.
2. Trata los valores mostrados como no actuales hasta que la fila ya no diga sin conexión.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## Algunos ajustes de ReefBeat aparecen en gris o no aparecen

**Qué significa:** Esto es intencionado, no un fallo. Los ajustes propios del dispositivo (a diferencia de las lecturas) solo se abren cuando tu teléfono está en la misma red que el propio dispositivo; fuera de esa red, solo se muestran las lecturas.

**Qué hacer:**
1. Visita el Wi-Fi del propio acuario para cambiar esos ajustes.
2. Las lecturas y el historial siguen funcionando con normalidad fuera del acuario.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## "No se pudo contactar con Cora. Comprueba tu Wi-Fi o tus datos móviles, y vuelve a intentarlo."

**Qué significa:** Tu teléfono no tiene una conexión utilizable a Cora Cloud al iniciar sesión. Esto es sobre la propia conectividad de tu teléfono, no sobre el equipo de tu acuario.

**Qué hacer:**
1. Comprueba que tu teléfono tiene una conexión Wi-Fi o de datos móviles funcionando.
2. Prueba una red distinta si hay alguna disponible.
3. **Reintentar**.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Todo está de repente en el idioma equivocado

**Qué significa:** El idioma de la cuenta se cambió desde algún dispositivo. El idioma es un ajuste para toda la cuenta, no por dispositivo.

**Qué hacer:**
1. Abre **Ajustes → Idioma** en cualquiera de las dos aplicaciones.
2. Vuelve a fijarlo si se cambió por error; el cambio se aplica en todas partes a la vez.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Una alerta o informe antiguo sigue en otro idioma después de cambiar

**Qué significa:** Esto es lo esperado, no un error. Cora no retraduce contenido que ya se generó; solo las alertas, informes y resúmenes nuevos siguen el idioma nuevo.

**Qué hacer:**
1. Nada que arreglar. Espera contenido nuevo, que usará el idioma actual.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Una alerta no deja de avisar aunque la haya confirmado

**Qué significa:** Confusión entre **Descartar** (cierra la alerta para siempre) y **Posponer** (la silencia temporalmente, hasta una semana).

**Qué hacer:**
1. Si entiendes y aceptas la condición, usa **Descartar**.
2. Si solo quieres silencio por un tiempo, usa **Posponer** y elige una duración.

**¿Sigue sin funcionar?** Consulta [Alertas y umbrales](/help/mobile-alerts), o envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Una dosis se detuvo a mitad de camino y apareció una alerta de "restauración"

**Qué significa:** El cabezal DŌS perdió contacto a mitad de una dosis, así que Cora te lo dice deliberadamente en lugar de asumir que entró la dosis completa.

**Qué hacer:**
1. Abre la alerta y revisa cuánto se dosificó realmente antes de que se detuviera.
2. Reanuda o ajusta la dosis según esa cantidad, no la cantidad programada originalmente.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## Una escena creada en el teléfono no aparece como editable en Cora Max

**Qué significa:** Editar escenas directamente en la tableta es una funcionalidad más reciente de Cora Max. El firmware más antiguo todavía puede ejecutar escenas creadas en el teléfono, solo que no editarlas ahí.

**Qué hacer:**
1. Actualiza Cora Max, o
2. Sigue editando esa escena desde el teléfono; se seguirá ejecutando en la tableta de cualquier forma.

**¿Sigue sin funcionar?** Consulta [Actualizaciones y recuperación](/help/max-updates), o envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant responde sobre el acuario equivocado

**Qué significa:** No se eligió ningún acuario antes de preguntar, o el acuario equivocado está activo en ese momento.

**Qué hacer:**
1. Elige primero el acuario que quieres decir.
2. Pregunta de nuevo.

**¿Sigue sin funcionar?** Consulta [El Asistente](/help/mobile-assistant), o envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant se niega a responder, o vuelve a mostrar una pantalla de consentimiento

**Qué significa:** "Permitir que el Cora Assistant use los datos guardados del acuario" se desactivó, así que no tiene nada a partir de lo cual responder.

**Qué hacer:**
1. Toca **Aceptar y continuar** en la pantalla de consentimiento para volver a activarlo.

**¿Sigue sin funcionar?** Consulta [El Asistente](/help/mobile-assistant), o envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un resultado de ICP de un laboratorio o por correo nunca apareció

**Qué significa:** Que un resultado entre en Cora necesita que se elija un acuario para él, y a veces un remitente reconocido, antes de que se adjunte a algún sitio.

**Qué hacer:**
1. Revisa el aviso de recepción que se muestra la primera vez que envías un resultado a Cora.
2. Confirma a qué acuario debe adjuntarse el resultado cuando se te pregunte.
3. Asegúrate de que el correo se envió desde la dirección que usaste para enviarlo antes, si has enviado uno anteriormente.

**¿Sigue sin funcionar?** Consulta [ICP e informes de salud](/help/mobile-icp-health), o envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Una notificación de ICP por correo no nombra ningún laboratorio

**Qué significa:** Un problema conocido con la notificación push de "elegir acuario" que no incluía el nombre del laboratorio. Ya se ha corregido en las versiones actuales.

**Qué hacer:**
1. Asegúrate de que Cora Mobile está actualizado a la última versión.
2. El resultado en sí no se ve afectado; solo al texto de la notificación le faltaba un nombre.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un widget muestra las unidades equivocadas

**Qué significa:** Este es el ajuste de unidades de visualización del acuario, no un problema de datos. Los valores se guardan igual sin importar cómo se muestren.

**Qué hacer:**
1. Abre **Ajustes** de ese acuario y revisa sus unidades de visualización.
2. Cámbialas ahí; cada teléfono y Cora Max que muestre ese acuario se actualiza para coincidir.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un medidor o umbral se ve distinto después de cambiar las unidades de visualización

**Qué significa:** Es lo esperado. Los medidores, casillas e historial se vuelven a dibujar en la unidad que elegiste; los valores subyacentes no han cambiado.

**Qué hacer:**
1. Nada que arreglar; esto es solo cosmético.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Max no se reconecta enseguida después de un corte de Wi-Fi

**Qué significa:** Después de perder su conexión, Cora Max espera un poco más antes de cada reintento en lugar de saturar la red, aumentando la espera hasta aproximadamente un minuto antes de volver a intentarlo.

**Qué hacer:**
1. Espera aproximadamente un minuto después de que tu red vuelva.
2. Si todavía no se ha reconectado después de eso, revisa el Wi-Fi en **Ajustes → Red**.

**¿Sigue sin funcionar?** Consulta [La pantalla de inicio de Cora Max](/help/max-tour), o envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Renombrar un Cora Max en el teléfono no cambia lo que muestra la tableta

**Qué significa:** El nombre que fijas desde el teléfono es una etiqueta de nivel de cuenta para ese dispositivo. El nombre que se muestra en la propia tableta durante el emparejamiento puede ser otra cosa distinta.

**Qué hacer:**
1. Comprueba qué "nombre" estás mirando: el de tu lista de dispositivos en el teléfono, o el de la propia pantalla de emparejamiento de la tableta.
2. Renombra desde la lista de dispositivos del teléfono si es la etiqueta de cuenta la que quieres cambiar.

**¿Sigue sin funcionar?** Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del dispositivo.

## No encuentro dónde desactivar la palabra de activación en Cora Max

**Qué significa:** El interruptor de palabra de activación vive bajo **Sonido**, no bajo el grupo de ajustes de Cora Assistant, lo cual sorprende a la mayoría de las personas.

**Qué hacer:**
1. Ve a **Ajustes → Sonido → Escucha de palabra de activación**.
2. Desactívala; todavía puedes tocar el icono de Cora para iniciar una sesión de voz.

**¿Sigue sin funcionar?** Consulta [Ajustes en Cora Max](/help/max-settings), o envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## El bloqueo infantil no deja entrar a nadie en Ajustes

**Qué significa:** Esto funciona como está previsto. El bloqueo infantil bloquea la pantalla táctil y los controles de voz después de un tiempo fijado sin ningún toque; las lecturas siguen actualizándose por debajo.

**Qué hacer:**
1. Pulsa **Subir volumen** o **Bajar volumen** tres veces en dos segundos, o
2. Mantén cinco dedos en la esquina superior derecha de la pantalla durante diez segundos.

**¿Sigue sin funcionar?** Consulta [Voz en Cora Max](/help/max-voice), o envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Sigo atascado

Envía un correo a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**. Dinos qué acuario, qué pantalla y qué esperabas ver; así consigues una respuesta útil más rápido.
