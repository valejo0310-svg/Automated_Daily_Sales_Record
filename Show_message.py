from Calculator import calcular_total, ventas
def mostrar_resumen():

    print("="*60)
    print("TOTAL PURCHASE".center(60))
    print("="*60)

    for venta in ventas:
        print("Producto:", venta["producto"])
        print("Cantidad vendida:", venta["cantidad"])
        print()

    total = calcular_total()
    print("Total recaudado: $", total)