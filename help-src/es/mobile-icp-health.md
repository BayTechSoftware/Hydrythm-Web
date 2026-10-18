---
title: ICP e informes de salud
description: Sube el PDF de una prueba ICP o haz que tu laboratorio lo envíe, lee la puntuación, sigue cada elemento a lo largo del tiempo y genera un informe de salud de todo tu sistema.
section: Cora Mobile
reviewed: 2026-10-17
order: 33
group: Intelligence
twin: max-intelligence
---

La pestaña **Inteligencia** es donde están tus resultados de laboratorio y tus informes a largo plazo. Elige primero un acuario arriba. Todo lo que hay en la pantalla pertenece a ese acuario.

![La pestaña Inteligencia](img/mobile-intelligence.webp "Sube un ICP, genera un informe de salud y mira qué ha cambiado desde el último.")

## Subir una prueba ICP {#uploading-an-icp-test}

Cora lee el informe PDF que te envía tu laboratorio. Descárgalo antes del correo o de la web de tu laboratorio. Las fotos, los escaneos y las capturas de pantalla no se pueden leer.

1. Toca **Subir ICP**.
2. Elige tu laboratorio, o déjalo en **Auto: detectar el laboratorio**. Cora tiene consejos para ATI, Fauna Marin, Modern Reef, Oceamo, Reef Zlements y Triton.
3. Indica qué es la muestra: **Agua de acuario**, **Agua RO/DI**, **Mezcla de sal** u **Otro**. Solo el agua de acuario actualiza tu panel y tus alertas.
4. Comprueba la fecha en que se tomó la muestra. Los laboratorios imprimen la fecha en que la analizaron, así que Cora te pide la tuya y dibuja los resultados según esa fecha.
5. Toca **Elegir PDF** y elige el archivo.

Normalmente tarda uno o dos minutos. Deja la pantalla abierta y el informe se abre en cuanto está listo. No tienes que escribir nada.

También puedes enviar el PDF por correo a **icp@in.coraiq.tech**. Envíalo desde tu correo de inicio de sesión o desde un correo de laboratorio verificado (mira más abajo), y llega como un resultado de un laboratorio.

Si subes el mismo informe dos veces, Cora te muestra el que ya tienes y no te lo vuelve a cobrar.

