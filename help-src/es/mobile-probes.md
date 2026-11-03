---
title: Asignación de parámetros y sondas
description: Ve las lecturas de cada dispositivo en una lista, elige con qué parámetro se muestra cada una y qué dispositivo la alimenta, y registra calibración y limpieza de sondas.
section: Cora Mobile
reviewed: 2026-11-03
order: 15
group: Equipment
---

Usa **Asignación de parámetros** para decirle a Cora con qué parámetro se muestra cada lectura y, cuando dos dispositivos informan de lo mismo, en cuál confiar. Ve a **Ajustes**, abre el acuario y toca **Asignación de parámetros**.

![Los ajustes del acuario en Cora Mobile, con Asignación de parámetros y Socios conectados](img/mobile-tank-settings.webp "Ajustes y después tu acuario: Asignación de parámetros es la segunda fila.")

Está entre **Editar acuario** y **Umbrales de alerta**. El lápiz de la parte superior del panel abre **Editar acuario**, que no la tiene. También puedes llegar desde las páginas de dispositivo de Neptune Apex.

La pantalla es una sola lista de dispositivos, con un campo de búsqueda (**Buscar parámetros**) encima. La búsqueda mira los nombres de parámetros, los nombres de lecturas, los dispositivos y las marcas. El mismo campo de búsqueda está en todos los selectores de parámetros.

## Una sola lista de dispositivos {#mapping}

![Asignación de parámetros en Cora Mobile, con un dispositivo abierto](img/mobile-probe-mapping.webp "Una sola lista de dispositivos. Abre un dispositivo para ver sus lecturas y como qué se muestra cada una.")

Bajo el campo de búsqueda, Cora explica la pantalla en una línea: las lecturas de cada dispositivo y el parámetro del acuario como el que se muestran. Toca una lectura para cambiarla.

