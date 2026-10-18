---
title: Mantenimiento
description: Añade tareas periódicas como limpiar el skimmer o cambiar las mangas filtrantes, recibe un recordatorio cuando toquen y márcalas como hechas o posponlas.
section: Cora Mobile
reviewed: 2026-10-17
order: 28
group: Records
twin: max-records
---

Mantenimiento guarda las tareas que tu acuario necesita con regularidad, con un recordatorio para cada una.

Toca **Mantenimiento** en la fila de botones que hay debajo del panel. También está en Ajustes → tu acuario → **Mantenimiento**.

![La lista de mantenimiento](img/mobile-maintenance.webp "El cumplimiento, las tareas atrasadas y, en cada tarea, cuándo se hizo por última vez y cuándo toca la próxima.")

## El resumen {#summary}

Arriba verás el **Cumplimiento de mantenimiento**, la parte de las tareas que ahora mismo están al día, y cuántas tareas están atrasadas.

Cada tarea de la lista tiene un color según esté atrasada, próxima o programada. También muestra cuándo la hiciste por última vez y cuándo toca la próxima.

## Añadir una tarea {#adding-a-task}

Toca **Agregar tarea** y elige:

- **Desde plantilla** para una tarea habitual con su intervalo ya puesto. Elígela, indica cuándo toca la próxima vez y a qué hora quieres el recordatorio, y toca **Confirmar**.
- **Tarea personalizada** para una tuya. Ponle un **Nombre de la tarea**, un **Intervalo (días)**, una **Categoría** y una **Próxima fecha de vencimiento**. Activa **Recordatorio** y elige **Recordarme a las** si quieres una notificación.

Algunas de las plantillas, con el intervalo con el que empiezan:

| Tarea | Intervalo |
|---|---|
| Cambiar mangas filtrantes | 3 días |
| Limpiar el vaso del skimmer | 7 días |
| Cambio de agua | 7 días |
| Probar parámetros del agua | 7 días |
| Reemplazar carbón | 30 días |
| Calibrar sonda de pH | 30 días |
| Limpiar bombas de circulación | 90 días |
| Subir resultados de ICP | 90 días |

Puedes cambiar el intervalo de cualquier tarea más adelante.

### Tareas que Cora añade para los equipos Red Sea {#red-sea-tasks}

Cuando conectas un ReefDose, un ReefATO+, un ReefMat o un ReefRun de Red Sea, Cora añade el mantenimiento que ese equipo necesita, ya con el intervalo correcto:

| Dispositivo | Tarea | Intervalo |
|---|---|---|
| ReefATO+ | Replace ReefATO+ EC sensor | 42 días |
| ReefATO+ | Replace ReefATO+ return pump | 135 días |
| ReefMat | Replace ReefMat carbon | 25 días |
| ReefRun | Check ReefRun skimmer venturi | 35 días |
| ReefRun | Replace ReefRun skimmer rotor | 135 días |
| ReefRun | Calibrate ReefRun full-cup sensor | 28 días |
| ReefRun | Calibrate ReefRun overskimming sensor | 28 días |
| ReefRun, por bomba | Service ReefRun pump motor | 135 días |
| ReefRun, por bomba | Clean ReefRun pump strainer | 42 días |
| ReefDose, por cabezal | Calibrate ReefDose head | 90 días |
| ReefDose, por cabezal | Replace ReefDose head tubing | 450 días |

Funcionan igual que cualquier tarea que añadas tú. Puedes cambiarles el nombre, cambiar el intervalo, posponerlas o eliminarlas. Si eliminas una, Cora no la vuelve a añadir para ese dispositivo.

### Probar el agua {#test-water}

Si tocas **Recordarme probar cada semana** en la tarjeta de la primera prueba, Cora añade una tarea semanal llamada **Probar el agua**, que vence el **Día de la prueba** que elijas. Funciona como cualquier otra tarea. Consulta [Configurar Cora Mobile](/help/mobile-setup). También puedes añadir un recordatorio de pruebas en cualquier momento con la plantilla **Probar parámetros del agua**.

