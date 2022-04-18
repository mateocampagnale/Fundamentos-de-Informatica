CANTIDAD_VENTAS = 4
COMISION        = 0.10
totalComision   = 0.0

sueldoBase = float(input('Ingrese sueldo base $'))
for venta in range(CANTIDAD_VENTAS):
    print('Ingrese monto de la venta No. {0} '.format(venta+1),end='$')
    venta = float(input())
    totalComision += (COMISION)*venta
    print('Las ganancias de comision son ${0}, y el total es ${1}'.format(totalComision,(totalComision+sueldoBase)))