- **Cada dispositivo aparece con el nombre que le diste.** Un dispositivo sin nombre aparece con su marca, y dos dispositivos sin nombre de la misma marca se numeran ("AquaWiz 1", "AquaWiz 2"). Los números de serie y los ID de dispositivo nunca se usan como nombres; están tras **Mostrar detalles** en la página del dispositivo. Consulta [La página de un dispositivo](/help/mobile-devices#a-devices-page).
- **Cada lectura aparece bajo el dispositivo que realmente la informa.** Cada fila muestra el nombre que el dispositivo da a la lectura, su último valor y **Se muestra como**, el parámetro del acuario que alimenta. Una lectura que ocultaste dice **No se muestra**.
- **Un acuario tiene un solo Neptune Apex**, por muchos dispositivos Cora que lo lean. Sus sondas son una sola lista bajo una sola sección **Apex** (o bajo el nombre que le diste). Un módulo de expansión del Apex, como un DŌS o un Trident, aparece con su propio nombre. Sus lecturas no se pueden redirigir; al tocar una puedes cambiar el nombre del parámetro.
- **Un dispositivo compartido con otros acuarios aparece en la lista de cada acuario al que está vinculado.** Su sección dice *También en* y los nombres de los otros acuarios, seguido de *Los cambios aquí solo se aplican a este acuario.*
- **Un dispositivo con dos lecturas o menos empieza abierto**; uno más largo empieza cerrado y muestra su número de lecturas, salvo que una de sus lecturas comparta un parámetro con otro dispositivo. Toca el nombre de un dispositivo para abrirlo o cerrarlo. Mientras buscas, todas las coincidencias están abiertas.

Cora reconoce sola los nombres estándar de las lecturas, así que la mayoría de las filas ya muestran el parámetro correcto. Corrige solo las pocas que no ha sabido identificar.

Un cambio se guarda en cuanto lo eliges, y no hay botón de guardar. Empieza a funcionar con las siguientes lecturas. Corregirlo aquí no reescribe el historial: las lecturas anteriores se quedan donde están, y solo cambia lo que se guarda desde ese momento. Las asignaciones que hiciste antes de este diseño se conservan sin cambios.

:::warning Cora no ve una lectura oculta
Si un parámetro no muestra lecturas pero el dispositivo funciona, comprueba si su lectura dice **No se muestra**.
:::

:::note Un sensor de fugas no se puede reasignar aquí
La alarma de un sensor de fugas depende de su propio nombre, así que su fila dice *La alarma de fuga depende de este nombre, así que no se puede cambiar aquí.* Funciona igual que siempre.
:::

:::note Dispositivos que aún necesitan una actualización
Un dispositivo que espera una actualización de firmware dice *Los cambios aquí se aplican tras actualizar el firmware de este dispositivo.* Tu elección se guarda y se aplica cuando la actualización esté instalada.
:::

## Elegir como qué se muestra una lectura {#shows-as}

Para cambiar como qué se muestra una lectura:

1. Ve a **Ajustes**, toca tu acuario en **Acuarios** y luego **Asignación de parámetros**.
2. Toca el nombre de un dispositivo para abrirlo. Para encontrar una lectura más rápido, escribe parte de su nombre en **Buscar parámetros**.
3. Toca la lectura. Se abre **Mostrar esta lectura como**.
4. Toca el parámetro como el que debe mostrarse. Tu elección se guarda al instante y la hoja se cierra.
5. Comprueba la etiqueta **Se muestra como** de la lectura en la lista. Ahora nombra el parámetro que elegiste.

![Mostrar esta lectura como, con la lista de tus parámetros y de dónde saca cada uno sus lecturas](img/mobile-probes-shows-as.webp "Cada parámetro indica de dónde vienen sus lecturas: un dispositivo, nada por ahora o tus resultados de ICP.")

Toca una lectura para abrir **Mostrar esta lectura como**. Arriba está la lectura misma: el dispositivo, el nombre de la lectura y su valor. Debajo:

- **Tus parámetros** lista cada parámetro de este acuario. Cada opción indica de dónde vienen sus lecturas, para que nunca tengas que adivinar entre dos nombres parecidos:
  - *Viene de* y el nombre del dispositivo que lo alimenta, o *También viene de* y el nombre de otro dispositivo cuando esta lectura ya se muestra como ese parámetro.
  - *Ningún dispositivo lo alimenta ahora. Último valor …* con hace cuánto, para un parámetro cuyo dispositivo ha dejado de informar.
  - *De tus resultados de pruebas* o *De resultados de ICP*, con el último valor, para un parámetro que solo tiene tus propios resultados.

  El lápiz (**Cambiar nombre**) junto a un parámetro le da tu propio nombre. Es el que aparece en tu panel, en las alertas y en Reef Buddy. Deja el nombre vacío para restablecerlo.
- **Más parámetros** está plegado. Contiene los parámetros estándar que este acuario aún no tiene.
- **Nuevo parámetro…** crea un parámetro propio, separado de tus otros parámetros. Mira más abajo.
- **No mostrar esta lectura** (*Cora la ignora*) impide que la lectura se registre como ningún parámetro. Una lectura oculta no sale en ningún panel y no genera alertas.

La hoja termina con *Se guarda en cuanto eliges. Las lecturas anteriores se quedan donde están.*

![El final de Mostrar esta lectura como, con Más parámetros, Nuevo parámetro y No mostrar esta lectura](img/mobile-probes-shows-as-end.webp "Baja hasta el final para ver Más parámetros, Nuevo parámetro… y No mostrar esta lectura.")

### Nuevo parámetro {#new-parameter}

Usa **Nuevo parámetro…** cuando una lectura no deba mezclarse con otra del mismo nombre, por ejemplo una segunda sonda de pH en el sump. Cora abre **Nuevo parámetro** y explica que la lectura de ese dispositivo se mostrará como un parámetro propio y que su unidad viene del dispositivo.

1. En **Mostrar esta lectura como**, baja hasta el final y toca **Nuevo parámetro…**.
2. Escribe un **Nombre**. Cualquier nombre, por ejemplo *pH sump* o *pH 2*, de hasta 32 caracteres.
3. Toca **Crear**. **Crear** sigue en gris mientras el nombre esté vacío. **Cancelar** cierra la ventana y no cambia nada.

![El cuadro Nuevo parámetro](img/mobile-probes-new-parameter.webp "Nuevo parámetro: la lectura obtiene un parámetro propio, con la unidad que viene del dispositivo.")

La lectura alimenta ahora el nuevo parámetro. El nombre conserva la grafía que escribiste. Si escribes el nombre de un parámetro que ya tienes, la lectura se une a él y su nombre no se modifica. No se copia ningún rango de alerta de otro parámetro.

## Pruebas y resultados de laboratorio {#tests-and-lab-results}

Los resultados de tus propias pruebas y tus resultados de ICP aparecen al final, en **Pruebas y resultados de laboratorio**. La sección empieza cerrada, porque solo un informe de ICP tiene decenas de elementos. Tócala para abrirla. Los resultados se agrupan en **Resultados de ICP** y **Tus resultados de pruebas**.

Cada resultado se asigna a un parámetro igual que la lectura de un dispositivo. Toca uno para abrir **Mostrar esta lectura como** y elegir el parámetro con el que aparece, por ejemplo para mantener el pH de un kit de pruebas separado del de una sonda. Cora lo dice en la sección: los resultados nuevos siguen tu elección, y los anteriores se quedan donde están. Un resultado de prueba o de ICP nunca se descarta, así que **No mostrar esta lectura** no se ofrece para él.

Los parámetros que no alimenta ninguna lectura de arriba y que no son pruebas aparecen en **Otros parámetros**. Toca uno para cambiarle el nombre.

## Varias sondas para un mismo parámetro {#multiple-probes}

Si dos lecturas se muestran como el mismo parámetro, ya sean de dos sondas de un dispositivo o de dos dispositivos distintos, aparece un aviso arriba de la lista. Dice por ejemplo *pH recibe lecturas de 2 dispositivos* (o *2 sondas*), seguido de lo que hace Cora: *Se muestra la más reciente.* o *Usando* el dispositivo que elegiste. Tócalo, o toca **Elegir una**, para abrir la hoja.

- **Lectura más reciente** (*El dispositivo que informó por última vez*) deja que Cora use el dispositivo que informó más recientemente. Los demás se quedan en el historial.
- Elige un dispositivo o una sonda para seguir solo esa. Cada una muestra su valor y hace cuántos minutos informó. Tu elección se aplica a ese parámetro en todo el acuario: su mosaico, su gráfico y sus alertas, no un solo widget.
- **Mostrar una por separado** (*Por ejemplo, una segunda sonda en el sump*) pregunta **¿Cuál se debe mostrar por separado?** y después abre **Mostrar esta lectura como** para la que elijas.

Si un dispositivo que elegiste deja de informar, el aviso dice *No reporta desde* y la hora, y ofrece **Usar la más reciente**, para que una sonda muerta no deje una lectura bloqueada.

Puedes comparar las fuentes en [la vista del parámetro](/help/mobile-metric-detail).

Cuando dos fuentes informan del mismo parámetro, gana la medición más reciente. Un valor en pantalla solo lo reemplaza una lectura con una hora de medición posterior, venga del dispositivo que venga. Una lectura más antigua, o un dispositivo que reenvía una antigua, va al historial y no sobrescribe el valor actual. Si elegiste un dispositivo, Cora sigue ese dispositivo.

El perfil del acuario también tiene una sección **Fuentes de parámetros** (está oculta mientras creas un acuario nuevo). Configura lo mismo de forma más resumida. Usa Asignación de parámetros cuando quieras ver todos los dispositivos y lecturas en un solo sitio.

## Registrar el cuidado de las sondas {#recording-probe-care}

Las sondas se descalibran. Cuando calibres, limpies o cambies una sonda, díselo a Cora, para que no confunda el salto de la lectura con un cambio real en el acuario.

1. Toca el widget del parámetro en el panel, por ejemplo pH, temperatura, salinidad u ORP.
2. Toca **Registrar cuidado de sonda** (el icono del sensor) en la barra superior.
3. Elige lo que hiciste: **Calibrada**, **Limpiada**, **Reemplazada**, **Reposicionada** o **Comparada con una referencia**. Puedes añadir una **Lectura de referencia** y una nota.
4. Toca **Registrar cuidado de sonda**.

La vista del parámetro muestra entonces cuánto hace que se calibró esa sonda. El cuidado de las sondas también funciona bien como [tarea de mantenimiento](/help/mobile-maintenance) periódica.

:::note Las fechas de calibración explican las diferencias
Cuando una sonda y un kit de pruebas no coinciden, mira cuándo calibraste la sonda por última vez. Casi siempre esa es la respuesta.
:::
