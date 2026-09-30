---
title: Añadir, editar y eliminar dispositivos
description: Cómo añadir equipos a Cora, asignarlos a un acuario y quitarlos bien, todo desde un mismo sitio.
section: Cora Mobile
reviewed: 2026-09-30
order: 9
group: Equipment
---

Añade, edita, asigna y quita cada dispositivo desde la pestaña **Dispositivos**, agrupados por marca. Cada grupo se puede plegar, así la lista se sigue leyendo bien aunque tengas una sala llena de equipos.

![La pestaña Dispositivos](img/mobile-devices.webp "Los equipos se agrupan por marca y cada grupo se puede plegar.")

## Añadir equipos

Toca **Agregar dispositivo** y elige la marca: **Cora**, **Neptune Apex**, **Red Sea**, **Jecod**, **Maxspect**, **GHL** *(beta)*, **HYDROS** *(beta)* o **AquaWiz**. Cada una abre justo lo que necesita para encontrar tu equipo: un escaneo de red, una dirección IP, un inicio de sesión o una clave de dispositivo. [Conectar tus equipos](/help/mobile-connections) explica lo que necesita cada marca.

**Cora** es como se empareja un Cora Max nuevo. Busca los que ya están en tu Wi-Fi, o cerca por Bluetooth. Si no lo encuentra, usa **Introducir dirección IP manualmente** en esa misma pantalla.

Cuando añades un equipo como un calentador, una bomba o un skimmer, Cora te sugiere marcas y modelos mientras escribes. Las sugerencias vienen de una lista amplia de marcas comprobadas. Si la tuya no sale, escríbela igual. Cora guarda lo que pongas.

:::note Cora y tu teléfono tienen que estar en la misma red
Los equipos que Cora detecta en tu red tienen que estar en la misma red que tu teléfono cuando los añades. **Después de configurarlos, solo se puede llegar a ellos por esa red** (o por Bluetooth, si el equipo lo usa), salvo que un dispositivo Cora en casa pueda hacerlo por ti.

Por eso, un equipo que en casa marca bien puede mostrar valores más antiguos cuando estás fuera, salvo que un Cora Max en casa pueda consultarlo. No es un fallo. Depende de desde dónde se puede llegar al equipo.
:::

## La página de un dispositivo

Abre cualquier dispositivo de la lista. Primero están sus controles, y luego tres secciones que funcionan igual para todas las marcas.

- **Acuarios** muestra a qué acuario (o acuarios) está asignado. Toca **Cambiar** para reasignarlo.
- **Conexión** es donde editas su dirección IP, su inicio de sesión o su clave de dispositivo.
- **Quitar dispositivo**, al final.

Cora Max, Neptune Apex y GHL pueden servir a más de un acuario, así que su selector de acuario es una lista de casillas. Cora Max se puede asignar hasta a cuatro. Consulta [Más de un dispositivo Cora](/help/mobile-multi-device). Todo lo demás, incluido HYDROS, sirve a un solo acuario a la vez: elegir uno distinto mueve el dispositivo ahí y lo quita del anterior.

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
| "Esperando a Cora Max" | Un controlador GHL que acabas de añadir: aparece en cuanto un Cora Max de su red lo haya leído |
| Nada | Nunca ha enviado datos. Revisa el acuario asignado y la conexión |

## Quitar un dispositivo

Abre el dispositivo y toca **Quitar dispositivo**. Cora te pide que confirmes: *"{name} se quitará de Cora. El dispositivo en sí no se restablece ni se modifica."*

**Tus lecturas se conservan.** Al quitar un dispositivo, Cora deja de recoger datos nuevos de él. El historial que ya tenía se queda en el acuario, y los widgets que lo usaban conservan sus lecturas pasadas.

Lo que pierdes es la conexión en directo y, si el dispositivo se conectaba con una cuenta del fabricante, el inicio de sesión guardado. Si lo vuelves a añadir, tendrás que iniciar sesión otra vez.

:::tip Silencia un dispositivo pesado sin quitarlo
Si un dispositivo funciona bien pero te avisa demasiado, cambia sus umbrales o sus notificaciones. Lo explicamos en [Alertas y umbrales](/help/mobile-alerts). Mantienes la conexión y los datos, y se acaban los avisos de más.
:::
