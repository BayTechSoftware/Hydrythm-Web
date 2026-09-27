---
title: Añadir, editar y eliminar dispositivos
description: Cómo añadir equipo a Cora, asignarlo a un acuario, renombrarlo y eliminarlo correctamente.
section: Cora Mobile
reviewed: 2026-09-27
order: 9
group: Equipment
---

La pestaña **Dispositivos** es todo lo que tienes conectado, agrupado por marca. Cada grupo se pliega para que un cuarto de acuarios lleno de equipos siga siendo legible.

![La pestaña Dispositivos](img/mobile-devices.webp "El equipo se agrupa por marca. Cada grupo se pliega.")

## Añadir equipo

Debajo de la lista hay tres botones, y hacen trabajos distintos:

| Botón | Añade |
|---|---|
| **Agregar dispositivo** | Un Cora Max. Encuentra unidades ya en tu Wi-Fi, o cercanas por Bluetooth. **Introducir dirección IP manualmente** está dentro de esta pantalla si la detección no lo encuentra. |
| **Buscar una bomba en tu red** | Bombas Jecod que se anuncian en la red local |
| **Agregar AquaWiz** | Un controlador AquaWiz, a través de tu cuenta AquaWiz |

![Añadir un Cora Max](img/mobile-add-device.webp "Agregar dispositivo busca un Cora Max por Wi-Fi y Bluetooth.")

Otro equipo (Neptune Apex y Red Sea ReefBeat) se conecta desde el acuario en lugar de desde esta lista. Consulta [Conectar tu equipo](/help/mobile-connections).

Añadir equipo como un calentador, una bomba o un skimmer ofrece un **autocompletado** de marca y modelo: empieza a escribir y Cora sugiere a partir de una lista amplia y verificada de marcas de equipos. Si la tuya no aparece, escríbela igualmente; Cora conserva lo que escribas.

:::note Cora y tu teléfono necesitan la misma red
El equipo detectado localmente debe estar en la misma red que tu teléfono cuando lo añades. **Después de configurarlo, sigue siendo accesible solo por esa red** (o por Bluetooth, para unidades que lo usan) a menos que un dispositivo Cora en el lugar pueda alcanzarlo por ti.

Un equipo que lee correctamente en casa puede por tanto mostrar valores más antiguos mientras estás fuera, a menos que un Cora Max en el lugar pueda consultarlo. Esto refleja desde dónde es accesible el equipo, no un fallo.
:::

## Asignar un dispositivo a un acuario

La mayoría del equipo pertenece a exactamente un acuario, y eso es lo que hace que sus lecturas aparezcan en el panel de ese acuario.

**Cora Max es la excepción**: se le pueden asignar hasta cuatro acuarios y cambia entre ellos en pantalla. Consulta [Más de un dispositivo Cora](/help/mobile-multi-device).

Abre el dispositivo y elige **Acuario**. Si tienes más de un sistema, este es el ajuste que importa más: un calentador asignado al acuario equivocado informa perfectamente bien, pero al lugar equivocado.

:::warning Asigna el acuario antes de confiar en las lecturas
Un dispositivo sin acuario sigue informando, pero sus números no tienen dónde aterrizar. Si un dispositivo que acabas de añadir no aparece en un panel, revisa esto primero.
:::

## Renombrar

Abre el dispositivo y edita su nombre. Usa el nombre que usas para él día a día: "Retorno", "Gyre izquierdo", "Calentador del sump". El nombre aparece en los widgets, en las alertas y en cualquier cosa que le preguntes a Cora, así que un nombre que signifique algo para ti aclara todo lo que viene después.

Renombrar es local a Cora. No cambia el nombre en la propia aplicación del fabricante.

## Comprobar si un dispositivo está sano

Cada fila muestra su estado actual. Lo que quieres ver es una hora de actualización reciente y ningún aviso.

| Lo que ves | Lo que significa |
|---|---|
| Una hora de actualización reciente | Funciona con normalidad |
| "Actualizado hace 3 h" en algo que informa cada hora | Bien |
| "No se pudo contactar…" | Un problema de red, o el dispositivo está apagado |
| "…rechazó el inicio de sesión" | La cuenta del fabricante necesita reconectarse; abre el dispositivo e inicia sesión de nuevo |
| Nada en absoluto | Nunca ha informado; revisa la asignación del acuario y la conexión |

## Eliminar un dispositivo

Abre el dispositivo y elige **Quitar**. Se te pedirá confirmar, y se te dirá exactamente qué se está eliminando.

**Tus lecturas se conservan.** Eliminar un dispositivo detiene la recopilación de datos nuevos de él; el historial que ya reunió se queda en el acuario, y cualquier widget apuntado a él conserva sus lecturas pasadas.

Lo que pierdes es el vínculo en vivo, y, cuando el dispositivo se conectaba a través de una cuenta del fabricante, el inicio de sesión guardado. Volver a añadirlo significa iniciar sesión de nuevo.

:::tip Silencia un dispositivo ruidoso sin eliminarlo
Si un dispositivo funciona correctamente pero alerta con demasiada frecuencia, ajusta sus umbrales o sus ajustes de notificación; consulta **[Alertas y umbrales](/help/mobile-alerts)**. Eso mantiene la conexión y los datos mientras detiene el ruido.
:::
