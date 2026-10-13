---
title: Configurar Cora Max
description: Empareja un Cora Max nuevo con Cora Mobile por Bluetooth, conéctalo al Wi-Fi, elige sus acuarios y cámbialo de acuario más adelante.
section: Cora Max
reviewed: 2026-10-13
order: 1
group: Getting started
twin: mobile-setup
---

Esta página te lleva de un Cora Max nuevo a una pantalla de pared funcionando. Lo emparejas desde tu teléfono por Bluetooth, y no escribes nada en la propia pantalla.

:::tip Configura antes tus acuarios en el teléfono
Cora Max muestra los acuarios y dispositivos de tu cuenta, y no puede crear un acuario por sí mismo. [Configúralos primero en Cora Mobile](/help/mobile-setup). Cora Max los recoge en cuanto lo emparejas.
:::

## Qué necesitas {#what-you-need}

- Cora Max, enchufado y encendido. Está pensado para quedarse enchufado.
- Cora Mobile en tu teléfono, con la sesión iniciada y **al menos un acuario** ya creado.
- El Bluetooth de tu teléfono activado, y el teléfono cerca de Cora Max.
- El nombre y la contraseña de tu red Wi-Fi.

Pon Cora Max donde puedas verlo desde el otro lado de la habitación y hablarle, lejos de salpicaduras y de los restos de sal.

## Qué muestra primero la pantalla {#what-the-screen-shows-first}

Enciende Cora Max. Muestra una pantalla de emparejamiento que dice **Abre la app de Cora en tu teléfono**, y después **Toca Añadir dispositivo.** y **Elige este Cora Max en la lista de dispositivos.** Debajo muestra **Detectable como** y su nombre, que termina en un código corto. Si estás emparejando más de uno, ese código los distingue en tu teléfono.

![La pantalla de emparejamiento de Cora Max, esperando a tu teléfono](img/max-pairing-screen.webp "Esperando a tu teléfono. La línea de abajo muestra el nombre que verás en tu teléfono.")

La misma pantalla tiene un breve aviso sobre las integraciones con equipos de otros fabricantes. Las condiciones que aceptaste en Cora Mobile también cubren Cora Max.

## Emparejar desde tu teléfono {#pairing}

Todo lo demás se hace en Cora Mobile. Una hoja te guía por cinco pasos, que se muestran arriba: **Conectar · Wi-Fi · Autenticación · Acuarios · Listo**.

1. **Encontrarlo.** Abre la pestaña **Dispositivos**, toca **Agregar dispositivo** y después **Cora**. La pantalla **Añade tu Cora** lista los dispositivos Cora de tu red y los dispositivos de configuración cercanos encontrados por Bluetooth. Toca **Buscar** si el tuyo todavía no aparece, y después toca tu Cora Max.

   ![La pantalla Añade tu Cora en Cora Mobile, buscando dispositivos](img/mobile-add-device.webp "Agregar dispositivo y luego Cora. Cora Mobile busca en tu Wi-Fi y por Bluetooth, con Introducir dirección IP manualmente debajo.")

2. **Conectar.** Tu teléfono se conecta a Cora Max por Bluetooth y muestra su dirección MAC, su firmware, su variante y su revisión de hardware. Comprueba que es el correcto y toca **Continuar**.

3. **Wi-Fi.** Elige tu red de la lista, o toca **Volver a buscar**, y escribe la contraseña en tu teléfono. A partir de aquí tu teléfono habla con Cora Max por Wi-Fi, así que mantén el teléfono en la misma red.

4. **Autenticación.** Tu teléfono vincula Cora Max a tu cuenta. Esto se hace solo, y Cora Max muestra su propio progreso, como **Verificando tu cuenta…** y **Configurando tu acuario…**.

   ![La pantalla de emparejamiento de Cora Max mostrando Verificando tu cuenta](img/max-pairing-verifying.webp "Cora Max muestra cada paso mientras tu teléfono lo vincula a tu cuenta.")

5. **Acuarios.** En **Asignar acuarios**, elige los acuarios que gestionará este Cora Max, **hasta cuatro**.

6. **Listo.** Tu teléfono dice que Cora Max está configurado y muestra un **PIN de recuperación**. Toca el botón que abre el panel de tu acuario, o **Ir a Dispositivos**. Cora Max muestra **Emparejado** y después **Abriendo panel…**.

:::warning Apunta el PIN de recuperación
El **PIN de recuperación** tiene seis dígitos y es la única forma de entrar en la recuperación de ese Cora Max. Para usarlo, mantén cinco dedos en la esquina superior derecha de la pantalla durante diez segundos y después escribe el PIN. La recuperación te permite volver a configurar el Wi-Fi, emparejar de nuevo, buscar una actualización o restablecer de fábrica. Puedes volver a encontrar el PIN en tu teléfono, en **Dispositivos → tu Cora Max → PIN de recuperación**, pero nunca en el propio Cora Max.
:::