:::note Cora necesita antes tu permiso
El análisis de ICP envía el informe a la IA, así que necesita **Permitir que el Cora Assistant use los datos guardados del acuario**. Si está desactivado, Cora te lo pregunta antes de subirlo. Consulta [qué cubre el interruptor](/help/mobile-assistant#what-the-switch-covers).
:::

## Qué correo puede usar un laboratorio {#which-email-a-lab-can-use}

Un laboratorio o un resultado enviado por correo encuentra tu cuenta por la dirección de correo que conoce. Es tu correo de inicio de sesión, más cualquier correo de laboratorio que añadas en **Ajustes → la tarjeta de tu cuenta (Cuenta y suscripción) → Correos de laboratorio e ICP**.

1. Toca **Agregar correo de laboratorio** y escribe la dirección que usa tu laboratorio.
2. Toca **Enviar código**. Cora envía un código de 6 dígitos a esa dirección. Caduca a los 10 minutos.
3. Escribe el código y toca **Verificar**. Si no te ha llegado, toca **Reenviar código**.

Puedes añadir hasta 3 correos de laboratorio. Cada uno muestra **Verificado** o **Esperando el código**, y **Quitar** quita uno. A partir de entonces, los resultados enviados a esa dirección ya no llegan a tu cuenta. No se puede añadir una dirección que ya pertenece a otra cuenta de Cora.

Si iniciaste sesión con un correo oculto de Apple, los laboratorios no pueden encontrar tu cuenta. La pantalla de ICP muestra una tarjeta, **Recibe resultados de laboratorio automáticamente**, que te lleva a este ajuste. Cuando inicies sesión con Apple, elige **Compartir mi correo electrónico** para evitar el problema.

## Enviar a Cora: resultados que te entrega un laboratorio o un correo {#send-to-cora-results-a-lab-or-an-email-delivers-for-you}

Algunos laboratorios pueden enviar un resultado directamente a Cora, y un PDF de ICP que envías por correo llega de la misma forma. No tienes que subir nada tú.

Si tienes un solo acuario, un resultado de un laboratorio de confianza, o uno que enviaste por correo, va directamente a ese acuario. Con más de un acuario, verás un aviso: *"Un resultado de laboratorio de {lab} te está esperando."* Toca **Elegir acuario** y elige el acuario al que pertenece. Cora no puede deducirlo sola.

El informe muestra **Enviado por {lab}** cerca de la parte de arriba, o **Recibido por correo**, para que lo distingas de uno que subiste tú.

Si **Permitir que el Cora Assistant use los datos guardados del acuario** está desactivado, el resultado espera con el mensaje *Cora Assistant necesita tu autorización para leerlo.* Da tu autorización y entra.

:::note La primera vez
La primera vez que llega un resultado de esta forma, Cora muestra una breve indicación de lo que está pasando, para que no parezca un error.
:::

### El primer resultado de un laboratorio nuevo

La primera vez que un laboratorio te envía un resultado, Cora te pide que lo apruebes antes de añadirlo a ningún sitio, aunque solo tengas un acuario. Verás quién lo envió y puedes marcar **Confiar en este laboratorio** para saltarte esta comprobación la próxima vez que llegue un resultado suyo.

Toca **Aprobar** para incorporarlo, o **Rechazar** para borrarlo sin añadirlo a ningún acuario.

### Laboratorios de confianza y qué pueden ver los laboratorios {#trusted-labs}

**Ajustes → Cora Assistant → Laboratorios de confianza** lista todos los laboratorios en los que has confiado. La lista aparece en cuanto confías en al menos uno. **Revocar** quita un laboratorio, así que su siguiente resultado vuelve a necesitar tu aprobación.

**Compartir el análisis de Cora con los laboratorios**, en la misma pantalla, decide qué ve un laboratorio después de enviarte un resultado. Activado, puede ver las puntuaciones y el análisis escrito de Cora. Desactivado, solo ve que el resultado se entregó. Está desactivado hasta que lo actives. El mismo interruptor también aparece en un informe que te envió un laboratorio.

Si algo de esto no funciona, consulta [Solución de problemas](/help/troubleshooting).

## Qué recibes

![Un informe de ICP](img/mobile-icp-report.webp "Cada informe lleva una puntuación y un resumen escrito para tu acuario.")

Recibes una puntuación sobre 100 y un resumen en lenguaje sencillo de lo que significa para tu sistema, teniendo en cuenta el tipo de acuario, su edad y tu fauna.

La puntuación compara tus resultados con sus rangos objetivo, incluidos los rangos que hayas fijado tú. Si algún resultado está fuera de su rango, la puntuación no puede pasar de 70, así que no puede decir **Saludable**. Si uno está muy fuera, no puede pasar de 40, por buenos que sean los demás. La etiqueta bajo la puntuación dice **Saludable** de 71 a 100, **Necesita atención** de 40 a 70 y **Crítico** de 0 a 39. Los informes de salud se puntúan igual.

Se sigue cada elemento, incluidos los oligoelementos y los contaminantes además de los parámetros principales. Cora registra los 71 elementos que puede informar un laboratorio, y la línea que algunos laboratorios llaman *Acidez* es el pH.

En cada fila de elemento verás el rango que imprimió el laboratorio, mostrado como *Rango del laboratorio*, junto al rango propio de Cora para ese elemento. Un elemento para el que Cora no tiene rango de referencia lleva la etiqueta **Sin rango de Cora**. El informe indica cuántos elementos tienen un rango de Cora y valora el resto con el conocimiento general de arrecife. Cora Assistant comenta todos los elementos analizados, y su comentario se mantiene aunque no haya rango de Cora.

Si el laboratorio imprime *n.d.*, o *no detectado*, para un elemento, Cora lo registra como 0 e indica que no se detectó.

Si un laboratorio informa la **gravedad específica** (o densidad relativa) en lugar de la salinidad, Cora la guarda como salinidad, mostrada igualmente en SG, y la evalúa con tu rango de salinidad.

:::note El CO2 disuelto no es el CO2 de la habitación
**CO₂ disuelto** en un informe de ICP es el CO2 del agua, en mg/L. Es una lectura distinta del CO2 del aire de tu habitación. Los dos tienen rangos distintos y nunca se mezclan.
:::

La tarjeta **Desde tu último ICP** muestra lo que más ha cambiado desde la última vez. Suele ser la forma más rápida de entrar en un informe nuevo.

Toca **Tendencias** para ver cualquier elemento a lo largo de todas las pruebas que has subido. Aquí es donde el ICP se vuelve realmente útil.

:::tip La segunda prueba es la interesante
Un ICP te dice dónde estás. El segundo te dice hacia dónde vas, y eso es con lo que puedes actuar. Haz pruebas con un ritmo regular, y no esperes a que algo vaya mal.
:::

## Una prueba de RO/DI o de agua de origen

Si subes agua RO/DI u otra agua de origen, elige **Agua RO/DI** al subirla. Cora no la puntúa según los objetivos de tu acuario. Te da un veredicto sencillo sobre si el agua está lo bastante limpia para usarla, y deja esos números fuera de las lecturas de tu acuario. Se guarda como un informe aparte. Cora hace lo mismo con **Mezcla de sal** u **Otro**: dice cómo se ve la muestra y no la puntúa como si fuera tu acuario.

## Informes de salud {#health-reports}

Un **Informe de salud** es una revisión más a fondo de todo el sistema, que se hace de vez en cuando. Mira a la vez todos los parámetros, todas las fuentes, tu dosificación, tu historial y tus resultados de ICP recientes.

Toca **Informe de salud** y después **Generar**. Normalmente tarda unos veinte segundos. Como el análisis de ICP, necesita **Permitir que el Cora Assistant use los datos guardados del acuario**.

Úsalo cuando quieras una revisión cuidadosa del acuario. Buenos momentos son antes de un cambio grande, después de un problema o cada pocas semanas como control.

Un informe abierto tiene botones arriba para exportarlo como PDF, compartir una instantánea del acuario o eliminarlo.

## El ICP frente a tus sondas

Cora compara tus resultados de laboratorio con lo que informan tus equipos. Si tu sonda de alcalinidad dice 8,4 y tu ICP dice 7,6, querrás saberlo, y Cora te lo muestra sin elegir uno a escondidas.

Es una de las cosas más útiles que hace un ICP en Cora. Tómalo como una **tercera opinión**. No es la última palabra. Los laboratorios difieren, y la forma de manipular, guardar y enviar una muestra mueve el resultado. Un solo ICP es un indicio, y dos pruebas que coinciden cuentan mucho más que una. Si la diferencia se mantiene, revisa la sonda. Eso no demuestra que la sonda esté mal.

:::tip Cambiar de laboratorio o de método de prueba
Si cambias de laboratorio, o pasas entre las pruebas ICP-OES e ICP-MS de un laboratorio, tus resultados pueden moverse aunque nada haya cambiado en tu acuario. Cora lo señala cuando los compara. ICP-OES no puede medir valores muy bajos de cromo, estaño, níquel, cobre, cobalto o selenio. Así que un resultado **Por debajo del límite de detección** de esos elementos en una prueba ICP-OES no significa que tu acuario no tenga nada.
:::

## Tu cuota

Tu plan fija cuántos análisis de ICP e informes de salud tienes cada mes. La línea bajo los botones muestra lo que has usado. Las cifras de cada plan están en [Planes y suscripciones](/help/mobile-plans).

Cuando se acaban tus análisis de ICP, Cora te muestra primero los planes a los que puedes pasar. Si prefieres no mejorar tu plan, pregunta **¿Guardar los resultados sin el análisis de IA?** Toca **Guardar mis resultados** y Cora sigue leyendo el informe y guarda todos los valores, así que las tendencias, el historial y tus lecturas se actualizan con normalidad. La puntuación y el análisis escrito quedan bloqueados. Puedes generarlos más tarde desde el propio informe cuando tengas un análisis de ICP disponible.

Además del límite de tu plan, Cora acepta hasta 10 subidas de ICP al día. Una subida rechazada por ese motivo no gasta ninguno de los análisis de ICP de tu plan. Eso sí, Cora Mobile solo muestra un error de subida general, así que si las subidas empiezan a fallar después de muchas en un día, vuelve a intentarlo mañana.

## Dónde están los informes

La pantalla Inteligencia mantiene separados los dos tipos. Los resultados de laboratorio están en **INFORMES DE ICP** y las revisiones generadas en **INFORMES DE SALUD**. Cada lista muestra primero el más reciente, con su puntuación. Toca uno para volver a abrirlo completo.

También puedes llegar a ellos desde **Ajustes**: abre un acuario y después **Informes ICP** o **Informes de salud**.
