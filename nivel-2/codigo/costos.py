"""Costo de ingredientes por porción de la carta al 31/10/2026.

Uso: python3 costos.py [carpeta_nivel] > ../costos.csv
Requiere pdftotext (poppler-utils) para leer facturas y notas.
"""
import csv, json, os, re, subprocess, sys
from decimal import Decimal as D, ROUND_HALF_UP

CORTE = '2026-10-31'
base = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')


def num(s):
    return D(s.replace('.', '').replace(',', '.'))


def texto(pdf):
    return subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True, check=True).stdout


def campo(t, nombre):
    return re.search(nombre + r':\s*(.+?)(?:\s{2,}|$)', t, re.M)[1].strip()


catalogo = {(r['producto'], r['presentacion']): D(r['cantidad_base'])
            for r in csv.DictReader(open(f'{base}/catalogo.csv', encoding='utf-8'))}
rendimientos = {r['producto']: (D(r['limpio_sobre_bruto']), D(r['cocido_sobre_limpio']))
                for r in csv.DictReader(open(f'{base}/rendimientos.csv', encoding='utf-8'))}

# Renglones de factura: (factura, renglón) -> producto, fecha, cantidad base, neto.
# El orden de columnas cambia entre facturas, así que se lee del encabezado.
renglones = {}
for nombre in sorted(os.listdir(f'{base}/facturas')):
    t = texto(f'{base}/facturas/{nombre}')
    factura = re.search(r'Factura (F-\d+)', t)[1]
    fecha = campo(t, 'Fecha')
    columnas = None
    for linea in t.splitlines():
        partes = re.split(r'\s{2,}', linea.strip())
        if partes[0] == 'R' and len(partes) == 7:
            columnas = partes[2:]
        elif columnas and partes[0].isdigit() and len(partes) == 7:
            v = dict(zip(columnas, partes[2:]))
            producto = partes[1].split()[0]
            cantidad, precio, bonif, neto = (num(v[k]) for k in ('Cant.', 'P. unitario', 'Bonif.%', 'Neto'))
            esperado = cantidad * precio * (1 - bonif / 100)
            if abs(esperado - neto) > D('0.01'):
                print(f'aviso: {factura} r{partes[0]} neto {neto} != {esperado:.2f}', file=sys.stderr)
            renglones[(factura, partes[0])] = {
                'producto': producto, 'fecha': fecha, 'factura': factura,
                'cantidad': cantidad * catalogo[(producto, v['Unidad'])], 'neto': neto}

# Notas de crédito emitidas hasta el corte: restan importe y, si es devolución, cantidad.
for nombre in sorted(os.listdir(f'{base}/notas')):
    t = texto(f'{base}/notas/{nombre}')
    if campo(t, 'Fecha') > CORTE:
        continue
    r = renglones[(campo(t, 'Factura asociada'), campo(t, 'Renglón'))]
    assert r['producto'] == campo(t, 'Producto').split()[0], nombre
    cant, unidad = campo(t, 'Cantidad devuelta').split()
    r['cantidad'] -= num(cant) * catalogo[(r['producto'], unidad)]
    r['neto'] -= num(campo(t, 'Importe acreditado').replace('$', '').strip())

# Precio por g, ml o unidad: última factura hasta el corte; a igual fecha, la de mayor identificador.
precio = {}
for r in renglones.values():
    if r['fecha'] <= CORTE:
        clave = (r['fecha'], r['factura'])
        if r['producto'] not in precio or clave > precio[r['producto']][0]:
            precio[r['producto']] = (clave, r['neto'] / r['cantidad'])

recetas = {r['codigo']: r for r in json.load(open(f'{base}/recetas.json', encoding='utf-8'))}


def costo(codigo):
    """Costo de la tanda o porción completa, sin redondeos."""
    total = D(0)
    for i in recetas[codigo]['ingredientes']:
        q, p = D(str(i['cantidad'])), i['producto']
        if p in recetas:  # preparación: proporción de su tanda terminada
            total += q * costo(p) / D(str(recetas[p]['rendimiento']))
            continue
        limpio_bruto, cocido_limpio = rendimientos[p]
        bruto = {'bruto': q, 'limpio': q / limpio_bruto, 'cocido': q / limpio_bruto / cocido_limpio}[i['estado']]
        total += bruto * precio[p][1]
    return total


salida = csv.writer(sys.stdout, lineterminator='\n')
salida.writerow(['plato', 'costo_por_porcion'])
for codigo, r in recetas.items():
    if r['unidad_rendimiento'] == 'porción':
        valor = costo(codigo) / D(str(r['rendimiento']))
        salida.writerow([codigo, valor.quantize(D('0.01'), ROUND_HALF_UP)])