### Si el emparejamiento se queda atascado {#if-pairing-gets-stuck}

- **El Bluetooth está desactivado. Actívalo y vuelve a tocar Buscar.** Activa el Bluetooth y vuelve a buscar.
- **El permiso de Bluetooth está desactivado para Cora.** Permite el Bluetooth para Cora en los ajustes de tu teléfono y toca **Buscar**. Un iPhone también puede pedir acceso a la red local. Permítelo también.
- **No se encontraron dispositivos de configuración Cora cercanos por Bluetooth.** Ponte al lado de Cora Max, comprueba que sigue mostrando la pantalla de emparejamiento y vuelve a buscar.
- **No se encontraron acuarios** en el paso Acuarios. Tu cuenta todavía no tiene ningún acuario. Crea uno en Cora Mobile y vuelve a intentar el paso.
- **Aún no vinculado a tu acuario** al final. Cora Max está emparejado, pero la vinculación con el acuario no terminó. Toca **Reintentar ahora**. Hasta que termine, las alertas de esta pantalla usan rangos predeterminados.

Más soluciones en [Solución de problemas](/help/troubleshooting#pairing-a-cora-max-fails).

## Después de emparejar {#after-pairing}

Cora Max ya ve los mismos acuarios, dispositivos, lecturas y registros que tu teléfono.

- Si uno de tus acuarios tuvo antes un Cora Max, Cora Max pregunta **¿Restaurar el diseño anterior para este acuario?** **Restaurar** recupera los ajustes de pantalla, sonido y alertas que guardó el anterior. **Empezar de nuevo** se los salta.
- Un acuario sin lecturas todavía muestra **Aún no hay lecturas** y un botón **Registra tu primera prueba**.
- Cora Max crea un panel inicial a partir del perfil de tu acuario. No copia el de tu teléfono.

Puedes emparejar más de un Cora Max con la misma cuenta, por ejemplo uno en el cuarto de los acuarios y otro en el salón. Cada uno puede mostrar acuarios distintos y tiene su propio diseño. Si dos muestran el mismo acuario, [Más de un dispositivo Cora](/help/mobile-multi-device) explica cuál lee los equipos.

## Crear el panel {#building-the-dashboard}

El panel de pantalla grande es una cuadrícula fija, y todo tiene que caber en una pantalla. La forma más rápida de organizarlo es desde tu teléfono: abre la pestaña **Dispositivos**, toca tu Cora Max y después toca **Diseño del panel** en la tarjeta del acuario. También puedes hacerlo en la pantalla de pared desde el menú del acuario.

Para reutilizar un diseño de otro Cora Max o de otro acuario, cárgalo desde **Mis paneles** en el editor. Más información en [Editar el panel de Cora Max](/help/max-dashboard-editing).

## Pasar Cora Max a otro acuario {#changing-which-tanks-it-shows}

Los acuarios que muestra un Cora Max se cambian en tu teléfono. Los ajustes propios de Cora Max no pueden hacerlo.

1. En Cora Mobile, abre la pestaña **Dispositivos** y toca tu Cora Max.
2. En **Acuarios**, toca **Agregar acuario** y elige el acuario. Un Cora Max admite hasta cuatro. Cuando ya tiene cuatro, el botón desaparece, así que quita uno antes.
3. Para quitar un acuario de esta pantalla, toca el icono rojo de quitar (**Quitar acuario**) en la tarjeta de ese acuario, y después toca **Quitar**.

Para pasar Cora Max de un acuario a otro, añade el acuario nuevo y después quita el antiguo. El acuario nuevo recibe un panel inicial creado a partir de su perfil. Organízalo con **Diseño del panel**.

Si este Cora Max era el Cora Max principal fijado para el acuario que quitaste, esa fijación se borra y el acuario vuelve a **Cualquiera activo (automático)**. Más información en [Dispositivos y estado de los dispositivos](/help/max-devices).

## Actualizaciones {#updates}

Cora Max se actualiza solo. Una versión nueva se descarga en segundo plano y se instala por la noche. Tu versión aparece arriba en **Ajustes → Ajustes de Cora Max**. Más información en [Actualizaciones y recuperación](/help/max-updates).

## Cambiarlo a otra red Wi-Fi {#moving-it-to-a-different-network}

Ve a **Ajustes → Ajustes de Cora Max → Wi-Fi**, elige la red nueva y escribe la contraseña. Cora Max sigue emparejado, así que no tienes que volver a configurarlo.
