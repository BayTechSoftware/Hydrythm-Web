---
title: Solución de problemas
description: Las lecturas se han parado, un dispositivo se ha desconectado, una alerta no desaparece o algo no cuadra. Empieza aquí.
section: Help
reviewed: 2026-09-27
order: 1
---

Busca lo que te está pasando.

## Un widget no muestra ningún valor

Sigue esta lista en orden:

1. **Mira la antigüedad de los widgets de al lado.** Si todo está desactualizado, el problema es la conexión, no el parámetro.
2. **Abre la pestaña Dispositivos.** Si no se puede llegar a un dispositivo, lo pone en su fila.
3. **Revisa a qué acuario está asignado.** Un dispositivo que envía datos al acuario equivocado se ve igual que uno que no envía nada. Abre el dispositivo y comprueba su acuario.
4. **Comprueba que existe la fuente.** Si no tienes un equipo que mida el fosfato ni lo anotas a mano, no habrá datos de fosfato.

## Una lectura está desactualizada

La antigüedad no miente: no ha llegado nada nuevo.

- **Los parámetros que anotas a mano** se quedan desactualizados si no anotas ninguna lectura. Anota una.
- **Si se desactualiza la lectura de un equipo**, es que el dispositivo ha dejado de enviar datos. Revisa su fila en **Dispositivos**.
- **Algunos equipos son lentos de por sí.** Un valorador que mide cada hora mostrará normalmente `1h`. No es un fallo.

## No se puede llegar a un dispositivo

Casi siempre es la red.

1. ¿El equipo está encendido y funciona en su propia app?
2. ¿Está en la misma red en la que lo añadiste?
3. ¿Has cambiado algo del router (uno nuevo, otro nombre de red, aislamiento de la red de invitados)?

Los equipos que se conectan por tu red local tienen que estar accesibles en esa red. Los que se conectan a través de una cuenta del fabricante no lo necesitan, pero esa cuenta tiene que seguir siendo válida.

## Un dispositivo dice que se rechazó el inicio de sesión

El fabricante ha rechazado el inicio de sesión guardado. Casi siempre es porque cambiaste tu contraseña en su cuenta.

Abre la fila del dispositivo y vuelve a iniciar sesión.

## Falla el emparejamiento de un Cora Max

Si al añadir un Cora Max el proceso se para a mitad, Cora Mobile te dice en qué paso ha fallado y por qué, con **Cancelar** y **Reintentar** debajo.

- *"Tu teléfono no pudo comunicarse con el Cora Max en tu red Wi-Fi."* Conecta el teléfono y el Cora Max a la misma red Wi-Fi. En iPhone, comprueba también que Cora tiene acceso a la red local. **Ajustes → Acceso a dispositivos** te lleva ahí (más en [Ajustes](/help/mobile-settings)). Luego toca **Reintentar**.
- *"El Cora Max no aceptó esta sesión de emparejamiento."* Reintentar no servirá. Cierra la pantalla y empieza de nuevo desde **Dispositivos → Agregar dispositivo**.

Con cualquier otro mensaje, toca **Reintentar**.

## Cora Max muestra datos viejos

Mira la etiqueta de estado de la barra superior. **En línea** y **Nube** quieren decir que todo va bien. Si tienes más de un Cora, la pantalla que no recoge las lecturas muestra **Nube**, y sus datos están igual de al día. **Desactualizado** o **Sin conexión** quieren decir que la pantalla ha perdido su fuente y muestra los últimos datos que recibió. Es lo que debe hacer, pero esos datos no son actuales.

- Revisa el Wi-Fi en **Ajustes → Ajustes de Cora Max → Wi-Fi**
- Comprueba que la red funciona
- Si la etiqueta dice **En línea** o **Nube** y los datos siguen siendo viejos, el problema está antes de Cora Max. Mira el mismo acuario en el teléfono

## Una alerta no desaparece

Una alerta desaparece cuando la lectura vuelve a estar en rango. Si no desaparece:

- **La lectura sigue fuera de rango.** Mira el historial del widget.
- **El umbral no encaja con tu acuario.** Consulta [Alertas y umbrales](/help/mobile-alerts).
- **La fuente falla.** Una sonda que necesita calibración da un número que de verdad está fuera de rango. Arregla la sonda, no el umbral.