### Desde una automatización {#from-an-automation}

Una [automatización](/help/mobile-automation) con la acción **Crear una tarea de mantenimiento** puede poner una tarea en esta lista cuando se activa su regla, o hacer que una tarea existente venza ahora. Una tarea nueva es una **Tarea única**, vence ahora y muestra *Creada por una automatización* con el motivo. Sale de la lista cuando la completas. Mientras siga abierta, la misma automatización no añade otra. Recibes una sola notificación.

## Recordatorios {#reminders}

Abre una tarea, activa **Recordatorio** y elige **Recordarme a las**. Recibes una notificación el día antes de que venza y otra ese mismo día. Mientras está atrasada, recibes un recordatorio cada pocos días. Si varias tareas de un acuario vencen a la vez, llegan en una sola notificación.

Los recordatorios están en **Recordatorios de mantenimiento**, en [Ajustes → Notificaciones](/help/mobile-notifications). Si prefieres ver una tarea solo en la lista, desactiva su **Recordatorio**.

## Marcar una tarea como hecha {#marking-done}

Desliza la tarea hacia la derecha, o ábrela y toca **Completar**. Si la deslizaste por error, toca **Deshacer** en el mensaje que aparece.

Cora guarda la hora en que la terminaste y cuenta la próxima fecha a partir de ahí. Así que si haces una tarea con tres días de retraso, la siguiente también se mueve tres días. Si la tarea está atrasada, Cora te pregunta primero **¿Cuándo lo hiciste?** Elige **Ahora mismo**, o **Elegir fecha y hora** si lo hiciste antes (mira más abajo).

La hoja de la tarea muestra su **Historial de finalizaciones**, incluido el retraso de cada una.

:::note Completar una tarea también escribe una entrada en el diario
Cora añade por ti una entrada breve a tu [diario](/help/mobile-journal), indicando si fue con retraso. Añade tu propia entrada cuando haya algo más que contar, por ejemplo si la bomba estaba llena de arena o las mangas estaban negras después de un solo día.
:::

## Marcar una tarea como hecha antes {#done-earlier}

¿Hiciste el trabajo ayer y olvidaste marcarlo? Abre la tarea, toca **Hecho antes…** y elige la fecha y la hora. Cora fecha la finalización, la entrada del diario y la próxima fecha a partir de esa hora, así que la próxima fecha es la hora que elegiste más el intervalo.

Puedes retroceder hasta un año, pero no antes de la última vez que completaste la tarea. Si eliges una hora que todavía no ha llegado, o anterior a la última finalización, Cora te lo dice y no guarda nada.

## Editar una tarea {#editing}

Toca una tarea para abrirla. Puedes cambiar el **Nombre de la tarea**, el **Intervalo (días)**, las **Notas (opcional)**, la **Próxima fecha de vencimiento** y el recordatorio, y después tocar **Guardar**. **Eliminar** la borra.

## Posponer {#snoozing}

¿No puedes hacer una tarea ahora? Ábrela, toca **Posponer** y elige **1 día**, **3 días**, **1 semana**, **2 semanas** o **1 mes**. Sigue en la lista como **Pospuesta** con su nueva fecha, y no recibes recordatorios hasta entonces.

:::warning Marca una tarea como hecha solo cuando la hayas hecho
La próxima fecha se cuenta a partir de la hora en que hiciste la tarea. Si marcas como hecha una tarea pendiente, se mueven todas las fechas siguientes. Si la hiciste antes, usa **Hecho antes…** y elige la hora real. Si no la hiciste, mejor posponla.
:::

No hay forma de pausar una tarea. Para una tarea que no toca en esta temporada, posponla **1 mes**, o elimínala y vuelve a añadirla más adelante.
