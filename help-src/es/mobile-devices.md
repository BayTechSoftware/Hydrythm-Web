---
title: Añadir, editar y eliminar dispositivos
description: Añade equipos a Cora, asígnalos a un acuario, cámbiales el nombre, comprueba que funcionan bien y quítalos, todo desde la pestaña Dispositivos.
section: Cora Mobile
reviewed: 2026-10-13
order: 11
group: Equipment
twin: max-devices
---

La pestaña **Dispositivos** es donde añades, asignas, renombras, revisas y quitas cada equipo. Los dispositivos se agrupan por marca, y cada grupo se puede plegar.

![La pestaña Dispositivos](img/mobile-devices.webp "Los equipos se agrupan por marca. Cada grupo se puede plegar.")

## Añadir equipos {#adding-equipment}

1. En la pestaña **Dispositivos**, toca **Agregar dispositivo**.
2. Elige la marca: **Cora**, **Neptune Apex**, **Red Sea**, **Jecod** o **AquaWiz**. Los usuarios Beta ven además **Maxspect**, **GHL**, **HYDROS**, **Focustronic**, **EcoTech**, **Inkbird** y **Cámara**, cada una con una etiqueta **Beta**.
3. Sigue los pasos de la marca. Según la marca, es un escaneo de red, una dirección IP, un inicio de sesión o una clave de dispositivo. [Conectar tus equipos](/help/mobile-connections) tiene los pasos de cada marca.
4. Elige el acuario al que pertenece.

![La lista Agregar dispositivo de un usuario Beta](img/mobile-add-device-beta.webp "Las marcas Beta llevan una etiqueta Beta.")

:::note Beta
**Beta.** Las integraciones Beta solo están abiertas a los usuarios Beta. Si no eres usuario Beta, no las verás en **Agregar dispositivo**. Para pedir acceso Beta, contacta con [soporte](/support.html). Más información en [Funciones Beta](/help/mobile-beta).
:::

Una fila que necesita un Cora Max en el acuario (Maxspect, GHL, EcoTech, Inkbird y Cámara) aparece en gris y dice **Requiere Cora Max** hasta que el acuario tiene uno.