## Dos fuentes no coinciden

Aquí Cora está funcionando bien. Si tu sonda y tu kit de pruebas no coinciden, eso es algo real que está pasando en tu sistema.

Un resultado de ICP es una buena tercera opinión, pero no zanja la cuestión. Cada laboratorio da resultados algo distintos, y cómo se manipula y se envía la muestra también influye. Que dos pruebas coincidan vale mucho más que una sola.

Lo normal es que haya que calibrar la sonda. A veces el kit de pruebas está caducado. Calibra la sonda, repite la prueba con reactivo nuevo y compara las dos en las mismas condiciones. Un [resultado de ICP](/help/mobile-icp-health) te da un tercer dato para comparar.

## No me llegan notificaciones

1. En **Ajustes → Notificaciones**, comprueba que esa categoría tiene permitidas las notificaciones push
2. Revisa los permisos de notificaciones de Cora en los ajustes del teléfono
3. Recuerda que el resumen diario no avisa los días en que no ha cambiado nada

## Saber por qué ha cambiado algo

En **Ajustes → Actividad** tienes cada cambio de toma, alimentación, dosis y enchufe, y quién lo pidió: Cora Mobile, una pantalla Cora, la voz, Cora Assistant, una regla de automatización, un botón inteligente o tu cuenta.

## El panel ha quedado mal después de editarlo

Carga un diseño guardado. Abre **Mis paneles** y elige uno.

Si no tienes ninguno guardado, vuelve a montar el diseño y guárdalo. A partir de ahí, volver a él es un solo toque.

En cualquier caso, las lecturas, el historial y las entradas del diario se guardan aparte del diseño, así que no se pierde nada de lo que hay detrás del panel.

## "Las lecturas de Red Sea han dejado de actualizarse"

Ningún dispositivo de la red de este acuario está consultando ahora tu equipo Red Sea, así que las lecturas de la pantalla no se han actualizado.

1. Abre **Ajustes → Cora Max principal** y comprueba que hay un Cora Max fijado (o que está elegido **Cualquiera activo (automático)**).
2. Abre el acuario en un dispositivo que esté en el mismo Wi-Fi que el equipo Red Sea.
3. Comprueba que el equipo Red Sea está encendido y conectado en su propia app.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## "No se pudo contactar con esta bomba: no se envió nada"

Una orden para una bomba Jecod o Jebao no llegó a salir. Lo normal es que la bomba esté apagada o fuera de su red.

1. Comprueba que la bomba está encendida.
2. Comprueba que está en la misma red en la que la añadiste.
3. Toca **Reintentar**.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## "No se pudo contactar a esta bomba por Bluetooth. Acércate a ella e intenta de nuevo."

Un equipo Jecod que solo funciona por Bluetooth está fuera del alcance de tu teléfono.

1. Acércate a la bomba.
2. Toca **Reintentar**.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## "No se pudo contactar con ese Gyre. No se inició ninguna alimentación."

Un gyre Maxspect (integración en beta) no respondió cuando Cora intentó ponerlo en modo alimentación.

1. Comprueba que el gyre está encendido y conectado a su red.
2. Toca **Reintentar**.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## "No se pudo contactar con ese Gyre. Su programa no cambió."

No se pudo enviar el horario a un gyre Maxspect (integración en beta).

1. Comprueba que tu teléfono o tu Cora Max están en la red del gyre.
2. Toca **Reintentar** en la pantalla del horario.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## "No se pudo contactar al Apex: nada cambió" / "no se dosificó nada"

Un Neptune Apex, un Trident o un cabezal DŌS no respondió a una orden o a una dosis.

1. Abre la app del Apex y comprueba que está conectado.
2. Revisa la conexión de red del dispositivo que estás usando.
3. Toca **Reintentar**.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## "Esto no se pudo enviar: ningún dispositivo de este acuario puede enviarlo"

Ningún dispositivo Cora de este acuario tiene los datos de conexión del Apex que hacen falta para ejecutar la orden, o el que los tiene está desconectado.

1. Añade los datos del Apex en **Ajustes** desde un dispositivo que esté conectado, o
2. Fija otro Cora Max que funcione como **Cora Max principal** de este acuario.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## Un Cora Max secundario muestra "Cora principal sin conexión"

