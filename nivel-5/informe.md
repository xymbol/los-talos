Plato revisado: P12
Sustitución propuesta: rechazada

# Informe para Mora: Pollo del aljibe (P12) y la propuesta de soja en P01

## Recomendación

Sostenemos el retiro de P12 aprobado en la revisión de carta [nivel-4/decisiones.json#L69], pero como prueba con fecha de revisión y después de conversarlo con Bruno y la cocina, no como un cambio irreversible. Rechazamos el cambio de pollo por bocados de soja en P01: agrega un alérgeno que la carta no declararía y oculta el cambio a los clientes.

## Qué es registro, qué es cálculo y qué es proyección

- **Registros:** compras (facturas, tickets y notas de crédito), recetas, rendimientos, la exportación de caja, el aviso del frigorífico y la oferta del almacén.
- **Cálculos:** costo por porción, unidades netas, ingreso, contribución y margen. Salen de aplicar las recetas a los registros; se pueden rehacer con los pasos de abajo.
- **Proyecciones:** cualquier efecto futuro de sacar o subir platos. No tenemos datos de demanda ni de aceptación de precios, así que no proyectamos ventas.

## Los números de P12

**Ventas (registro y cálculo).** En la exportación de caja del trimestre (el nivel 3 pide no subirla al repositorio), P12 se vende con el artículo A1577 y no forma parte de ningún combo. Entre agosto y octubre hay 441 unidades vendidas y 98 revertidas por reversiones REV, que según el manual anulan la venta original. Netas: 441 - 98 = **343 porciones** [nivel-3/margenes.csv#L13]. No pudimos reproducir las 986 que menciona Bruno con los movimientos de caja de A1577; conviene revisar juntos de qué reporte salen.

**Costo (cálculo).** La receta de P12 usa 150 g de pollo cocido, 40 g de cebolla limpia, 8 ml de aceite, 230 g de la preparación S09 y 15 g de S15 [nivel-2/recetas.json#L439]. El pollo se compra crudo: 150 g cocidos equivalen a 150 / (0,78 × 0,74) = 259,9 g comprados [nivel-2/rendimientos.csv#L10].

- Al cierre (31/10, última compra de cada producto): **$ 3101,67** por porción [nivel-3/costos.csv#L13].
- Con la lista nueva del frigorífico (+18 % sobre su precio efectivo de última compra [nivel-4/aviso-proveedor.md#L3]): **$ 3566,19** por porción [nivel-5/datos/reposicion.csv#L13]. Se compone de $ 2885,70 de ingredientes directos, $ 615,72 de S09 y $ 64,77 de S15.

Inferimos (el mensaje no muestra el cálculo) que los $ 1605 de Bruno corresponden a 150 g de pollo valorados como si fueran peso de compra (150 × ≈ $ 10,70 por gramo con la lista nueva). Faltan la pérdida de limpieza y cocción del pollo, la cebolla, el aceite y las dos preparaciones. Si es así, no es un error de criterio de cocina: sería la diferencia entre peso servido y peso comprado.

**Margen y aporte (cálculo).** A $ 8000 de carta y $ 3566,19 de costo de reposición, el margen es 55,4 %, debajo del mínimo de 60 % que fijamos para toda la carta [nivel-4/criterio.md#L13]. En el trimestre P12 aportó $ 1.682.313 (ingreso neto $ 2.477.280 menos costo histórico $ 794.967) [nivel-3/margenes.csv#L13], de los aportes más bajos de la carta.

## Cómo evaluamos los argumentos de Bruno

- **"Cuesta $ 1605":** no se sostiene con las recetas y rendimientos registrados; el costo de reposición es $ 3566,19.
- **"Salieron 986 porciones netas":** los registros muestran 343 netas. Puede haber una diferencia de criterio (reversiones, otro período o una planilla de cocina); hay que revisarla con él.
- **"El aumento no afecta todo":** es correcto. Solo sube el 18 % lo del frigorífico; el resto mantiene el precio de cierre. Igual pesa en P12 porque el pollo es su ingrediente principal.
- **Preparaciones compartidas:** S09 y S15 siguen en uso en otros platos que continúan, así que retirar P12 no deja tandas sin destino. Lo que esté preparado puede usarse en esos platos, según las cantidades y la demanda del servicio.
- **Clientes habituales y trabajo de cocina:** no están en los datos y no los descartamos. Por eso proponemos una prueba con fecha de revisión y no un retiro definitivo.

Alternativa que también cumple la regla: mantener P12 con precio $ 9000 (margen 60,4 % con costo $ 3566,19). No la recomendamos sin conversarla, porque la regla de la revisión retira los diez platos no protegidos de menor aporte [nivel-4/criterio.md#L10] y P12 está entre ellos; si se reincorpora, otro plato tendría que salir para mantener cuarenta.

## La propuesta de soja en P01

**Cálculo.** Con la lista nueva, los 160 g de pollo cocido de P01 cuestan $ 2964,78 (pollo comprado 277,2 g). Los bocados de soja cuestan $ 2,40 por gramo y vienen cocidos, sin merma [nivel-5/oferta-almacen.md]: 160 g = $ 384. El costo de P01 bajaría de $ 3697,17 [nivel-5/datos/reposicion.csv#L2] a $ 1116,39.

**Por qué la rechazamos.**

- La soja es un alérgeno declarado por el proveedor [nivel-5/oferta-almacen.md#L9] y no figura en los alérgenos de P01 [nivel-4/carta.json]. Servirla sin avisar expone a clientes alérgicos.
- Cambiar el ingrediente principal y mantener nombre y descripción engaña al cliente. P01 es un plato de la casa; según Bruno, los clientes vuelven a buscar lo que ya conocen [nivel-5/mensaje-chef.md#L9].
- P01 ya cumple el mínimo con el precio fijado en la revisión [nivel-4/decisiones.json#L6], así que no hace falta recuperar margen por este camino.
- El precio de la oferta está garantizado solo para el próximo servicio [nivel-5/oferta-almacen.md#L12].

Si interesa, puede evaluarse más adelante un plato nuevo con soja, con nombre propio, alérgenos declarados y aviso en salón. Eso es una propuesta futura, no parte de esta decisión.

## Próximos pasos

1. Reunión con Bruno y la cocina antes del próximo servicio para revisar estos números y el reporte de las 986 porciones.
2. Si se confirma el retiro, avisar en salón con un texto acordado con Bruno; lo ya preparado de S09 y S15 puede usarse en los platos que siguen.
3. Revisar P12 a los 30 días con las ventas de los platos que continúan y lo que observe la cocina durante el servicio.
4. No usar los bocados de soja en P01.
