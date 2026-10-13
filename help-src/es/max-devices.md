---
title: Dispositivos y estado de los dispositivos
description: Ve y cambia el nombre de los equipos que lee Cora Max, elige qué Cora Max lee cada acuario, arregla un acuario cuyas lecturas se han detenido y gestiona un Cora Max desde tu teléfono.
section: Cora Max
reviewed: 2026-10-13
order: 7
group: Equipment
twin: mobile-devices
---

**Ajustes → Dispositivos** en Cora Max lista los equipos que puede ver y cómo está cada dispositivo. El icono de dispositivos de la barra superior abre la misma lista, filtrada por el acuario que hay en pantalla.

## La lista de dispositivos {#the-device-list}

![La lista de dispositivos en Cora Max, filtrada por acuario y agrupada por marca](img/max-devices.webp "Filtra por acuario, y después cada dispositivo agrupado por marca, con un resumen de una línea y su acuario.")

Cora Max ve los mismos equipos que tu teléfono, porque los dos leen la misma cuenta.

Usa las etiquetas de filtro de arriba para mostrar **Todos los acuarios** o solo uno. Los dispositivos se agrupan por marca. Cada entrada tiene un punto de estado (gris cuando Cora todavía no lo sabe, verde cuando funciona, naranja para un aviso o un fallo, rojo cuando está desconectado), un resumen de una línea de lo que tiene el dispositivo (*21 tomas · 4 alimentaciones*, *quedan 19 pruebas*), el acuario al que pertenece y cuándo se vio por última vez (**Visto por última vez**). Los dispositivos Beta llevan una etiqueta **Beta**.

Toca un dispositivo para abrir su página. Todas las páginas de dispositivo se abren con una sección **Estado**. Lo que puede hacer cada página está en [Controlar equipos desde Cora Max](/help/max-device-control).

Si la lista dice **Todavía cargando algunos dispositivos: esta lista puede estar incompleta.**, espera un momento.

:::note Beta
**Beta.** Las luces, bombas y dosificadoras EcoTech, los monitores de aire de habitación Inkbird y las cámaras están en Beta y solo están abiertos a los usuarios Beta. Si no eres usuario Beta, no los verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html). Más información en [Funciones Beta](/help/mobile-beta).
:::

### Cambiar el nombre de un dispositivo {#renaming-a-device}

Toca el lápiz de la fila de un dispositivo, o de su página, y escribe el nombre nuevo. Deja el nombre vacío para volver al nombre propio del dispositivo. El nombre se comparte con tu teléfono, así que también cambia allí.

### Añadir y quitar dispositivos {#adding-and-removing-devices}

Los dispositivos se añaden, se asignan y se quitan en tu teléfono. Cora Max los muestra y los controla. Si todavía no hay dispositivos, esta pantalla dice **Agrega dispositivos en la app de Cora.** Más información en [Añadir, editar y eliminar dispositivos](/help/mobile-devices).

## Cora Max principal: qué dispositivo habla con tus equipos {#primary-cora-max}

El **Cora Max principal** es el Cora Max (u otro dispositivo Cora) que lee el controlador y el resto de equipos de un acuario para toda la cuenta. Cada acuario solo necesita un dispositivo que haga esto. Todas las demás pantallas muestran lo que lee.

Para verlo o cambiarlo, abre **Ajustes → [tu acuario] → Cora Max principal**. Tienes dos opciones.

- **Cualquiera activo (automático)** significa que todos los dispositivos Cora en línea que pueden llegar a los equipos de este acuario se reparten el trabajo, y vale la última escritura. Usa esta opción salvo que tengas un motivo para fijar un dispositivo.
- Fijar un dispositivo, para que solo ese dispositivo lea los equipos. Si se desconecta, ningún otro Cora Max lo sustituye. Solo Cora Mobile, abierta en el mismo Wi-Fi, lee los equipos hasta que fijes otro o vuelvas a **Cualquiera activo (automático)**.

Esto se fija una vez para el acuario, y se aplica a todas las pantallas Cora. Puedes cambiarlo desde cualquier Cora Max que muestre el acuario, o desde Cora Mobile (**Hacer Cora Max principal** en la página del Cora Max). Más información en [Más de un dispositivo Cora](/help/mobile-multi-device).