El Cora Max principal de este acuario se ha desconectado, así que esta pantalla secundaria muestra los últimos datos que recibió, no datos en directo.

1. Comprueba la alimentación y el Wi-Fi del Cora Max principal.
2. Espera a que se vuelva a conectar, o cambia el **Cora Max principal** a un dispositivo que esté conectado.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## "El dispositivo está sin conexión. Mostrando el último estado conocido."

Es lo normal cuando un dispositivo se desconecta. Ha dejado de enviar datos, y Cora muestra los últimos valores que tenía sin hacerlos pasar por actuales.

1. Revisa la conexión de red del dispositivo.
2. No tomes esos valores como actuales hasta que la fila deje de decir que está sin conexión.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## Algunos ajustes de ReefBeat salen en gris o no aparecen

No es un fallo. Los ajustes propios del dispositivo (lo que no son lecturas) solo se abren cuando el teléfono está en la misma red que el dispositivo. Fuera de esa red solo ves las lecturas.

1. Conéctate al Wi-Fi del acuario para cambiar esos ajustes.
2. Lejos del acuario, las lecturas y el historial siguen funcionando con normalidad.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## "No se pudo contactar con Cora. Comprueba tu Wi-Fi o tus datos móviles, y vuelve a intentarlo."

Al iniciar sesión, tu teléfono no tiene una conexión que funcione con Cora Cloud. El problema es la conexión del teléfono, no los equipos de tu acuario.

1. Comprueba que el teléfono tiene Wi-Fi o datos móviles funcionando.
2. Si tienes otra red a mano, prueba con ella.
3. Toca **Reintentar**.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## De repente todo está en otro idioma

Alguien ha cambiado el idioma de la cuenta desde algún dispositivo. El idioma es un solo ajuste para toda la cuenta, no uno por dispositivo.

1. Abre **Ajustes → Idioma** en Cora Mobile o en Cora Max.
2. Si se cambió por error, vuelve a ponerlo. El cambio se aplica en todas partes a la vez.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Una alerta o un informe antiguo sigue en el otro idioma

Es lo esperado. Cora no vuelve a traducir lo que ya estaba generado. Solo las alertas, informes y resúmenes nuevos salen en el idioma nuevo.

1. No hay nada que arreglar. Lo nuevo que llegue saldrá en el idioma actual.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Una alerta sigue avisando aunque ya la he visto

**Posponer** y **Descartar** en Cora Max solo silencian ese Cora Max. Tu teléfono sigue recibiendo notificaciones mientras la lectura esté fuera de rango.

1. Para recibir avisos con menos frecuencia en el teléfono, abre la regla de alerta en Cora Mobile y pon un **Tiempo de espera entre alertas** más largo (hasta 1 semana).
2. Si el umbral no encaja con tu acuario, cambia el propio umbral.

Si sigue sin funcionar, consulta [Alertas y umbrales](/help/mobile-alerts) o escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Una dosis se paró a mitad y salió una alerta de "restauración"

El cabezal DŌS perdió la conexión a mitad de la dosis. Cora te avisa y no da por hecho que entró la dosis completa.

1. Abre la alerta y mira cuánto se dosificó de verdad antes de que se parara.
2. Reanuda o ajusta la dosis según esa cantidad, no según la que estaba programada.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del acuario y del dispositivo.

## Una escena creada en el teléfono no se puede editar en Cora Max

Editar escenas directamente en Cora Max es una función reciente. Con un firmware más antiguo, Cora Max puede ejecutar las escenas creadas en el teléfono, pero no editarlas.

1. Actualiza Cora Max, o
2. Sigue editando esa escena desde el teléfono. Cora Max la ejecutará igual.

Si sigue sin funcionar, consulta [Actualizaciones y recuperación](/help/max-updates) o escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant responde sobre otro acuario

No elegiste un acuario antes de preguntar, o el acuario activo no es el que querías.

1. Elige primero el acuario del que quieres hablar.
2. Vuelve a preguntar.

Si sigue sin funcionar, consulta [El Asistente](/help/mobile-assistant) o escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant no responde o vuelve a mostrar la pantalla de consentimiento

La opción **Permitir que el Cora Assistant use los datos guardados del acuario** está desactivada, así que no tiene datos con los que responder.

