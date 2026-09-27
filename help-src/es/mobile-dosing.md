---
title: Dosificación
description: Dile a Cora qué dosificas para que pueda convertir mililitros en un cambio real en tu acuario.
section: Cora Mobile
reviewed: 2026-09-27
order: 18
group: Records
---

Cora solo puede hacer los cálculos de dosificación si sabe la concentración de tus productos. Configúralo una vez y todo lo que depende de ello (la calculadora, el seguimiento del consumo, y lo que Cora te dice sobre tu dosificación) se convierte en números reales en lugar de suposiciones.

**Ajustes → Productos de dosificación.**

![Productos de dosificación](img/mobile-dosing.webp "Los productos llevan la concentración que usa Cora para los cálculos de dosis y consumo.")

## La biblioteca de productos

Cora viene con una biblioteca de productos comunes. Busca el tuyo y añádelo; la concentración viene incluida.

Cada producto registra cuánto sube un parámetro por mililitro (o por gramo, para productos secos) en un volumen fijo de agua. Ese es el número que convierte "5 ml" en "+0,2 dKH en tu acuario".

Los productos pueden llevar valores de alcalinidad, calcio, magnesio, nitrato o fosfato; un producto de dos partes lleva uno de cada, un producto equilibrado varios.

## Añadir el tuyo

Si tu producto no está en la biblioteca, añádelo como uno personalizado e introduce su concentración. La etiqueta del fabricante casi siempre lo indica: "1 ml por 100 litros sube la alcalinidad 0,1 dKH", o similar.

:::warning Introduce la concentración indicada por el fabricante
Una concentración incorrecta hace que todos los cálculos de dosis de ese producto queden mal en la misma proporción. Si no tienes el dato, deja fuera el producto en lugar de estimarlo.
:::

La **mezcla de sal** de tu acuario es algo distinto de un producto de dosificación: se fija en el perfil del acuario, no aquí, y Cora mantiene un catálogo verificado de sales de arrecife comunes con sus valores publicados para elegir. Consulta **[Perfil del acuario](/help/mobile-tank-profile)**.

## La calculadora de dosis

Con los productos configurados, Cora puede calcular una corrección usando el volumen real de tu acuario a partir de su perfil.

Calcula **subidas**: alcalinidad, calcio, magnesio, y nitrato o fosfato cuando los estás subiendo.

Para **bajadas** da orientación en lugar de una dosis; no se puede dosificar un parámetro hacia abajo, y la respuesta es un cambio de agua, un cambio de medio filtrante o un cambio en lo que ya estás dosificando.

:::warning Las correcciones grandes se reparten, no se dosifican de una vez
Cora limita cuánto se puede mover un parámetro en un día y reparte una corrección mayor en varios días. Una sola dosis grande es como se sobresalta un acuario; la calculadora no va a proponer una.
:::

El volumen que introdujiste al configurar importa aquí. Un volumen indicado con un 20% de error da cifras de dosis con un 20% de error.

## Consumo

Una vez que Cora puede ver tanto tus dosis como tus lecturas, puede calcular qué está consumiendo realmente tu acuario, y avisarte cuando eso cambia.

Un cambio en la demanda es una señal para mirar, no un diagnóstico. Una demanda de alcalinidad en aumento suele reflejar crecimiento; un cambio brusco en cualquier dirección puede venir igual de una dosis que no se está entregando, un error de medición, precipitación, un cambio de agua o un cambio en el equipo. Revisa qué cambió alrededor de esa fecha antes de sacar una conclusión.

## Equipo de dosificación

Si tienes una unidad de dosificación conectada, sus cabezales aparecen como dispositivos con sus propias lecturas: cuánto le queda a cada cabezal, y qué ha estado dosificando. Consulta **[Conectar tu equipo](/help/mobile-connections)**.
