#Valor neto de un producto

producto=input("ingrese el nombre del producto:")
valorProducto=int(input("ingrese el valor del producto:"))
valorNeto=float(0.81)
valorSinIva=float(valorProducto*valorNeto)

print("-----DETALLE PRODUCTO-----")
print(f"nombre del producto: {producto}")
print(f"valor del producto: {valorProducto}")
print(f"valor del producto sin IVA: {valorSinIva}")