1. Toca **Aceptar y continuar** en la pantalla de consentimiento para volver a activarla.

Si sigue sin funcionar, consulta [El Asistente](/help/mobile-assistant) o escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un resultado de ICP del laboratorio o enviado por correo no ha aparecido

Para que un resultado entre en Cora, hay que elegir a qué acuario va. A veces también tiene que llegar de un remitente conocido.

1. Mira el aviso de recepción que aparece la primera vez que envías un resultado a Cora.
2. Cuando te lo pregunte, confirma a qué acuario va el resultado.
3. Si ya habías enviado alguno antes, comprueba que el correo sale de la misma dirección que usaste entonces.

Si sigue sin funcionar, consulta [ICP e informes de salud](/help/mobile-icp-health) o escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Una notificación de ICP por correo no dice de qué laboratorio es

Era un fallo conocido: la notificación push de "elegir acuario" no incluía el nombre del laboratorio. Está corregido en las versiones actuales.

1. Actualiza Cora Mobile a la última versión.
2. El resultado en sí está bien. Solo faltaba el nombre en el texto de la notificación.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un widget muestra unidades que no quiero

Es el ajuste de unidades del acuario, no un problema de datos. Los valores se guardan igual, se muestren como se muestren.

1. Abre los **Ajustes** de ese acuario y revisa sus unidades.
2. Cámbialas ahí. Todos los teléfonos y Cora Max que muestran ese acuario se actualizan.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un medidor o un umbral se ve distinto después de cambiar las unidades

Es lo esperado. Los medidores, las casillas y el historial se vuelven a dibujar en la unidad que elegiste. Los valores no han cambiado.

1. No hay nada que arreglar. Solo cambia cómo se ve.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Max no se vuelve a conectar enseguida después de un corte de Wi-Fi

Cuando pierde la conexión, Cora Max espera un poco más antes de cada intento para no saturar la red, hasta llegar a más o menos un minuto entre intentos.

1. Espera un minuto más o menos después de que vuelva la red.
2. Si pasado ese tiempo sigue sin conectarse, revisa el Wi-Fi en **Ajustes → Ajustes de Cora Max → Wi-Fi**.

Si sigue sin funcionar, consulta [La pantalla de inicio de Cora Max](/help/max-tour) o escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cambié el nombre de un Cora Max en el teléfono y en la pantalla no cambia

El nombre que pones desde el teléfono es una etiqueta de la cuenta para ese dispositivo. El nombre que aparece en el propio Cora Max durante el emparejamiento puede ser otro.

1. Comprueba qué nombre estás mirando: el de la lista de dispositivos del teléfono o el de la pantalla de emparejamiento del Cora Max.
2. Si lo que quieres cambiar es la etiqueta de la cuenta, cámbiala desde la lista de dispositivos del teléfono.

Si sigue sin funcionar, escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con el nombre del dispositivo.

## No encuentro dónde desactivar la palabra de activación en Cora Max

El interruptor de la palabra de activación está en la sección **Sonido y voz**, no en los ajustes de Cora Assistant, que es donde casi todo el mundo mira primero.

1. Ve a **Ajustes → Ajustes de Cora Max → Sonido y voz → Escucha de palabra de activación**.
2. Desactívala. Podrás seguir tocando el icono de Cora para empezar una sesión de voz.

Si sigue sin funcionar, consulta [Ajustes en Cora Max](/help/max-settings) o escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## El bloqueo infantil no deja entrar a nadie en Ajustes

Funciona así. Pasado un tiempo sin que nadie toque la pantalla, el bloqueo infantil impide que nadie encienda o apague equipos desde esta pantalla, ni tocando ni por voz. Las lecturas siguen actualizándose, y puedes seguir haciéndole preguntas a Cora. Para desbloquear:

1. Pulsa **Subir volumen** o **Bajar volumen** tres veces en dos segundos, o
2. Mantén cinco dedos en la esquina superior derecha de la pantalla durante diez segundos.

Si sigue sin funcionar, consulta [Voz en Cora Max](/help/max-voice) o escribe a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Sigo sin solucionarlo

Escríbenos a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**. Dinos qué acuario, qué pantalla y qué esperabas ver. Así te podremos ayudar antes.
