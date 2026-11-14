# Nivel 2: costo por porción de la carta

`costos.py` calcula el costo de ingredientes por porción de los 50 platos al 31/10/2026 y escribe `nivel-2/costos.csv`.

## Entradas

Todas en `nivel-2/`, tal como se recibieron:

- `facturas/*.pdf`: 40 facturas. Se leen con `pdftotext -layout`. El orden de columnas cambia entre facturas, así que cada renglón se interpreta según el encabezado de su factura. Se verifica que el neto coincida con cantidad por precio menos bonificación.
- `notas/*.pdf`: notas de crédito. Cada una ajusta la factura y el renglón que indica. Solo se aplican las emitidas hasta el 31/10. Una bonificación resta importe; una devolución resta importe y cantidad.
- `catalogo.csv`: gramos, mililitros o unidades de cada presentación de cada producto.
- `rendimientos.csv`: cocientes limpio/bruto y cocido/limpio.
- `recetas.json`: 50 platos (por porción) y 15 subrecetas (por tanda).

## Cálculo

1. Para cada renglón, cantidad equivalente = cantidad por presentación del catálogo. Se le aplican las notas.
2. Precio por g, ml o unidad de cada producto = neto ajustado / cantidad ajustada, de la última factura con fecha hasta el 31/10. A igual fecha prevalece el identificador mayor.
3. Cada ingrediente se lleva a peso bruto: limpio se divide por limpio/bruto; cocido, además por cocido/limpio.
4. Una subreceta aporta su costo de tanda por la proporción usada de su rendimiento final. Puede contener otras subrecetas.
5. El agua no tiene costo. No hay redondeos intermedios; el resultado se redondea a dos decimales, mitad hacia arriba.

## Cómo reproducirlo

Con Python 3 y poppler-utils (`pdftotext`), sin otras dependencias:

```
cd nivel-2/codigo
python3 costos.py > ../costos.csv
```
