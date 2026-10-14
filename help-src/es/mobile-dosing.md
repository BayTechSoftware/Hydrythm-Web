---
title: Productos de dosificación y la calculadora de dosis
description: Comprueba la concentración de tus productos de alcalinidad, calcio y magnesio, añade los tuyos y usa la calculadora de dosis para saber cuánto añadir.
section: Cora Mobile
reviewed: 2026-10-13
order: 27
group: Records
---

Cora solo puede hacer cálculos de dosificación si sabe la concentración de tus productos. Esta página explica la lista de productos y la calculadora de dosis que la usa.

Ve a **Ajustes → Productos de dosificación**.

![Productos de dosificación](img/mobile-dosing.webp "Cada producto lleva la concentración que usa Cora para calcular dosis y consumo.")

## La biblioteca de productos {#the-product-library}

La pantalla **Productos de dosificación** ya incluye productos habituales, agrupados en **Alcalinidad (dKH)**, **Calcio (ppm)** y **Magnesio (ppm)**. Busca el tuyo y tócalo para comprobar su concentración.

Cada concentración indica cuánto sube el parámetro 1 ml (o 1 g, en un producto seco) en un volumen fijo de agua. Con ese número, "5 ml" se convierte en "+0,2 dKH en tu acuario". Cambia entre **por 100 L** y **por 100 gal** arriba.

Cambia la concentración de un producto incluido solo si tu botella dice otra cosa. Toca el producto para abrir **Ajustar concentración**. **Restablecer al valor predeterminado** vuelve a poner el valor de Cora.

## Añadir tu propio producto {#adding-your-own}

Si tu producto no está en la lista, toca **+** (**Agregar producto personalizado**). Ponle un **Nombre del producto**, elige **Líquido (ml)** o **Seco (g)** y rellena su concentración de alcalinidad, calcio o magnesio. Deja un campo en blanco si el producto no mueve ese parámetro. Un producto de dos partes rellena uno en cada parte, y un producto equilibrado varios.

La concentración casi siempre viene en la etiqueta, con algo como "1 ml por 100 litros sube la alcalinidad 0,1 dKH".

:::warning Usa la concentración que indica el fabricante
Si la concentración está mal, todas las dosis que Cora calcule para ese producto salen mal en la misma proporción. Si no encuentras el dato, no añadas el producto. No lo calcules a ojo.
:::

Los productos de nitrato y fosfato salen de la lista propia de Cora en la calculadora. No se pueden añadir aquí.

La **sal** de tu acuario no es un producto de dosificación. Se indica en el perfil del acuario, y Cora tiene un catálogo de sales de arrecife habituales con sus valores publicados, con fuentes, para que elijas. Consulta [El perfil de tu acuario](/help/mobile-tank-profile).

## La calculadora de dosis {#the-dose-calculator}

La calculadora calcula cuánto producto hace falta para llevar un parámetro hasta su objetivo. Está disponible para alcalinidad, calcio, magnesio, nitrato y fosfato.

1. En el panel, toca el widget del parámetro para abrirlo.
2. Toca el icono de la calculadora arriba. Si tiene un punto, la lectura está por debajo del objetivo.
3. Revisa los números que ha rellenado Cora:
   - El valor actual es tu última lectura. Cámbialo si acabas de medir.
   - El objetivo es el centro de tu rango de alerta para ese parámetro, o el rango típico de arrecife si no has puesto uno.
   - **Volumen neto de agua (L)** es el 90% del volumen de tu acuario, para descontar la roca y la arena. Cámbialo si sabes la cifra real.
4. Elige el **Producto**. Primero salen tus propios productos del perfil del acuario y después los de las marcas. También puedes poner una **Concentración personalizada**.

Cora muestra el total necesario para llegar al objetivo.

:::warning Reparte una corrección grande
La calculadora da el total, no una dosis diaria. Si el total supone un salto mayor de lo que es seguro en un día, te lo dice, y lo repartes en varios días. **Preguntarle a Cora** abre Cora Assistant con tus números, si quieres ayuda para planificar cuánto dar al día.
:::

Cuando hayas dosificado, toca **Registrar la dosis que aplicaste**. Añade una entrada a tu [diario](/help/mobile-journal).

Si ya estás en el objetivo o por encima, la calculadora te dice que no hay nada que añadir. Ningún parámetro baja dosificando. La solución es un cambio de agua, cambiar el material filtrante o cambiar lo que ya dosificas.

Aquí importa el volumen. Si se desvía un 20%, las dosis también se desvían un 20%.

## Consumo {#consumption}

Cuando Cora ve tus dosis y tus lecturas, puede calcular cuánto consume tu acuario y avisarte cuando eso cambia.

Si cambia el consumo, míralo con calma antes de sacar conclusiones. Un mayor consumo de alcalinidad suele significar crecimiento, pero una variación brusca, en cualquier dirección, también puede deberse a una dosis omitida, un error al medir, precipitación, un cambio de agua o un cambio en el equipo. Comprueba qué más cambió por esas fechas.

## Equipos de dosificación {#dosing-equipment}

Si tienes una dosificadora conectada, como una Neptune DŌS o una Red Sea ReefDose, sus cabezales aparecen con sus propias lecturas, incluido lo que le queda a cada cabezal y lo que ha dosificado. Cómo manejarlos y rellenarlos se explica en [Controlar tus equipos](/help/mobile-device-control), y sus alertas de envase bajo y de dosis omitida en [Alertas de dosificadores](/help/mobile-device-control#doser-alerts).

Una automatización también puede dosificar con un cabezal DŌS, con un máximo de 10 mL por cabezal al día. Consulta [Automatizaciones y escenas](/help/mobile-automation#actions).