:::note Cora Max principal y el dispositivo que responde son dos ajustes distintos
Cora Max principal decide qué dispositivo **lee tus equipos**. El **Dispositivo que responde** en Cora Mobile decide cuál **responde a "Hey Cora"**. Si tienes más de un Cora Max, puedes configurarlos por separado. Más información en [Hablar con Cora](/help/max-voice).
:::

## Si las lecturas de un acuario se detienen {#if-a-tanks-readings-stop}

Si las lecturas de un acuario se detienen mientras otro acuario de la misma pantalla se sigue actualizando, empieza por aquí.

1. Abre **Ajustes → [ese acuario] → Cora Max principal**. Comprueba que hay un dispositivo asignado y que está en línea.
2. Si otro Cora Max de este acuario muestra **Cora principal sin conexión** en su barra superior, el principal ha perdido la conexión. Qué significa la etiqueta de estado se explica en [La pantalla de inicio de Cora Max](/help/max-tour#what-the-status-pill-means).
3. **Ajustes → Ajustes de Cora Max → Red y actualizaciones → Sondeo de dispositivos** muestra cada cuánto lee este Cora Max tus dispositivos. Aquí solo puedes verlo. Se configura desde Cora Mobile.
4. Revisa la sección **Estado** de **Ajustes → Ajustes de Cora Max**. Muestra el estado de consulta, la hora de la última consulta y la última escritura en la nube de cada acuario, sin cambiar nada.

Si eso no ayuda, echa un vistazo a [Solución de problemas](/help/troubleshooting).

## Gestionar un Cora Max desde tu teléfono {#managing-a-cora-max-from-your-phone}

Abre la pestaña **Dispositivos** en tu teléfono y toca el Cora Max. La tarjeta de arriba muestra su variante, su firmware y cuándo se vio por última vez. Desde ahí puedes cambiarle el nombre y, cuando hay una versión nueva, tocar **Actualizar a v…** para instalarla ahora. La tarjeta **PIN de recuperación** está justo debajo.

![La página de un Cora Max en Cora Mobile, con Bloqueo infantil, Consulta del dispositivo, Zona horaria y Acuarios asignados](img/max-from-phone.webp "Los ajustes propios de un Cora Max en tu teléfono: Bloqueo infantil, Consulta del dispositivo y Zona horaria, y después sus acuarios.")

Estos ajustes solo afectan a **esa pantalla**, igual que si los cambiaras en la pared:

| Sección | Ajustes |
|---|---|
| **Pantalla** | **Brillo**, **Atenuar después de** |
| **Sonido y voz** | **Sonido de alerta** activa o desactiva el aviso sonoro de alerta en esa pantalla, y **Volumen de alerta** fija lo fuerte que suena. Las alertas se siguen mostrando en pantalla, y el historial de alertas y las notificaciones push no cambian |
| **Bloqueo infantil** | **Bloqueo infantil** bloquea la pantalla táctil de esa pantalla e impide que maneje equipos por voz |
| **Red y actualizaciones** | **Consulta del dispositivo** (cada cuánto lee tus equipos) y **Zona horaria** (se usa para la atenuación nocturna y la ventana de actualización) |

En **Acuarios**, cada acuario que muestra este Cora Max tiene una tarjeta con **Diseño del panel**, **Editar acuario** y su dispositivo de consulta. **Agregar acuario** y el icono de quitar cambian qué acuarios muestra, y esos cambios se aplican a toda la cuenta. Solo puedes hacerlos en tu teléfono. Los pasos están en [Configurar Cora Max](/help/max-setup#changing-which-tanks-it-shows). Qué dispositivo es el Cora Max principal de un acuario se puede cambiar desde tu teléfono o desde Cora Max.

En **Restablecer**, **Restablecer pantalla** devuelve la pantalla a su pantalla de emparejamiento. Se queda en tu Wi-Fi, así que puedes volver a emparejarla por Bluetooth, y los datos de tu acuario se conservan. **Quitar dispositivo** la quita de tu cuenta. Las lecturas de tu acuario se conservan, y puedes volver a emparejarla más adelante.