:::note Sin un Cora Max, algunos equipos son solo locales
A los equipos Neptune Apex, Red Sea y Jecod se llega por tu red doméstica o por Bluetooth. Sin un Cora Max, la pantalla de añadir dice *Sin Cora Max, esta integración solo funciona localmente en la app Mobile.* Tu teléfono solo los lee y los controla mientras está en la misma red (o al alcance del Bluetooth). Fuera de casa ves las últimas lecturas que guardó tu teléfono y no puedes controlarlos. Un Cora Max en el acuario los lee a todas horas y transmite tus órdenes. Más información en [Conectar tus equipos](/help/mobile-connections#local-only).
:::

Cuando añades un equipo de tu red, tu teléfono tiene que estar en la misma red que el equipo.

## Emparejar un Cora Max {#pairing-a-cora-max}

![La pantalla Añade tu Cora en Cora Mobile, buscando dispositivos](img/mobile-add-device.webp "Agregar dispositivo y luego Cora. Cora Mobile busca en tu Wi-Fi y por Bluetooth, con Introducir dirección IP manualmente debajo.")

**Cora** es como se empareja un Cora Max nuevo. Encuentra las unidades que ya están en tu Wi-Fi, o las que están cerca por Bluetooth. Si no encuentra la tuya, usa **Introducir dirección IP manualmente** en la misma pantalla. Todos los pasos están en [Configurar Cora Max](/help/max-setup).

## La página de un dispositivo {#a-devices-page}

Toca cualquier dispositivo de la lista para abrir su página. Primero están sus controles, y después secciones que funcionan igual para todas las marcas.

- **Estado** muestra el **Modelo**, el **N.º de serie**, el **Firmware** y cuándo supo Cora de él por última vez (**Visto por última vez**).
- **Acuarios** muestra a qué acuario (o acuarios) está asignado. Toca **Cambiar** para reasignarlo.
- **Conexión** es donde editas su dirección IP, su inicio de sesión o su clave de dispositivo.
- **Quitar dispositivo**, al final.

Cora Max, Neptune Apex y GHL pueden servir a más de un acuario, así que su selector de acuario es una lista de casillas. Cora Max se puede asignar hasta a cuatro. Consulta [Más de un dispositivo Cora](/help/mobile-multi-device). Todo lo demás, incluido HYDROS, sirve a un solo acuario a la vez. Elegir uno distinto mueve el dispositivo ahí y lo quita del anterior.

:::warning Asigna el acuario antes de fiarte de las lecturas
Un dispositivo sin acuario sigue informando, pero sus números no tienen dónde ir. Si un dispositivo que acabas de añadir no sale en ningún panel, revisa esto primero.
:::

Lo que hacen los controles de cada marca está en [Controlar tus equipos](/help/mobile-device-control).

## Cambiar el nombre {#renaming}

Abre el dispositivo y toca el lápiz junto a su nombre. Ponle el que usas en el día a día, como "Retorno", "Gyre izquierdo" o "Calentador del sump". El nombre sale en los widgets, en las alertas y en todo lo que le preguntes a Cora.

Los nombres pueden tener hasta 40 caracteres. Deja el nombre vacío para volver al nombre propio del dispositivo. Si dos dispositivos del mismo tipo no tienen nombre, Cora los distingue con un código corto después del nombre. Cora nunca usa un número de serie como nombre.

El nombre nuevo solo se aplica en Cora. No cambia el nombre en la app del propio fabricante.

## Comprobar que un dispositivo funciona bien {#health}

Cada dispositivo es una fila de la pestaña Dispositivos, con su icono, su nombre, su modelo y su acuario. El punto de la fila indica su estado.

| Punto | Qué significa |
|---|---|
| Gris | Cora todavía no lo sabe |
| Verde | Funciona con normalidad |
| Naranja | Un aviso o un fallo |
| Rojo | Sin conexión |

Para ver más, abre el dispositivo. Su sección **Estado** muestra cuándo supo Cora de él por última vez. Lo que quieres ver es una hora reciente y ningún aviso.

| Lo que ves | Qué significa |
|---|---|
| Una hora de actualización reciente | Funciona con normalidad |
| "Actualizado hace 3 h" en algo que solo informa cada pocas horas | Todo bien |
| "No se pudo contactar…" | Un problema de red, o el dispositivo está apagado |
| "…rechazó el inicio de sesión" | Hay que volver a conectar la cuenta del fabricante. Abre el dispositivo e inicia sesión otra vez |
| "Esperando a Cora Max" | Un controlador GHL o un monitor Inkbird que acabas de añadir: aparece en cuanto un Cora Max lo haya leído |
| Lecturas más antiguas cuando estás fuera | Normal en Apex, Red Sea y Jecod sin un Cora Max en el acuario (mira más arriba) |
| Nada | Nunca ha informado. Revisa el acuario asignado y la conexión |

Cuando un dispositivo deja de informar, Cora puede avisarte. Los tiempos están en [Alertas y umbrales](/help/mobile-alerts). Para cualquier otra cosa, consulta [Solución de problemas](/help/troubleshooting).

## Quitar un dispositivo {#removing-a-device}

Abre el dispositivo y toca **Quitar dispositivo**, o desliza su fila hacia la izquierda en la pestaña Dispositivos. Cora te pide que confirmes: *"{name} se quitará de Cora. El dispositivo en sí no se restablece ni se modifica."*

**Tus lecturas se conservan.** Al quitar un dispositivo, Cora deja de recoger datos nuevos de él. El historial que ya había reunido se queda en el acuario, y los widgets que lo usaban conservan sus lecturas pasadas.

Pierdes la conexión en directo. Si el dispositivo se conectaba con una cuenta del fabricante, también pierdes el inicio de sesión guardado, así que tendrás que iniciar sesión otra vez si lo vuelves a añadir.

:::tip Silencia un dispositivo ruidoso sin quitarlo
Si un dispositivo funciona bien pero avisa demasiado, cambia sus umbrales o sus ajustes de notificación en [Alertas y umbrales](/help/mobile-alerts). Mantienes la conexión y los datos, y se acaba el ruido.
:::
