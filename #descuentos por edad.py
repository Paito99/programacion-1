#descuentos por edad

edad= int(input("ingrese su edad"))

 if edad >0 and edad >15:
     print(f"Edad: {edad}, tiene descuento de un 50 %.")
     
elif edad >30 and edad <30:
     print(f"Edad: {edad}, tiene descuento de un 20 %.")
     
elif edad >60:
     print(f"Edad: {edad}, tiene descuento de un 90 %.")
     
else :
    print(f"Edad: {edad}, no aplica descuento.")