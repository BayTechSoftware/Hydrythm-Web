---
title: Añadir, editar y eliminar dispositivos
description: Cómo añadir equipos a Cora, asignarlos a un acuario, cambiarles el nombre y quitarlos bien.
section: Cora Mobile
reviewed: 2026-09-27
order: 9
group: Equipment
---

En la pestaña **Dispositivos** está todo lo que tienes conectado, agrupado por marca. Cada grupo se puede plegar, así la lista se sigue leyendo bien aunque tengas una sala llena de equipos.

![La pestaña Dispositivos](img/mobile-devices.webp "Los equipos se agrupan por marca y cada grupo se puede plegar.")

## Añadir equipos

Debajo de la lista hay tres botones y cada uno sirve para algo distinto:

| Botón | Qué añade |
|---|---|
| **Agregar dispositivo** | Un Cora Max. Busca los que ya están en tu Wi-Fi o cerca por Bluetooth. Si no lo encuentra, dentro de esta pantalla tienes **Introducir dirección IP manualmente**. |
| **Buscar una bomba en tu red** | Bombas Jecod que se anuncian en la red local |
| **Agregar AquaWiz** | Un controlador AquaWiz, con tu cuenta de AquaWiz |

![Añadir un Cora Max](img/mobile-add-device.webp "Agregar dispositivo busca un Cora Max por Wi-Fi y Bluetooth.")

Los demás equipos (Neptune Apex y Red Sea ReefBeat) se conectan desde el acuario, no desde esta lista. Lo explicamos en [Conectar tus equipos](/help/mobile-connections).

Cuando añades un equipo como un calentador, una bomba o un skimmer, puedes **autocompletar** la marca y el modelo. Empieza a escribir y Cora te sugiere nombres de una lista amplia de marcas comprobadas. Si la tuya no sale, escríbela igual. Cora guarda lo que pongas.

:::note Cora y tu teléfono tienen que estar en la misma red
Los equipos que se detectan en la red local tienen que estar en la misma red que tu teléfono cuando los añades. **Después de configurarlos, solo se puede llegar a ellos por esa red** (o por Bluetooth, si el equipo lo usa), salvo que un dispositivo Cora en casa pueda hacerlo por ti.

Por eso, un equipo que en casa marca bien puede mostrar valores más antiguos cuando estás fuera, salvo que un Cora Max en casa pueda consultarlo. No es un fallo. Depende de desde dónde se puede llegar al equipo.
:::

## Asignar un dispositivo a un acuario

Casi todos los equipos pertenecen a un solo acuario. Esa asignación es la que hace que sus lecturas salgan en el panel de ese acuario.

**Cora Max es la excepción.** Puedes asignarle hasta cuatro acuarios y pasar de uno a otro en su pantalla. Más información en [Más de un dispositivo Cora](/help/mobile-multi-device).

Abre el dispositivo y elige **Acuario**. Si tienes más de un sistema, este es el ajuste más importante. Un calentador asignado al acuario equivocado envía sus datos sin problema, pero al sitio equivocado.

:::warning Asigna el acuario antes de fiarte de las lecturas
Un dispositivo sin acuario sigue enviando datos, pero sus números no tienen dónde aparecer. Si acabas de añadir un dispositivo y no sale en ningún panel, revisa esto primero.
:::

## Cambiar el nombre

Abre el dispositivo y edita el nombre. Ponle el que usas en el día a día: "Retorno", "Gyre izquierdo", "Calentador del sump". El nombre sale en los widgets, en las alertas y en todo lo que le preguntes a Cora. Si significa algo para ti, todo lo demás se entiende mejor.

El nombre solo cambia en Cora. En la aplicación del fabricante sigue igual.

## Comprobar que un dispositivo funciona bien

Cada fila muestra su estado actual. Lo que quieres ver es una hora de actualización reciente y ningún aviso.

| Lo que ves | Qué significa |
|---|---|
| Una hora de actualización reciente | Funciona con normalidad |
| "Actualizado hace 3 h" en algo que solo informa cada pocas horas | Todo bien |
| "No se pudo contactar…" | Un problema de red, o el dispositivo está apagado |
| "…rechazó el inicio de sesión" | Hay que volver a conectar la cuenta del fabricante. Abre el dispositivo e inicia sesión otra vez |
| Nada | Nunca ha enviado datos. Revisa el acuario asignado y la conexión |

## Quitar un dispositivo

Abre el dispositivo y elige **Quitar**. Tendrás que confirmarlo y verás exactamente qué se va a quitar.

**Tus lecturas se conservan.** Al quitar un dispositivo, Cora deja de recoger datos nuevos de él. El historial que ya tenía se queda en el acuario, y los widgets que lo usaban conservan sus lecturas pasadas.

Lo que pierdes es la conexión en directo y, si el dispositivo se conectaba con una cuenta del fabricante, el inicio de sesión guardado. Si lo vuelves a añadir, tendrás que iniciar sesión otra vez.

:::tip Silencia un dispositivo pesado sin quitarlo
Si un dispositivo funciona bien pero te avisa demasiado, cambia sus umbrales o sus notificaciones. Lo explicamos en [Alertas y umbrales](/help/mobile-alerts). Mantienes la conexión y los datos, y se acaban los avisos de más.
:::
